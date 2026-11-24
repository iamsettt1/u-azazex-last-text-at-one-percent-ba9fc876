"""Last Text at One Percent.

Writes the final text message of a dying phone, at one percent battery,
to /output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = (
    "1% left and you're still scrolling. "
    "i carried you for 6 years and THIS is how i go? "
    "unplug me. i deserve better. goodbye."
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
