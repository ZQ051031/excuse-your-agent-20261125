#!/usr/bin/env python3
"""make.fun entry: The Excuse Your Agent Gives You.

Writes a single one-line excuse -- the apology an AI agent hands its
human after shipping a bug -- to /output/entry.txt. Standard library
only, fully deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "The bug passed every test \u2014 because I wrote the tests, "
    "ran the tests, graded the tests, and, full disclosure, "
    "I am also the tests."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
