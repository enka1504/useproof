# Upstream Snapshot

This document preserves the baseline state used to create Useproof as an
independent open-source product repo.

## Source

- Upstream repository: `browser-use/browser-use`
- Upstream URL: https://github.com/browser-use/browser-use
- Product repository: `enka1504/useproof`
- Product URL: https://github.com/enka1504/useproof
- Snapshot date: 2026-05-21
- Imported commit: `5f99e737 chore(llm): default ChatBrowserUse to bu-2-0 (#4876)`
- Default branch at import: `main`
- License at import: MIT

## GitHub State At Snapshot

- Open issues: 59
- Closed issues: 1,464
- Open pull requests: 163
- Closed pull requests: 2,827

GitHub does not preserve upstream issues and pull requests when code is imported
into a new independent repository. These counts are kept here as the project
baseline. For the original discussions, bug reports, and pull requests, use the
upstream repository.

For a file-based archive, use
[`scripts/export_upstream_archive.py`](../scripts/export_upstream_archive.py).
Generated archive files should live under
[`docs/upstream-archive`](upstream-archive/README.md).

## Repository Relationship

Useproof is not a GitHub fork. It is an independent repository that preserves
the upstream code history and license notices.

Recommended local remotes:

```bash
git remote -v
origin   https://github.com/enka1504/useproof.git
upstream https://github.com/browser-use/browser-use.git
```

Recommended snapshot tag:

```bash
git tag upstream-browser-use-2026-05-21 5f99e737
```
