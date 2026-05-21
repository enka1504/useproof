# Roadmap

## Milestone 0: Product Baseline

- Preserve upstream browser-use history
- Add Useproof README, product direction, roadmap, and attribution
- Keep upstream sync path available through the `upstream` remote
- Define the first workflow spec shape
- Preserve upstream issue and pull-request metadata as a file archive

## Milestone 1: Local Proof Runner

- Add `useproof run <workflow-file>`
- Support a minimal YAML workflow format
- Run one browser-agent task from a workflow file
- Save run output under `.useproof/runs/`
- Capture screenshots, final URL, agent steps, and pass/fail status

## Milestone 2: Assertions

- Add assertion types:
  - page contains text
  - URL matches pattern
  - element or visible text exists
  - agent captured value exists
- Produce machine-readable JSON reports
- Produce human-readable Markdown reports

## Milestone 3: CI Mode

- Add `useproof run --ci`
- Exit non-zero on failed proof runs
- Add GitHub Actions example
- Store artifacts in predictable paths
- Add retry and timeout controls

## Milestone 4: Replay And Debugging

- Add browser trace capture
- Add run timeline view
- Add failure summary with last screenshot and last agent action
- Add prompt/model/config metadata to each run

## Milestone 5: Monitoring Product

- Add scheduled runs
- Add Slack/email alert adapters
- Add hosted runner design
- Add team dashboard design
- Add pricing and packaging notes after open-source usage is validated

## First Product Bet

The first narrow product promise should be:

> Useproof runs your most important web workflow and gives you proof it worked.

Everything else should serve that promise.
