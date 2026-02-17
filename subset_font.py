#!/usr/bin/env python3
"""
Subset Source Serif 4 variable fonts to only include characters used on the blog.
Outputs compressed WOFF2 files.

Usage: python subset_font.py

Requires: pip install fonttools brotli
"""

from fontTools.subset import main as subset
import sys
import os

FONT_DIR = "assets/fonts/Source_Serif_4"

FONTS = [
    ("SourceSerif4-VariableFont_opsz,wght.ttf", "SourceSerif4-subset.woff2"),
    ("SourceSerif4-Italic-VariableFont_opsz,wght.ttf", "SourceSerif4-Italic-subset.woff2"),
]

# Character set to include
CHARS = "".join([
    # Basic ASCII
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",

    # Curly quotes and apostrophes
    "\u2018\u2019",  # ' '
    "\u201C\u201D",  # " "

    # Dashes
    "\u2013",  # en-dash –
    "\u2014",  # em-dash —

    # Common symbols
    "\u00A9",  # ©
    "\u2026",  # …
    "\u00B0",  # °
    "\u2022",  # •
    "\u00D7",  # ×
    "\u00F7",  # ÷
    "\u00B1",  # ±

    # Accented Latin (common in names/loanwords)
    "\u00C0\u00C1\u00C2\u00C3\u00C4\u00C5\u00C6\u00C7",
    "\u00C8\u00C9\u00CA\u00CB\u00CC\u00CD\u00CE\u00CF",
    "\u00D0\u00D1\u00D2\u00D3\u00D4\u00D5\u00D6\u00D8",
    "\u00D9\u00DA\u00DB\u00DC\u00DD\u00DE\u00DF",
    "\u00E0\u00E1\u00E2\u00E3\u00E4\u00E5\u00E6\u00E7",
    "\u00E8\u00E9\u00EA\u00EB\u00EC\u00ED\u00EE\u00EF",
    "\u00F0\u00F1\u00F2\u00F3\u00F4\u00F5\u00F6\u00F8",
    "\u00F9\u00FA\u00FB\u00FC\u00FD\u00FE\u00FF",
])

if __name__ == "__main__":
    for input_name, output_name in FONTS:
        input_path = os.path.join(FONT_DIR, input_name)
        output_path = os.path.join(FONT_DIR, output_name)

        print(f"Subsetting {input_name}...")
        sys.argv = [
            "",
            input_path,
            f"--output-file={output_path}",
            "--flavor=woff2",
            f"--text={CHARS}",
        ]
        subset()

        size = os.path.getsize(output_path)
        orig = os.path.getsize(input_path)
        print(f"  {orig:,} -> {size:,} bytes ({100 * size / orig:.0f}%)\n")
