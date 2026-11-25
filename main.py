#!/usr/bin/env python3
"""office-jokes: write one funny line about office life.

Pure Python 3 standard library. No network, no randomness, no clock:
running the program twice writes byte-identical output.

The entry is a single line of text about office life -- an employee
warns the boss that AI is coming for the job, and the boss promotes
the AI instead, so now the AI approves the time off. It is written to
``entry.txt`` in the output directory (``$MAKEFUN_OUTPUT_DIR``,
default ``/output``), with no trailing newline, so the file holds
exactly the line the judge reads.

The program refuses to write an entry that would fail the bounty gate:
it asserts the text is one line, non-blank, under 200 characters, and
free of em-dashes (an em-dash reads as AI-written in a one-liner).
"""

import os
import sys

ENTRY = (
    "I told my boss AI was coming for my job. He promoted it, "
    "and now it approves my time off."
)


def main() -> int:
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\u2014" in ENTRY:
        print("error: entry must not contain an em-dash", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) < 200:
        print(
            "error: entry is %d characters, must be under 200" % len(ENTRY),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %s (%d characters)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
