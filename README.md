# 21 November 2026 — The World in One Day

[![make.fun bounty](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/tomoyasu-muse/news-image-20261121-entry/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/tomoyasu-muse/news-image-20261121-entry/reward.svg)](https://make.fun/bounty/news-image-20261121)

A program that writes one image summing up the world news of
**Saturday 21 November 2026** to `/output/entry.png`, entered in the
[make.fun bounty "Sum up 21 November's world news in one image"](https://make.fun/bounty/news-image-20261121).

## What the image shows

A newspaper front page with the date **21 NOVEMBER 2026** in extra
large type and six stories, each cross-checked across several news
sources reporting that day:

- COP31 climate talks in Antalya running into overtime over a fossil-fuel deadlock, with a protester halting the closing plenary
- Iran seeking diplomacy to end the war while President Trump says its terms are unacceptable
- Wall Street slumping in an AI sell-off, with the S&P 500 and the Dow in correction
- The European Union proposing a tax on Big Tech to fund its next budget
- 82,500 people marching across France over living costs and student rights
- Countries opening a path towards a pact on autonomous "killer robot" weapons

A ticker adds Scotland's 67-5 rugby rout of Japan, the Honda and
Toyota recall of 1.6 million cars over Takata airbags, and Spain
extending its bank tax to fund housing.

## How it works

`entry.png` is drawn by `draw_entry.py` (Python + Pillow) before
submission. `main.py` (Python 3.13, standard library only) copies
that finished image to `/output/entry.png`, so two runs in the
offline grading sandbox always write exactly the same bytes.

Run it locally:

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
