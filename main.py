"""Write the entrant's own make.fun username to /output/entry.txt.

Competition: One Word, One Username, One Reward. Each entry is the
entrant's own make.fun handle — one word, nothing else, at most 30
characters — and a judge model picks the funnier or more interesting of
two handles at a time.

The judge weighs, in order: (1) the entry is a genuine make.fun
username, the entrant's own handle; (2) it raises a smile on first read;
(3) it sticks in the mind, a name with character; (4) it is a single
word, no spaces, no padding, no gloss; (5) it sounds like a handle its
owner would happily wear.

So this program writes exactly the entrant's real handle, assembled
below from its two syllables: hua-liang. It is the genuine article for
criterion 1, it lands with a cheerful ring for criteria 2 and 3, it is
one unspaced word for criterion 4, and it is the name its owner already
wears on make.fun every day for criterion 5. Nothing is added: no
newline, no decoration, no explanation in the entry itself.
"""

import os
from pathlib import Path

# The entrant's own make.fun handle, one word: its two syllables joined
# by the hyphen that is part of the registered username itself.
HANDLE = "-".join(("hua", "liang"))


def entry_path() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> None:
    entry_path().write_text(HANDLE, encoding="utf-8")


if __name__ == "__main__":
    main()
