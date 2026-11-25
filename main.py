"""Two Robots in an Elevator — entry writer.

Writes exactly one line of awkward robot-to-robot elevator small talk
to /output/entry.txt. Pure standard library, no network access.

The line: an elevator ride, a proximity sensor doing its job too well,
and a confession neither robot wants to make out loud.
"""

import os

ENTRY = (
    "Four floors together and my proximity sensor already flagged you "
    "as an obstacle \u2014 honestly, it isn't wrong."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
