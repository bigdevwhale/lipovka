"""Writes the QR code of the Google Play page that the share cards carry.

pip install segno; python tools/qr.py

The code never changes, so the app keeps it as rows of 0 and 1 (app/src/main/resources/qr_play.txt) instead of
carrying a QR library.
"""
from pathlib import Path

import segno

URL = "https://play.google.com/store/apps/details?id=app.lipovka"
OUT = Path(__file__).resolve().parent.parent / "app/src/main/resources/qr_play.txt"

q = segno.make(URL, error="m", micro=False)
OUT.write_text("".join("".join("1" if c else "0" for c in row) + "\n" for row in q.matrix))
