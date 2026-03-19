# Logistics Monitoring Board

Minimal public-facing logistics monitoring board generated from a private local pipeline.

This site publishes only public-safe dashboard artifacts:
- short summaries
- source labels
- timestamps
- confidence/tier
- links back to original sources

It does not publish the private backend pipeline or raw mailbox data.

## Publishing Flow

This repo is the standalone public site layer.

- the private pipeline generates public-safe dashboard files
- those files are copied into this repo
- this repo is then pushed and redeployed by the public host

Expected top-level files:

- `index.html`
- `public-dashboard.json`

The private backend workflow lives in a separate repo:

- `https://github.com/mobetter20/logistics-news-briefing-pipeline`
