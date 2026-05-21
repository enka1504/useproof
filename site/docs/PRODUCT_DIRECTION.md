# Product Direction

## Product Promise

Useproof is the flight recorder for browser agents.

It does not merely run an agent. It records the casefile, the run tape, the
verdict, and the receipts so a team can inspect what happened.

## Category

Agentic casefile evidence.

Useproof is not a generic browser agent, chatbot, scraper, or automation
marketplace. It is the evidence layer for teams that need browser agents to
produce auditable results.

## Primary Users

- Developers who need PR verdicts for critical web flows
- QA teams who need resilient end-to-end evidence
- SaaS founders who need production smoke checks without a large QA team
- Agent builders who need regression tapes for browser-using agents

## Wedge

Traditional end-to-end tests are repeatable but brittle. Browser agents are
flexible but hard to trust.

Useproof adds a third category:

- natural-language casefiles
- explicit verdict rules
- durable receipts
- run tapes that explain what happened
- dossiers that make the result shareable

## First Use Case

The first product bet is a checkout, signup, login, onboarding, or admin flow
that a team wants to verify after every deploy.

The output is not just pass or fail. It is a dossier:

- casefile
- model and browser configuration
- run tape
- receipts
- verdict
- final dossier

## Open-Source Core

- Casefile format
- Local runner
- Verdict engine
- Receipt writer
- Markdown and JSON dossiers
- CI-friendly exit codes
- Upstream browser automation engine

## Hosted Product Path

- Managed browser runners
- Scheduled production casefiles
- Team dossier history
- Replay UI
- Flakiness analytics
- Slack and email verdict alerts
- Private receipt storage
- Audit logs

## Product Rule

Every feature should improve one of three things:

- Can the casefile run?
- Can the verdict be trusted?
- Can the dossier be shared?
