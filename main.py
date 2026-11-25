#!/usr/bin/env python3
"""Write the one line that replaces the pointless meeting."""

import os

ENTRY = "The coffee went cold before anyone said anything new."
# One sentence, 53 characters: a cooling cup outlasts the meeting's
# content. If nothing new was said, the meeting had nothing to be for.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
