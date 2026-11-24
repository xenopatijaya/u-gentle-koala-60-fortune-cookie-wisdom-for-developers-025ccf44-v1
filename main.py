"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line (103 characters) to
/output/entry.txt. Python standard library only.
"""

import os

ENTRY = (
    "The code you wrote at midnight will meet you at noon, "
    "polite, patient, and nothing like what you meant."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip() == ENTRY
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
