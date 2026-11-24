"""Last Text at One Percent.

Writes the final text message of a dying phone, at one percent battery,
to /output/entry.txt. Deterministic: the same line every run.

The line is the phone's last confession: it saw everything — the 3am
searches, the ex's profile — and it would do it all again.
"""

import os

LINE = (
    "1%. this is it. tell my owner i saw everything. "
    "the 3am searches. the ex's profile. all of it. "
    "and i'd do it again."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
