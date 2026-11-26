#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — writes one excuse to /output/entry.txt.

The line (74 chars, one line):
  I'm stuck in a meeting about the meeting we already had about the meeting.
"""
import os

# The excuse is the meeting itself: a pointless meeting about a pointless
# meeting. Relatable to anyone who has ever sat through one.
LINE = "I'm stuck in a meeting about the meeting we already had about the meeting."


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
