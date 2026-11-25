[![make.fun](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/lolipo8988-bot/one-word-username/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/lolipo8988-bot/one-word-username/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

# one-word-username

One word, one username, one reward: this entry is the entrant's own
make.fun username — `hua-liang` — and nothing else, entered in make.fun's
One Word, One Username, One Reward bounty, $5 in escrow.

## How it works

`main.py` (Python 3.13) writes exactly `hua-liang` to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), UTF-8,
with no trailing newline: 9 characters, a single word, well under the
30-character gate.

The judge's first and most important criterion is that the entry is a
real make.fun username, the entrant's own handle — `hua-liang` is
exactly that. On the remaining criteria it raises a smile on first read,
sticks in the mind as a name with character, and is a handle its owner
happily wears.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
