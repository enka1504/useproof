<p align="center">
  <img src="docs/assets/useproof-mark.svg" alt="Useproof logo" width="104">
</p>

<h1 align="center">Useproof</h1>

<p align="center">
  <strong>Agentic browser checks with evidence you can inspect.</strong>
</p>

<p align="center">
  Describe a web workflow, run it with a browser agent, assert the outcome, and keep the proof.
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-12211F"></a>
  <a href="pyproject.toml"><img alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11%2B-0EAD93"></a>
  <a href="docs/ROADMAP.md"><img alt="Status: product shaping" src="https://img.shields.io/badge/status-product%20shaping-F2B84B"></a>
</p>

## What Useproof Is

Useproof is an open-source product project for turning AI browser agents into
repeatable workflow checks.

The product promise is narrow on purpose:

> If an agent says a workflow worked, Useproof should show the proof.

Useproof starts from the browser automation engine of
[`browser-use`](https://github.com/browser-use/browser-use), then adds a product
layer for workflow specs, assertions, artifacts, CI reports, and scheduled
monitoring.

## Proof Workflow

```text
Describe -> Run -> Assert -> Capture -> Replay -> Monitor
```

```yaml
name: checkout-smoke-test
goal: Prove that the demo checkout still works.

agent:
  task: Log in, add the demo product to cart, and complete checkout with the test card.
  model: auto

assert:
  - page_contains: Order confirmed
  - url_matches: /orders/
  - capture: confirmation_number

artifacts:
  - screenshot
  - agent_steps
  - browser_trace
  - markdown_report
```

The output should answer the questions a team actually asks after a deploy:

- What did the agent do?
- What did it see?
- Which assertion passed or failed?
- What screenshot, trace, or replay proves it?
- Can this run again in CI or on a schedule?

## Product Surface

- `useproof run`: local workflow proof runner
- `useproof check`: CI mode with deterministic exit codes
- `.useproof/runs/`: run artifacts, reports, screenshots, and traces
- `docs/upstream-archive/`: preserved upstream issue and PR context
- Hosted product path: managed browser runners, scheduled monitors, team history, replay, and alerts

The current implementation still exposes the upstream `browser_use` Python
package while Useproof-specific product surfaces are introduced.

## Repository Map

- [docs/README.md](docs/README.md): documentation index
- [docs/WORKFLOW_SPEC.md](docs/WORKFLOW_SPEC.md): proposed proof workflow format
- [docs/EXAMPLES.md](docs/EXAMPLES.md): example proof workflows
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md): target product architecture
- [docs/BRAND.md](docs/BRAND.md): product identity and design system
- [docs/ROADMAP.md](docs/ROADMAP.md): build plan
- [docs/UPSTREAM_SNAPSHOT.md](docs/UPSTREAM_SNAPSHOT.md): imported upstream baseline
- [NOTICE.md](NOTICE.md): attribution and license notice

## Development Status

Useproof is in product-shaping mode. The foundation is imported and attributed;
the next work is to build the Useproof runner, workflow spec, artifact model,
and CI reporting around the existing browser agent engine.

## Upstream And License

Useproof is an independent repository, not a GitHub fork. It preserves upstream
history and attribution from `browser-use/browser-use` under the MIT License.

The original upstream README is preserved at
[docs/UPSTREAM_BROWSER_USE_README.md](docs/UPSTREAM_BROWSER_USE_README.md).
