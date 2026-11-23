"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt. Deterministic, no network,
no input files, standard library only.
"""

import os

JOKE = "My AI agent demoed my app live, fixed one bug on stage, broke login \u2014 and the client called it agile."


def main() -> None:
    text = JOKE
    chars = len(text)
    assert 1 <= chars <= 280, f"joke must be 1-280 chars, got {chars}"
    assert text.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Verify the write landed exactly: re-read and compare.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the joke"


if __name__ == "__main__":
    main()
