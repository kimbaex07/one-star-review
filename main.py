#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun entry.

Writes the graded deadpan one-star review to entry.txt next to this file.
Pure Python standard library, no network, no input files.

The review: sleep gets one star. It shows up late, leaves early, and
its free trial expires the second you get comfortable — a real complaint
filed in earnest against a thing that cannot be fixed, with the turn
landing in the last few words.
"""

import os

ENTRY = "Sleep: one star. Shows up late, leaves early, and the free trial expires the second you get comfortable. Do not recommend to the tired."

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    path = os.path.join(HERE, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Grading sandbox: the scorer reads /output/entry.txt, collected as
    # another user, so the copy there must be world-readable (mode 0644).
    out_dir = "/output"
    if os.path.isdir(out_dir):
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(out_path, 0o644)
    print("Wrote %d chars: %r" % (len(ENTRY), ENTRY))


if __name__ == "__main__":
    main()
