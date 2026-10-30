"""Builds the Google Play graphics in docs/google-play/graphics from the README screenshots.

python tools/play.py

Takes docs/screenshots/<lang>/*.jpg (1080 px wide renders of the demo, see tools/shots.py) and writes
the 512 px icon, the 1024x500 feature graphics and eight 1080x1920 captioned screenshots per language.
Play wants screenshots no longer than twice their width, so each screen is cut short under its caption.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs/google-play/graphics"
SHOTS = ROOT / "docs/screenshots"
FONT = ROOT / "app/src/main/res/font/m6x11.ttf"

GREEN = (0x3D, 0x5E, 0x43)
GREEN_DEEP = (0x1B, 0x2B, 0x22)
LIGHT = (0xFB, 0xF3, 0xDC)
INK = (0x22, 0x16, 0x0F)
LAMP = (0xF4, 0xCC, 0x5A)
RED = (0xA3, 0x3A, 0x2C)
BLUE = (0x26, 0x37, 0x5E)

# The order they appear in the store, with the caption over each: a light line and a lamp-yellow one.
PAGES = [
    ("1-post", ("Your real steps carry", "the village post"), ("Ваши шаги несут", "деревенскую почту")),
    ("2-gate", ("At the gate: the news", "and a jar of jam"), ("У калитки — новости", "и банка варенья")),
    ("3-village", ("A village that grows", "as you walk"), ("Деревня растёт", "с каждым километром")),
    ("8-letter", ("Stories that unfold", "over years"), ("Истории длятся", "годами")),
    ("4-room", ("Gifts fill your room", "above the post office"), ("Подарки — в комнату", "над почтой")),
    ("6-evening", ("The evening lamp", "and the day's news"), ("Вечером — лампа", "и новости дня")),
    ("5-album", ("Stamps go", "into the album"), ("Марки —", "в альбом")),
    ("7-diary", ("The postman's diary,", "kilometre by kilometre"), ("Дневник почтальона,", "километр за километром")),
]


def font(size):
    return ImageFont.truetype(str(FONT), size)


def fit(text, size, width):
    """m6x11 is drawn on a 16-unit grid, so it shrinks a whole pixel step at a time and stays crisp."""
    while font(size).getlength(text) > width:
        size -= 16
    return font(size)


def airmail(d, y, w, h=24, step=48):
    """The red and blue stripes of an airmail envelope's edge."""
    for x in range(-h, w + h, step):
        for dx, colour in ((0, RED), (step // 2, BLUE)):
            x0 = x + dx
            d.polygon([(x0, y), (x0 + step // 4, y), (x0 + step // 4 + h, y + h), (x0 + h, y + h)], fill=colour)


def board(w, h):
    g = Image.new("RGB", (w, h), GREEN)
    d = ImageDraw.Draw(g)
    d.fontmode = "1"
    d.rectangle((0, 0, w, 24), fill=LIGHT)
    airmail(d, 0, w)
    return g.convert("RGBA")


def lay(g, card, x, y):
    """A screen on the board: a soft shadow and a thick pixel-ink frame round it."""
    sh = Image.new("RGBA", (card.width + 80, card.height + 80), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle((40, 50, 40 + card.width, 50 + card.height), fill=(10, 20, 12, 130))
    g.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)), (x - 40, y - 40))
    g.alpha_composite(card.convert("RGBA"), (x, y))
    ImageDraw.Draw(g).rectangle((x - 6, y - 6, x + card.width + 5, y + card.height + 5), outline=INK, width=6)


def screenshot(src, caption):
    W, H = 1080, 1920
    g = board(W, H)
    d = ImageDraw.Draw(g)
    d.fontmode = "1"
    size = min(fit(line, 96, W - 120).size for line in caption)
    title = font(size)
    d.text((W / 2, 130), caption[0], font=title, fill=LIGHT, anchor="mm")
    d.text((W / 2, 230), caption[1], font=title, fill=LAMP, anchor="mm")
    im = Image.open(src).convert("RGB")
    w = 840
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    top = 330
    # The screen runs off the bottom edge, like a road that goes on.
    lay(g, im.crop((0, 0, w, H - top + 20)), (W - w) // 2, top)
    return g.convert("RGB")


def feature(lang):
    W, H = 1024, 500
    g = board(W, H)
    d = ImageDraw.Draw(g)
    d.fontmode = "1"
    d.rectangle((0, H - 24, W, H), fill=LIGHT)
    airmail(d, H - 24, W)
    # The postman at the gate with a letter.
    gate = Image.open(SHOTS / lang / "2-gate.jpg").convert("RGB").crop((0, 0, 1080, 1060))
    gate = gate.resize((round(gate.width * 380 / gate.height), 380), Image.LANCZOS)
    lay(g, gate, W - gate.width - 52, 60)
    logo = Image.open(ROOT / "docs/logo.png").convert("RGBA").crop((40, 104, 472, 448))
    logo = logo.resize((logo.width // 4, logo.height // 4), Image.NEAREST)
    g.alpha_composite(logo, (48, 70))
    name, lines = ("Lipovka Post", ["Your steps carry", "the village post"]) if lang == "en" else \
        ("Почта в Липовке", ["Ваши шаги несут", "деревенскую почту"])
    d.text((48, 180), name, font=fit(name, 80, 470), fill=LIGHT)
    d.rectangle((48, 278, 500, 283), fill=GREEN_DEEP)
    sub = fit(max(lines, key=lambda l: font(48).getlength(l)), 48, 470)
    for i, l in enumerate(lines):
        d.text((48, 306 + i * 58), l, font=sub, fill=LAMP if i == 1 else LIGHT)
    g.convert("RGB").save(OUT / f"feature-graphic-{lang}.png", optimize=True)


def icon():
    """The README logo is already a full square, so Play's mask finds no corners."""
    Image.open(ROOT / "docs/logo.png").convert("RGB").resize((512, 512), Image.NEAREST).save(OUT / "icon-512.png", optimize=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    icon()
    for lang in ("en", "ru"):
        feature(lang)
        folder = OUT / f"screenshots-{lang}"
        folder.mkdir(exist_ok=True)
        for i, (name, en, ru) in enumerate(PAGES, 1):
            screenshot(SHOTS / lang / f"{name}.jpg", en if lang == "en" else ru).save(folder / f"{i}.png", optimize=True)
    print("done:", OUT)


if __name__ == "__main__":
    main()
