#!/usr/bin/env python3
"""One-Line Robot Wedding Vows entry.

Writes a single original funny robot wedding vow to /output/entry.txt
(1-160 characters, UTF-8, a single sentence). Standard library only,
no network, no input.

The line is built from two fragments: a setup (the classic vow
cadence, robot-flavoured — "lawfully wedded unit", "in sickness and
in low battery") and a punch (the vow's "until death do us part" is
undercut at the very last word by the warranty running out).
``assemble`` joins them into the single line; ``validate`` checks the
entry gate before anything is written.
"""

from pathlib import Path

SETUP = "I take you to be my lawfully wedded unit, to have and to hold, in sickness and in low battery, until death do us part"
PUNCH = "\u2014 or until our warranties expire."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one vow line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-160 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 160:
        raise ValueError(f"line must be 1-160 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
