# Board Operations

## Purpose

This repo is the published target for the logistics signals board.
It should stay lightweight and resumable. Normal content generation belongs in the sibling
pipeline repo, not here.

## Normal Publish Path

The preferred publish path is to run the source repo publisher:

```bash
python3 ../logistics-news-briefing-pipeline/scripts/publish_signals_board.py --skip-build
```

That command copies the current source artifacts into this repo, commits them, and pushes to GitHub.

## Manual Recovery

Use manual recovery only if the source repo artifacts are already current and the publish step itself failed.

Manual recovery means:

1. Copy the published files from `../logistics-news-briefing-pipeline/internal_intelligence/output/`
2. Verify `latest.json` reflects the expected date
3. Commit and push this repo

Do not use manual recovery to bypass stale or broken upstream source artifacts.

## Health Commands

Check shared assistant-policy drift:

```bash
python3 scripts/check_instruction_sync.py
```

Quick status:

```bash
git status --short --branch
```

## Current Contract Notes

- `latest.json` is the current board snapshot contract.
- `public-dashboard.json` remains in the repo for legacy freshness checks.
- The remote watchdog currently checks the legacy file path, so removing or redefining it requires consultation first.

## Consultation Gate

Pause and consult before changing:

- the set of published files
- the meaning of `latest.json`
- the legacy `public-dashboard.json` support path
- push/commit behavior in the publish flow
