# Product Direction

## Product Promise

Useproof helps teams prove that important browser workflows still work.

It does that with agentic execution plus inspectable evidence: assertions,
screenshots, traces, run logs, and replay-ready reports.

## Category

Agentic workflow QA and monitoring.

Useproof is not a generic browser agent, chatbot, scraper, or automation
marketplace. It is the evidence layer for browser agents.

## Primary Users

- Developers who need PR checks for critical web flows
- QA teams who need resilient end-to-end coverage
- SaaS founders who need production smoke tests without a large QA team
- Agent builders who need regression checks for browser-using agents

## Wedge

Traditional end-to-end tests are repeatable but brittle. Browser agents are
flexible but hard to trust.

Useproof sits between them:

- natural-language workflow execution
- explicit machine-checkable assertions
- durable proof artifacts
- local and CI execution first
- scheduled monitoring later

## First Use Case

The first product bet is a checkout, signup, login, onboarding, or admin flow
that a team wants to verify after every deploy.

The output is not just pass or fail. It is a proof bundle:

- workflow spec
- model and browser configuration
- agent step timeline
- screenshots
- assertion result
- final report

## Open-Source Core

- Workflow spec format
- Local runner
- Assertion engine
- Artifact writer
- Markdown and JSON reports
- CI-friendly exit codes
- Upstream browser automation engine

## Hosted Product Path

- Managed browser runners
- Scheduled production monitors
- Team run history
- Replay UI
- Flakiness analytics
- Slack and email alerts
- Private artifact storage
- Audit logs

## Product Rule

Every feature should improve one of three things:

- Can the workflow run?
- Can the result be trusted?
- Can the proof be shared?
