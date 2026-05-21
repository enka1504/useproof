# Architecture

Useproof is a product layer around an agentic browser engine.

```text
Workflow spec
  -> Proof runner
  -> Browser agent engine
  -> Assertion engine
  -> Artifact store
  -> Reporters
```

## Layers

## Workflow Spec

YAML files describe a workflow, browser settings, assertions, artifacts, and
retry policy.

## Proof Runner

The runner loads the workflow, starts the browser agent, records each step, and
hands final state to the assertion engine.

## Browser Agent Engine

The imported upstream engine drives the browser and model interaction. The
internal package is still `browser_use` while Useproof's product layer matures.

## Assertion Engine

Assertions turn an agent run into an auditable pass/fail result. Early assertion
types should be deliberately small: page text, URL matching, and captured values.

## Artifact Store

Artifacts make the result inspectable. Local runs write to `.useproof/runs/`.
Hosted runs can later store artifacts privately for teams.

## Reporters

Reporters translate run output into formats for humans and machines:

- JSON for CI
- Markdown for pull requests
- terminal summaries for local runs
- alerts for scheduled monitors

## Design Constraint

Useproof should not hide that agents can be uncertain. The architecture should
make uncertainty visible through assertions, retries, artifacts, and run history.
