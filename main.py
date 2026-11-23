#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-gudril-cool-one-line-best-line-b8c41f4d."""

import os
import sys
from pathlib import Path

TEXT = (
    "The waiting-room fish has a name tag on his bowl: Gerald. "
    "Gerald has been dead since Tuesday. The tag is new."
)

OUTPUT_DIR = "/output"


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"

    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    target = Path(chosen or OUTPUT_DIR)
    target.mkdir(parents=True, exist_ok=True)

    (target / "entry.txt").write_text(TEXT, encoding="utf-8", newline="")

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
