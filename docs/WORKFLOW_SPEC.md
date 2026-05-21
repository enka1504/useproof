# Workflow Spec

Useproof workflows should be easy to read in a pull request and precise enough
to run in CI.

## Example

```yaml
name: checkout-smoke-test
goal: Prove the demo checkout works after deploy.

agent:
  task: Log in, add the demo product to cart, and complete checkout with the test card.
  model: auto
  max_steps: 25

browser:
  headless: true
  viewport:
    width: 1440
    height: 1100

assert:
  - page_contains: Order confirmed
  - url_matches: /orders/
  - capture: confirmation_number

artifacts:
  - screenshot
  - agent_steps
  - browser_trace
  - markdown_report

retry:
  attempts: 1
  on:
    - navigation_timeout
    - model_rate_limit
```

More examples live in [docs/EXAMPLES.md](EXAMPLES.md).

## Shape

`name`
: Stable identifier for the workflow.

`goal`
: Human-readable reason this workflow exists.

`agent.task`
: Natural-language browser task.

`agent.model`
: Model selector. `auto` should use the repo default.

`browser`
: Browser execution settings.

`assert`
: Machine-checkable expectations.

`artifacts`
: Evidence to save for the run.

`retry`
: Controlled retry policy.

## First Assertion Types

- `page_contains`: visible page text must appear
- `url_matches`: final URL must match a substring or pattern
- `capture`: named value should be extracted into the report

## Output Contract

Each run should create:

```text
.useproof/runs/<run-id>/
  workflow.yml
  result.json
  report.md
  screenshots/
  traces/
```

The JSON report is for machines. The Markdown report is for humans.
