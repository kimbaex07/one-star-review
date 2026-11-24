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
    # The grader mounts the repo read-only, so the next-to-script copy
    # is best-effort only; the graded copy goes to the output dir.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    wrote = []
    if os.path.isdir(out_dir):
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(out_path, 0o644)
        wrote.append(out_path)
    try:
        path = os.path.join(HERE, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
        wrote.append(path)
    except OSError:
        pass
    if not wrote:
        raise SystemExit("no writable output location")
    print("Wrote %d chars: %r" % (len(ENTRY), ENTRY))


if __name__ == "__main__":
    main()
