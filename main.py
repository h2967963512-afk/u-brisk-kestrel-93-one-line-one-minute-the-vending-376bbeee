"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one pickup line spoken by a vending machine to a
# passing human. One line, 94 characters — inside the 200-character
# gate. It is the machine itself speaking, draws on the machine's own
# world (snacks behind glass, the coil), and the punch lands in the
# last few words. Charming, not creepy.
# Revision note (parent pass): re-checked after the local run —
# the 94-character line is unchanged; this note only records the check.
import os

TEXT = (
    "I've got forty snacks behind this glass and not one of them "
    "makes my coil spin the way you do."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
