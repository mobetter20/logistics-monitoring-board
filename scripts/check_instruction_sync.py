#!/usr/bin/env python3
"""Verify or repair shared assistant rules across policy and wrapper files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "policy": ROOT / "docs" / "assistant-policy.md",
    "agents": ROOT / "AGENTS.md",
    "claude": ROOT / "CLAUDE.md",
}
START = "<!-- BEGIN SHARED RULES -->"
END = "<!-- END SHARED RULES -->"


def extract_block(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    start = text.find(START)
    end = text.find(END)
    if start == -1 or end == -1 or end < start:
        raise SystemExit(f"Missing shared-rule markers in {path}")
    return text[start + len(START):end].strip()


def replace_block(path: Path, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    start = text.find(START)
    end = text.find(END)
    if start == -1 or end == -1 or end < start:
        raise SystemExit(f"Missing shared-rule markers in {path}")
    updated = text[: start + len(START)] + "\n" + block.strip() + "\n" + text[end:]
    path.write_text(updated, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify that shared assistant rules stay identical across policy and wrapper files."
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Copy the canonical docs/assistant-policy.md shared-rule block into AGENTS.md and CLAUDE.md.",
    )
    args = parser.parse_args()

    missing = [path for path in FILES.values() if not path.exists()]
    if missing:
        for path in missing:
            print(f"Missing file: {path}", file=sys.stderr)
        return 1

    blocks = {name: extract_block(path) for name, path in FILES.items()}
    reference = blocks["policy"]
    failed = False
    for name in ("agents", "claude"):
        if blocks[name] != reference:
            failed = True
            if args.fix:
                replace_block(FILES[name], reference)
                print(f"Updated shared assistant rules: {FILES[name]}")
            else:
                print(f"Shared assistant rules drift detected: {FILES[name]}", file=sys.stderr)

    if failed:
        if args.fix:
            print("Shared assistant rules are in sync.")
            return 0
        print("Update docs/assistant-policy.md first, then keep wrapper shared-rule blocks identical.", file=sys.stderr)
        return 1

    print("Shared assistant rules are in sync.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
