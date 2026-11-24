#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry for make.fun.

Writes exactly one sentence (at most 220 characters) pitching the
Sock-Matching Drone to entry.txt in the output directory, with no
trailing newline.
"""

import os
from pathlib import Path

SENTENCE = (
    "Presenting the Sock-Matching Drone: it hovers over your laundry basket, "
    "pairs every sock with its true mate, and files a tiny missing-persons "
    "report for the ones the dryer ate."
)


def _self_check() -> None:
    # Exactly one sentence: a single terminal period and no other
    # sentence-ending punctuation, and at most 220 characters.
    assert len(SENTENCE) <= 220, f"pitch too long: {len(SENTENCE)} chars"
    assert SENTENCE.endswith("."), "pitch must end with a period"
    assert SENTENCE.count(".") == 1, "pitch must be exactly one sentence"
    assert "!" not in SENTENCE and "?" not in SENTENCE


def main() -> None:
    _self_check()
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
