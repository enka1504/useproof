# Contributing

Useproof is being shaped as a product, so contributions should connect clearly
to casefiles, verdicts, receipts, dossiers, or upstream compatibility.

## Good First Areas

- Casefile examples
- Verdict rule design
- Receipt layout
- Markdown and JSON dossiers
- CI integration
- Upstream archive improvements
- Documentation cleanup

## Before Opening A PR

- Keep upstream attribution intact.
- Avoid broad internal renames until the product layer is stable.
- Include a short explanation of the casefile your change improves.
- Add or update docs when behavior or product surface changes.

## Local Checks

```bash
python3 -m py_compile scripts/export_upstream_archive.py
python3 -c "import tomllib; tomllib.load(open('pyproject.toml', 'rb'))"
```

Use the heavier upstream test suite when touching the browser engine.

## Pull Request Shape

Every PR should answer:

- What casefile or verdict does this improve?
- What changed?
- How was it verified?
- What remains risky or incomplete?
