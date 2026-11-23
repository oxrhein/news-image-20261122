#!/usr/bin/env python3
"""Entry for make.fun news-image-20261122.

Writes one image, /output/entry.png in the grader, summarising the
world news of Sunday 22 November 2026 in a dense one-page newspaper:
10 stories plus a ticker.

The image is built at authoring time by build_image.py (Pillow, from
news.json) and shipped in this repository as image.png. This program
only copies those exact bytes to the output directory, using the
standard library only, with no network, no clock and no randomness,
so two runs write identical bytes.

Run locally:
    python3 main.py
    # writes output/entry.png

Grader:
    python3 -P -s /bot/main.py
    # writes $MAKEFUN_OUTPUT_DIR/entry.png
"""
import os
import shutil
import sys

SOURCE_NAME = "image.png"
OUTPUT_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.join(here, "output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, OUTPUT_NAME)
    shutil.copyfile(source, dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
