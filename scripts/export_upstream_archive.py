#!/usr/bin/env python3
"""Export upstream GitHub issue and pull-request metadata for Useproof.

This script intentionally archives upstream discussions as files instead of
recreating them as live Useproof issues or pull requests. That keeps the new
product repo clean while preserving the source project's context.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_REPOSITORY = 'browser-use/browser-use'
DEFAULT_OUTPUT_DIR = Path('docs/upstream-archive')
DEFAULT_PER_PAGE = 100


@dataclass(frozen=True)
class ArchiveConfig:
	repository: str
	output_dir: Path
	include_comments: bool
	sleep_seconds: float
	token: str | None


def request_json(url: str, token: str | None) -> tuple[Any, str | None]:
	headers = {
		'Accept': 'application/vnd.github+json',
		'User-Agent': 'useproof-upstream-archive',
		'X-GitHub-Api-Version': '2022-11-28',
	}
	if token:
		headers['Authorization'] = f'Bearer {token}'

	request = urllib.request.Request(url, headers=headers)

	try:
		with urllib.request.urlopen(request) as response:
			payload = json.loads(response.read().decode('utf-8'))
			return payload, response.headers.get('Link')
	except urllib.error.HTTPError as error:
		body = error.read().decode('utf-8', errors='replace')
		raise RuntimeError(f'GitHub API request failed: {error.code} {url}\n{body}') from error


def build_url(endpoint: str, params: dict[str, str]) -> str:
	query = urllib.parse.urlencode({**params, 'per_page': str(DEFAULT_PER_PAGE)})
	return f'{endpoint}?{query}'


def next_link_url(link_header: str | None) -> str | None:
	if not link_header:
		return None

	for item in link_header.split(','):
		url_part, *param_parts = item.split(';')
		params = {part.strip() for part in param_parts}
		if 'rel="next"' not in params:
			continue

		url_part = url_part.strip()
		if url_part.startswith('<') and url_part.endswith('>'):
			return url_part[1:-1]

	return None


def paged_request(endpoint: str, params: dict[str, str], token: str | None, sleep_seconds: float) -> list[dict[str, Any]]:
	items: list[dict[str, Any]] = []
	url: str | None = build_url(endpoint, params)
	seen_urls: set[str] = set()

	while url:
		if url in seen_urls:
			raise RuntimeError(f'GitHub pagination loop detected at {url}')

		seen_urls.add(url)
		batch, link_header = request_json(url, token)

		if not isinstance(batch, list):
			raise RuntimeError(f'Expected a list response from {url}')

		if not batch:
			break

		items.extend(batch)
		url = next_link_url(link_header)

		if url and sleep_seconds:
			time.sleep(sleep_seconds)

	return items


def compact_user(user: dict[str, Any] | None) -> dict[str, Any] | None:
	if not user:
		return None
	return {
		'login': user.get('login'),
		'id': user.get('id'),
		'type': user.get('type'),
		'html_url': user.get('html_url'),
	}


def compact_label(label: dict[str, Any]) -> dict[str, Any]:
	return {
		'name': label.get('name'),
		'color': label.get('color'),
		'description': label.get('description'),
	}


def compact_milestone(milestone: dict[str, Any] | None) -> dict[str, Any] | None:
	if not milestone:
		return None
	return {
		'number': milestone.get('number'),
		'title': milestone.get('title'),
		'state': milestone.get('state'),
		'html_url': milestone.get('html_url'),
	}


def compact_issue(item: dict[str, Any], item_type: str) -> dict[str, Any]:
	return {
		'type': item_type,
		'number': item.get('number'),
		'title': item.get('title'),
		'state': item.get('state'),
		'state_reason': item.get('state_reason'),
		'user': compact_user(item.get('user')),
		'assignees': [compact_user(user) for user in item.get('assignees', [])],
		'labels': [compact_label(label) for label in item.get('labels', [])],
		'milestone': compact_milestone(item.get('milestone')),
		'comments': item.get('comments'),
		'created_at': item.get('created_at'),
		'updated_at': item.get('updated_at'),
		'closed_at': item.get('closed_at'),
		'html_url': item.get('html_url'),
		'body': item.get('body') or '',
	}


def compact_pull_request(item: dict[str, Any], issue_wrapper: dict[str, Any] | None) -> dict[str, Any]:
	return {
		'type': 'pull_request',
		'number': item.get('number'),
		'title': item.get('title'),
		'state': item.get('state'),
		'user': compact_user(item.get('user')),
		'assignees': [compact_user(user) for user in (issue_wrapper or {}).get('assignees', [])],
		'labels': [compact_label(label) for label in (issue_wrapper or {}).get('labels', [])],
		'milestone': compact_milestone((issue_wrapper or {}).get('milestone')),
		'comments': (issue_wrapper or {}).get('comments'),
		'draft': item.get('draft'),
		'merged_at': item.get('merged_at'),
		'created_at': item.get('created_at'),
		'updated_at': item.get('updated_at'),
		'closed_at': item.get('closed_at'),
		'html_url': item.get('html_url'),
		'base': {
			'ref': (item.get('base') or {}).get('ref'),
			'sha': (item.get('base') or {}).get('sha'),
			'repo': ((item.get('base') or {}).get('repo') or {}).get('full_name'),
		},
		'head': {
			'ref': (item.get('head') or {}).get('ref'),
			'sha': (item.get('head') or {}).get('sha'),
			'repo': ((item.get('head') or {}).get('repo') or {}).get('full_name'),
		},
		'body': item.get('body') or '',
	}


def compact_comment(comment: dict[str, Any]) -> dict[str, Any]:
	return {
		'id': comment.get('id'),
		'user': compact_user(comment.get('user')),
		'created_at': comment.get('created_at'),
		'updated_at': comment.get('updated_at'),
		'html_url': comment.get('html_url'),
		'body': comment.get('body') or '',
	}


def write_json(path: Path, value: Any) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def write_markdown_index(output_dir: Path, repository: str, issues: list[dict[str, Any]], pulls: list[dict[str, Any]]) -> None:
	open_issues = [item for item in issues if item['state'] == 'open']
	closed_issues = [item for item in issues if item['state'] == 'closed']
	open_pulls = [item for item in pulls if item['state'] == 'open']
	closed_pulls = [item for item in pulls if item['state'] == 'closed']

	lines = [
		'# Upstream Archive',
		'',
		f'- Repository: `{repository}`',
		f'- Exported at: `{datetime.now(timezone.utc).isoformat()}`',
		f'- Open issues: {len(open_issues)}',
		f'- Closed issues: {len(closed_issues)}',
		f'- Open pull requests: {len(open_pulls)}',
		f'- Closed pull requests: {len(closed_pulls)}',
		'',
		'## Files',
		'',
		'- `issues.json`: issue metadata and bodies',
		'- `pull_requests.json`: pull-request metadata and bodies',
		'- `comments/`: optional issue and pull-request comments when exported with `--include-comments`',
		'',
		'These files preserve upstream context without turning Useproof into a GitHub fork.',
		'',
	]

	(output_dir / 'README.md').write_text('\n'.join(lines), encoding='utf-8')


def write_manifest(
	output_dir: Path,
	repository: str,
	issues: list[dict[str, Any]],
	pulls: list[dict[str, Any]],
	include_comments: bool,
) -> None:
	open_issues = [item for item in issues if item['state'] == 'open']
	closed_issues = [item for item in issues if item['state'] == 'closed']
	open_pulls = [item for item in pulls if item['state'] == 'open']
	closed_pulls = [item for item in pulls if item['state'] == 'closed']

	write_json(
		output_dir / 'manifest.json',
		{
			'source_repository': repository,
			'source_url': f'https://github.com/{repository}',
			'product_repository': 'enka1504/useproof',
			'product_url': 'https://github.com/enka1504/useproof',
			'exported_at': datetime.now(timezone.utc).isoformat(),
			'github_state': {
				'open_issues': len(open_issues),
				'closed_issues': len(closed_issues),
				'open_pull_requests': len(open_pulls),
				'closed_pull_requests': len(closed_pulls),
			},
			'archive_status': {
				'metadata_exported': True,
				'comments_exported': include_comments,
			},
		},
	)


def export_comments(config: ArchiveConfig, items: list[dict[str, Any]]) -> None:
	owner, repo = config.repository.split('/', 1)
	base = f'https://api.github.com/repos/{owner}/{repo}/issues'
	comments_dir = config.output_dir / 'comments'

	for item in items:
		if not item.get('comments'):
			continue

		number = item['number']
		comments = paged_request(f'{base}/{number}/comments', {}, config.token, config.sleep_seconds)
		write_json(comments_dir / f'{number}.json', [compact_comment(comment) for comment in comments])


def export_archive(config: ArchiveConfig) -> None:
	owner, repo = config.repository.split('/', 1)
	base = f'https://api.github.com/repos/{owner}/{repo}'

	issue_items = paged_request(
		f'{base}/issues',
		{'state': 'all', 'sort': 'created', 'direction': 'asc'},
		config.token,
		config.sleep_seconds,
	)
	pull_items = paged_request(
		f'{base}/pulls',
		{'state': 'all', 'sort': 'created', 'direction': 'asc'},
		config.token,
		config.sleep_seconds,
	)

	issue_wrappers_by_number = {item['number']: item for item in issue_items}
	issues = [compact_issue(item, 'issue') for item in issue_items if 'pull_request' not in item]
	pulls = [compact_pull_request(item, issue_wrappers_by_number.get(item['number'])) for item in pull_items]

	write_json(config.output_dir / 'issues.json', issues)
	write_json(config.output_dir / 'pull_requests.json', pulls)
	write_markdown_index(config.output_dir, config.repository, issues, pulls)
	write_manifest(config.output_dir, config.repository, issues, pulls, config.include_comments)

	if config.include_comments:
		export_comments(config, [*issues, *pulls])


def parse_args() -> ArchiveConfig:
	parser = argparse.ArgumentParser(description='Export upstream GitHub issues and pull requests as archive files.')
	parser.add_argument('--repository', default=DEFAULT_REPOSITORY, help='Repository in owner/name form.')
	parser.add_argument('--output-dir', type=Path, default=DEFAULT_OUTPUT_DIR, help='Directory for archive files.')
	parser.add_argument('--include-comments', action='store_true', help='Also export issue and pull-request comments.')
	parser.add_argument('--sleep-seconds', type=float, default=0.2, help='Delay between paginated requests.')
	args = parser.parse_args()

	token = find_token()

	return ArchiveConfig(
		repository=args.repository,
		output_dir=args.output_dir,
		include_comments=args.include_comments,
		sleep_seconds=args.sleep_seconds,
		token=token,
	)


def find_token() -> str | None:
	env_token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
	if env_token:
		return env_token

	if not shutil.which('gh'):
		return None

	try:
		result = subprocess.run(
			['gh', 'auth', 'token'],
			check=False,
			capture_output=True,
			text=True,
			timeout=10,
		)
	except (OSError, subprocess.SubprocessError):
		return None

	if result.returncode != 0:
		return None

	token = result.stdout.strip()
	return token or None


def main() -> int:
	config = parse_args()

	if not config.token:
		print(
			'Warning: GITHUB_TOKEN/GH_TOKEN is not set. Public GitHub API rate limits may stop a full export.',
			file=sys.stderr,
		)

	export_archive(config)
	return 0


if __name__ == '__main__':
	raise SystemExit(main())
