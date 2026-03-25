# CLAUDE.md

This repo keeps shared assistant rules in `docs/assistant-policy.md`.
Run `python3 scripts/check_instruction_sync.py` after editing shared rules.

<!-- BEGIN SHARED RULES -->
## Shared Rules

- Preserve the board’s current publish contract unless the user explicitly approves a behavior-affecting change.
- Treat this repo as a published target, not as the primary content-generation system.
- Prefer republishing from the source pipeline repo over hand-editing generated HTML or JSON.
- Keep shared assistant rules identical across `docs/assistant-policy.md`, `AGENTS.md`, and `CLAUDE.md`.
- Consult before changing publish behavior, freshness expectations, or legacy file support such as `public-dashboard.json`.
<!-- END SHARED RULES -->

## Claude-Specific Notes

- Keep Claude-specific guidance outside the shared-rule block so the board repo stays cross-platform.
- Do not convert this repo into a standalone Claude-only publishing workflow.
