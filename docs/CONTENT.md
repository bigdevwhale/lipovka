# Content format

All content lives in `app/src/main/assets/content/` as UTF-8 TSV files: one header row, then one row
per line, columns separated by a single TAB. Text never contains a TAB or a newline. Empty cells are
empty strings. Every text column comes in Russian (`_ru`) and English (`_en`); the English is a natural
translation, not a word-for-word one. `tools/check_content.py` validates everything.

Speech in the game is spoken to the postman with polite «вы» (plural verbs) so it works for anyone.

## residents.tsv (written by hand)

`id  house  district  sprite  look  birthday  name_ru  name_en  about_ru  about_en`

## Arcs — `arcs/*.tsv`

A story arc is a sequence of beats; each beat is one piece of mail. The engine sends beat n+1 only after
beat n was delivered and its conditions hold, so an arc unfolds over months and years on its own.

Columns (18):

| column | meaning |
|--------|---------|
| `arc` | arc id, e.g. `anna`, `agafya_sister`, `me_autumn1` |
| `n` | 1, 2, 3… order within the arc |
| `gap` | minimum days after the previous beat of this arc was delivered (for n=1: days after the arc's district opens / the game starts). Typical 4–40. |
| `months` | allowed months, e.g. `10,11` (empty = any) |
| `on` | a fixed date `MM-DD` (e.g. `12-31`): the beat arrives on that date (empty = any day) |
| `needs` | flags that must be set, comma-separated (empty = none). Built-in flags: `d1`…`d5` (district open), `km10`, `km25`, `km50`, `km100`, `km250`, `km500`, `km1000`, `km2000`, `km3000` (total km walked), `dog` (Bublik walks with you) |
| `kind` | `letter`, `postcard`, `parcel`, `telegram`, `registered`, `newspaper`, `notice` |
| `to` | a resident id, or `me` for the postman |
| `from_ru`, `from_en` | the sender line on the envelope: «Степан, т/х «Онега»» / "Stepan, MV Onega" (≤ 40 chars) |
| `brief_ru`, `brief_en` | one line for the evening news (≤ 70 chars): «У Анны хорошие вести: Степан будет к Покрову.» |
| `news_ru`, `news_en` | what the resident says at the gate after reading, 1–4 sentences, ≤ 320 chars, no surrounding quotes. For `to=me` this is the letter itself (≤ 700 chars, may be signed). |
| `reply` | empty; a resident id (the resident hands you a reply for that neighbour, it goes in tomorrow's bag); or `out` (a reply to send far away, dropped in the outbox) |
| `gift` | empty or an item key (see items) |
| `stamp` | empty or a stamp key (see stamps): collected when delivered |
| `sets` | empty or one flag this beat sets when delivered, e.g. `anna.married` |

Rules:
- `needs` may only use built-in flags or flags `sets` by some beat (in any file). Keep cross-arc flags rare.
- A beat addressed to a resident of a district that isn't open yet waits until it opens.
- Pace: an arc of a Lipovka resident should take 2.5–3 years of game time (sum of gaps plus waiting for
  months/dates); district arcs 1.5–2.5 years. Mix short gaps (a reply comes in a week) with long ones.
- Use `months`/`on` for seasonal beats (New Year, haymaking, the river freezing…). Remember the game can
  start in any month, so an arc must not assume where in the year it starts; tie seasonal beats to months.
- About one beat in four gives a gift, one in three a stamp. Gifts and stamps fit the story.

## Items — `items/*.tsv` (gifts in the postman's room)

`key  family  variant  name_ru  name_en` — key is unique across all files, lowercase with `_`.

Families and variants (the art is drawn per family; the variant picks colours):

- `jar`: jam, cranberry, honey, cucumbers, mushrooms, applejam, blueberry, lingonberry, cloudberry
- `pie`: apple, cabbage, berry, fish
- `bread`: loaf, kalach, gingerbread, pretzel
- `basket`: apples, mushrooms, berries, eggs, cones
- `socks`: red, green, grey, blue, striped
- `mittens`: red, white, blue, patterned
- `scarf`: red, green, blue, check
- `postcard`: sea, mountains, city, flowers, winter, ship, space, lake, birch, train
- `photo`: portrait, wedding, group, landscape, old, baby
- `book`: red, blue, green, brown, notebook
- `candle`: white, honey
- `toy`: horse, whistle, matryoshka, boat, bear, top
- `carving`: spoon, bird, frame, bear, sign
- `bouquet`: dried, rowan, wheat, cornflowers, willow
- `feather`: owl, crane, jay
- `found`: shell, cone, pebble, amber, horseshoe, key
- `fish`: dried, smoked
- `honeycomb`: frame
- `tea`: tin, herbs, rosehip
- `plant`: geranium, violet, cactus, aloe, lemon
- `qsl`: red, blue, green, gold (a radio amateur's QSL card)
- `lamp`: kerosene, lantern (railway)
- `map`: old, star
- `badge`: post, honey, star, medal
- `record`: black, blue (gramophone record)
- `cheese`: round, wedge
- `bell`: small, sleigh
- `thermometer`: window

## Stamps — `stamps/*.tsv`

`key  family  bg  value  name_ru  name_en  series`

- `family` (the picture): house, mill, ship, boat, train, plane, bird, crane, owl, swallow, fish, flower,
  tree, birch, fir, mushroom, berry, apple, bee, horse, cow, goat, cat, dog, snowflake, star, moon, sun,
  rain, rainbow, lighthouse, bridge, kettle, letter, telegram, radio, book, lake, mountain, globe, rocket,
  fireworks, sled, lantern, bell, clock, heart, anchor, violin, camera
- `bg`: sky, dusk, night, red, green, blue, gold, cream, violet, sea
- `value`: the face value, 1–99 (kopecks)
- `series`: lipovka, zarechye, station, ozerki, kordon, gorodok, seasons, holidays, far, post, radio

## Templates — `templates.tsv` (recurring mail, forever)

`key  every  day  months  to  kind  from_ru  from_en  brief_ru  brief_en  news_ru  news_en  stamp`

- `every`: `weekly` (day = 1–7, Monday = 1), `monthly` (day = 1–28), `yearly` (day = `MM-DD`),
  `birthday` (day empty: on each listed resident's birthday)
- `to`: comma-separated resident ids
- `news_ru`/`news_en`: several variants separated by ` | ` (space, pipe, space); one is picked each time.
  Placeholders: `{name}` the resident's first name, `{year}` how many years the postman has served (1, 2…).

## Fillers — `fillers.tsv` (everyday letters that fill the bag)

`tags  from_ru  from_en  brief_ru  brief_en  news_ru  news_en`

- `tags`: who may receive it: `old`, `young`, `family`, `child`, `any` (comma-separated)
- Generic but concrete: a letter from a cousin, a nephew's drawing, a catalogue, a reply from a pen-pal,
  a recipe, a parcel of old clothes… `{name}` works here too. Each filler is used at most once a year per
  resident.

## Events — `events.tsv` (seasonal village events, every year)

`key  start  end  district  look  name_ru  name_en  notice_ru  notice_en  brief_ru  brief_en  stamp`

- `start`/`end`: `MM-DD`, or `easter±N` (Orthodox Easter, used only for Maslenitsa: `easter-55`…`easter-49`)
- `look`: how the village looks during it: fair, newyear, maslenitsa, kupala, haymaking, harvest, cranes,
  firstsnow, icebreak, fishing, railway, apples, mushrooms, school, lilac, swallows, frost, berries, none
- `notice_*`: the poster delivered to a few houses on the first day; `brief_*`: the evening line.
