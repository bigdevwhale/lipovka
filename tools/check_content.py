"""Validates the content TSVs (see docs/CONTENT.md).

python tools/check_content.py            # everything
python tools/check_content.py arcs/a.tsv # one file, plus the shared tables it refers to

Prints every problem and exits with 1 if there are any.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "app/src/main/assets/content"

ARC_COLS = ["arc", "n", "gap", "months", "on", "needs", "kind", "to", "from_ru", "from_en", "brief_ru", "brief_en",
            "news_ru", "news_en", "reply", "gift", "stamp", "sets"]
ITEM_COLS = ["key", "family", "variant", "name_ru", "name_en"]
STAMP_COLS = ["key", "family", "bg", "value", "name_ru", "name_en", "series"]
TPL_COLS = ["key", "every", "day", "months", "to", "kind", "from_ru", "from_en", "brief_ru", "brief_en", "news_ru", "news_en", "stamp"]
FILL_COLS = ["tags", "from_ru", "from_en", "brief_ru", "brief_en", "news_ru", "news_en"]
EVENT_COLS = ["key", "start", "end", "district", "look", "name_ru", "name_en", "notice_ru", "notice_en", "brief_ru", "brief_en", "stamp"]

KINDS = {"letter", "postcard", "parcel", "telegram", "registered", "newspaper", "notice"}
ITEM_FAMILIES = {
    "jar": "jam cranberry honey cucumbers mushrooms applejam blueberry lingonberry cloudberry",
    "pie": "apple cabbage berry fish", "bread": "loaf kalach gingerbread pretzel",
    "basket": "apples mushrooms berries eggs cones", "socks": "red green grey blue striped",
    "mittens": "red white blue patterned", "scarf": "red green blue check",
    "postcard": "sea mountains city flowers winter ship space lake birch train",
    "photo": "portrait wedding group landscape old baby", "book": "red blue green brown notebook",
    "candle": "white honey", "toy": "horse whistle matryoshka boat bear top",
    "carving": "spoon bird frame bear sign", "bouquet": "dried rowan wheat cornflowers willow",
    "feather": "owl crane jay", "found": "shell cone pebble amber horseshoe key", "fish": "dried smoked",
    "honeycomb": "frame", "tea": "tin herbs rosehip", "plant": "geranium violet cactus aloe lemon",
    "qsl": "red blue green gold", "lamp": "kerosene lantern", "map": "old star", "badge": "post honey star medal",
    "record": "black blue", "cheese": "round wedge", "bell": "small sleigh", "thermometer": "window",
}
ITEM_FAMILIES = {k: set(v.split()) for k, v in ITEM_FAMILIES.items()}
STAMP_FAMILIES = set("""house mill ship boat train plane bird crane owl swallow fish flower tree birch fir mushroom berry
apple bee horse cow goat cat dog snowflake star moon sun rain rainbow lighthouse bridge kettle letter telegram radio
book lake mountain globe rocket fireworks sled lantern bell clock heart anchor violin camera""".split())
STAMP_BG = set("sky dusk night red green blue gold cream violet sea".split())
SERIES = set("lipovka zarechye station ozerki kordon gorodok seasons holidays far post radio".split())
LOOKS = set("""fair newyear maslenitsa kupala haymaking harvest cranes firstsnow icebreak fishing railway apples
mushrooms school lilac swallows frost berries none""".split())
BUILTIN = {f"d{i}" for i in range(1, 6)} | {f"km{k}" for k in (10, 25, 50, 100, 250, 500, 1000, 2000, 3000)} | {"dog"}

problems = []


def bad(where, msg):
    problems.append(f"{where}: {msg}")


def read(path, cols):
    rows = []
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    if not lines:
        bad(path.name, "empty file")
        return rows
    head = lines[0].split("\t")
    if head != cols:
        bad(path.name, f"header must be {cols}, got {head}")
    for i, line in enumerate(lines[1:], start=2):
        if "\r" in line:
            bad(f"{path.name}:{i}", "CR character (use LF line endings)")
        f = line.split("\t")
        if len(f) != len(cols):
            bad(f"{path.name}:{i}", f"{len(f)} columns, expected {len(cols)}")
            continue
        rows.append((f"{path.name}:{i}", dict(zip(cols, f))))
    return rows


def text_ok(where, row, key, limit):
    for lang in ("ru", "en"):
        v = row[f"{key}_{lang}"]
        if not v.strip():
            bad(where, f"{key}_{lang} is empty")
        if len(v) > limit:
            bad(where, f"{key}_{lang} is {len(v)} chars (max {limit})")
        if lang == "en" and re.search("[а-яА-ЯёЁ]", v):
            bad(where, f"{key}_en has Cyrillic")
        if lang == "ru" and not re.search("[а-яА-ЯёЁ]", v):
            bad(where, f"{key}_ru has no Cyrillic")


def mmdd(v):
    m = re.fullmatch(r"(\d\d)-(\d\d)", v)
    return m and 1 <= int(m[1]) <= 12 and 1 <= int(m[2]) <= 31


def main():
    residents = {}
    for where, r in read(C / "residents.tsv", ["id", "house", "district", "sprite", "look", "birthday", "name_ru", "name_en", "about_ru", "about_en"]):
        residents[r["id"]] = r
    ids = set(residents) | {"me"}

    items = {}
    for p in sorted((C / "items").glob("*.tsv")):
        for where, r in read(p, ITEM_COLS):
            if r["key"] in items:
                bad(where, f"duplicate item {r['key']}")
            items[r["key"]] = r
            if r["family"] not in ITEM_FAMILIES:
                bad(where, f"unknown item family {r['family']}")
            elif r["variant"] not in ITEM_FAMILIES[r["family"]]:
                bad(where, f"unknown variant {r['variant']} for {r['family']}")
            text_ok(where, r, "name", 40)

    stamps = {}
    for p in sorted((C / "stamps").glob("*.tsv")):
        for where, r in read(p, STAMP_COLS):
            if r["key"] in stamps:
                bad(where, f"duplicate stamp {r['key']}")
            stamps[r["key"]] = r
            if r["family"] not in STAMP_FAMILIES:
                bad(where, f"unknown stamp family {r['family']}")
            if r["bg"] not in STAMP_BG:
                bad(where, f"unknown stamp bg {r['bg']}")
            if r["series"] not in SERIES:
                bad(where, f"unknown series {r['series']}")
            if not r["value"].isdigit() or not 1 <= int(r["value"]) <= 99:
                bad(where, f"value must be 1..99")
            text_ok(where, r, "name", 40)

    used_items, used_stamps = set(), set()
    flags_set, flags_needed = set(), []
    beats = []
    for p in sorted((C / "arcs").glob("*.tsv")):
        beats += read(p, ARC_COLS)
    arcs = {}
    for where, r in beats:
        arcs.setdefault(r["arc"], []).append((where, r))
        if not re.fullmatch(r"[a-z0-9_]+", r["arc"]):
            bad(where, f"bad arc id {r['arc']}")
        if not r["n"].isdigit():
            bad(where, "n must be a number")
        if not r["gap"].isdigit():
            bad(where, "gap must be a number of days")
        if r["months"] and not all(m.strip().isdigit() and 1 <= int(m) <= 12 for m in r["months"].split(",")):
            bad(where, f"bad months {r['months']}")
        if r["on"] and not mmdd(r["on"]):
            bad(where, f"bad on date {r['on']}")
        if r["on"] and r["months"] and int(r["on"][:2]) not in {int(m) for m in r["months"].split(",")}:
            bad(where, "on date is outside months")
        if r["kind"] not in KINDS:
            bad(where, f"unknown kind {r['kind']}")
        if r["to"] not in ids:
            bad(where, f"unknown recipient {r['to']}")
        if r["reply"] and r["reply"] != "out" and r["reply"] not in residents:
            bad(where, f"unknown reply target {r['reply']}")
        if r["to"] == "me" and r["reply"]:
            bad(where, "letters to me have no reply")
        if r["gift"]:
            used_items.add(r["gift"])
            if r["gift"] not in items:
                bad(where, f"unknown gift {r['gift']}")
        if r["stamp"]:
            used_stamps.add(r["stamp"])
            if r["stamp"] not in stamps:
                bad(where, f"unknown stamp {r['stamp']}")
        if r["sets"]:
            flags_set.add(r["sets"])
        for f in filter(None, (x.strip() for x in r["needs"].split(","))):
            flags_needed.append((where, f))
        text_ok(where, r, "from", 40)
        text_ok(where, r, "brief", 80)
        text_ok(where, r, "news", 700 if r["to"] == "me" else 340)
    for where, f in flags_needed:
        if f not in BUILTIN and f not in flags_set:
            bad(where, f"flag {f} is never set")
    for arc, rows in arcs.items():
        ns = sorted(int(r["n"]) for _, r in rows if r["n"].isdigit())
        if ns != list(range(1, len(ns) + 1)):
            bad(arc, f"beats must be numbered 1..{len(ns)}, got {ns}")

    if (C / "templates.tsv").exists():
        for where, r in read(C / "templates.tsv", TPL_COLS):
            if r["every"] not in {"weekly", "monthly", "yearly", "birthday"}:
                bad(where, f"bad every {r['every']}")
            if r["every"] == "weekly" and r["day"] not in list("1234567"):
                bad(where, "weekly day must be 1..7")
            if r["every"] == "monthly" and not (r["day"].isdigit() and 1 <= int(r["day"]) <= 28):
                bad(where, "monthly day must be 1..28")
            if r["every"] == "yearly" and not mmdd(r["day"]):
                bad(where, "yearly day must be MM-DD")
            for t in r["to"].split(","):
                if t.strip() not in residents:
                    bad(where, f"unknown recipient {t}")
            if r["kind"] not in KINDS:
                bad(where, f"unknown kind {r['kind']}")
            if r["stamp"] and r["stamp"] not in stamps:
                bad(where, f"unknown stamp {r['stamp']}")
            used_stamps.add(r["stamp"])
            text_ok(where, r, "from", 40)
            text_ok(where, r, "brief", 80)
            text_ok(where, r, "news", 2400)
            if len(r["news_ru"].split(" | ")) != len(r["news_en"].split(" | ")):
                bad(where, "news_ru and news_en have different numbers of variants")

    if (C / "fillers.tsv").exists():
        for where, r in read(C / "fillers.tsv", FILL_COLS):
            for t in r["tags"].split(","):
                if t.strip() not in {"old", "young", "family", "child", "any"}:
                    bad(where, f"bad tag {t}")
            text_ok(where, r, "from", 40)
            text_ok(where, r, "brief", 80)
            text_ok(where, r, "news", 340)

    if (C / "events.tsv").exists():
        for where, r in read(C / "events.tsv", EVENT_COLS):
            for k in ("start", "end"):
                if not (mmdd(r[k]) or re.fullmatch(r"easter[+-]\d+", r[k])):
                    bad(where, f"bad {k} {r[k]}")
            if r["district"] not in list("012345"):
                bad(where, "district must be 0..5")
            if r["look"] not in LOOKS:
                bad(where, f"unknown look {r['look']}")
            if r["stamp"] and r["stamp"] not in stamps:
                bad(where, f"unknown stamp {r['stamp']}")
            used_stamps.add(r["stamp"])
            text_ok(where, r, "name", 40)
            text_ok(where, r, "notice", 340)
            text_ok(where, r, "brief", 80)

    for k in sorted(set(items) - used_items):
        bad("items", f"item {k} is never given")
    for k in sorted(set(stamps) - used_stamps):
        bad("stamps", f"stamp {k} is never collected")

    print(f"{len(residents)} residents, {len(arcs)} arcs, {len(beats)} beats, {len(items)} items, {len(stamps)} stamps")
    for p in problems:
        print(p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
