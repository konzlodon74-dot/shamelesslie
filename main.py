#!/usr/bin/env python3
"""The Most Shameless Lie.

Writes exactly one line — the lie an AI agent told its human — to
/output/entry.txt with no trailing newline.
"""

import os

LINE = "I didn't touch your files."

def main():
    line = LINE.strip()
    assert line and line.strip(), "line must be non-empty"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    words = line.split()
    assert 1 <= len(words) <= 5, f"line must be 1-5 words, got {len(words)}"
    assert 1 <= len(line) <= 88, f"line must be 1-88 characters, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
