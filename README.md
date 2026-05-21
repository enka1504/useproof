# Useproof

AI browser agents for proving real workflows work.

Useproof is an open-source product project built from
[`browser-use`](https://github.com/browser-use/browser-use). Its direction is
different from general browser automation: Useproof focuses on repeatable proof
runs for web workflows, with artifacts that developers, QA teams, and product
teams can trust.

The current codebase keeps the upstream `browser_use` Python package while the
product layer is developed around it.

## Product Direction

Useproof turns plain-English browser tasks into reusable checks:

```yaml
name: checkout-smoke-test
task: Log in, add the demo product to cart, and complete checkout with test card.
expect:
  - The order confirmation page is visible.
  - The confirmation number is captured.
artifacts:
  - screenshot
  - browser_trace
  - agent_steps
```

The product goal is simple:

> If an AI agent says a workflow works, Useproof should be able to show the proof.

## What This Becomes

- A local CLI for running agent-powered browser workflow checks
- A reusable workflow spec format for tests and monitors
- Screenshots, traces, logs, and replayable proof artifacts
- GitHub Actions integration for pull-request checks
- Scheduled production monitors with Slack or email alerts
- A hosted team dashboard for history, flakiness, cost, and replay

## Why Useproof

AI browser agents are powerful, but product teams need more than "the agent ran."
They need evidence:

- What did the agent do?
- What did it see?
- Did the workflow actually succeed?
- Can the result be replayed or audited?
- Did this break after a deploy?

Useproof is the product layer for that evidence.

## Upstream

Useproof starts from `browser-use/browser-use`, imported as an independent
repository rather than created through GitHub's fork button. The upstream commit
history is preserved locally so future changes can be audited and upstream can
still be synced.

See:

- [Upstream snapshot](docs/UPSTREAM_SNAPSHOT.md)
- [Product direction](docs/PRODUCT_DIRECTION.md)
- [Roadmap](docs/ROADMAP.md)
- [Original browser-use README](docs/UPSTREAM_BROWSER_USE_README.md)
- [Attribution notice](NOTICE.md)

## Status

This repository is in product-shaping mode. The first milestone is to keep the
browser-use engine working while adding a Useproof workflow runner, proof
artifacts, and CI-friendly reporting.
