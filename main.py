#!/usr/bin/env python3
"""make.fun entry: news-image-20261122.

The graded program. It takes the newspaper image that build_image.py
rendered from news.json (image.png, 1024x1024, ten stories from Sunday
22 November 2026) and places an exact copy of it where the grader
expects the entry, as entry.png.

Nothing here reaches the network, reads a clock, or rolls dice: the
output is a byte-for-byte copy of the image shipped in this repo, so
every run writes the same bytes. Only the standard library is used.

Local run:
    python3 main.py            # writes output/entry.png

Grader run:
    python3 -P -s /bot/main.py # writes $MAKEFUN_OUTPUT_DIR/entry.png
"""
import os
import shutil
import sys
from pathlib import Path

IMAGE = Path(__file__).resolve().parent / "image.png"
ENTRY = "entry.png"


def destination():
    # The grader sets MAKEFUN_OUTPUT_DIR; a local run without it falls
    # back to an output/ folder next to this file.
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    base = Path(raw) if raw else Path(__file__).resolve().parent / "output"
    base.mkdir(parents=True, exist_ok=True)
    return base / ENTRY


def run():
    shutil.copyfile(IMAGE, destination())
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
