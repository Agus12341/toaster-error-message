#!/usr/bin/env python3
"""Write this entry's toaster error message to entry.txt in the output folder."""

import os

# The gate checks entry.txt as UTF-8 text of 1-120 characters: this
# message is 114 code points, in the toaster's own apologetic voice.
TEXT = "I am sorry. Your bread went in as bread and came out as charcoal for the third time. I am beginning to suspect me."


def write_entry(out_dir: str) -> None:
    """Write the error message, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
