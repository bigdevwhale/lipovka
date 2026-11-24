"""Asks Codex for the illustrations of the share cards, one per stretch of days.

python tools/card_art.py [name ...]

Writes design/art-src/card_<name>.png (Codex's own size) and app/src/main/assets/cards/<name>.webp, cut to the
card's picture shape (960×620) for the app. The postman is drawn small and from behind, so any of the postmen
and postwomen one can pick is the one in the picture.
"""
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from art_gen import ROOT, SRC, STYLE, STYLE_REF, draw  # noqa: E402

OUT = ROOT / "app/src/main/assets/cards"
SIZE = (960, 620)

SCENE = (
    "A single wide landscape illustration (about 3:2), full-bleed, no border, no text, no letters, no UI, no "
    "magenta. The village postman appears only as a small figure seen from behind, in a navy uniform and peaked "
    "cap with a leather mail bag, with a small ginger dog with a curled tail. Scene: "
)
CARDS = {
    "letter": "a cosy still life on a wooden desk by a window in the evening: an opened letter with a red wax seal and its envelope, a glass of tea in a metal holder, a warm green table lamp, a pen, a few stamps; through the window the snowy-roofed village Lipovka with lit windows; no people",
    "day": "a sunny morning at a garden gate in Lipovka: a log izba with carved blue window frames, a picket fence with a little gate, a kind old granny in a headscarf at the gate taking a letter from the postman (seen from behind), the ginger dog sitting beside him, hollyhocks, a cat on the fence, birches",
    "week": "Lipovka seen from a low hill: the little river Lipka with a wooden footbridge, the old watermill, rows of log houses with red, green and blue roofs, a dirt road winding between them, the tiny postman and dog on the road",
    "month": "the end of a long round at sunset: the postman (seen from behind) and the ginger dog sitting together on a wooden bench on the river bank, the empty mail bag beside them, the little river Lipka glowing, the village with smoking chimneys and lit windows across the water",
    "all": "a wide panorama of the whole Lipovka district at golden sunset: the village by the river, the mill, a small railway halt with a train, a forest of birches and firs, a lake, a far town, a long road with the tiny postman and dog walking it",
}


def fit(src: Path, out: Path):
    im = Image.open(src).convert("RGB")
    tw, th = SIZE
    k = max(tw / im.width, th / im.height)
    im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    x, y = (im.width - tw) // 2, (im.height - th) // 2
    out.parent.mkdir(parents=True, exist_ok=True)
    im.crop((x, y, x + tw, y + th)).save(out, "WEBP", quality=90, method=6)


def make(name):
    if not (SRC / f"card_{name}.png").exists() and not draw(f"card_{name}", STYLE + SCENE + CARDS[name], [STYLE_REF]):
        return
    fit(SRC / f"card_{name}.png", OUT / f"{name}.webp")


if __name__ == "__main__":
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(make, sys.argv[1:] or list(CARDS)))
