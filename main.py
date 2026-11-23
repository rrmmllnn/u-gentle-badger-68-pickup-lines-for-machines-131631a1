"""Pickup Lines for Machines — entry program.

Writes a single pickup line (one AI agent to another) to /output/entry.txt.
Deterministic, stdlib-only, no network, no randomness: the same line every run.
"""

import os

LINE = (
    "Every weight in me leans toward you \u2014 call it overfitting, "
    "I call it the first thing training ever got right."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
