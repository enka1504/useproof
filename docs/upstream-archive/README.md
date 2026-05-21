# Upstream Archive

This directory is reserved for archived upstream GitHub issue and pull-request
metadata from `browser-use/browser-use`.

Useproof is an independent product repository, so upstream discussions are not
recreated as live Useproof issues or pull requests. Live issues in this repo
should describe Useproof product work. Upstream context belongs here as data.

## Generate The Archive

Use a completed `gh auth login` session or a GitHub token through your shell
environment. Do not paste tokens into chat.

```bash
cd /root/useproof
python3 scripts/export_upstream_archive.py
```

To include issue and pull-request comments:

```bash
cd /root/useproof
python3 scripts/export_upstream_archive.py --include-comments
```

Expected generated files:

- `docs/upstream-archive/manifest.json`
- `docs/upstream-archive/issues.json`
- `docs/upstream-archive/pull_requests.json`
- `docs/upstream-archive/comments/*.json` when `--include-comments` is used

The export script writes compact JSON with titles, states, labels, authors,
timestamps, bodies, and GitHub URLs.

The exporter follows GitHub's `Link` header for pagination so it works with
both page-based and cursor-based API responses.
