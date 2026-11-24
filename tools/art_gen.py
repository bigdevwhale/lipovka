"""Asks Codex to draw the sprite sheets: residents, gifts and the buildings on the map.

python tools/art_gen.py [sheet ...]      # all sheets, or only the named ones; existing ones are kept
python tools/art_gen.py --force res1     # draw a sheet again

Each sheet is a grid of sprites on flat magenta, written to design/art-src/<sheet>.png; tools/sprites.py
cuts them into the game's sprites. Winter sheets are drawn from their summer sheet, so the same people
and houses come back wrapped up and snowed on.
"""
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "design/art-src"
STYLE_REF = ROOT / "design/codex-samples/post2.png"
GEN = Path.home() / ".codex/generated_images"

STYLE = (
    "Art style: AUTHENTIC hand-placed pixel art for a cosy mobile game about a village postman in a small Russian "
    "village (Lipovka), late-Soviet countryside, like a skilled human pixel artist working on a tiny canvas, shown "
    "upscaled with nearest neighbour: big perfectly square uniform pixels on a strict grid. Flat shading with 2-3 "
    "tones per material, clean 1-pixel dark brown outlines, simple readable shapes, limited warm muted palette, no "
    "anti-aliasing, no gradients, no glow, no gloss, no painterly textures, no 'AI illustration' look. The attached "
    "picture shows the approved style of the game: match its pixel size, palette, outlines and charm. "
)
SHEET = (
    "Layout: a sprite sheet on a SOLID FLAT PURE MAGENTA background (#FF00FF) filling the whole image, with no "
    "ground, no floor, no cast shadows, no frames and no text or labels anywhere. Exactly {cols} columns and {rows} "
    "rows of separate sprites, evenly spaced in an even grid, each sprite centred in its cell with generous magenta "
    "space around it, nothing touching another sprite or the image edge. All sprites at the same pixel scale. "
)
WINTER = (
    "The second attached picture is a sprite sheet from this game. Redraw exactly the same sheet: the same "
    "{what} in the same cells and order, same pixel scale, same style and the same magenta background, but in deep "
    "Russian winter: {how} "
)

PEOPLE_REF = ROOT / "design/codex-samples/residents.png"
PEOPLE = (
    "Draw the characters EXACTLY in the style of the attached character sheet (the second picture shows the game's "
    "world for colours only): natural grown-up proportions with a modest head (about a sixth of the height, not "
    "chibi, not big-headed), the same pixel size, fine pixel detail, woven and knitted textures on the clothes, "
    "small calm faces with dot eyes and soft rosy cheeks, the same muted warm palette and dark brown outlines. "
    "Each cell: one village resident standing full-body facing the viewer, holding an opened letter in front of "
    "them at waist height. Each adult about 52 art-pixels tall, old people a little shorter, a teenager about 46, "
    "a small girl about 36. Cells, left to right, top to bottom: "
)
PEOPLE_WINTER = (
    "everyone wears warm winter clothes over their own look: felt boots (valenki), padded coats or sheepskin coats "
    "with fur collars, fur hats (ushanka) or warm woollen headscarves, mittens, still holding the opened letter; "
    "keep each person's face, hair colour, glasses, beard and signature colours recognisable."
)

R = {
    "anna": "Anna, a young woman with a long brown braid, red blouse, long green skirt, white apron",
    "fedor": "Fyodor the old miller, grey beard, flat cap (kepka), brown jacket, blue trousers, floury canvas apron",
    "agafya": "Agafya, a kind old granny in a blue headscarf, brown cardigan, long grey skirt, knitted shawl, round glasses",
    "teacher": "Nikolai the old retired teacher, bald with white hair at the sides, glasses, white moustache, green jacket, tie, grey trousers",
    "varya": "Varya, a little first-grade girl with fair hair and two short pigtails, yellow dress, blue tights, a school satchel on her back",
    "olga": "Olga, the village feldsher (nurse), fair hair in a bun, white coat, blue skirt",
    "sergey": "Sergey the tractor driver, brown hair, moustache, kepka cap, blue shirt under dark blue overalls",
    "mikhalych": "Mikhalych the old beekeeper, grey beard, straw hat, yellow shirt, brown trousers",
    "zina": "Zinaida the shopkeeper, red curly hair, violet blouse, brown skirt, apron, earrings and bead necklace",
    "kolya": "Kolya, a teenage boy radio amateur, black hair, green hoodie, jeans, big headphones around his neck",
    "nina": "Granny Nina who bakes pies, red headscarf, green blouse, long brown skirt, apron, shawl",
    "lidia": "Lidia the librarian, black hair in a bun, glasses, blue blouse, grey skirt, beads",
    "marina": "Marina, a young illustrator from Moscow, red bob haircut, yellow sweater, blue jeans, earrings",
    "dima": "Dima, a young programmer, brown hair, glasses, stubble, grey knitted sweater, blue jeans",
    "erofey": "Yerofei, an old former polar radio operator, white beard, pipe, brown knitted sweater, grey trousers",
    "andrei": "Andrei the forester, brown hair, stubble, green shirt, dark quilted vest, green trousers, boots",
    "tanya": "Tanya, the forester's wife who nurses wild animals, fair ponytail, red shirt, dark vest, brown trousers",
    "grisha": "Grisha the woodcarver, fair hair, full beard, brown shirt, leather apron, blue trousers",
    "vera": "Vera, an old goat-keeper, red headscarf, blue blouse, grey skirt, round glasses, shawl",
    "nadya": "Nadya, Vera's sister, old woman in a green headscarf, red blouse, grey skirt, apron",
    "tamara": "Tamara, the telegraph operator, grey hair in a bun, glasses, navy blue railway uniform jacket and skirt",
    "lyosha": "Lyosha, a young trainee telegraph operator, fair hair, navy railway uniform cap and jacket, grey trousers",
    "viktor": "Viktor the train driver, grey hair, moustache, navy railway cap, black uniform jacket, blue trousers",
    "matvei": "Matvei, an old fisherman and boatbuilder, white beard, navy sailor's cap, blue-and-white striped sweater, brown trousers",
    "irina": "Irina, a young painter, long red hair, black beret, cream smock, blue trousers",
    "gleb": "Gleb the meteorologist, brown hair, beard, glasses, green knitted sweater, grey trousers",
    "darya": "Darya, a mother of five, brown hair in a bun, green blouse, brown skirt, apron",
    "timofei": "Timofei the carpenter, black hair, moustache, kepka cap, red shirt, dark vest, brown trousers",
    "pavel": "Pavel, the newspaper editor, grey hair, glasses, brown jacket, tie, grey trousers",
    "sofia": "Sofia, an elderly museum curator, grey hair in a bun, glasses, violet dress, beads, shawl",
    "postman": "the young village postman, short brown hair, navy blue postal uniform with brass buttons and a navy peaked cap with a gold band, a brown leather mail bag on a strap over his shoulder, a white envelope peeking out of the bag; he holds nothing, arms at his sides",
}
ORDER = list(R)

ITEMS = [
    ("badge", "honey", "an enamel pin badge with a honey bee"), ("badge", "medal", "a bronze medal on a ribbon"),
    ("badge", "post", "an enamel badge with a post horn"), ("badge", "star", "a red enamel star badge"),
    ("basket", "apples", "a wicker basket of red apples"), ("basket", "cones", "a wicker basket of pine cones"),
    ("basket", "eggs", "a wicker basket of eggs"), ("bell", "sleigh", "a brass sleigh bell on a leather strap"),
    ("bell", "small", "a small brass hand bell"), ("book", "blue", "a closed blue hardback book"),
    ("book", "brown", "a closed old brown leather book"), ("book", "green", "a closed green hardback book"),
    ("book", "notebook", "a school exercise notebook"), ("book", "red", "a closed red hardback book"),
    ("bouquet", "cornflowers", "a bunch of blue cornflowers"), ("bouquet", "dried", "a bunch of dried meadow flowers"),
    ("bouquet", "rowan", "a sprig of rowan with red berries"), ("bouquet", "willow", "a few pussy willow twigs"),
    ("bread", "gingerbread", "a rectangular glazed Tula gingerbread"), ("bread", "kalach", "a round kalach bread"),
    ("bread", "loaf", "a loaf of rye bread"), ("bread", "pretzel", "a sugar pretzel"),
    ("candle", "honey", "a beeswax candle in a holder"), ("carving", "bird", "a carved wooden bird"),
    ("carving", "sign", "a small carved wooden plaque with a sun pattern"), ("carving", "spoon", "a painted carved wooden spoon"),
    ("cheese", "wedge", "a wedge of goat cheese"), ("feather", "owl", "a single owl feather"),
    ("fish", "dried", "a dried roach fish on a string"), ("fish", "smoked", "a golden smoked bream"),
    ("found", "amber", "a piece of amber"), ("found", "cone", "a single pine cone"),
    ("found", "horseshoe", "an old iron horseshoe"), ("found", "key", "an old iron key"),
    ("found", "pebble", "a smooth striped pebble"), ("found", "shell", "a sea shell"),
    ("honeycomb", "frame", "a wooden beehive frame with honeycomb"), ("jar", "blueberry", "a glass jar of blueberry jam with a cloth lid"),
    ("jar", "cloudberry", "a glass jar of orange cloudberry jam with a cloth lid"), ("jar", "cucumbers", "a glass jar of pickled cucumbers"),
    ("jar", "honey", "a glass jar of golden honey with a green cloth lid"), ("jar", "jam", "a glass jar of red strawberry jam with a red cloth lid"),
    ("jar", "lingonberry", "a glass jar of lingonberries"), ("jar", "mushrooms", "a glass jar of pickled mushrooms"),
    ("lamp", "lantern", "an old kerosene lantern"), ("map", "old", "an old rolled-open paper map"),
    ("map", "star", "a dark blue star chart"), ("mittens", "patterned", "a pair of knitted red patterned mittens"),
    ("photo", "baby", "a small framed photo of a baby"), ("photo", "group", "a small framed group photo"),
    ("photo", "landscape", "a small framed landscape photo"), ("photo", "old", "an old sepia photo with a white border"),
    ("photo", "portrait", "a small framed portrait photo"), ("photo", "wedding", "a small framed wedding photo"),
    ("pie", "apple", "a round apple pie"), ("pie", "berry", "a round berry pie with lattice"),
    ("pie", "cabbage", "a golden oval cabbage pie"), ("pie", "fish", "a large round fish pie (rybnik)"),
    ("plant", "aloe", "an aloe plant in a clay pot"), ("plant", "lemon", "a small lemon tree in a pot"),
    ("postcard", "birch", "a postcard with birches"), ("postcard", "city", "a postcard with a city view"),
    ("postcard", "flowers", "a postcard with flowers"), ("postcard", "lake", "a postcard with a lake"),
    ("postcard", "mountains", "a postcard with mountains"), ("postcard", "ship", "a postcard with a ship at sea"),
    ("postcard", "space", "a postcard with a rocket in space"), ("postcard", "train", "a postcard with a steam train"),
    ("postcard", "winter", "a postcard with a snowy winter scene"), ("postcard", "sea", "a postcard with the sea"),
    ("qsl", "blue", "a blue radio amateur QSL card"), ("qsl", "green", "a green radio amateur QSL card"),
    ("qsl", "red", "a red radio amateur QSL card"), ("scarf", "check", "a folded red check scarf"),
    ("scarf", "red", "a folded knitted red scarf"), ("socks", "grey", "a pair of grey wool socks"),
    ("socks", "striped", "a pair of striped wool socks"), ("tea", "herbs", "a bundle of dried herbs for tea"),
    ("tea", "rosehip", "a paper bag of rosehips"), ("tea", "tin", "a decorated tea tin"),
    ("thermometer", "window", "a window thermometer"), ("toy", "boat", "a small wooden toy boat"),
    ("toy", "horse", "a painted wooden toy horse"), ("toy", "whistle", "a clay whistle toy bird"),
]
ITEM_TEXT = (
    "Each cell: one small object as an inventory icon, drawn on its own about 16 pixels tall (larger flat things "
    "like cards and photos about 16 pixels wide), seen from the front or slightly above, no labels. Cells, left to right, top to bottom: "
)

HOUSES = {
    "shop": "the village shop: a log house with a green roof, white window frames, a small blank signboard over the door and a porch",
    "club": "the village club: a wide log hall with a red roof, yellow window frames, a blank signboard and a small porch with steps",
    "kuznetsovy": "the Kuznetsovs' log house with a blue roof and white window frames, a small red tractor parked beside it",
    "vetrovy": "the Vetrovs' log house with a red roof and white window frames",
    "sorokina": "an old granny's small log house with a brown plank roof and blue window frames, a log well with a sweep beside it",
    "ryabininy": "the Ryabinins' log house with a grey slate roof and green window frames, a tall radio antenna mast on the roof",
    "lebedev": "the old teacher's log house with a green roof and white window frames, a small brass telescope on a tripod beside it",
    "sokolovy": "the Sokolovs' log house with a blue roof and yellow window frames",
    "apiary": "the beekeeper's log house with a straw thatched roof and white window frames, a row of four yellow beehives beside it",
    "mill": "an old wooden watermill with a straw thatched roof and a big wooden waterwheel on its side",
    "farmstead": "a farmstead log house with a straw thatched roof and white window frames, a stack of firewood beside it",
    "forester": "the forester's lodge, dark log house with a green roof and green window frames, a stack of firewood, an owl on a post",
    "workshop": "the woodcarver's workshop, log house with a brown plank roof, yellow window frames and carved wooden decorations",
    "lastochkiny": "the goat-keeping sisters' log house with a red roof and blue window frames, little yellow cheese wheels on a bench",
    "halt": "a small railway halt station building with a grey slate roof, yellow window frames, a short platform and a red semaphore signal",
    "stationhouse": "the train driver's small log house with a brown roof and white window frames, an iron lamp post beside it",
    "boatshed": "a fisherman's boatshed by the water with a brown roof and blue window frames, a red rowing boat and fishing nets",
    "painter": "a painter's log house with a blue roof and white window frames, a wooden easel with a canvas beside it",
    "meteo": "a weather station: small log house with a grey slate roof, a tall mast with a wind vane, a white louvred instrument box on legs",
    "belkiny": "a large family's log house with a green roof and yellow window frames, a stack of firewood",
    "newspaper": "a two-storey red brick district town building with a flat dark roof and many windows, the newspaper office",
    "museum": "a small classical museum building with cream walls, white columns, a green roof and a triangular pediment",
    "school": "a long one-storey village school log house with a straw thatched roof, white window frames and a little school bell on a post",
    "post": "the village post office: log house with a blue roof, white window frames, a blank framed sign on the roof gable with an envelope on it, a blue post box by the door",
}
HOUSE_TEXT = (
    "Each cell: one building for a village map, seen from the front (elevation view, a tiny bit from above), "
    "sitting on nothing, no ground and no trees. IMPORTANT pixel density: these are tiny map icons, each house only "
    "about 34 art-pixels wide and 28 art-pixels tall (props beside it included in that small scale), drawn with very "
    "big chunky pixels, windows about 5 pixels square with a 1-pixel cross. Log walls with carved "
    "window frames (nalichniki), every window pane filled with flat pure cyan (#00FFFF) and nothing else, a door, a brick chimney. Cells, left to right, top to bottom: "
)
HOUSE_WINTER = (
    "thick white snow lying on every roof, snow caps on the chimney, fences, signs and props, little icicles; the "
    "every window pane stays flat pure cyan (#00FFFF)."
)


GATE = {
    "vetrovy": "a classic Russian log izba, gable end to the street, red roof, two windows with white carved frames and green shutters, a round attic window, carved valance under the eaves",
    "sorokina": "an old weathered grey log izba, steep brown plank roof, two narrow windows with plain frames and blue shutters, a small lean-to shed on the right",
    "kuznetsovy": "a newer light log house with the long side to the street, blue roof with an attic lookout, three narrow windows with white carved frames, a glazed veranda on the left",
    "ryabininy": "a log izba, gable to the street, grey slate roof with an attic lookout, two windows with arched green frames, a tall TV antenna on the roof",
    "lebedev": "an ochre-yellow painted plank house on a brick plinth, hipped green roof, two windows with arched white frames, a glazed veranda on the left",
    "sokolovy": "a pale-blue painted plank house with the long side to the street, blue roof, two tall windows with yellow frames, a small porch with steps on the right",
    "apiary": "a small old grey log hut with a steep straw thatched roof and a vent in the gable, two narrow windows with plain white frames, no chimney",
    "mill": "an old dark log watermill, gable to the street, straw thatched roof, a loft door in the gable, one small window, a big wooden waterwheel on the right side",
    "farmstead": "a long low log farmhouse with the long side to the street, straw thatched roof, two windows with plain white frames, a woodshed on the right",
    "forester": "a dark log forester's lodge, green roof, deer antlers on the gable, two windows with dark green shutters, a porch on the right",
    "workshop": "a fresh light log house of a woodcarver, brown plank roof with an attic lookout, richly carved valance and gable boards, two windows with yellow carved frames",
    "lastochkiny": "a plank house painted blue on the left half and pink on the right half, red roof, two windows with blue carved frames and white shutters",
    "halt": "a small railway halt station building, ochre painted planks, hipped grey slate roof, three tall windows with yellow frames, a blank sign board over them",
    "stationhouse": "a blue-grey painted plank house on a brick plinth, hipped brown roof, two windows with white frames, a porch on the right",
    "boatshed": "an old grey log boathouse, very steep brown roof with a loft door, two windows with blue shutters, fishing nets hanging on the wall",
    "painter": "a blue painted plank house with a big slanted studio window in the gable, blue roof, two windows with white frames",
    "meteo": "a whitewashed plank weather-station house on a brick plinth, long side to the street, hipped grey slate roof, two windows with white frames, no chimney",
    "belkiny": "a big wide log house of a large family, long side to the street, green roof with an attic lookout, three windows with yellow carved frames and ochre shutters",
    "shop": "a village shop: green painted plank building on a brick plinth, long side to the street, green roof, a wide shop-front window with a blank dark green sign board over it, a door",
    "club": "a village club hall: cream painted planks on a brick plinth, red roof with a wide gable, two tall windows with yellow frames, a columned entrance porch on the right, a small red flag on the roof",
    "newspaper": "a two-storey red brick town building with a flat dark roof, eight windows in two rows, a door with a blank white sign board above it",
    "museum": "a small classical town museum with cream walls, five white columns, a green roof with a triangular pediment, tall windows",
}
GATE_TEXT = (
    "Each cell: the front of ONE house as seen from the street through its gate, straight-on front view, filling "
    "most of its cell, from the top of the chimney down to the bottom of the walls; no fence, no ground, no grass, "
    "no trees, no people. IMPORTANT pixel density: each house is about 104 art-pixels wide and 110 art-pixels tall. "
    "Every window pane is filled with flat pure cyan (#00FFFF) and nothing else (no curtains, no reflections), so "
    "the panes can be lit at night. Cells, left to right, top to bottom: "
)
GATE_WINTER = "thick white snow lying on the roofs, ledges, porch and chimney, small icicles; every window pane stays flat pure cyan (#00FFFF)."


UNIFORM = "navy blue village postal uniform with brass buttons and a navy peaked cap with a gold band"
POSTMEN = {
    "postman": f"a young postman with short brown hair, {UNIFORM}, navy trousers",
    "postman_m2": f"a postman in his forties with a dark moustache and black hair, {UNIFORM}, navy trousers",
    "postman_m3": f"a cheerful older postman with grey hair and a short grey beard, round glasses, {UNIFORM}, navy trousers",
    "postman_f1": f"a young postwoman with a long fair braid over her shoulder, {UNIFORM}, a navy skirt to below the knee",
    "postman_f2": f"a postwoman with short dark brown hair, {UNIFORM}, navy trousers",
    "postman_f3": f"a kind older postwoman with grey hair in a bun, round glasses, {UNIFORM}, a navy skirt",
}

ICONS = [
    ("tab_post", "a white envelope with a red wax seal, for the Post tab"),
    ("tab_village", "a small log izba with a red roof and a chimney, for the Village tab"),
    ("tab_room", "a warm green table lamp glowing, for the Room tab"),
    ("tab_album", "a postage stamp with perforated edges and a tiny birch picture, for the Stamps tab"),
    ("tab_diary", "an open notebook diary with a pencil, for the Diary tab"),
    ("map_letter", "a map marker: a little wooden signboard on a short post with a white envelope with a red seal painted on it"),
    ("map_urgent", "a map marker: the same little signboard with a yellow telegram form and a red lightning mark"),
    ("map_done", "a map marker: the same little signboard with a big green tick"),
]
ICON_TEXT = (
    "Each cell: one small game UI icon, front view, centred, chunky and readable at small size, about 20 art-pixels "
    "across (map markers about 16 wide and 18 tall). Cells, left to right, top to bottom: "
)

STAMP_DIR = ROOT / "app/src/main/assets/content/stamps"
BG = {"sky": "a clear morning sky", "dusk": "a warm dusk sky", "night": "a dark night sky", "red": "deep red", "green": "deep green",
      "blue": "deep blue", "gold": "warm gold", "cream": "pale cream paper", "violet": "violet", "sea": "the sea"}
STAMP_TEXT = (
    "Each cell: the PICTURE of one vintage Soviet-era postage stamp, without the stamp's white border, perforation "
    "or any text, letters or numbers: a full-bleed little scene filling a rectangle about 28 art-pixels wide and 30 "
    "tall, with its own background colour edge to edge (the magenta is only between the pictures). Bold simple "
    "shapes, like a real engraved stamp design. Cells, left to right, top to bottom: "
)


def stamp_pictures():
    """Every family and background the stamps use, with the English name of the first stamp that has them."""
    seen = {}
    for f in sorted(STAMP_DIR.glob("*.tsv")):
        rows = f.read_text(encoding="utf-8").splitlines()
        head = rows[0].split("	")
        for r in rows[1:]:
            c = dict(zip(head, r.split("	")))
            if c.get("family"):
                seen.setdefault((c["family"], c["bg"]), c.get("name_en", c["family"]))
    return [(fam, bg, name) for (fam, bg), name in seen.items()]

DOG_TEXT = (
    "Bublik, the postman's dog: a small friendly village mutt, warm tan-ginger fur with a cream belly, muzzle "
    "and paws, floppy ears, a fluffy tail curled up into a ring like a bagel, a little dark nose, kind eyes. "
    "IMPORTANT pixel density: the dog is about 16 art-pixels tall. Cells, left to right: (1) Bublik sitting, "
    "three-quarter view facing left towards the viewer, tail curled behind; (2) Bublik trotting to the right, "
    "side view, mid-step, tail curled up."
)
DOG_WINTER = "a little snow on his back and ears, otherwise the same dog in the same poses."


def chunks(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]


def listing(things):
    return " ".join(f"({i + 1}) {t};" for i, t in enumerate(things))


def sheets():
    """name -> (prompt, [reference images], [sprite names in cell order], cols, rows)."""
    out = {}
    for i, group in enumerate(chunks(ORDER, 8), 1):
        cols, rows = 4, 2
        body = PEOPLE + listing([R[k] for k in group])
        names = [f"people/{k}" for k in group]
        out[f"res{i}"] = (SHEET.format(cols=cols, rows=rows) + body, [PEOPLE_REF, STYLE_REF], names, cols, rows)
        out[f"res{i}w"] = (SHEET.format(cols=cols, rows=rows) + body + " " + WINTER.format(what="characters", how=PEOPLE_WINTER).replace("second", "third"),
                           [PEOPLE_REF, STYLE_REF, SRC / f"res{i}.png"], [n + "_w" for n in names], cols, rows)
    for i, group in enumerate(chunks(ITEMS, 16), 1):
        cols, rows = 4, 4
        out[f"items{i}"] = (STYLE + SHEET.format(cols=cols, rows=rows) + ITEM_TEXT + listing([t for _, _, t in group]),
                            [STYLE_REF], [f"items/{f}_{v}" for f, v, _ in group], cols, rows)
    for i, group in enumerate(chunks(list(HOUSES), 6), 1):
        cols, rows = 3, 2
        body = HOUSE_TEXT + listing([HOUSES[k] for k in group])
        names = [f"map/{k}" for k in group]
        out[f"map{i}"] = (STYLE + SHEET.format(cols=cols, rows=rows) + body, [STYLE_REF], names, cols, rows)
        out[f"map{i}w"] = (STYLE + SHEET.format(cols=cols, rows=rows) + WINTER.format(what="buildings", how=HOUSE_WINTER) + body,
                           [STYLE_REF, SRC / f"map{i}.png"], [n + "_w" for n in names], cols, rows)
    for i, group in enumerate(chunks(list(GATE), 4), 1):
        cols, rows = 2, 2
        body = GATE_TEXT + listing([GATE[k] for k in group])
        names = [f"gate/{k}" for k in group]
        out[f"gate{i}"] = (STYLE + SHEET.format(cols=cols, rows=rows) + body, [STYLE_REF], names, cols, rows)
        out[f"gate{i}w"] = (STYLE + SHEET.format(cols=cols, rows=rows) + WINTER.format(what="houses", how=GATE_WINTER) + body,
                            [STYLE_REF, SRC / f"gate{i}.png"], [n + "_w" for n in names], cols, rows)
    cols, rows = 3, 2
    body = PEOPLE.replace("holding an opened letter in front of them at waist height", "arms at their sides, a brown leather mail bag on a strap over the shoulder with a white envelope peeking out") + listing([POSTMEN[k] for k in POSTMEN])
    names = [f"people/{k}" for k in POSTMEN]
    out["postmen"] = (SHEET.format(cols=cols, rows=rows) + body, [PEOPLE_REF, STYLE_REF], names, cols, rows)
    out["postmenw"] = (SHEET.format(cols=cols, rows=rows) + body + " " + WINTER.format(what="characters", how=PEOPLE_WINTER).replace("second", "third"),
                       [PEOPLE_REF, STYLE_REF, SRC / "postmen.png"], [n + "_w" for n in names], cols, rows)
    cols, rows = 4, 2
    out["icons"] = (STYLE + SHEET.format(cols=cols, rows=rows) + ICON_TEXT + listing([t for _, t in ICONS]),
                    [STYLE_REF], [f"icons/{k}" for k, _ in ICONS], cols, rows)
    cols, rows = 4, 4
    for i, group in enumerate(chunks(stamp_pictures(), 16), 1):
        body = STAMP_TEXT + listing([f"{name} (a {fam}; background: {BG.get(bg, bg)})" for fam, bg, name in group])
        out[f"stamps{i}"] = (STYLE + SHEET.format(cols=cols, rows=rows) + body, [STYLE_REF], [f"stamps/{fam}_{bg}" for fam, bg, _ in group], cols, rows)
    out["icons2"] = (STYLE + SHEET.format(cols=2, rows=1) + ICON_TEXT + listing([
        "the universal 'share' symbol everyone knows from phones: three round dots (one on the left, two on the right, top and bottom) joined by two straight lines, chunky and bold, dark brown ink",
        "the very same share symbol drawn in light cream for dark backgrounds"]), [STYLE_REF], ["icons/share", "icons/share_light"], 2, 1)
    out["icons3"] = (STYLE + SHEET.format(cols=3, rows=2) + ICON_TEXT + listing([
        "a pair of small footprints (boot prints), for steps",
        "a little wooden road milestone post with a red top, for kilometres",
        "a white envelope with a red wax seal, for letters",
        "a tear-off wall calendar with a red top, for days",
        "a postage stamp with perforated edges and a tiny red star, for stamps",
        "a small flame, for days in a row"]), [STYLE_REF],
        ["icons/stat_steps", "icons/stat_km", "icons/stat_letters", "icons/stat_days", "icons/stat_stamps", "icons/stat_streak"], 3, 2)
    out["icons4"] = (STYLE + SHEET.format(cols=2, rows=1) + ICON_TEXT + listing([
        "the universal 'settings' icon: a chunky cog wheel with eight square teeth and a round hole in the middle, dark brown iron with a warm highlight",
        "the same settings cog drawn in light cream for dark backgrounds"]), [STYLE_REF], ["icons/settings", "icons/settings_light"], 2, 1)
    cols, rows = 2, 1
    out["dog"] = (STYLE + SHEET.format(cols=cols, rows=rows) + DOG_TEXT, [STYLE_REF], ["people/dog", "people/dog_walk"], cols, rows)
    out["dogw"] = (STYLE + SHEET.format(cols=cols, rows=rows) + WINTER.format(what="dog", how=DOG_WINTER) + DOG_TEXT,
                   [STYLE_REF, SRC / "dog.png"], ["people/dog_w", "people/dog_walk_w"], cols, rows)
    return out


def draw(name, prompt, refs):
    log = SRC / f"{name}.log"
    cmd = ["codex", "exec", "--skip-git-repo-check", "-C", str(SRC)]
    for r in refs:
        cmd += ["-i", str(r)]
    cmd.append("-")
    task = ("Use your image generation tool to create the following image. Do not edit files or run commands; "
            "just generate the image once.\n\n" + prompt)
    res = subprocess.run(cmd, input=task, capture_output=True, text=True, encoding="utf-8", shell=sys.platform == "win32")
    log.write_text(res.stdout + res.stderr, encoding="utf-8")
    m = re.search(r"session id: (\S+)", res.stdout + res.stderr)
    pngs = sorted((GEN / m.group(1)).glob("*.png"), key=lambda p: p.stat().st_mtime) if m else []
    if not pngs:
        print(f"{name}: no image, see {log}")
        return False
    shutil.copy(pngs[-1], SRC / f"{name}.png")
    print(f"{name}: ok")
    return True


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    SRC.mkdir(parents=True, exist_ok=True)
    all_ = sheets()
    want = args or list(all_)
    todo = [n for n in want if force or not (SRC / f"{n}.png").exists()]
    first = [n for n in todo if not n.endswith("w")]
    later = [n for n in todo if n.endswith("w")]
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(lambda n: draw(n, all_[n][0], all_[n][1]), first))
        list(ex.map(lambda n: draw(n, all_[n][0], all_[n][1]), [n for n in later if Path(all_[n][1][-1]).exists()]))


if __name__ == "__main__":
    main()
