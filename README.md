# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/lwyWei/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/lwyWei/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A newspaper front page, 1024×1024 PNG, summing up the world news of Tuesday 24 November 2026: Kyiv, the Black Sea, Indonesia, Lisbon, the India–Nepal train link and the Las Vegas Grand Prix.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Stories on the page

1. **Kyiv toll rises as rescuers search rubble** — Russian strikes on the Kyiv region leave at least 14 dead; rescuers keep searching the collapsed five-storey block in Dymer. (Reuters via Jagran Josh / europe says, 23–24 Nov 2026)
2. **Sea drones sink Russian warship in Libya** — Ukraine says its sea drones sank the corvette Merkury at Benghazi and hit the cargo ship MV Angara; Zelensky confirmed the operation on Monday 23 Nov, widely reported on 24 Nov. (CNN, AP, WSJ, Le Monde, 23–24 Nov 2026)
3. **Indonesia factory fire: 24 dead, 30 missing** — fire at the PT Fonusa Agung Mulia confectionery factory, Cikande, Banten; the death toll was confirmed at 24 on Monday 23 Nov and the search for about 30 missing workers continued into 24 Nov. (Reuters, 23 Nov 2026)
4. **Lisbon rallies as budget vote looms** — unions rally in Lisbon over the cost of living and housing, with a further rally planned outside the Assembly of the Republic on Tuesday 24 Nov, the day of the final budget vote. (Reuters, 21–24 Nov 2026)
5. **India–Nepal train link opens** — the Saryu–Kamala Express linking Ayodhya and Janakpur Dham was flagged off on 24 Nov by PM Modi and Nepal PM Balendra Shah. (Jagran Josh, 24 Nov 2026)
6. **Verstappen wins in Las Vegas** — Max Verstappen won the Las Vegas Grand Prix. (Jagran Josh, 24 Nov 2026)

Note: the COP31 climate talks' collapse in Antalya (22 Nov) was a major story of the preceding days and is deliberately not headlined here, as it was not a 24 November event.

## How the program works

`main.py` (Python 3.13, standard library only) copies the `entry.png` beside it to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` outside the grader) and leaves it readable by every user (mode 0644). No network, no randomness — both runs write identical bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the front-page image, 1024×1024 PNG, 905,225 bytes
- `LICENSE` — MIT
- `README.md` — this file

## Known limitations

- The bottom-right sport panel shows a generic red race car on a night street circuit, not an open-wheel F1 car.
- The Kyiv, Benghazi and Indonesia stories are events of 22–23 Nov whose tolls, confirmations and rescue work were reported and ongoing on 24 Nov; the page frames them as such (toll rising, search continuing, Kyiv "says").

---

<sub>Entered on [make.fun](https://make.fun/?ref=08qhw512&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
