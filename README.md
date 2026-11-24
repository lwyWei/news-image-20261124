# The World — Tuesday 24 November 2026

Draft entry for the make.fun bounty `news-image-20261124`
("Sum up 24 November's world news in one image").
**Draft only — not submitted.**

## What it is

A newspaper front page, 1024×1024 PNG, that sums up the world news of
Tuesday 24 November 2026. The masthead names the day; the lead story and
five further panels cover the day across regions and fields.

## Stories on the page

1. **Kyiv toll rises as rescuers search rubble** — Russian strikes on the
   Kyiv region leave at least 14 dead; rescuers keep searching the
   collapsed five-storey block in Dymer. (Reuters via Jagran Josh /
   europe says, 23–24 Nov 2026)
2. **Sea drones sink Russian warship in Libya** — Ukraine says its sea
   drones sank the corvette Merkury at Benghazi and hit the cargo ship
   MV Angara; Zelensky confirmed the operation on Monday 23 Nov, widely
   reported on 24 Nov. (CNN, AP, WSJ, Le Monde, 23–24 Nov 2026)
3. **Indonesia factory fire: 24 dead, 30 missing** — fire at the
   PT Fonusa Agung Mulia confectionery factory, Cikande, Banten; the
   death toll was confirmed at 24 on Monday 23 Nov and the search for
   about 30 missing workers continued into 24 Nov. (Reuters, 23 Nov 2026)
4. **Lisbon rallies as budget vote looms** — unions rally in Lisbon over
   the cost of living and housing, with a further rally planned outside
   the Assembly of the Republic on Tuesday 24 Nov, the day of the final
   budget vote. (Reuters, 21–24 Nov 2026)
5. **India–Nepal train link opens** — the Saryu–Kamala Express linking
   Ayodhya and Janakpur Dham was flagged off on 24 Nov by PM Modi and
   Nepal PM Balendra Shah. (Jagran Josh, 24 Nov 2026)
6. **Verstappen wins in Las Vegas** — Max Verstappen won the Las Vegas
   Grand Prix. (Jagran Josh, 24 Nov 2026)

Note: the COP31 climate talks' collapse in Antalya (22 Nov) was a major
story of the preceding days and is deliberately not headlined here, as
it was not a 24 November event.

## How the program works

`main.py` (Python 3.13, standard library only) copies the `entry.png`
beside it to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`
outside the grader). No network, no randomness — both runs write
identical bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the front-page image, 1024×1024 PNG, 905,225 bytes
- `LICENSE` — MIT
- `README.md` — this file

## Test

Run twice with different output dirs and compare hashes:

```sh
mkdir -p /tmp/out1 /tmp/out2
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png
```

## Known limitations

- The bottom-right sport panel shows a generic red race car on a night
  street circuit, not an open-wheel F1 car.
- The Kyiv, Benghazi and Indonesia stories are events of 22–23 Nov whose
  tolls, confirmations and rescue work were reported and ongoing on
  24 Nov; the page frames them as such (toll rising, search continuing,
  Kyiv "says").
