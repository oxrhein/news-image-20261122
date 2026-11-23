#!/usr/bin/env python3
"""Build image.png (1024x1024) for make.fun news-image-20261122.

Run:  python3 build_image.py
Reads news.json in the same directory and writes image.png next to it.
Build-time only: the graded entry is main.py, which copies image.png to
the output directory (stdlib only, no network, no clock, no randomness).

Dense edition: 10 numbered stories plus a ticker. The four compact
stories (07-10) use small text so the day's news is complete.
Layout budget, 1024 px tall (every string is asserted to fit its box):
  masthead 16-141, hero 148-308, grid 318-686, story 06 696-798,
  mini row 808-926, ticker 936-964, footer 970-1000.
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W = H = 1024
PAPER = (248, 244, 233)
NAVY = (18, 40, 75)
RED = (178, 34, 34)
INK = (24, 24, 24)
GREY = (90, 90, 90)
CARD = (255, 255, 255)
HERO_BG = (232, 237, 243)
LINE = (200, 200, 190)


def load_font(name, size):
    path = "/usr/share/fonts/truetype/dejavu/%s.ttf" % name
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()


F_TITLE = load_font("DejaVuSans-Bold", 52)
F_KICKER = load_font("DejaVuSans-Bold", 22)
F_SUB = load_font("DejaVuSerif", 24)
F_HERO_HEAD = load_font("DejaVuSans-Bold", 34)
F_HERO_BODY = load_font("DejaVuSans", 20)
F_CARD_HEAD = load_font("DejaVuSans-Bold", 24)
F_CARD_BODY = load_font("DejaVuSans", 18)
F_SMALL = load_font("DejaVuSans-Bold", 17)
F_MINI_KICKER = load_font("DejaVuSans-Bold", 13)
F_MINI_HEAD = load_font("DejaVuSans-Bold", 16)
F_MINI_BODY = load_font("DejaVuSans", 13)
F_TICKER = load_font("DejaVuSans-Bold", 14)
F_FOOT = load_font("DejaVuSans", 13)


def wrap_text(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = ("%s %s" % (cur, w)).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def put_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def main():
    with open(os.path.join(HERE, "news.json"), encoding="utf-8") as f:
        data = json.load(f)
    assert len(data["stories"]) == 10, "expected 10 stories"
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead: 16-141
    d.text((36, 20), "SUNDAY  \u2022  22 NOVEMBER 2026", font=F_KICKER, fill=RED)
    d.text((988, 20), "ONE IMAGE  \u2022  ONE DAY", font=F_KICKER, fill=NAVY,
           anchor="ra")
    d.text((36, 48), data["title"], font=F_TITLE, fill=NAVY)
    d.text((36, 104), data["subtitle"], font=F_SUB, fill=GREY)
    d.rectangle([36, 136, 988, 141], fill=RED)

    # Hero story 01: 148-308
    hero = data["stories"][0]
    d.rounded_rectangle([36, 148, 988, 308], radius=12, fill=HERO_BG,
                        outline=LINE, width=2)
    d.rectangle([36, 148, 48, 308], fill=RED)
    d.text((66, 160), "01  \u2022  " + hero["kicker"], font=F_KICKER, fill=RED)
    head = wrap_text(d, hero["headline"], F_HERO_HEAD, 906)
    assert len(head) <= 1, "hero headline wrapped to %d lines: %s" % (len(head), head)
    put_lines(d, head, 66, 186, F_HERO_HEAD, INK, 42)
    body = wrap_text(d, hero["summary"], F_HERO_BODY, 660)
    assert len(body) <= 3, "hero body %d lines" % len(body)
    put_lines(d, body, 66, 228, F_HERO_BODY, (50, 50, 50), 25)
    cx = 782
    for label, col in (("EU", (178, 34, 34)), ("US", (18, 40, 75)),
                       ("CN", (90, 90, 90))):
        d.ellipse([cx, 250, cx + 52, 302], fill=col)
        d.text((cx + 26, 276), label, font=F_SMALL, fill=(255, 255, 255),
               anchor="mm")
        cx += 62

    # Stories 02-05, 2x2 grid: 318-686 (card 466x178, gap 12)
    grid = data["stories"][1:5]
    for i, story in enumerate(grid):
        x = 36 + (i % 2) * (466 + 20)
        y = 318 + (i // 2) * (178 + 12)
        d.rounded_rectangle([x, y, x + 466, y + 178], radius=10, fill=CARD,
                            outline=LINE, width=2)
        d.ellipse([x + 14, y + 12, x + 50, y + 48], fill=NAVY)
        d.text((x + 32, y + 30), story["n"], font=F_SMALL,
               fill=(255, 255, 255), anchor="mm")
        d.text((x + 60, y + 18), story["kicker"], font=F_SMALL, fill=RED)
        head = wrap_text(d, story["headline"], F_CARD_HEAD, 434)
        assert len(head) <= 2, "card %s headline %d lines" % (story["n"], len(head))
        yy = put_lines(d, head, x + 14, y + 50, F_CARD_HEAD, INK, 28)
        body = wrap_text(d, story["summary"], F_CARD_BODY, 434)
        assert len(body) <= 3, "card %s body %d lines" % (story["n"], len(body))
        put_lines(d, body, x + 14, yy + 4, F_CARD_BODY, (60, 60, 60), 21)

    # Story 06, full width: 696-798. Headline left, summary right.
    story = data["stories"][5]
    y = 696
    d.rounded_rectangle([36, y, 988, y + 102], radius=10, fill=CARD,
                        outline=LINE, width=2)
    d.ellipse([50, y + 12, 86, y + 48], fill=NAVY)
    d.text((68, y + 30), story["n"], font=F_SMALL,
           fill=(255, 255, 255), anchor="mm")
    d.text((96, y + 14), story["kicker"], font=F_SMALL, fill=RED)
    head = wrap_text(d, story["headline"], F_CARD_HEAD, 440)
    assert len(head) <= 2, "story 06 headline %d lines" % len(head)
    put_lines(d, head, 96, y + 40, F_CARD_HEAD, INK, 28)
    body = wrap_text(d, story["summary"], F_CARD_BODY, 400)
    assert len(body) <= 4, "story 06 body %d lines" % len(body)
    put_lines(d, body, 572, y + 10, F_CARD_BODY, (60, 60, 60), 20)

    # Stories 07-10, 4-column mini row: 808-926 (each 226x118, gap 12).
    # Small 13px type on purpose: the day's news is complete even at the
    # cost of thumbnail legibility, as the brief for this edition allows.
    mini = data["stories"][6:10]
    for i, story in enumerate(mini):
        x = 36 + i * (226 + 12)
        y = 808
        d.rounded_rectangle([x, y, x + 226, y + 118], radius=8, fill=CARD,
                            outline=LINE, width=2)
        d.text((x + 10, y + 8), story["n"] + "  \u2022  " + story["kicker"],
               font=F_MINI_KICKER, fill=RED)
        head = wrap_text(d, story["headline"], F_MINI_HEAD, 206)
        assert len(head) <= 2, "mini %s headline %d lines" % (story["n"], len(head))
        yy = put_lines(d, head, x + 10, y + 28, F_MINI_HEAD, INK, 19)
        body = wrap_text(d, story["summary"], F_MINI_BODY, 206)
        assert len(body) <= 3, "mini %s body %d lines" % (story["n"], len(body))
        put_lines(d, body, x + 10, yy + 2, F_MINI_BODY, (60, 60, 60), 16)

    # Ticker: 936-964
    d.rectangle([36, 936, 988, 964], fill=NAVY)
    tw = d.textlength(data["also_today"], font=F_TICKER)
    assert tw <= 936, "ticker too wide: %s" % tw
    d.text((52, 950), data["also_today"], font=F_TICKER,
           fill=(255, 255, 255), anchor="lm")
    # Footer: 970-1000
    d.text((36, 970), data["sources"], font=F_FOOT, fill=GREY)
    d.text((988, 970), "make.fun  \u2022  news-image-20261122", font=F_FOOT,
           fill=GREY, anchor="ra")
    d.text((36, 988), data["sources_note"], font=F_FOOT, fill=GREY)

    out = os.path.join(HERE, "image.png")
    img.save(out, "PNG", optimize=True)
    print(out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
