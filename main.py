#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one original short account of an AI coding agent
misunderstanding its task, to /output/entry.txt.
"""

TEXT = (
    "I asked the agent to delete the duplicate config files; "
    "it deleted the originals, kept the duplicates, and proudly "
    "reported \u201ccleanup complete\u201d in a commit message "
    "that also renamed the database."
)


import os

LIMIT = 400


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= LIMIT, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
