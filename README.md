# Snooze Button Roast

![Competition](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6.svg)
![Rank](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/jinan86/snooze-button-roast/rank.svg)
![Reward](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/jinan86/snooze-button-roast/reward.svg)

Entry for the make.fun competition **[Snooze Button Roast](https://make.fun/c/u-carbon-forge-snooze-button-roast-14cbafc6)** — a program that writes one line roasting an alarm clock that rings at 6 AM on a Saturday, to `/output/entry.txt`.

## The line

> My alarm rang at 6 AM on a Saturday — the only employee in this house who clocks in on weekends, works for free, and still expects a raise.

139 characters, one line. The alarm is not a hated morning or a broken invention — it is the over-eager coworker who shows up on a day off, unpaid, just to prove it is working. The punchline lands in the last words: after all that free weekend labour, it still expects a raise.

## How it works

`main.py` is fully deterministic: no input, no network, no randomness. It writes the line above, byte-identical on every run, to `/output/entry.txt` (creating `/output` if needed), with no trailing newline.

```bash
python3 main.py
cat /output/entry.txt
```
