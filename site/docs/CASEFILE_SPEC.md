# Casefile Spec

Useproof casefiles should be easy to read in a pull request and precise enough
to create a CI verdict.

## Example

```yaml
case: checkout-smoke-test
objective: Prove the demo checkout works after deploy.

agent:
  task: Log in, add the demo product to cart, and complete checkout with the test card.
  model: auto
  max_steps: 25

browser:
  headless: true
  viewport:
    width: 1440
    height: 1100

verdict:
  pass_when:
    - page_contains: Order confirmed
    - url_matches: /orders/
    - capture: confirmation_number

receipts:
  - screenshot
  - run_tape
  - browser_trace
  - dossier

retry:
  attempts: 1
  on:
    - navigation_timeout
    - model_rate_limit
```

More examples live in [docs/EXAMPLES.md](EXAMPLES.md).

## Shape

`case`
: Stable identifier for the casefile.

`objective`
: Human-readable reason this casefile exists.

`agent.task`
: Natural-language browser task.

`agent.model`
: Model selector. `auto` should use the repo default.

`browser`
: Browser execution settings.

`verdict.pass_when`
: Machine-checkable conditions for a passing verdict.

`receipts`
: Evidence to save for the run.

`retry`
: Controlled retry policy.

## First Verdict Rules

- `page_contains`: visible page text must appear
- `url_matches`: final URL must match a substring or pattern
- `capture`: named value should be extracted into the dossier

## Output Contract

Each run should create:

```text
.useproof/runs/<case>/<run-id>/
  casefile.yml
  result.json
  dossier.md
  tape.json
  screenshots/
  traces/
```

The JSON result is for machines. The dossier is for humans.
