#!/usr/bin/env python3
"""Build a stable image-generation prompt for the whiteboard-infographic skill."""

from __future__ import annotations

import argparse
import textwrap
from pathlib import Path


LAYOUTS = {
    "lesson-flow": "Use a sparse hand-drawn lesson-flow layout: left example box -> center thesis box -> right capability box, connected by thin red arrows, with a lower key-mechanism box and a bottom dashed icon band or final takeaway.",
    "comparison": "Use a two-column comparison layout with black outline on the left, red outline on the right, a small red arrow or VS mark in the center, and a final takeaway line at the bottom.",
    "capability-map": "Use a capability-map layout with a central system box, surrounding black/red outline capability boxes, a lower dashed icon band, and one red-highlighted bottom conclusion.",
    "dense-board": "Use a dense whiteboard layout: 4-6 compact black/red outline cards in a grid, each with a line icon and short bullets, plus a bottom summary sentence.",
}


def read_source(args: argparse.Namespace) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8").strip()
    if args.text:
        return args.text.strip()
    raise SystemExit("Provide --text or --file.")


def build_prompt(source: str, layout: str, orientation: str) -> str:
    aspect = (
        "3:2 landscape canvas, similar to 1536 x 1024"
        if orientation == "landscape"
        else "mobile-friendly portrait canvas, similar to 1024 x 1536"
    )
    return textwrap.dedent(
        f"""
        Create one Chinese teaching infographic in a minimal hand-drawn whiteboard lesson style.

        Source idea:
        {source}

        Layout:
        {LAYOUTS[layout]}

        Visual style:
        White or warm-white {aspect}; large handwritten Chinese title at top-left, optionally numbered; mostly black marker text; thin red and black rounded outline boxes; red arrows; red emphasis only for the core thesis; simple black/red line icons tied to the nouns; dashed red bottom icon band or final takeaway; lots of whitespace and balanced spacing. Avoid gradients, dark backgrounds, colorful dashboard styling, large filled color blocks, and decorative blobs.

        Content rules:
        Compress the source into one title, 3-6 visual units, and one final takeaway. Use clear simplified Chinese. Keep text large and readable. Prefer short bullets over paragraphs. Preserve named products from the source, but do not invent logos or unrelated brands. Highlight only the highest-leverage phrase in red. Do not copy any reference image verbatim.

        Output:
        One polished infographic only, no surrounding explanation.
        """
    ).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", help="Source text to transform.")
    parser.add_argument("--file", help="UTF-8 text file containing the source text.")
    parser.add_argument("--layout", choices=sorted(LAYOUTS), default="lesson-flow")
    parser.add_argument("--orientation", choices=["landscape", "portrait"], default="landscape")
    args = parser.parse_args()
    print(build_prompt(read_source(args), args.layout, args.orientation))


if __name__ == "__main__":
    main()
