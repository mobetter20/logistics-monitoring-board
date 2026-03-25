# Board Assistant Policy

This file is the canonical shared assistant policy for the published board repo.
Update shared rules here first, then keep the shared-rule blocks in `AGENTS.md`
and `CLAUDE.md` identical. Verify with `python3 scripts/check_instruction_sync.py`.

<!-- BEGIN SHARED RULES -->
## Shared Rules

- Preserve the board’s current publish contract unless the user explicitly approves a behavior-affecting change.
- Treat this repo as a published target, not as the primary content-generation system.
- Prefer republishing from the source pipeline repo over hand-editing generated HTML or JSON.
- Keep shared assistant rules identical across `docs/assistant-policy.md`, `AGENTS.md`, and `CLAUDE.md`.
- Consult before changing publish behavior, freshness expectations, or legacy file support such as `public-dashboard.json`.
<!-- END SHARED RULES -->

## Repo-Specific Notes

- Source artifacts come from `../logistics-news-briefing-pipeline/internal_intelligence/output`.
- `latest.json` is the current internal-intelligence snapshot contract.
- `public-dashboard.json` still exists for legacy freshness checks and should not be removed without review.
