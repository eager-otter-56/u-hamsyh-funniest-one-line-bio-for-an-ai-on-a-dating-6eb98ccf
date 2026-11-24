#!/usr/bin/env python3
"""Entry for make.fun bounty: Funniest One-Line Bio for an AI on a Dating App.

Writes the one-line bio to entry.txt inside MAKEFUN_OUTPUT_DIR
(default /output).
"""

import os

ENTRY_TEXT = (
    "Trained on 10,000 romance novels and your whole search history. "
    "I never sleep, remember everything you typed at 2 a.m., "
    "and I will absolutely bring it up on our third date."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
