# Roadmap

## 0. Product Identity

- Preserve upstream history, license, and attribution
- Replace the public repo surface with the flight-recorder identity
- Add casefile spec, architecture, brand, and contribution docs
- Preserve upstream issue and PR context as an archive

## 1. Recorder

- Add `useproof run <casefile.yml>`
- Parse the first casefile spec
- Run one browser-agent task
- Write `.useproof/runs/<case>/<run-id>/`
- Capture screenshots, run tape, config, and final result

## 2. Verdicts

- Add `page_contains`
- Add `url_matches`
- Add `capture`
- Add timeout and retry controls
- Emit JSON verdicts and Markdown dossiers

## 3. CI Mode

- Add `useproof check <casefile.yml>`
- Exit non-zero on failed verdicts
- Add a GitHub Actions example
- Upload receipts predictably
- Make PR output short enough to scan

## 4. Replay

- Save trace metadata
- Add a run timeline
- Show last known page state on failure
- Preserve model, prompt, and browser settings for each run

## 5. Monitoring

- Add scheduled local runs
- Add Slack and email alert adapters
- Design hosted runner API
- Design team dossier history

## 6. Productization

- Package the CLI as `useproof`
- Publish docs
- Add examples for login, checkout, onboarding, and admin flows
- Define the hosted product boundary
- Decide which upstream internals should be renamed only after the proof model is validated
