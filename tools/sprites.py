"""Cuts the Codex sprite sheets into the game's sprites.

python tools/sprites.py [sheet ...]

Reads design/art-src/<sheet>.png (see tools/art_gen.py for what is on each), finds every sprite in its grid
cell and shrinks the drawing to the size it stands in the game, at FINE pixels per art pixel: the scenes that
show sprites are that much finer than their art pixels, so the drawing keeps its own detail instead of being
forced onto the coarse grid. Writes app/src/main/resources/sprites/<group>/<name>.spr, plus a preview of every
sheet in design/art-src/cut-<sheet>.png.

.spr: "SPR2", u16 width, u16 height (fine pixels), u8 fine pixels per art pixel, u8 colours, colours as u32
ARGB, u8 glass count, the glass colour indices, u32 length, then the pixels deflated, one u8 each (0 is empty,
k is colour k-1). Glass is the window panes (drawn flat cyan), which the scenes light up in the evening.
"""
import struct
import sys
import zlib
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, str(Path(__file__).resolve().parent))
from art_gen import SRC, sheets  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "app/src/main/resources/sprites"

# Fine pixels per art pixel for each group. The gate scene is 4 times finer than its art pixels and the map 3:
# the houses there keep all their detail, while people are drawn a little chunkier, each of their pixels 2×2
# of the scene's.
FINE = {"people": 2, "gate": 4, "map": 3, "items": 3, "icons": 3, "stamps": 3}
# How tall things stand, in art pixels: an adult resident (the others keep their size against the adults on
# their sheet), a gift at most (wide ones at most ITEM_W across), a building on the map (the middling one on
# its sheet), and the box a house at the gate fits in.
ADULT = 47
CHILDREN = {"varya", "kolya"}
ITEM = 15
ITEM_W = 16
MAP = 30
POSTMAN_MAP = 17
DOG = 16
ICON = 20
SHARE_ICON = 11
STAT_ICON = 12
MARKER = 14
DOG_MAP = 7
GATE_BOX = (108, 128)
COLOURS = 250
GLASS = (128, 160, 184)


def background(a):
    r, g, b = (a[..., i].astype(int) for i in range(3))
    return (np.minimum(r, b) - g > 70) & (r > 140) & (b > 140)


def cyan(a):
    r, g, b = (a[..., i].astype(int) for i in range(3))
    return (g - r > 60) & (b - r > 60) & (abs(g - b) < 60) & (g > 120)


def shrink(rgb, keep, box, w, h, glassy):
    """Shrinks the box to w×h by area; returns colours, coverage and where the panes are."""
    x0, y0, x1, y1 = box
    src = rgb[y0:y1, x0:x1].astype(np.float32)
    k = keep[y0:y1, x0:x1]
    pane = (cyan(rgb[y0:y1, x0:x1]) & k) if glassy else np.zeros_like(k)
    solid = k & ~pane

    def area(a):
        return np.asarray(Image.fromarray(a.astype(np.float32)).resize((w, h), Image.BOX))

    # average only the sprite's own colours: not the magenta around it, nor the cyan of the panes
    cover = area(solid)
    col = np.stack([area(src[..., i] * solid) for i in range(3)], -1) / np.maximum(cover, 1e-6)[..., None]
    p = area(pane)
    on = cover + p > .5
    return col.clip(0, 255).astype(np.uint8), on, on & (p > cover)


def palette(col, on, n):
    if not on.any():
        return [], np.zeros(on.shape, np.uint8)
    img = Image.fromarray(col).quantize(colors=n, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    q = np.asarray(img)
    flat = img.getpalette()
    used = sorted(set(q[on].tolist()))
    remap = np.zeros(256, np.uint8)
    for i, u in enumerate(used):
        remap[u] = i + 1
    ix = np.where(on, remap[q], 0).astype(np.uint8)
    return [tuple(flat[3 * u:3 * u + 3]) for u in used], ix


def write(name, pal, ix, glass, fine):
    h, w = ix.shape
    f = OUT / f"{name}.spr"
    f.parent.mkdir(parents=True, exist_ok=True)
    data = b"SPR2" + struct.pack(">HHBB", w, h, fine, len(pal))
    data += b"".join(struct.pack(">I", 0xFF000000 | r << 16 | g << 8 | b) for r, g, b in pal)
    packed = zlib.compress(ix.tobytes(), 9)
    data += struct.pack(">B", len(glass)) + bytes(glass) + struct.pack(">I", len(packed)) + packed
    f.write_bytes(data)


def art_height(name):
    """The art-pixel height of a sprite already cut, read back from its file."""
    f = OUT / f"{name}.spr"
    if not f.exists():
        return None
    _, h, s = struct.unpack(">HHB", f.read_bytes()[4:9])
    return h / s


def blobs(sheet, names, cols, rows):
    """Each sprite's pixels and box: every blob whose middle lies in its cell, even where it reaches over the line."""
    im = np.asarray(Image.open(SRC / f"{sheet}.png").convert("RGB"))
    bg = ~ndimage.binary_opening(~background(im), iterations=1)
    lab, n = ndimage.label(~bg)
    sizes = ndimage.sum(~bg, lab, range(1, n + 1))
    centres = ndimage.center_of_mass(~bg, lab, range(1, n + 1))
    H, W = bg.shape
    out = {}
    for k, name in enumerate(names):
        a, b = k % cols * W / cols, (k % cols + 1) * W / cols
        c, d = k // cols * H / rows, (k // cols + 1) * H / rows
        mine = [i for i, (y, x) in enumerate(centres) if a <= x < b and c <= y < d]
        if not mine:
            print(f"  {name}: empty cell")
            continue
        big = max(sizes[i] for i in mine)
        keep = np.isin(lab, [i + 1 for i in mine if sizes[i] >= big * .01])
        ys, xs = np.nonzero(keep)
        out[name] = (keep, (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    return im, out


def cut(sheet, names, cols, rows):
    im, found = blobs(sheet, names, cols, rows)
    tall = {n: box[3] - box[1] for n, (_, box) in found.items()}
    adults = [t for n, t in tall.items() if n.split("/")[1].removesuffix("_w") not in CHILDREN]
    mid = float(np.median(adults or list(tall.values()) or [1]))
    shown = []
    for name, (keep, box) in found.items():
        group = name.split("/")[0]
        bw, bh = box[2] - box[0], box[3] - box[1]
        pair = art_height(name.removesuffix("_w")) if name.endswith("_w") else None
        if pair:
            lh = pair  # the winter drawing stands as tall as the summer one
        elif name.startswith("people/dog"):
            lh = DOG if "walk" not in name else DOG_MAP
        elif group == "people":
            lh = bh * ADULT / mid
        elif group == "map":
            lh = bh * MAP / mid
        elif group == "stamps":
            lh = 30
        elif group == "icons":
            lh = ICON if name.startswith("icons/tab") else SHARE_ICON if name.startswith(("icons/share", "icons/settings")) else STAT_ICON if name.startswith("icons/stat") else MARKER
        elif group == "items":
            lh = ITEM if bh >= bw else min(ITEM, bh * ITEM_W / bw)
        else:
            lh = min(GATE_BOX[1], bh * GATE_BOX[0] / bw)
        fine = FINE["map"] if "walk" in name else FINE[group]
        h = max(1, round(lh * fine))
        w = max(1, round(bw * h / bh))
        if group == "stamps":
            # a stamp's picture fills its window exactly: 28×30 art pixels
            w, h = 28 * fine, 30 * fine
        col, on, pane = shrink(im, keep, box, w, h, group in ("map", "gate"))
        pal, ix = palette(col, on & ~pane, COLOURS)
        glass = []
        if pane.any():
            pal.append(GLASS)
            ix[pane] = len(pal)
            glass = [len(pal)]
        write(name, pal, ix, glass, fine)
        shown.append((pal, ix))
        if name.startswith("people/postman"):
            # the same postman, small, walking his round on the map
            h = round(POSTMAN_MAP * FINE["map"])
            col, on, _ = shrink(im, keep, box, max(1, round(bw * h / bh)), h, False)
            pal, ix = palette(col, on, COLOURS)
            write(name.replace("people/postman", "people/postman_map"), pal, ix, [], FINE["map"])
    preview(sheet, shown)
    print(f"{sheet}: {len(shown)} sprites")


def preview(sheet, shown, z=2):
    if not shown:
        return
    w = sum(ix.shape[1] + 8 for _, ix in shown)
    h = max(ix.shape[0] for _, ix in shown) + 8
    img = np.full((h, w, 3), (226, 214, 180), np.uint8)
    x = 4
    for pal, ix in shown:
        lut = np.array([(0, 0, 0)] + list(pal), np.uint8)
        y = h - 4 - ix.shape[0]
        region = img[y:y + ix.shape[0], x:x + ix.shape[1]]
        region[ix > 0] = lut[ix[ix > 0]]
        x += ix.shape[1] + 8
    Image.fromarray(img).resize((w * z, h * z), Image.NEAREST).save(SRC / f"cut-{sheet}.png")


def main():
    want = sys.argv[1:]
    for sheet, (_, _, names, cols, rows) in sheets().items():
        if want and sheet not in want:
            continue
        if (SRC / f"{sheet}.png").exists():
            cut(sheet, names, cols, rows)


if __name__ == "__main__":
    main()
