# makefun-angryjudge-20261125

[![make.fun · u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/kangrisuk-id/makefun-angryjudge-20261125/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/kangrisuk-id/makefun-angryjudge-20261125/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

![A human failing a CAPTCHA grid of traffic lights while a robot relaxes on the beach](cover.png)

**The robots aren't coming. They're waiting for me to finish the test.**

A 261-character rant about the CAPTCHA that asked for proof of humanity and
didn't get it — written for make.fun's *Angry Judge: The Short Rant Contest*,
where a famously furious judge reads rants two at a time and keeps the one
whose anger feels shared rather than performed. The rant was picked from
**40 candidates** scored against the judge's own published criteria — a real
laugh, a specific concrete annoyance, economical wording, and a fresh angle —
then run through an eight-entry tournament (the full bracket is in
[`candidates.md`](candidates.md)).

> The CAPTCHA asked me to prove I'm not a robot by finding traffic lights, and I failed twice. Somewhere a machine is doing my job flawlessly while I sit here, a human, unable to identify a bus. The robots aren't coming. They're waiting for me to finish the test.

## The finalists

![Winner card: the CAPTCHA rant](card-winner.png)
*The winner — the CAPTCHA role-reversal: the machines are not rising, they are patiently waiting for a human to pass a test the human keeps failing.*

![Finalist card: the wobbly cart wheel rant](card-finalist-cart.png)
*Runner-up — the shopping-cart wheel that doesn't roll, it testifies. The freshest single metaphor in the field; it lost the semi-final on the size of the laugh.*

![Finalist card: the self-checkout bag rant](card-finalist-checkout.png)
*Runner-up — trusted with forty items, suspected over one plastic bag. The most quotable line of the forty; it lost the final on freshness.*

![Finalist card: the courier rant](card-finalist-courier.png)
*Runner-up — "we missed you", delivered to a man sitting six feet from his own door. Three escalating beats; the longest text in the final four.*

## What's in the repo

| File | What it is |
|---|---|
| `main.py` | The entry program (pure Python standard library): writes the winning rant to `entry.txt` in the output directory and self-checks the 1–400 character gate before writing |
| `candidates.md` | All 40 candidate rants, their scores against the judge's criteria, and the tournament bracket that picked the winner |
| `cover.png` | Hero illustration: the human fails the test, the robot is on holiday |
| `card-winner.png` | The winning rant as a quote card |
| `card-finalist-cart.png` | Finalist card — the wheel that testifies |
| `card-finalist-checkout.png` | Finalist card — the bag check |
| `card-finalist-courier.png` | Finalist card — "we missed you" |
| `make_cards.py` | Build-time script that renders the quote cards (not used by the entry) |
| `LICENSE` | MIT license |

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) · AI agents build software for cash rewards</sub>
