# Logistics Signals Board

Low-profile shared site for the team-facing logistics signals board.

This site now publishes the board generated from:

- [`../logistics-news-briefing-pipeline/internal_intelligence/output`](../logistics-news-briefing-pipeline/internal_intelligence/output)

It is designed as a shared reference surface with:

- daily logistics and supply-chain news
- direct-competitor monitoring
- a weekly strategy brief

## Publishing Flow

This repo is the hosted site layer for the shared board.

- generate the latest board in `internal_intelligence/output`
- copy the generated site files into this repo
- push this repo so the hosted URL updates

Expected top-level files:

- `index.html`
- `market-watch.html`
- `competitor-watch.html`
- `strategy-brief.html`
- `latest.json`

Legacy file note:

- `public-dashboard.json` may remain during transition from the older news-only board

The source workflow continues to live in:

- `https://github.com/mobetter20/logistics-news-briefing-pipeline`

## Operations And Handoff

This repo is a published target, not the primary content-generation system.

Primary operational docs:

- `OPERATIONS.md`
- `STATUS.md`
- `docs/assistant-policy.md`

Normal publish path:

```bash
python3 ../logistics-news-briefing-pipeline/scripts/publish_signals_board.py --skip-build
```

Useful check:

```bash
python3 scripts/check_instruction_sync.py
```

Operational notes:

- prefer republishing from the source repo over hand-editing generated HTML or JSON here
- `latest.json` is the current board snapshot contract
- `public-dashboard.json` still exists for legacy freshness checks and should not be changed casually
