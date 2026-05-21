# Architecture

Useproof is a flight-recorder layer around an agentic browser engine.

```text
Casefile
  -> Recorder
  -> Browser agent engine
  -> Run tape
  -> Verdict engine
  -> Receipt store
  -> Dossier writers
```

## Layers

## Casefile

YAML files describe the objective, browser settings, verdict rules, receipts,
and retry policy.

## Recorder

The recorder loads the casefile, starts the browser agent, records each step,
and hands final state to the verdict engine.

## Browser Agent Engine

The imported upstream engine drives the browser and model interaction. The
internal package is still `browser_use` while Useproof's product layer matures.

## Run Tape

The tape is the chronological record of what the agent tried, saw, clicked,
typed, captured, retried, and concluded.

## Verdict Engine

Verdict rules turn an agent run into an auditable pass/fail result. Early rules
should be deliberately small: page text, URL matching, and captured values.

## Receipt Store

Receipts make the result inspectable. Local runs write to `.useproof/runs/`.
Hosted runs can later store receipts privately for teams.

## Dossier Writers

Dossier writers translate run output into formats for humans and machines:

- JSON for CI
- Markdown for pull requests
- terminal summaries for local runs
- alerts for scheduled monitors

## Design Constraint

Useproof should not hide that agents can be uncertain. The architecture should
make uncertainty visible through verdict rules, retries, receipts, and run
history.
