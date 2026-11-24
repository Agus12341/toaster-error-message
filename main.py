#!/usr/bin/env python3
"""Write this entry's toaster error message to entry.txt in the output folder."""

import os

TEXT = "I am sorry. Your bread went in as bread and came out as charcoal for the third time. I am beginning to suspect me."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
