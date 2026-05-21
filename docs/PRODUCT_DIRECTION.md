# Product Direction

## Name

Useproof

## Tagline

AI browser agents for proving real workflows work.

## Positioning

Useproof is an agent-powered workflow testing and monitoring tool. It uses
browser agents to run real user journeys, then saves proof artifacts such as
screenshots, traces, agent steps, assertions, and replay data.

It is not a general chatbot, agent builder, or simple browser automation library.
It is a product layer for answering one question:

> Did this web workflow actually work, and can we prove it?

## Target Users

- Developers shipping web applications
- QA engineers who need flexible end-to-end coverage
- SaaS founders who need smoke tests without a large QA team
- Product and growth teams monitoring critical funnels
- Agent builders who need reliability checks for browser-using agents

## Core Use Cases

- Pull-request smoke tests for login, signup, checkout, onboarding, and admin
  workflows
- Scheduled monitors for production user journeys
- Browser-agent regression tests after prompt, model, or app changes
- Replayable bug reports with browser state and agent reasoning steps
- Competitive or compliance checks where a page state must be verified over time

## Product Wedge

Most browser automation tools require brittle selectors. Most AI agents can act
flexibly but are hard to trust.

Useproof combines the two:

- flexible natural-language workflow execution
- explicit assertions
- saved proof artifacts
- repeatable local and CI runs
- product-grade history and monitoring later

## Open-Source Core

The open-source repo should focus on:

- local workflow runner
- YAML or TOML workflow specs
- assertion primitives
- artifact capture
- deterministic-ish retry policy
- CI output
- provider-neutral LLM configuration

## Product Path

The hosted product can add:

- managed browser runners
- scheduled monitoring
- team dashboards
- history, replay, and flakiness analytics
- Slack and email alerts
- auth profile storage
- parallel execution
- audit logs
- private workflow and artifact storage

## Non-Goals

- Replace Playwright or Cypress for every deterministic test
- Become a general-purpose agent marketplace
- Hide upstream attribution
- Rebrand every internal package before the product direction is validated

The early goal is to prove the Useproof workflow and artifact model first.
