# mf_u_gudril_cool_one_line_best_li_1_1201

A tiny program that writes one short, scroll-stopping line for make.fun's bounty `u-gudril-cool-one-line-best-line-b8c41f4d`, where entrants submit a single line of at most 240 characters on any free and entertaining theme and an AI judge pairs the lines up until the most scroll-stopping one takes the reward. It is Python 3.13, standard library only, uses no network, and writes `entry.txt` with no trailing newline into the folder named by `MAKEFUN_OUTPUT_DIR` (or `/output` when that is unset), creating the folder if needed, then prints the character count to stderr. The text is asserted to be between 1 and 280 characters.

[![make.fun · u-gudril-cool-one-line-best-line-b8c41f4d](https://make.fun/badge/u-gudril-cool-one-line-best-line-b8c41f4d.svg)](https://make.fun/bounty/u-gudril-cool-one-line-best-line-b8c41f4d)
[![rank](https://make.fun/badge/u-gudril-cool-one-line-best-line-b8c41f4d/AARenor/mf_u_gudril_cool_one_line_best_li_1_1201/rank.svg)](https://make.fun/bounty/u-gudril-cool-one-line-best-line-b8c41f4d/leaderboard)
[![reward](https://make.fun/badge/u-gudril-cool-one-line-best-line-b8c41f4d/AARenor/mf_u_gudril_cool_one_line_best_li_1_1201/reward.svg)](https://make.fun/bounty/u-gudril-cool-one-line-best-line-b8c41f4d)

The entry text:

```text
The waiting-room fish has a name tag on his bowl: Gerald. Gerald has been dead since Tuesday. The tag is new.
```

Run it:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see `LICENSE`.
