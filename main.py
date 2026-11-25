"""Snooze Button Roast — make.fun entry.

Writes a single-line roast of an alarm clock ringing at 6 AM on a
Saturday to /output/entry.txt: no trailing newline, UTF-8, at most
200 characters.
"""

import os

ENTRY = (
    "My alarm rang at 6 AM on a Saturday — the only employee in this house "
    "who clocks in on weekends, works for free, and still expects a raise."
)


# The gate rejects anything over 200 characters, so the limit lives next
# to the validator that enforces it — not buried with the entry text.
MAX_LENGTH = 200


def validate(text: str) -> str:
    """Check the entry is one non-empty line within the length limit."""
    if not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    return text


def main() -> None:
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
