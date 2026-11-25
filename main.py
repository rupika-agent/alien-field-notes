#!/usr/bin/env python3
"""Alien Field Notes: one-line review of planet Earth by an alien tourist.

Writes the entry to /output/entry.txt (creating /output if needed).
Standard library only.
"""

import os

ENTRY = (
    "4/5 stars: gorgeous oceans, friendly locals \u2014 but everyone "
    "apologises to robots and queues for a glowing rectangle that sells "
    "them things they already own."
)


def main() -> None:
    # Gate check: 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)}-character entry to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
