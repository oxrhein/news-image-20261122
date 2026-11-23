# news-image-20261122 — The World in One Image

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/oxrhein/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/oxrhein/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for the make.fun bounty **news-image-20261122** ($100, closes
Tue 24 Nov 2026 07:00 WIB / Mon 23 Nov 2026 24:00 UTC): sum up the
world news of Sunday 22 November 2026 in one image.

## Format

A one-page newspaper, "THE WORLD IN ONE IMAGE", following the format
that won the 19 November edition of this bounty (@superskie, $50):
a masthead naming the date, a hero story, four more stories in a 2×2
grid, a sixth full-width story, four compact stories in a mini row, an
"Also today" ticker and a sources footer. Cream paper, navy headlines,
red kickers — each story clear from its headline and short summary
alone. This edition is deliberately dense: ten stories, with small
type on the four compact ones, so the day's news is complete.

## The ten stories (all 22 November 2026)

1. **COP31 talks collapse with no deal at all** (Antalya, climate) —
   two weeks of negotiations ended with no agreement after the EU
   rejected a final draft with no mention of fossil fuels.
2. **Russian drone flattens Kyiv apartment block** (Ukraine) — a
   five-storey block partly destroyed; at least 14 people missing.
3. **Iran shows off underground 'missile city'** (Gulf) — footage of
   a new launcher firing two missiles at once, as Washington weighs
   renewed strikes.
4. **FBI probes hack of national crime database** (Washington, tech) —
   apparent breach of the National Crime Information Center.
5. **Candy factory fire kills 3, dozens missing** (Banten, Indonesia)
   — fire at a factory in Cikande; dozens still unaccounted for.
6. **BepiColombo reaches Mercury after 8 years** (space) — the
   Europe–Japan probe entered Mercury orbit after an eight-year
   journey.
7. **Mexico captures 'El Chapo Isidro'** (Guasave) — special forces
   seized cartel boss Fausto Isidro Meza Flores; 11 died in the raid.
8. **Minister quits over exam AI-cheating row** (Seoul) — education
   chief Choi Kyo-jin quit over CSAT cheating chaos.
9. **Funeral boat sinks, 24 dead** (Bayelsa, Nigeria) — a crowded
   boat to a burial capsized; 24 died, 24 were rescued.
10. **Sea drones hit Russian warship** (Benghazi, Libya) — suspected
    Ukrainian drones badly damaged the corvette Merkury at the base.

Also today: West Bank settler attacks condemned, Iran hits 3 tankers
near Hormuz, stocks slide on AI sell-off. Sources: CNN, AP, Reuters,
Korea JoongAng Daily, TBS, Al Jazeera — see `news.json` for the story
list and source URLs.

## How it works

`build_image.py` (Pillow, build time only) renders `image.png`
(1024×1024, 160,175 bytes, SHA-256
641a25543e097b2e32c6985c985e80053ba9c094315108c5f64a64d9420c0e3b)
from `news.json`. `main.py` is the graded entry: Python standard
library only, no network, no clock, no randomness — it copies
`image.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, so two runs write
byte-identical output.

Run locally:

    python3 build_image.py   # rebuild image.png from news.json
    python3 main.py          # writes output/entry.png

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=z55ph46d&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
