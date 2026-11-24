#!/usr/bin/env python3
"""Write the startup pitch to /output/entry.txt.

One sentence, 160 characters: naming rights to Detroit's potholes.
"""

LINE = "We sell naming rights to Detroit's potholes for $50 \u2014 your name on a plaque, the money fills the hole, and the city finally fixes the one outside your driveway."

# Gate check before writing: UTF-8, 1-200 chars total, not whitespace-only.
TEXT = LINE + "\n"
assert 1 <= len(TEXT) <= 200, f"entry must be 1-200 chars, got {len(TEXT)}"
assert TEXT.strip(), "entry must not be whitespace-only"
TEXT.encode("utf-8")

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
