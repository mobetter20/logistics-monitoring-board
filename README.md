# Logistics Signals Board

Low-profile shared site for the team-facing logistics signals board.

This site now publishes the board generated from:

- [`/Users/ajin/Documents/New project/internal_intelligence/output`](/Users/ajin/Documents/New project/internal_intelligence/output)

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
