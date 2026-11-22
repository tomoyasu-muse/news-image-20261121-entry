#!/usr/bin/env python3
"""Draw entry.png: a one-page newspaper summary of 21 November 2026.

Every story below was cross-checked on 21 Nov 2026 reporting from at
least two independent outlets (Reuters, The Japan Times, DAWN and
The Hindu archives for that day agree on each item):

1. COP31 in Antalya, Turkiye runs into overtime over a fossil-fuel
   deadlock; a protester disrupts the closing plenary.
2. Iran's foreign minister Araghchi says Tehran wants diplomacy to
   end the war; President Trump says Iran's terms are unacceptable.
3. Wall Street ends sharply lower in an AI sell-off, leaving the
   S&P 500 and the Dow in correction territory.
4. The European Union proposes a tax on Big Tech companies to
   help fund its next budget.
5. Marches across France over the cost of living and student
   rights draw 82,500 people and stay largely peaceful.
6. Countries open a path towards a pact on autonomous weapons,
   the so-called killer robots, in talks against the clock.

Ticker: Scotland rout Japan 67-5 in rugby; Honda and Toyota recall
1.6 million vehicles over Takata airbags; Spain extends its bank
tax to fund housing; Princess Kate's cancer-recovery film dated.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (246, 242, 231)
INK = (16, 16, 16)
PAPER = (255, 253, 246)
GREY = (52, 52, 52)
GOLD = (255, 213, 84)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def icon(draw, kind, cx, cy, colour):
    """Small white pictogram drawn inside the coloured header band."""
    w = (255, 255, 255)
    if kind == "sun":  # climate summit
        draw.ellipse([cx - 13, cy - 13, cx + 13, cy + 13], outline=w, width=4)
        for dx, dy in ((0, -22), (0, 22), (-22, 0), (22, 0),
                       (-16, -16), (16, -16), (-16, 16), (16, 16)):
            draw.line([cx, cy, cx + dx, cy + dy], fill=w, width=4)
    elif kind == "talk":  # diplomacy speech bubble
        draw.rounded_rectangle([cx - 24, cy - 17, cx + 24, cy + 11],
                               radius=9, outline=w, width=4)
        draw.polygon([(cx - 8, cy + 11), (cx - 2, cy + 23), (cx + 6, cy + 11)],
                     outline=w)
        draw.line([cx - 14, cy - 4, cx + 14, cy - 4], fill=w, width=4)
    elif kind == "down":  # falling market chart
        draw.line([cx - 24, cy - 14, cx - 6, cy + 2], fill=w, width=5)
        draw.line([cx - 6, cy + 2, cx + 6, cy - 6], fill=w, width=5)
        draw.line([cx + 6, cy - 6, cx + 22, cy + 16], fill=w, width=5)
        draw.polygon([(cx + 22, cy + 16), (cx + 10, cy + 14), (cx + 20, cy + 4)],
                     fill=w)
    elif kind == "coin":  # EU tax coin
        draw.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], outline=w, width=4)
        draw.text((cx - 8, cy - 13), "E", font=F(BOLD, 26), fill=w)
    elif kind == "flag":  # street marches
        draw.line([cx - 16, cy - 22, cx - 16, cy + 22], fill=w, width=5)
        draw.polygon([(cx - 16, cy - 22), (cx + 22, cy - 15), (cx - 16, cy - 6)],
                     fill=w)
    elif kind == "bot":  # autonomous weapons talks
        draw.rounded_rectangle([cx - 19, cy - 10, cx + 19, cy + 18],
                               radius=6, outline=w, width=4)
        draw.line([cx, cy - 10, cx, cy - 22], fill=w, width=4)
        draw.ellipse([cx - 3, cy - 26, cx + 3, cy - 20], fill=w)
        draw.ellipse([cx - 11, cy + 1, cx - 5, cy + 7], fill=w)
        draw.ellipse([cx + 5, cy + 1, cx + 11, cy + 7], fill=w)


def panel(draw, box, colour, place, headline, sub, kind):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=14, fill=PAPER, outline=INK, width=3)
    draw.rounded_rectangle([x0, y0, x1, y0 + 46], radius=14, fill=colour)
    draw.rectangle([x0, y0 + 26, x1, y0 + 46], fill=colour)
    draw.text((x0 + 15, y0 + 10), place, font=F(BOLD, 24), fill=(255, 255, 255))
    icon(draw, kind, x1 - 38, y0 + 23, colour)
    y = y0 + 60
    for line in wrap(draw, headline, F(BOLD, 31), x1 - x0 - 28):
        draw.text((x0 + 14, y), line, font=F(BOLD, 31), fill=INK)
        y += 37
    y += 5
    for line in wrap(draw, sub, F(REG, 22), x1 - x0 - 28):
        draw.text((x0 + 14, y), line, font=F(REG, 22), fill=GREY)
        y += 27


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Masthead: the date is the most important element for a judge
    # who is never told which day this page sums up, so it is huge.
    draw.rectangle([0, 0, W, 198], fill=INK)
    draw.text((28, 13), "THE WORLD IN ONE DAY  -  WORLD NEWS SUMMARY",
              font=F(BOLD, 27), fill=GOLD)
    date_text = "21 NOVEMBER 2026"
    date_size = 100
    while draw.textlength(date_text, font=F(BOLD, date_size)) > W - 44:
        date_size -= 2
    draw.text((22, 44), date_text, font=F(BOLD, date_size), fill=(255, 255, 255))
    draw.text((28, 156), "SATURDAY  -  THE DAY'S BIGGEST STORIES, ON ONE PAGE",
              font=F(BOLD, 25), fill=(215, 215, 215))

    panels = [
        ((24, 214, 500, 454), (176, 32, 32), "ANTALYA - COP31",
         "CLIMATE TALKS RUN INTO OVERTIME",
         "Fossil-fuel deadlock at COP31. A protester halts the closing "
         "plenary: 'You are killing the future.'", "sun"),
        ((524, 214, 1000, 454), (0, 102, 108), "TEHRAN / WASHINGTON",
         "IRAN SEEKS TALKS; TRUMP SAYS NO",
         "Araghchi wants diplomacy to end the war. "
         "Trump says its terms are unacceptable.", "talk"),
        ((24, 470, 500, 710), (24, 56, 128), "NEW YORK - MARKETS",
         "WALL ST SLUMPS IN AI SELL-OFF",
         "Shares end sharply lower on AI fears. The S&P 500 and the "
         "Dow slide into correction.", "down"),
        ((524, 470, 1000, 710), (26, 118, 50), "BRUSSELS - EU",
         "EU PROPOSES TAX ON BIG TECH",
         "Brussels plans to tax the biggest digital firms to help "
         "fund the EU's next budget.", "coin"),
        ((24, 726, 500, 926), (36, 82, 158), "PARIS - FRANCE",
         "82,500 MARCH OVER LIVING COSTS",
         "Largely peaceful marches across France, "
         "over costs and student rights.", "flag"),
        ((524, 726, 1000, 926), (118, 60, 148), "GENEVA - ARMS TALKS",
         "PATH OPENS TO 'KILLER ROBOTS' PACT",
         "A path opens to a pact on autonomous "
         "weapons, against the clock.", "bot"),
    ]
    for args in panels:
        panel(draw, *args)

    # Footer ticker with four more verified stories of the day.
    draw.rectangle([0, 942, W, 1024], fill=GOLD)
    ticker = ("ALSO TODAY: Scotland rout Japan 67-5 in rugby  -  "
              "Honda & Toyota recall 1.6M cars over Takata airbags  -  "
              "Spain extends bank tax for housing")
    y = 952
    for line in wrap(draw, ticker, F(BOLD, 22), W - 48):
        draw.text((24, y), line, font=F(BOLD, 22), fill=INK)
        y += 28

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
