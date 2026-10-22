"""Group B content: Lipovka — Mikhalych, Zina, Kolya, Granny Nina, Lidia, the Sokolovs.

python tools/content_src/b.py          ->  arcs/b.tsv, items/b.tsv, stamps/b.tsv
python tools/content_src/b.py --sim    ->  also prints how long each arc takes for every start month
"""
import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "app/src/main/assets/content"

ARC_COLS = ["arc", "n", "gap", "months", "on", "needs", "kind", "to", "from_ru", "from_en", "brief_ru", "brief_en",
            "news_ru", "news_en", "reply", "gift", "stamp", "sets"]

ITEMS = [
    # key, family, variant, name_ru, name_en
    ("b_honey_linden", "jar", "honey", "Липовый мёд Михалыча", "Mikhalych's linden honey"),
    ("b_wax_candle", "candle", "honey", "Восковая свеча", "A beeswax candle"),
    ("b_comb", "honeycomb", "frame", "Рамка с сотами", "A honeycomb frame"),
    ("b_oregano_tea", "tea", "herbs", "Душица с башкирской горы", "Oregano from a Bashkir hill"),
    ("b_fair_badge", "badge", "honey", "Значок медовой ярмарки", "Honey fair badge"),
    ("b_marfa_honey", "jar", "honey", "Марфин мёд", "Marfa's honey"),
    ("b_bee_book", "book", "brown", "Книжка «Пчела знает»", "The Bee Knows, signed"),
    ("b_tea_sample", "tea", "tin", "Чай из каталога", "Tea from the catalogue"),
    ("b_kalach", "bread", "kalach", "Зинин калач", "Zina's kalach"),
    ("b_tula_gingerbread", "bread", "gingerbread", "Тульский пряник", "A Tula gingerbread"),
    ("b_ivan_tea", "tea", "herbs", "Иван-чай от Лизы", "Liza's fireweed tea"),
    ("b_tearoom_photo", "photo", "group", "Фото из чайной", "A photo from the tea room"),
    ("b_qsl_japan", "qsl", "red", "Карточка из Саппоро", "A QSL card from Sapporo"),
    ("b_qsl_sedov", "qsl", "blue", "Карточка с «Седова»", "A QSL card from the Sedov"),
    ("b_qsl_zealand", "qsl", "green", "Карточка из Новой Зеландии", "A QSL card from New Zealand"),
    ("b_fuji_card", "postcard", "mountains", "Открытка с Фудзи", "A Mount Fuji postcard"),
    ("b_pie_berry", "pie", "berry", "Ягодный пирог на дорогу", "A berry pie for the road"),
    ("b_window_thermo", "thermometer", "window", "Термометр от Глеба", "Gleb's window thermometer"),
    ("b_pie_cabbage", "pie", "cabbage", "Пирог бабы Нины", "Granny Nina's pie"),
    ("b_sushki", "bread", "pretzel", "Сушки для кордона", "Sushki meant for the cordon"),
    ("b_nina_mushrooms", "jar", "mushrooms", "Грибочки бабы Нины", "Granny Nina's mushrooms"),
    ("b_pie_apple", "pie", "apple", "Яблочный пирог «на нервах»", "A nervous apple pie"),
    ("b_nina_scarf", "scarf", "red", "Красный шарф бабы Нины", "Granny Nina's red scarf"),
    ("b_detective", "book", "red", "Лишний детектив", "A spare detective novel"),
    ("b_amber", "found", "amber", "Янтарик из Калининграда", "A bit of Baltic amber"),
    ("b_gift_book", "book", "blue", "Книга от читателей", "A book sent by readers"),
    ("b_pie_fish", "pie", "fish", "Рыбник бабы Нины", "Granny Nina's fish pie"),
    ("b_morozko_photo", "photo", "group", "Фото с «Морозко»", "A photo from Morozko"),
    ("b_big_mittens", "mittens", "patterned", "Варежки не по размеру", "Mittens of the wrong size"),
    ("b_goat_bell", "bell", "small", "Козий колокольчик", "A goat bell"),
    ("b_apples", "basket", "apples", "Яблоки Соколовых", "The Sokolovs' apples"),
    ("b_knitted_socks", "socks", "striped", "Носки от Диминой мамы", "Socks from Dima's mum"),
    ("b_asya_card", "postcard", "flowers", "Открытка «Ася и коза»", "Marina's card: Asya and the goat"),
    ("b_dima_pickles", "jar", "cucumbers", "Огурцы Димы", "Dima's pickles"),
    ("b_willow", "bouquet", "willow", "Вербочки от Аси", "Pussy willow from Asya"),
    ("b_surguch_book", "book", "green", "«Кот Сургуч и почта Липовки»", "Surguch the Cat and the Lipovka Post"),
]

STAMPS = [
    # key, family, bg, value, name_ru, name_en, series
    ("b_bee_lipa", "bee", "gold", 5, "Пчела на липе", "Bee on a linden", "lipovka"),
    ("b_wintering", "snowflake", "night", 4, "Зимовка", "Wintering", "seasons"),
    ("b_bort", "tree", "green", 12, "Борть", "The wild hive", "far"),
    ("b_altai", "mountain", "sky", 10, "Алтай", "The Altai", "far"),
    ("b_queen_post", "bee", "cream", 25, "Живая посылка", "Live parcel", "post"),
    ("b_linden", "flower", "gold", 6, "Липа цветёт", "Linden in bloom", "seasons"),
    ("b_honey_fair", "sun", "gold", 15, "Медовая ярмарка", "Honey fair", "holidays"),
    ("b_yakutia", "moon", "night", 20, "Якутская ночь", "Yakutian night", "far"),
    ("b_bee_book", "book", "cream", 8, "Пчела знает", "The Bee Knows", "lipovka"),
    ("b_tea_kettle", "kettle", "red", 3, "Чайник", "The kettle", "lipovka"),
    ("b_spb", "bridge", "dusk", 10, "Петербург", "St Petersburg", "far"),
    ("b_new_year", "fireworks", "night", 7, "С Новым годом", "Happy New Year", "holidays"),
    ("b_samovar", "kettle", "gold", 30, "Тульский самовар", "Tula samovar", "lipovka"),
    ("b_heart", "heart", "red", 10, "С любовью", "With love", "holidays"),
    ("b_birthday", "flower", "red", 5, "С днём рождения", "Happy birthday", "holidays"),
    ("b_qsl_bureau", "radio", "blue", 4, "QSL-бюро", "QSL bureau", "radio"),
    ("b_crane_japan", "crane", "sky", 40, "Журавли Хоккайдо", "Hokkaido cranes", "far"),
    ("b_iss", "rocket", "night", 12, "На орбите", "In orbit", "radio"),
    ("b_parrot", "bird", "green", 35, "Амазония", "Amazonia", "far"),
    ("b_icebreaker", "anchor", "sea", 15, "Радист ледокола", "Icebreaker operator", "radio"),
    ("b_sedov", "ship", "sea", 50, "Барк «Седов»", "Barque Sedov", "far"),
    ("b_kordon", "fir", "green", 6, "Сосновый кордон", "Pine Cordon", "kordon"),
    ("b_blizzard", "snowflake", "night", 8, "Буран на кордоне", "Blizzard at the cordon", "kordon"),
    ("b_antarctica", "snowflake", "sky", 60, "Антарктида", "Antarctica", "radio"),
    ("b_globe", "globe", "sea", 45, "Антиподы", "Antipodes", "far"),
    ("b_telegram", "telegram", "cream", 10, "Телеграмма", "Telegram", "post"),
    ("b_iceland", "lighthouse", "sea", 30, "Исландия", "Iceland", "far"),
    ("b_birch", "birch", "sky", 3, "Берёза с антенной", "Birch with an aerial", "lipovka"),
    ("b_library", "book", "blue", 4, "Библиотека", "The library", "lipovka"),
    ("b_baltic", "lighthouse", "dusk", 14, "Балтика", "The Baltic", "far"),
    ("b_letters", "letter", "cream", 5, "Письма со всей страны", "Letters from everywhere", "post"),
    ("b_morozko", "fir", "night", 9, "Морозко", "Morozko", "holidays"),
    ("b_film", "camera", "dusk", 7, "Кино в клубе", "Club cinema", "lipovka"),
    ("b_star_award", "star", "gold", 20, "Лучшая библиотека", "Best library", "lipovka"),
    ("b_chimney", "house", "dusk", 5, "Дымок из трубы", "Chimney smoke", "lipovka"),
    ("b_frost", "snowflake", "sky", 6, "Минус тридцать", "Thirty below", "seasons"),
    ("b_seeds", "flower", "green", 2, "Рассада", "Seedlings", "seasons"),
    ("b_goat", "goat", "green", 8, "Коза Ириска", "Iriska the goat", "zarechye"),
    ("b_apple", "apple", "red", 4, "Яблоки", "Apples", "seasons"),
    ("b_baby_sun", "sun", "sky", 10, "Солнышко", "Little sun", "holidays"),
    ("b_rowan", "berry", "red", 5, "Рябина", "Rowan", "seasons"),
    ("b_siskin", "bird", "cream", 6, "Синица", "Blue tit", "post"),
    ("b_cat_post", "cat", "blue", 10, "Кот Сургуч", "Surguch the cat", "post"),
]

ROWS = []
_n = {}


def B(arc, gap, kind, to, frm, brief, news, months="", on="", needs="", reply="", gift="", stamp="", sets=""):
    _n[arc] = _n.get(arc, 0) + 1
    ROWS.append([arc, str(_n[arc]), str(gap), months, on, needs, kind, to, frm[0], frm[1], brief[0], brief[1],
                 news[0], news[1], reply, gift, stamp, sets])


# =====================================================================================================
# MIKHALYCH — the beekeeper. Bees are people to him: «барышни», the queen Marfa.
# =====================================================================================================
A = "mikhalych"
CLUB = ("Клуб пчеловодов, секр. Гусев", "Beekeepers' Club, Sec. Gusev")
HERALD = ("«Пасечный вестник»", "The Apiary Herald")
RASHIT = ("Рашит Ишбулатов, Башкирия", "Rashit Ishbulatov, Bashkiria")

B(A, 3, "newspaper", "mikhalych", HERALD,
  ("Михалычу пришёл «Пасечный вестник» — листок клуба пчеловодов.",
   "Mikhalych got the Apiary Herald, the beekeepers' club newsletter."),
  ("Учат, как понять, о чём пчёлы гудят. Будто я не знаю. Мои барышни гудят о двух вещах: о погоде и о соседях. "
   "Четыре страницы про это. Ничего, почитаю им вслух, им приятно, когда про них пишут.",
   "They teach you how to tell what bees are humming about. As if I didn't know. My young ladies hum about two "
   "things: the weather and the neighbours. Four pages on that. Never mind, I'll read it to them aloud — they like being written about."),
  stamp="b_bee_lipa")

B(A, 12, "letter", "mikhalych", ("Л. Г. Шустова, Норильск", "L. G. Shustova, Norilsk"),
  ("Михалычу написали из Норильска: банка мёда доехала целой.",
   "A letter from Norilsk: Mikhalych's jar of honey arrived in one piece."),
  ("Учительница из Норильска пишет: открыла банку посреди полярной ночи — и на кухне запахло июлем. "
   "Будет, говорит, по ложке в день, чтобы на год хватило. Отнесёте ответ? Напишу ей про донник: она не знает, что такое донник.",
   "A schoolteacher in Norilsk writes that she opened the jar in the middle of the polar night and her kitchen "
   "smelled of July. A spoonful a day, she says, to make it last the year. Will you take my answer? I'll tell her "
   "about sweet clover. She doesn't know what sweet clover is."),
  reply="out")

B(A, 20, "letter", "mikhalych", ("Пчелопитомник, Бурзянский р-н", "Bee nursery, Burzyan district"),
  ("Михалычу ответили из Башкирии: матку пришлют почтой.",
   "Bashkiria replied to Mikhalych: the queen bee will come by post."),
  ("Заказал себе матку из Башкирии, бурзянскую. Тёмная лесная пчела, бортевая — такие в дуплах живут, сколько мир стоит. "
   "Пишут: пришлём почтой. Почтой! Вы уж тогда сумку не трясите. Отвечу им, что жду.",
   "I've ordered a queen from Bashkiria, a Burzyan bee. A dark forest bee — they've lived in hollow trees for "
   "as long as the world has stood. They write: we'll send her by post. By post! Don't shake your bag that day. "
   "I'll write back that I'm waiting."),
  reply="out", stamp="b_bort")

B(A, 25, "parcel", "mikhalych", CLUB,
  ("Михалычу прислали вощину — готовит новые соты.",
   "Mikhalych received foundation wax for new honeycomb."),
  ("Вощина пришла, будущие соты. Понюхайте, как пахнет. А это вам свечка, сам катал из прошлогоднего воска. "
   "Зажжёте вечером — и в комнате будет пахнуть, как у меня в омшанике: тепло и немножко лета.",
   "The foundation's come — tomorrow's honeycomb. Smell it. And here's a candle for you, I rolled it myself "
   "from last year's wax. Light it in the evening and your room will smell like my winter house: warm, with a "
   "little summer in it."),
  gift="b_wax_candle")

B(A, 30, "telegram", "mikhalych", ("Пчелопитомник, Башкирия", "Bee nursery, Bashkiria"),
  ("Телеграмма Михалычу: «Матка выслана, встречайте».",
   "A telegram for Mikhalych: 'Queen sent, meet her.'"),
  ("МАТКА ВЫСЛАНА ПОЧТОЙ ВСТРЕЧАЙТЕ. Слышали? Встречайте! Как поезд. Я теперь каждое утро к вам на почту ходить буду, "
   "не сердитесь. Ей в дороге нужно тепло, темно и чтобы не трясли.",
   "QUEEN SENT BY POST MEET HER. Did you hear? Meet her! Like a train. I'll be at the post office every morning "
   "now, don't be cross. On the road she needs warmth, darkness and no shaking."),
  months="5,6,7")

B(A, 4, "parcel", "mikhalych", ("Пчелопитомник, Башкирия", "Bee nursery, Bashkiria"),
  ("Живая пчелиная матка доехала до Михалыча по почте!",
   "A live queen bee reached Mikhalych by post!"),
  ("Живая! Слышите, шуршит? Это свита, восемь пчёлок, кормят её в дороге, канди у них с собой. "
   "Царица в клеточке со спичечный коробок, а проехала полстраны. Назову её Марфой. Постойте, я при вас её в улей пущу — вы же её везли.",
   "Alive! Hear the rustling? That's her retinue, eight worker bees feeding her on the road, they brought their "
   "own candy. A queen in a cage the size of a matchbox, and she's crossed half the country. I'll call her Marfa. "
   "Stay — I'll let her into the hive while you watch. You carried her, after all."),
  months="5,6,7,8", stamp="b_queen_post", sets="mikhalych.queen")

B(A, 18, "letter", "mikhalych", CLUB,
  ("Клуб просит Михалыча написать, как приняли новую матку.",
   "The club asks Mikhalych how the new queen was accepted."),
  ("Гусев пишет: «Сообщите, как приняли». Приняли! Три дня семья её через сетку нюхала, а теперь Марфа уже червит — "
   "полторы тысячи яиц в день. Я за всю жизнь столько не сделал. Отнесите заметку, я там и про вас написал: везли бережно.",
   "Gusev writes: 'Report how she was received.' Received! The colony sniffed her through the mesh for three days, "
   "and now Marfa is laying — fifteen hundred eggs a day. I haven't done that much in my whole life. Take my note to "
   "them; I wrote about you too, that you carried her gently."),
  months="6,7,8", reply="out")

B(A, 5, "postcard", "mikhalych", ("Покупатели со всей страны", "Customers from all over"),
  ("У Михалыча день рождения — открытки от покупателей отовсюду.",
   "It's Mikhalych's birthday: postcards from customers everywhere."),
  ("Я в самый медовый день родился, мать говорила — оттого и сладкоежка. Тридцать открыток! И из Норильска, от "
   "учительницы, с оленем. Пчёлам расскажу. Оставлю им сегодня лишнюю рамку, пусть тоже празднуют.",
   "I was born on the sweetest day of the year — my mother said that's why I've a sweet tooth. Thirty postcards! "
   "One from Norilsk too, from the teacher, with a reindeer. I'll tell the bees. I'll leave them an extra frame "
   "today so they can celebrate as well."),
  months="8", on="08-14", stamp="b_linden")

B(A, 18, "letter", "mikhalych", ("Заказы: Тула, Омск, Псков", "Orders: Tula, Omsk, Pskov"),
  ("Михалычу пачка заказов на мёд — качка в разгаре.",
   "A stack of honey orders for Mikhalych: the extracting is in full swing."),
  ("Качаю! Медогонка с утра гудит, руки липкие, письма тоже — простите, если конверт к вам пристанет. "
   "Тула просит гречишного, Омск — липового, Псков — «какого не жалко». Псков люблю. Вот вам рамка, жуйте прямо с воском.",
   "Extracting! The honey spinner's been humming since dawn, my hands are sticky and so are the letters — sorry if "
   "an envelope sticks to you. Tula wants buckwheat, Omsk wants linden, Pskov wants 'whatever you can spare'. I love "
   "Pskov. Here's a frame for you — chew it, wax and all."),
  months="8,9", gift="b_comb")

B(A, 20, "newspaper", "mikhalych", HERALD,
  ("В «Пасечном вестнике» итоги медовой ярмарки. Михалыч не ездил.",
   "The Apiary Herald prints the honey fair results. Mikhalych didn't go."),
  ("Ярмарка прошла без меня, и Гусев взял золото. Гречишным! Гречишный у него хороший, не спорю, тёмный, как дёготь. "
   "Но моя липа… Ладно. На будущий год поеду. Марфа таких дочерей наведёт — Гусев свой мёд обратно в ульи понесёт.",
   "The fair went on without me and Gusev took the gold. With buckwheat! Good buckwheat, I won't deny it, dark as "
   "tar. But my linden… Fine. Next year I'm going. Marfa will raise such daughters that Gusev will carry his honey "
   "back to the hives."),
  months="8,9,10")

B(A, 20, "letter", "mikhalych", CLUB,
  ("Клуб просит Михалыча отчитаться, как ульи ушли в зиму.",
   "The club wants Mikhalych to report how his hives went into winter."),
  ("Отчёт им подавай. Пишу: двадцать два семейства, все в омшанике, все при мёде. Последних сегодня занёс. "
   "Гудят там тихонько, ровно — будто в соседней комнате печка топится. Возьмите баночку, это липовый, самый первый.",
   "They want a report. I'm writing: twenty-two colonies, all in the winter house, all with honey. Carried the "
   "last ones in today. They hum in there quietly and evenly, like a stove burning in the next room. Take a jar — "
   "linden, the first of the year."),
  months="10,11", gift="b_honey_linden")

B(A, 30, "letter", "mikhalych", RASHIT,
  ("Михалычу пишет пчеловод из Башкирии — тот, что прислал Марфу.",
   "The Bashkir beekeeper who sent Marfa writes to Mikhalych."),
  ("Рашит спрашивает, как Марфа. У них снегу по пояс, пчёлы тоже спят. Чудно: ни разу его не видел, а будто с соседом "
   "через забор говорю. Отпишу, что Марфа зимует в третьем улье, у самой стенки, где теплее.",
   "Rashit asks after Marfa. They've snow up to the waist and their bees are asleep too. Funny: I've never seen the "
   "man, and it's like talking to a neighbour over the fence. I'll write that Marfa's wintering in hive three, right "
   "by the wall where it's warmest."),
  months="11,12", reply="out", stamp="b_bort")

B(A, 25, "newspaper", "mikhalych", HERALD,
  ("Зимний «Пасечный вестник»: как слушать улей через трубку.",
   "The winter Apiary Herald: how to listen to a hive through a tube."),
  ("Советуют слушать улей через резиновую трубку. Я тридцать лет ухом к стенке прикладываюсь. Гудят ровно — спят. "
   "Шипят — кто-то их потревожил. Мышь, наверное. Пойду проверю, у меня с мышами отдельный разговор.",
   "They recommend listening to a hive through a rubber tube. I've put my ear to the wall for thirty years. "
   "An even hum — they're asleep. A hiss — someone's bothering them. A mouse, most likely. I'll go and check; "
   "the mice and I have things to discuss."),
  months="12,1,2", stamp="b_wintering")

B(A, 40, "parcel", "mikhalych", RASHIT,
  ("Рашит прислал Михалычу гостинец — дикий бортевой мёд.",
   "Rashit sent Mikhalych a present: wild honey from a tree hive."),
  ("Бортевой мёд, из дупла. Попробовал: горчит, дикий, лесом пахнет. Моему не чета — мой-то домашний, воспитанный. "
   "А это вам — душица с его горы, в чай. Он и вам кланяется, я ему про вас писал.",
   "Tree-hive honey, from a hollow. I tasted it: bitter, wild, smells of the forest. Nothing like mine — mine's "
   "home-bred, well brought up. And this is for you: oregano from his hill, for your tea. He sends his regards; "
   "I've written to him about you."),
  months="1,2,3", gift="b_oregano_tea")

B(A, 20, "postcard", "mikhalych", ("Ефим, пасека на Алтае", "Yefim, an apiary in the Altai"),
  ("Михалычу открытка с Алтая: у друга уже был облёт.",
   "A postcard from the Altai: a friend's bees have had their first flight."),
  ("Ефим хвастает: у него облёт был. А у меня сегодня! Вылетели, покружили — и весь двор в жёлтых точечках: "
   "всю зиму терпели, простите. Соседка бельё вывесила, теперь со мной не разговаривает. К медосбору помиримся, банку ей отнесу.",
   "Yefim's boasting about his bees' first flight. Well, mine was today! Out they flew, round they went, and the "
   "whole yard is speckled yellow — they'd held it in all winter, forgive me. My neighbour had her washing out; "
   "she isn't speaking to me. We'll make up by the honey harvest, I'll take her a jar."),
  months="3,4", stamp="b_altai")

B(A, 30, "parcel", "mikhalych", CLUB,
  ("У Михалыча помощница — клуб прислал детскую сетку.",
   "Mikhalych has a helper: the club sent a child's bee veil."),
  ("Варя Кузнецова ко мне в помощницы просится, говорит, будет учёной по пчёлам. Клуб прислал сетку детскую — гляньте, "
   "маленькая какая. Дымарь Варя уже держит правильно. А главное — руками не машет. Пчела того, кто машет, не уважает.",
   "Varya Kuznetsova wants to be my helper — she says she'll be a bee scientist. The club sent a child's veil — "
   "look how small. She already holds the smoker right. And the main thing, she doesn't flap her arms. A bee has "
   "no respect for anyone who flaps."),
  months="4,5,6")

B(A, 30, "letter", "mikhalych", ("Оргкомитет медовой ярмарки", "Honey Fair Committee"),
  ("Михалыча приняли на областную медовую ярмарку.",
   "Mikhalych has been accepted for the regional honey fair."),
  ("Приняли заявку! Повезу липовый, майский и — вот увидите — Марфин. Её дочки нынче носят мёд светлый, как солнце "
   "сквозь занавеску. Варя этикетки рисует: на каждой пчела в косынке.",
   "They've accepted me! I'm taking linden, May honey and — just you watch — Marfa's. Her daughters are bringing "
   "in honey this year as pale as sunlight through a curtain. Varya's drawing the labels: on each one a bee in a headscarf."),
  months="6,7")

B(A, 30, "registered", "mikhalych", ("Областная медовая ярмарка", "Regional Honey Fair"),
  ("Михалычу заказным пришла медаль медовой ярмарки — серебро!",
   "Mikhalych's honey fair medal came by registered post: silver!"),
  ("Серебро! За липовый. Гусев опять золото, ну и пусть, мы с ним вечером чай пили и помирились. А это вам значок — "
   "их всем участникам давали, я два взял. Вы ж Марфу везли, значит, тоже из участников.",
   "Silver! For the linden. Gusev took gold again, and good luck to him — we had tea that evening and made peace. "
   "And this badge is for you: every participant got one and I took two. You carried Marfa, so you took part too."),
  months="8,9", gift="b_fair_badge", stamp="b_honey_fair", sets="mikhalych.medal")

B(A, 12, "newspaper", "mikhalych", ("«Сельская новь»", "The Village News"),
  ("В «Сельской нови» статья про Михалыча и его медаль.",
   "The Village News runs a piece on Mikhalych and his medal."),
  ("Пропечатали! «Пасечник Рой: пчела любит тихих». Это я сказал, точно. А фотография — ой. Шляпа набок, борода в воске. "
   "Ну что ж, какой есть. Вырежу и в омшанике повешу: пусть барышни видят, с кем живут.",
   "They printed it! 'Beekeeper Roy: bees love quiet people.' I did say that. But the photo — oh dear. Hat askew, "
   "wax in my beard. Well, that's me. I'll cut it out and hang it in the winter house so the ladies can see who "
   "they live with."),
  months="9,10")

B(A, 25, "letter", "mikhalych", ("Айта, 10 лет, Якутск", "Aita, aged 10, Yakutsk"),
  ("Девочка из Якутска спрашивает Михалыча: можно ли у них держать пчёл?",
   "A girl in Yakutsk asks Mikhalych if bees can live where she does."),
  ("Айта пишет, прочитала про меня. Спрашивает: можно ли у них держать пчёл? Можно, Айта! В Якутии пасеки есть: лето "
   "короткое, да жаркое, пчела успевает. Весь вечер буду ей отвечать, с картинками. Потом отнесёте.",
   "Aita read about me. She asks whether you can keep bees where she lives. You can, Aita! There are apiaries in "
   "Yakutia: the summer's short but hot, and the bees make it in time. I'll spend the whole evening on my answer, "
   "with drawings. Then you'll take it."),
  months="10,11", reply="out", stamp="b_yakutia")

B(A, 40, "letter", "mikhalych", CLUB,
  ("Клуб просит Михалыча написать книжку о пчёлах.",
   "The club asks Mikhalych to write a little book about bees."),
  ("Книжку, говорят, напишите. Для начинающих. Я — книжку! Я за всю жизнь только накладные писал. Хотя… зимой ночи "
   "длинные. Завёл тетрадку, первая глава — «Как с пчелой здороваться». Не смейтесь, это самое важное.",
   "Write a book, they say. For beginners. Me — a book! I've written nothing in my life but delivery notes. "
   "Although… winter nights are long. I've started an exercise book; chapter one is 'How to Greet a Bee'. Don't "
   "laugh, it's the most important part."),
  months="12,1,2")

B(A, 35, "parcel", "mikhalych", ("Радиодетали почтой, Москва", "Radio parts by mail, Moscow"),
  ("Михалычу посылка с радиодеталями. Это Колины весы для улья.",
   "Radio parts for Mikhalych? They're for Kolya's hive scales."),
  ("Это Коле Рябинину, на мой адрес выписал. Весы делает под улей, с передатчиком: будет по радио слышно, сколько "
   "Марфины внучки за день принесли. Я-то по гулу знаю. Но пусть: интересно, кто из нас точнее.",
   "This is for Kolya Ryabinin; he had it sent to my address. He's building scales to go under a hive, with a "
   "transmitter: you'll hear over the radio how much Marfa's granddaughters brought in that day. I can tell by "
   "the hum. But let him — I'm curious which of us is more accurate."),
  months="2,3,4")

B(A, 30, "letter", "mikhalych", ("Редактор клуба, Вологда", "Club editor, Vologda"),
  ("Редактор прислал Михалычу замечания к рукописи.",
   "The editor sent Mikhalych notes on his manuscript."),
  ("Редактор пишет: «Пётр Михайлович, у вас пчёлы в каждой главе обижаются, радуются и сплетничают. Это не по науке». "
   "А по чему же ещё? Сорок лет с ними живу. Оставил. Рисунки Марина Соколова сделает: с натуры, говорит.",
   "The editor writes: 'Pyotr Mikhailovich, in every chapter your bees take offence, rejoice and gossip. That isn't "
   "scientific.' What else would it be? I've lived with them forty years. I left it in. Marina Sokolova will do the "
   "drawings — from life, she says."),
  months="4,5")

B(A, 35, "letter", "mikhalych", RASHIT,
  ("У Марфы теперь династия: её дочерей просят три клуба.",
   "Marfa has a dynasty now: three clubs want her daughters."),
  ("Рашит пишет, у него Марфину родню просят. А у меня самого просят! Три клуба: пришлите дочку Марфы. Была одна царица "
   "в коробке, а теперь — династия. Возьмите баночку Марфиного, лучше у меня не бывало.",
   "Rashit writes that people are asking him for Marfa's kin. They're asking me too! Three clubs: send us one of "
   "Marfa's daughters. One queen in a box, and now a dynasty. Take a jar of Marfa's — I've never had better."),
  months="5,6,7", gift="b_marfa_honey")

B(A, 30, "parcel", "mikhalych", ("Типография, Городок", "Printing house, Gorodok"),
  ("Михалычу пришла его книжка — «Пчела знает».",
   "Mikhalych's book has arrived: The Bee Knows."),
  ("Вот она. «Пчела знает». Сто экземпляров, тоненькая, а тяжёлая — от гордости, наверное. Первую — тому, кто Марфу вёз. "
   "Подписал: «Почте Липовки — с поклоном и мёдом». И пчела на обложке Маринина, в косынке, как у Вари.",
   "Here it is. The Bee Knows. A hundred copies, thin, yet heavy — with pride, I expect. The first goes to whoever "
   "carried Marfa. I signed it: 'To the Lipovka Post, with a bow and honey.' And the bee on the cover is Marina's, "
   "in a headscarf, like Varya's."),
  months="6,7,8", gift="b_bee_book", stamp="b_bee_book")

B(A, 40, "letter", "mikhalych", ("Читатели «Пчела знает»", "Readers of The Bee Knows"),
  ("Михалычу пишут читатели его книжки.",
   "Readers of his book write to Mikhalych."),
  ("Один пишет: прочитал и пошёл к своим ульям здороваться. Вот! Значит, не зря. Барышни мои летают, а я вечерами "
   "письма читаю — им вслух, конечно. Вы заходите: чай у меня всегда с мёдом, а мёд — всегда с разговором.",
   "One man writes that he read it and went straight out to say hello to his hives. There! Not for nothing, then. "
   "My ladies are out flying, and in the evenings I read the letters — aloud to them, of course. Do drop in: my tea "
   "always comes with honey, and my honey always comes with a chat."),
  months="8,9,10", stamp="b_letters")

# =====================================================================================================
# ZINA — the shop. Quick, nosy, generous. Son Artyom in St Petersburg, the tea room, Liza.
# =====================================================================================================
A = "zina"
DEPOT = ("Оптовая база, Городок", "Wholesale depot, Gorodok")
ARTYOM = ("Артём, Санкт-Петербург", "Artyom, St Petersburg")
LIZA = ("Лиза, Санкт-Петербург", "Liza, St Petersburg")
TULA = ("Тульский самоварный завод", "Tula Samovar Works")
NOTICE_Z = ("Зинаида Павловна, магазин", "Zinaida Pavlovna, the shop")

B(A, 2, "letter", "zina", DEPOT,
  ("Зинаиде Павловне счёт с оптовой базы: гречка опять дороже.",
   "An invoice from the depot for Zinaida Pavlovna: buckwheat's up again."),
  ("Гречка опять подорожала, на рубль сорок, грабёж. А вы к Соколовым заходили? У них из трубы такой дым, будто шины жгут. "
   "Москвичи, что с них взять. Нате вот карамельку, вид у вас усталый.",
   "Buckwheat's gone up again, a rouble forty — daylight robbery. Have you been by the Sokolovs'? Their chimney "
   "smokes like they're burning tyres. Muscovites, what do you expect. Here, have a sweet, you look tired."))

B(A, 12, "letter", "zina", ARTYOM,
  ("Зинаиде Павловне письмо от сына Артёма из Петербурга.",
   "Zinaida Pavlovna has a letter from her son Artyom in St Petersburg."),
  ("Артёмка пишет! У него мосты, сопромат — не знаю, что это, но звучит страшно. Просит огурцов моих. Двадцать один год, "
   "в Петербурге живёт, а просит огурцов из Липовки. Значит, правильно растила. Отправлю банку — пусть с соседом поделится.",
   "Artyom's written! Bridges, strength of materials — I don't know what that is, but it sounds frightening. He's "
   "asking for my pickles. Twenty-one, living in St Petersburg, and he wants cucumbers from Lipovka. So I raised "
   "him right. I'll send a jar; he can share with his roommate."),
  reply="out", stamp="b_spb")

B(A, 15, "parcel", "zina", ("Чайный дом, каталог", "Tea house catalogue"),
  ("Зине пришёл каталог чая. Зина мечтает о чайной.",
   "Zina got a tea catalogue. She's dreaming of a tea room."),
  ("Каталог чая, сорок сортов. Скажу по секрету, хоть вы и так никому: хочу чайную. В задней комнате, где сейчас макароны "
   "штабелем. Столики, скатерти, самовар. Чтоб люди не хлеб брали и бегом, а сидели. Вот пробник вам — я уже кружочками обвела.",
   "A tea catalogue, forty kinds. I'll tell you a secret, though you'd never tell anyone anyway: I want a tea room. "
   "In the back, where the pasta's stacked now. Little tables, tablecloths, a samovar. So people don't just grab "
   "bread and run, but sit. Here's a sample for you — I've already circled what I like."),
  gift="b_tea_sample", stamp="b_tea_kettle")

B(A, 30, "letter", "zina", TULA,
  ("Зине прислали каталог тульских самоваров.",
   "Zina has a catalogue of Tula samovars."),
  ("Самовары! На углях, на шишках, электрические — нет, электрический это чайник с претензией. Вот этот: медный, "
   "семь литров, с медалями на боку. Дорого. Но я двадцать лет на одной кассе сижу, могу себе одну глупость позволить. "
   "Никому не говорите. Хотя нет, скажите.",
   "Samovars! Charcoal, pine cones, electric — no, an electric one's just a kettle with airs. This one: copper, "
   "seven litres, medals on its side. Expensive. But I've sat at the same till for twenty years; I'm allowed one "
   "folly. Don't tell anyone. Actually, do."),
  stamp="b_samovar")

B(A, 25, "registered", "zina", ("Администрация поселения", "Village Council"),
  ("Зине разрешили открыть чайную в задней комнате магазина.",
   "Zina's been allowed to open a tea room at the back of the shop."),
  ("Разрешили! Печать, подпись: «при соблюдении санитарных норм». Соблюду, у меня и так чище, чем у них в кабинете. "
   "Макароны теперь куда? Ладно, в сарай. Вы мне в субботу ящики перетаскать не поможете? Шучу. Но если поможете — пирожок.",
   "Approved! Stamp, signature: 'subject to sanitary standards'. I'll meet them; my place is cleaner than their "
   "office as it is. Where does the pasta go now? Fine, the shed. Would you help me shift the crates on Saturday? "
   "Joking. But if you do, there's a pie in it."),
  months="2,3,4,5,6")

B(A, 20, "parcel", "zina", ("Фарфоровый завод, посуда почтой", "Porcelain works, mail order"),
  ("Зине пришли чашки для чайной — одна с отбитым краем.",
   "Cups for Zina's tea room arrived — one with a chipped rim."),
  ("Двенадцать чашек, синие, с золотым ободком. Одиннадцать целых. А эта с отбитым краешком. Жалобу писать не буду: "
   "пусть у вас на почте живёт, вы ж там чай пьёте из чего попало, я видела. Только краем к себе не поворачивайте.",
   "Twelve cups, blue with a gold rim. Eleven whole. This one's chipped. I won't complain — let it live at your "
   "post office, you drink tea out of any old thing there, I've seen. Just don't turn the chip towards you."),
  months="3,4,5,6")

B(A, 25, "letter", "zina", ARTYOM,
  ("Артём приедет летом — с другом, красить чайную.",
   "Artyom's coming in summer with a friend to paint the tea room."),
  ("Артём летом приедет с товарищем, с Серёжей, обещают чайную покрасить. Товарищ… Я в письме спрашиваю: Серёжа-то хоть "
   "с бородой? Он отвечает: с бородой, мама, успокойся. Ладно. Краску закажу голубую, как у вас на почте крыша.",
   "Artyom's coming this summer with a friend, Seryozha; they've promised to paint the tea room. A friend… I asked "
   "in my letter: does this Seryozha at least have a beard? He wrote back: yes, Mum, he has a beard, calm down. "
   "All right. I'll order blue paint, like your post office roof."),
  months="4,5,6", reply="out")

B(A, 20, "parcel", "zina", TULA,
  ("Зине привезли медный самовар — тяжёлый, с медалями.",
   "Zina's copper samovar has arrived: heavy, with medals."),
  ("Довезли! Вы ж его, бедные, на тележке катили? Медный, семь литров, медали на боку, как у генерала. Я его уже назвала — "
   "Пал Палыч. Вечером первый раз раздуем, сапогом, как бабка моя делала. Приходите — первая чашка ваша.",
   "It's here! You poor things, did you wheel it on a trolley? Copper, seven litres, medals like a general's. I've "
   "named him already — Pal Palych. Tonight we fire him up for the first time, with a boot for bellows, like my "
   "granny did. Come — the first cup is yours."),
  months="5,6,7", stamp="b_samovar")

B(A, 10, "notice", "nina", NOTICE_Z,
  ("Зина зовёт всю Липовку на открытие чайной.",
   "Zina invites all of Lipovka to the opening of her tea room."),
  ("Зина чайную открывает, вы посмотрите. Всё, буду ей пироги носить, на продажу — а то куда мне одной столько? Коля ест, "
   "да разве он ест: сидит, ключом своим стучит, пирог в руке стынет.",
   "Zina's opening a tea room, would you believe. That's it, I'll take her my pies to sell — what am I to do with "
   "so many on my own? Kolya eats, but does he really? He sits tapping that key of his, and the pie goes cold in his hand."),
  months="6,7,8")

B(A, 1, "notice", "mikhalych", NOTICE_Z,
  ("Михалыч получил приглашение в чайную и сразу стал торговаться.",
   "Mikhalych got the tea room invitation and started haggling at once."),
  ("Предложил Зине мёд к самовару. Так она торговаться стала! Я говорю: Зина, вниз не торгуются. А она: я вверх торгуюсь, "
   "твой мёд дешевле стоить не может. Вот женщина. Пойду на открытие, рубашку новую надену.",
   "I offered Zina honey for her samovar. And she started haggling! I said, Zina, you don't haggle down. And she "
   "said, I'm haggling up — your honey can't cost that little. What a woman. I'll go to the opening in my new shirt."))

B(A, 1, "notice", "lidia", NOTICE_Z,
  ("Лидия Аркадьевна идёт на открытие Зининой чайной.",
   "Lidia Arkadyevna is going to the opening of Zina's tea room."),
  ("Ну что ж, теперь в Липовке два культурных учреждения, и в одном дают пирожки. Конкуренции я, пожалуй, не выдержу. "
   "Пойду. Возьму с собой книжку и оставлю у Зины на полке: вдруг кто за чаем прочтёт.",
   "Well, now Lipovka has two cultural institutions, and one of them serves pies. I doubt I can compete. I'll go. "
   "I'll take a book and leave it on Zina's shelf — someone might read it over tea."),
  sets="zina.tearoom")

B(A, 20, "letter", "zina", ARTYOM,
  ("Артём прислал фото: чайная, самовар, Серёжа с кистью.",
   "Artyom sent a photo: the tea room, the samovar, Seryozha with a brush."),
  ("Фотографию прислал: я у самовара, Серёжа с кистью, Артём щурится. Серёжа, кстати, хороший оказался, всю стену покрасил "
   "и ни разу не присел. Вы пряник возьмите, тульский: заказала к чайной, а их никто не берёт — все мои пирожки берут.",
   "He sent a photo: me by the samovar, Seryozha with a brush, Artyom squinting. Seryozha turned out a good lad — "
   "painted a whole wall without once sitting down. Take a gingerbread, a Tula one: I ordered them for the tea room "
   "and nobody buys them, they all buy my pies."),
  months="7,8,9", gift="b_tula_gingerbread")

B(A, 40, "letter", "zina", DEPOT,
  ("Зине накладные с базы: чайная требует сахару.",
   "Invoices for Zina: the tea room is getting through the sugar."),
  ("Сахару — вдвое против прошлой осени. Это всё чайная: сидят, пьют, по пять кусков. Лидия Аркадьевна с книжкой — та без "
   "сахара, принципиально. А мужики по пять и ещё в карман. Ну и пусть, сладко живём. Вам с собой кусочек положить?",
   "Twice the sugar of last autumn. It's the tea room: they sit and drink, five lumps each. Lidia Arkadyevna and "
   "her book — none, on principle. The men take five and another for the pocket. Let them; life is sweet. Shall I "
   "put a lump in your bag?"),
  months="9,10,11")

B(A, 20, "postcard", "zina", ARTYOM,
  ("Артём поздравил маму с Новым годом. Приехать не может — сессия.",
   "Artyom wishes his mum a happy New Year. He can't come: exams."),
  ("Не приедет на Новый год, сессия. А я холодца наварила на роту. Ничего, до Старого Нового года постоит, он у меня "
   "крепкий. Открытку видите? Мост ночью, разведённый. Это он, значит, мне весь Петербург прислал.",
   "He's not coming for New Year — exams. And I've made enough aspic for a regiment. Never mind, it'll keep till "
   "the Old New Year, mine sets firm. See the card? A bridge at night, raised. That's him sending me the whole of St Petersburg."),
  months="12", stamp="b_new_year")

B(A, 10, "telegram", "zina", ARTYOM,
  ("Телеграмма Зине: Артём сдал сессию и едет домой!",
   "A telegram for Zina: Artyom passed his exams and is coming home!"),
  ("СЕССИЯ СДАНА ПЯТЬ ПЯТЬ ЧЕТЫРЕ ЕДУ ЧЕТВЕРГ. Четвёрка — по чему, интересно? Ладно, не скажу, что заметила. Магазин в четверг "
   "закрываю — нет, не закрываю: пусть за прилавком со мной сидит, все посмотрят, какой вырос. Калач берите, я их три напекла.",
   "EXAMS PASSED A A B COMING THURSDAY. A B in what, I wonder? Fine, I won't let on I noticed. I'll shut the shop "
   "on Thursday — no, I won't: he can sit behind the counter with me and everyone can see how he's grown. Have a "
   "kalach, I baked three."),
  months="1,2", gift="b_kalach")

B(A, 40, "postcard", "zina", ARTYOM,
  ("Артём написал маме: у него есть Лиза.",
   "Artyom has told his mum: there's someone called Liza."),
  ("Лиза! Её зовут Лиза! Как бы между прочим, в самом конце, мелко: «Да, мама, познакомься: Лиза». Познакомься — как? "
   "Через открытку? Учится на реставратора, старую мебель лечит. Пусть и меня полечит: у меня от таких новостей сердце скачет.",
   "Liza! Her name's Liza! Tucked in at the very end, in tiny writing: 'Oh, and Mum, meet Liza.' Meet her how? "
   "Through a postcard? She's training as a restorer — mends old furniture. She can mend me too: news like this "
   "sets my heart galloping."),
  months="2,3", stamp="b_heart")

B(A, 30, "letter", "zina", LIZA,
  ("Зине написала сама Лиза — вежливо и ровным почерком.",
   "Liza herself wrote to Zina, politely, in a neat hand."),
  ("Сама написала! Почерк ровный, с наклоном, как в прописи. Спрашивает рецепт моих пирожков с луком и яйцом — Артём, видно, "
   "проболтался. Я ей рецепт и ещё полстраницы сверху, какой он был в пять лет. Отнесёте? Только не помните.",
   "She wrote herself! A neat sloping hand, like a copybook. She asks for my egg-and-onion pie recipe — Artyom "
   "must have let it slip. I've sent the recipe and half a page on what he was like at five. Will you take it? "
   "Don't crumple it."),
  months="3,4", reply="out", stamp="b_spb")

B(A, 35, "parcel", "zina", LIZA,
  ("Лиза прислала Зине иван-чай и вышитое полотенце.",
   "Liza sent Zina fireweed tea and an embroidered towel."),
  ("Посылка от Лизы: иван-чай, сама на Карельском перешейке собирала, и полотенце для чайной. Сама вышивала! Самовар на "
   "полотенце — вылитый Пал Палыч. Нате, вам пачка. Остальное заварю, проверю, умеет ли она чай выбирать. Умеет, по запаху слышу.",
   "A parcel from Liza: fireweed tea she picked herself on the Karelian Isthmus, and a towel for the tea room. "
   "She embroidered it! The samovar on it is Pal Palych to the life. Here's a packet for you. I'll brew the rest "
   "and see whether she knows her tea. She does — I can tell by the smell."),
  months="4,5,6", gift="b_ivan_tea")

B(A, 30, "letter", "zina", ARTYOM,
  ("Артём защитил диплом: теперь он инженер-мостовик.",
   "Artyom has graduated: he's a bridge engineer now."),
  ("Защитился! Инженер-мостовик мой Артём. Взяли на работу, будет мосты строить. Я ему пишу: у нас мост в Заречье сколько чинили — "
   "приезжай, покажи, как надо. А он: приедем, мама, летом, с Лизой. С Лизой! Значит, всё серьёзно.",
   "He's graduated! My Artyom's a bridge engineer. He's got a job building bridges. I wrote: look how long it took "
   "them to fix our bridge to Zarechye — come and show them how it's done. And he says: we'll come next summer, "
   "Mum, with Liza. With Liza! So it's serious."),
  months="6,7", stamp="b_spb")

B(A, 30, "postcard", "zina", ("Артём и Лиза", "Artyom and Liza"),
  ("Зине на день рождения открытка, подписанная «Артём и Лиза».",
   "A birthday card for Zina, signed 'Artyom and Liza'."),
  ("Видите, как подписали: «Артём и Лиза». Вместе, одной ручкой. Поставлю эту открытку в чайной на самовар, пусть все "
   "читают, кто зайдёт. Взрослая женщина, а реву, как девчонка. Ешьте торт, медовик, мёд Михалычев.",
   "See how they signed it: 'Artyom and Liza'. Together, with one pen. I'll stand it on the samovar in the tea room "
   "for everyone to read. A grown woman, crying like a girl. Have some cake — honey cake, with Mikhalych's honey."),
  months="9", on="09-09", stamp="b_birthday")

B(A, 50, "letter", "zina", LIZA,
  ("Лиза просит Зину не выбрасывать старый буфет.",
   "Liza begs Zina not to throw out the old sideboard."),
  ("Лиза пишет: «Зинаида Павловна, не выбрасывайте буфет». Это тот, облезлый, что в чайной стоит, ещё от свекрови. Летом, "
   "говорит, приедет и сделает из него конфетку. А я его в прошлую пятницу чуть на дрова не отдала. Теперь хожу вокруг и глажу.",
   "Liza writes: 'Zinaida Pavlovna, don't throw out the sideboard.' The shabby one in the tea room, from my "
   "mother-in-law. She says she'll come in summer and make it a treat. And last Friday I nearly gave it away for "
   "firewood. Now I walk round it and stroke it."),
  months="11,12,1")

B(A, 60, "telegram", "zina", ARTYOM,
  ("Телеграмма Зине: летом Артём приедет с Лизой.",
   "A telegram for Zina: Artyom is bringing Liza this summer."),
  ("ПРИЕДЕМ ДЕСЯТОГО ИЮЛЯ ЛИЗОЙ ГОТОВЬ ЧАЙНУЮ ГОТОВЬ СЕБЯ. «Себя» — это что значит? Это он намекает? Пойду к Лидии, пусть "
   "растолкует, она филолог. Хотя чего толковать, сама знаю. Ох. Вы за прилавком пару часов не постоите?",
   "ARRIVING JULY TENTH WITH LIZA GET TEAROOM READY GET YOURSELF READY. 'Yourself' — what does that mean? Is he "
   "hinting? I'll ask Lidia to explain, she studied language. Though what's to explain, I know. Oh my. Could you "
   "mind the counter for a couple of hours?"),
  months="5,6")

B(A, 30, "parcel", "zina", LIZA,
  ("Лиза прислала из Петербурга фото: помолвка в чайной.",
   "Liza sent a photo from St Petersburg: an engagement in the tea room."),
  ("Уехали — и сразу посылка. Фотография: я, Артём и Лиза у буфета. Буфет как новый, лаком блестит. А у Лизы на руке — "
   "видите? — колечко. Он ей прямо в чайной предложил, при Пал Палыче. Это вам, у меня их две. Повесьте у себя, вы ж свои.",
   "They'd only just gone and here's a parcel. A photo: me, Artyom and Liza by the sideboard. It looks brand new, "
   "the varnish gleams. And on Liza's hand — see? — a ring. He proposed right in the tea room, in front of Pal "
   "Palych. This one's for you, I have two. Hang it up — you're one of us."),
  months="7,8", gift="b_tearoom_photo")

B(A, 20, "letter", "zina", ("Артём и Лиза", "Artyom and Liza"),
  ("Артём и Лиза сыграют свадьбу в Липовке, в Зининой чайной.",
   "Artyom and Liza will hold their wedding in Lipovka, in Zina's tea room."),
  ("Свадьбу хотят у нас. Здесь, в чайной! Не в Петербурге, не в ресторане — в моей задней комнате, где макароны стояли. "
   "Будущим летом. Я уже список гостей пишу: вся деревня, и вы первым номером. Не отказывайтесь, я вас знаю.",
   "They want the wedding here. In the tea room! Not in St Petersburg, not in a restaurant — in my back room where "
   "the pasta used to be. Next summer. I'm already writing the guest list: the whole village, with you at number "
   "one. Don't say no, I know you."),
  months="8,9,10", stamp="b_heart")

# =====================================================================================================
# KOLYA — radio amateur, shy until a call sign comes up. QSL cards, Gleb at the cordon, exams, college.
# =====================================================================================================
A = "kolya"
BUREAU = ("QSL-бюро, Союз радиолюбителей", "QSL Bureau, Radio Amateurs' Union")
EFIR = ("Радиоклуб «Эфир», Городок", "Ether Radio Club, Gorodok")
GLEB = ("Г. А. Туманов, метеостанция", "G. A. Tumanov, weather station")
YAMADA = ("Такэси Ямада, Саппоро", "Takeshi Yamada, Sapporo")
COLLEGE = ("Колледж связи, Городок", "College of Communications, Gorodok")

B(A, 3, "parcel", "kolya", BUREAU,
  ("Коле Рябинину пришли его первые QSL-карточки.",
   "Kolya Ryabinin received his very first QSL cards."),
  ("Карточки! Мои первые! Вот Финляндия, OH2 — это Хельсинки! Вот Минск, вот Караганда. Значит, они меня правда слышали, "
   "мне не приснилось. Я полгода в эфир звал. Извините. Я просто… они настоящие. С марками.",
   "Cards! My first! Here's Finland, OH2 — that's Helsinki! Here's Minsk, here's Karaganda. So they really did hear "
   "me, I didn't dream it. I've been calling for six months. Sorry. It's just… they're real. With stamps."),
  stamp="b_qsl_bureau")

B(A, 25, "letter", "kolya", EFIR,
  ("Колю зовут в Городок сдавать экзамен на категорию.",
   "Kolya is invited to Gorodok to sit his radio licence exam."),
  ("Радиоклуб пишет: скоро экзамен на третью категорию. Третья — это больше мощности, больше диапазонов, это как из лодки "
   "пересесть на катер. Там морзянку принимают на слух. Учу. Бабушка говорит, я даже во сне пальцем по одеялу стучу.",
   "The radio club says the exam for the third class is coming up. Third class means more power, more bands — like "
   "moving from a rowing boat to a launch. You have to copy Morse by ear. I'm learning. Granny says I tap on the "
   "blanket in my sleep."))

B(A, 35, "letter", "kolya", YAMADA,
  ("Коле карточка из Японии — с журавлями Хоккайдо.",
   "A QSL card from Japan for Kolya, with Hokkaido cranes."),
  ("JA8! Восьмёрка — это Хоккайдо! Ямада-сан, ему семьдесят, и он прислал две карточки: одну мне, а одну «вашему "
   "почтальону». Правда, так и написал. Я ему в эфире рассказал, кто мне их носит. Возьмите. Это японские журавли.",
   "JA8! Eight means Hokkaido! Yamada-san is seventy, and he sent two cards: one for me and one 'for your postman'. "
   "Really, that's what he wrote. I told him on the air who brings me my mail. Take it. Those are Japanese cranes."),
  gift="b_qsl_japan", stamp="b_crane_japan", sets="kolya.japan")

B(A, 35, "parcel", "kolya", ("Радиорынок, Москва", "Radio market, Moscow"),
  ("Коле посылка: телеграфный ключ и сорок метров провода.",
   "A parcel for Kolya: a Morse key and forty metres of wire."),
  ("Ключ! Телеграфный! И провод на антенну, сорок метров. Бабушка говорит, опять я через весь огород паутину натяну, а бельё "
   "куда. Я ей объяснил: под антенной бельё сохнет быстрее, там волны. Она не поверила. Я тоже, но звучит научно.",
   "A key! A proper Morse key! And forty metres of aerial wire. Granny says I'll string another cobweb across the "
   "whole garden, and where's the washing to go. I told her washing dries faster under an aerial, because of the "
   "waves. She didn't believe me. Nor do I, but it sounds scientific."))

B(A, 35, "letter", "kolya", EFIR,
  ("Коля всю ночь слушал Антарктиду. Его самого не услышали.",
   "Kolya listened to Antarctica all night. They didn't hear him."),
  ("Клуб написал, что неделя Антарктиды. И сегодня ночью я её слышал! Мирный, RI1ANM — три раза в тетрадку записал, чтобы "
   "не забыть. Меня не услышали: там тысячи зовут, а у меня провод на берёзе. Но я их слышал. Бабушке не говорите, что до четырёх не спал.",
   "The club wrote that it's Antarctica week. And last night I heard it! Mirny, RI1ANM — I wrote it down three "
   "times so I wouldn't forget. They didn't hear me: thousands are calling and I've got a wire on a birch tree. "
   "But I heard them. Don't tell Granny I was up till four."))

B(A, 40, "letter", "kolya", EFIR,
  ("Коле назначили экзамен на радиолюбительскую категорию.",
   "Kolya's radio exam has been set for spring."),
  ("Экзамен через месяц, в Городке. Сто двадцать знаков в минуту на слух. Сто двадцать! Говорят, Ерофей Кузьмич в Заречье "
   "на полярке двести давал. Вот бы к нему поучиться. А пока: точка-тире-точка… Это «Р». Простите, я теперь со всеми так разговариваю.",
   "The exam's in a month, in Gorodok. A hundred and twenty characters a minute by ear. A hundred and twenty! They "
   "say Yerofei Kuzmich over in Zarechye did two hundred at a polar station. I wish I could learn from him. "
   "Meanwhile: dot-dash-dot… That's R. Sorry, I talk like this to everyone now."),
  months="1,2,3")

B(A, 15, "registered", "kolya", EFIR,
  ("Коля сдал экзамен: заказным пришла новая лицензия.",
   "Kolya passed his exam: his new licence came by registered post."),
  ("Сдал! Сто двадцать знаков, ни одной ошибки. Ну, одна, но я её сам исправил. Третья категория: теперь можно дальше, громче, "
   "по всему миру. Бабушка хочет в рамочку и на стену. Я сказал: только не над плитой.",
   "Passed! A hundred and twenty characters, not a single mistake. Well, one, but I corrected it myself. Third "
   "class: now I can go further, louder, all round the world. Granny wants it framed on the wall. I said: anywhere "
   "but over the stove."),
  months="2,3,4,5")

B(A, 40, "letter", "kolya", ("Педру, Манаус, Бразилия", "Pedro, Manaus, Brazil"),
  ("Коле карточка из Бразилии, с самой Амазонки.",
   "A QSL card for Kolya from Brazil, right from the Amazon."),
  ("PY8! Бразилия, Манаус, самая серёдка Амазонки! Двенадцать тысяч километров. Педру пишет, что у них плюс тридцать два и "
   "попугаи под окном орут, мешают эфиру. А у нас гуси Кузнецовых. Выходит, у всех одно и то же, только птицы разные.",
   "PY8! Brazil, Manaus, the very middle of the Amazon! Twelve thousand kilometres. Pedro writes that it's "
   "thirty-two degrees there and parrots scream under his window and spoil reception. Here it's the Kuznetsovs' "
   "geese. So it's the same everywhere, just different birds."),
  stamp="b_parrot")

B(A, 35, "letter", "kolya", EFIR,
  ("Клуб зовёт Колю на полевой день — работать в эфир с холма.",
   "The club invites Kolya to Field Day — on the air from a hilltop."),
  ("Полевой день! Это когда радисты уходят в поле и работают от батарей, как будто цивилизации нет. Я пойду на холм у "
   "водонапорной башни: там и связь, и высоко. Клуб выслал флажок и протокол. Если увидите на холме палатку — это я, а не туристы.",
   "Field Day! That's when operators go out into the fields and work on batteries, as if civilisation had ended. "
   "I'll go up the hill by the water tower: there's signal there, and it's high. The club sent a pennant and a log "
   "sheet. If you see a tent on the hill, that's me, not tourists."),
  months="5,6,7")

B(A, 40, "parcel", "kolya", ("В. А. Трофимов, Архангельск", "V. A. Trofimov, Arkhangelsk"),
  ("Старый радист из Архангельска прислал Коле свой ключ.",
   "An old radio operator in Arkhangelsk sent Kolya his own key."),
  ("Это Василий Алексеевич, он пятьдесят лет радистом на ледоколах ходил. Мы на сорока метрах разговаривали. И вот: прислал "
   "свой ключ, латунный, и аппаратный журнал за семьдесят девятый год. Пишет: «Передаю тебе эфир». Я… не знаю, что сказать. Буду беречь.",
   "It's Vasily Alekseyevich — he was a radio operator on icebreakers for fifty years. We talked on forty metres. "
   "And he's sent me his key, a brass one, and his station log from 1979. He writes: 'I'm handing the air over to "
   "you.' I… I don't know what to say. I'll look after it."),
  stamp="b_icebreaker")

B(A, 35, "letter", "kolya", ("Барк «Седов», Атлантика", "Barque Sedov, the Atlantic"),
  ("Коле карточка с барка «Седов» — связь с парусником в океане.",
   "A QSL for Kolya from the barque Sedov — a contact with a ship at sea."),
  ("Морская мобильная! Дробь эм-эм — значит, в море! Барк «Седов», парусник, шёл через Атлантику, и мы связались. Кадет Женя, "
   "ему девятнадцать, на мачту лазает. Карточки отправил из Лас-Пальмаса. Вот вам вторая — «Седов» под всеми парусами.",
   "Maritime mobile! Slash MM — that means at sea! The barque Sedov, a tall ship crossing the Atlantic, and we made "
   "contact. Cadet Zhenya, nineteen, climbs the masts. He posted the cards from Las Palmas. Here's the spare one for "
   "you — the Sedov under full sail."),
  months="6,7,8,9", gift="b_qsl_sedov", stamp="b_sedov")

B(A, 45, "letter", "kolya", GLEB,
  ("Коля связался с метеостанцией на Сосновом кордоне.",
   "Kolya made contact with the weather station at Pine Cordon."),
  ("Сосновый кордон! Глеб Андреевич, метеоролог, он там совсем один. Я с Японией говорил, с Бразилией, а тут свои, рядом, "
   "за лесом — и слышно хуже Бразилии! Карточку сам нарисовал: флюгер и сосны. Договорились выходить на связь по четвергам.",
   "Pine Cordon! Gleb Andreyevich, the meteorologist — he's all on his own out there. I've talked to Japan, to "
   "Brazil, and here's someone of our own, just beyond the forest — and he's harder to hear than Brazil! He drew "
   "the card himself: a weather vane and pines. We've agreed to meet on the air every Thursday."),
  months="8,9,10,11", stamp="b_kordon", sets="kolya.gleb")

B(A, 25, "letter", "kolya", GLEB,
  ("Глеб с кордона прислал Коле прогноз — для всей Липовки.",
   "Gleb at the cordon sent Kolya a forecast for all of Lipovka."),
  ("Глеб Андреевич прислал прогноз на неделю, от руки, с нарисованным барометром. Говорит: раз мы в эфире, будь моим "
   "корреспондентом, вешай в магазине. Повесил. Теперь все ко мне: «Коль, а дождь когда?» Я как диктор. Только уши краснеют.",
   "Gleb Andreyevich sent a week's forecast, handwritten, with a little barometer drawn on it. He says: since we're "
   "on the air together, be my correspondent — pin it up in the shop. I did. Now everyone asks me, 'Kolya, when's "
   "the rain?' I'm like a newsreader. Except my ears go red."),
  months="9,10,11,12", stamp="b_kordon")

B(A, 35, "letter", "kolya", COLLEGE,
  ("Колю зовут на день открытых дверей в колледж связи.",
   "Kolya is invited to an open day at the College of Communications."),
  ("Колледж связи в Городке. Там радиомонтаж, антенны, свой радиоклуб, на крыше мачта… Бабушка сказала: «Езжай, посмотри». "
   "А сама потом долго посуду мыла. Тихо так мыла. Я ещё не решил. Почти решил.",
   "The College of Communications in Gorodok. Radio assembly, aerials, their own radio club, a mast on the roof… "
   "Granny said, 'Go on, have a look.' And then she washed the dishes for a long time. Very quietly. I haven't "
   "decided yet. Almost."),
  months="9,10,11")

B(A, 40, "letter", "kolya", EFIR,
  ("Коля провёл связь с Антарктидой! Клуб засчитал её в диплом.",
   "Kolya made contact with Antarctica! The club counted it for an award."),
  ("Я провёл связь с Антарктидой. Сам! Мирный, Сергей Николаевич: «Липовка, слышу вас пять-девять». Пять-девять — это идеально! "
   "Клуб засчитал. А карточку станция пришлёт нескоро: почта у них уходит с кораблём, раз в год.",
   "I made contact with Antarctica. Me! Mirny, Sergei Nikolayevich: 'Lipovka, I hear you five-nine.' Five-nine "
   "means perfect! The club has counted it. But the station's card won't come for ages: their mail leaves with "
   "the ship, once a year."),
  months="12,1,2")

B(A, 30, "letter", "kolya", ("Союз радиолюбителей", "Radio Amateurs' Union"),
  ("Коля занял третье место в области в новогодних соревнованиях.",
   "Kolya came third in the region in the New Year radio contest."),
  ("Третье место в области среди юниоров! Я всю новогоднюю ночь в эфире сидел, пока все салаты ели. Бабушка мне салат к рации "
   "принесла и стояла, слушала, как я Новый год по всем часовым поясам встречаю. Диплом с печатью. Второй в рамочку.",
   "Third in the region among juniors! I sat on the air all New Year's night while everyone ate salads. Granny "
   "brought my salad to the radio and stood listening as I saw the New Year in across every time zone. A "
   "certificate with a seal. That's the second one for a frame."),
  months="1,2", stamp="b_new_year")

B(A, 30, "letter", "kolya", GLEB,
  ("На кордоне буран. Глеб пишет Коле письмо при керосинке.",
   "A blizzard at the cordon. Gleb writes to Kolya by lamplight."),
  ("У Глеба Андреевича буран третьи сутки, станцию по крышу замело. Он всё равно каждые три часа ходит снимать показания — "
   "по верёвке, чтоб не потеряться. Пишет, мой голос в наушниках в такие ночи — как окно с огоньком. Бабушка послушала и пирожков ему собрала.",
   "Gleb Andreyevich has had a blizzard for three days; the station is buried to the roof. He still goes out every "
   "three hours to read the instruments — along a rope so he won't get lost. He writes that on nights like that my "
   "voice in his headphones is like a lit window. Granny heard that and packed him some pies."),
  months="1,2,3", stamp="b_blizzard")

B(A, 45, "letter", "kolya", GLEB,
  ("Глеб советует Коле: иди учиться на связиста.",
   "Gleb tells Kolya: go and study to be a radio engineer."),
  ("Глеб Андреевич пишет: «Николай, иди учись. Связь — это профессия, а не забава. Ты уже связист, осталось бумагу получить». "
   "Он меня Николаем зовёт, только он и учительница. Я решил. Вы первые знаете, после Глеба. Бабушке вечером скажу. Наверное.",
   "Gleb Andreyevich writes: 'Nikolai, go and study. Radio is a profession, not a pastime. You're already an "
   "operator, you just need the paper.' He calls me Nikolai — only he and my teacher do. I've decided. You're the "
   "first to know, after Gleb. I'll tell Granny tonight. Probably."),
  months="2,3,4")

B(A, 40, "letter", "kolya", YAMADA,
  ("Внук Ямады учит русский и хочет переписываться с Колей.",
   "Yamada's grandson is learning Russian and wants to write to Kolya."),
  ("Ямада-сан пишет, его внук Рё учит русский и хочет мне писать. Обычными письмами, не в эфире! Я уже три страницы сочинил: "
   "про Липовку, про мельницу, про вас тоже. Отнесёте? А открытку с Фудзи он велел отдать почтальону.",
   "Yamada-san writes that his grandson Ryo is learning Russian and wants to write to me. Ordinary letters, not on "
   "the air! I've already written three pages: about Lipovka, the mill, and you too. Will you take it? And he said "
   "this Mount Fuji postcard is for the postman."),
  reply="out", gift="b_fuji_card")

B(A, 30, "letter", "kolya", COLLEGE,
  ("Колледж прислал Коле список документов для поступления.",
   "The college sent Kolya the list of documents for admission."),
  ("Список документов: аттестат, справка, фотографии три на четыре. Сфотографировался у Димы Соколова на фоне простыни. "
   "Вышел как беглый каторжник. Бабушка говорит — красавец. Ей виднее, она меня с рождения знает.",
   "The list: school certificate, medical form, photos three by four. Dima Sokolov took my picture against a bed "
   "sheet. I look like an escaped convict. Granny says I'm handsome. She should know; she's known me since I was born."),
  months="3,4,5")

B(A, 30, "letter", "kolya", ("Школа, Липовка", "Lipovka School"),
  ("Коле пришло расписание выпускных экзаменов.",
   "Kolya has his final exam timetable."),
  ("Расписание экзаменов. Математика двадцать девятого. Я спокоен. Я совершенно спокоен. Я сегодня вместо «здравствуйте» "
   "сказал Зинаиде Павловне «си-кью, си-кью». Она мне баранку дала. Решила, наверное, что я заболел.",
   "The exam timetable. Maths on the twenty-ninth. I'm calm. I'm perfectly calm. Today I said 'CQ, CQ' to Zinaida "
   "Pavlovna instead of 'good morning'. She gave me a bagel. She must have thought I was ill."),
  months="5,6")

B(A, 15, "letter", "kolya", ("Станция Мирный, Антарктида", "Mirny Station, Antarctica"),
  ("Коле пришла карточка из Антарктиды — полгода шла.",
   "Kolya's card from Antarctica has come at last, half a year on the way."),
  ("Пришла! Полгода шла — с кораблём через два океана, потом поездом, потом вы. На штемпеле «Мирный». Эту я никому не отдам, "
   "простите, даже вам. Но подержать — подержите. Чувствуете? Она холодная. Шучу. Не знаю. Мне кажется, холодная.",
   "It's come! Six months on the way — by ship across two oceans, then by train, then you. The postmark says Mirny. "
   "This one I won't give to anyone, sorry, not even you. But you can hold it. Feel that? It's cold. Joking. I "
   "don't know. It feels cold to me."),
  months="6,7", stamp="b_antarctica")

B(A, 10, "telegram", "kolya", ("Туманов, Сосновый кордон", "Tumanov, Pine Cordon"),
  ("Телеграмма Коле с кордона: Глеб поздравляет с экзаменами.",
   "A telegram for Kolya from the cordon: Gleb congratulates him."),
  ("ПОЗДРАВЛЯЮ ЭКЗАМЕНАМИ ГОРЖУСЬ ТУМАНОВ. Я ему вчера в эфире сказал, что сдал, а он всё равно телеграмму прислал, настоящую: "
   "чтобы, говорит, на бумаге было. Горжусь. Бабушка её два раза перечитала и к Зинаиде Павловне носила показывать.",
   "CONGRATULATIONS EXAMS PROUD OF YOU TUMANOV. I told him on the air yesterday that I'd passed, and he still sent a "
   "telegram, a real one — so it's on paper, he says. Proud. Granny read it twice and took it to show Zinaida Pavlovna."),
  months="6,7", stamp="b_telegram")

B(A, 15, "registered", "kolya", COLLEGE,
  ("Колю приняли в колледж связи в Городке!",
   "Kolya has been accepted at the College of Communications in Gorodok!"),
  ("Приняли. На радиотехника. С первого сентября общежитие, комната на троих, а на крыше колледжа антенна, я узнавал, "
   "трёхэлементная… Простите. Не знаю, что ещё говорить. Бабушка плачет и печёт. Одновременно. Возьмите пирог, она на роту напекла.",
   "Accepted. Radio engineering. From the first of September — a hostel, three to a room, and an aerial on the "
   "college roof, I checked, a three-element… Sorry. I don't know what else to say. Granny is crying and baking. "
   "At the same time. Take a pie, she's baked for a regiment."),
  months="7,8", gift="b_pie_berry", sets="kolya.college")

B(A, 10, "letter", "kolya", ("Джек, Новая Зеландия", "Jack, New Zealand"),
  ("Коле карточка из Новой Зеландии — с другой стороны Земли.",
   "A QSL for Kolya from New Zealand, the other side of the Earth."),
  ("ZL! Новая Зеландия! Я по глобусу проверил: если отсюда прокопать насквозь, выйдешь почти к ним. Джек пишет, что у них "
   "сейчас зима, а Липовку на карте не нашёл, но поверил мне на слово. На карточке овцы, миллион. Берите, у меня ещё одна.",
   "ZL! New Zealand! I checked on the globe: dig straight down from here and you'd come out almost at their place. "
   "Jack writes that it's winter there now, and that he couldn't find Lipovka on the map but took my word for it. "
   "There are sheep on the card, a million. Take it, I've got another."),
  months="7,8,9", gift="b_qsl_zealand", stamp="b_globe")

B(A, 14, "parcel", "kolya", GLEB,
  ("Глеб с кордона прислал Коле в дорогу свой старый барометр.",
   "Gleb sent Kolya his old barometer for the road."),
  ("Глеб Андреевич прислал мне свой карманный барометр, а вам — оконный термометр: почтальон, говорит, погоду должен знать первым. "
   "Завтра уезжаю. Антенну с берёзы не снимаю, буду на выходных выходить в эфир отсюда. Вы бабушку навещайте, ладно? Хоть просто так.",
   "Gleb Andreyevich sent me his pocket barometer, and you a window thermometer — a postman, he says, should know "
   "the weather first. I leave tomorrow. I'm not taking the aerial off the birch; I'll go on the air from home at "
   "weekends. Look in on Granny, will you? Even without a letter."),
  months="8,9", gift="b_window_thermo")

B(A, 40, "letter", "nina", BUREAU,
  ("Коля уехал, а карточки всё идут — баба Нина складывает их в жестянку.",
   "Kolya's gone, but his cards keep coming. Granny Nina keeps them in a tin."),
  ("Уехал, а карточки всё идут и идут. Вот, опять — эта из Исландии, что ли, с маяком. Я их в жестянку из-под чая складываю, "
   "до субботы. Приедет — разберёт. Сяду иногда, переберу: Бразилия, Япония… Весь свет моему Коле пишет. Садитесь, у меня щи.",
   "He's gone, and still the cards come. Here's another — from Iceland, I think, with a lighthouse. I keep them in "
   "an old tea tin till Saturday. He'll sort them when he's home. Sometimes I sit and go through them: Brazil, "
   "Japan… The whole world writes to my Kolya. Sit down, I've got cabbage soup."),
  months="10,11", stamp="b_iceland")

A = "kolya_birthday"

B(A, 30, "letter", "kolya", ("Программа ARISS", "The ARISS programme"),
  ("Коле в день рождения — диплом с орбиты.",
   "On his birthday Kolya gets a certificate from orbit."),
  ("Двенадцатое апреля — и мой день рождения, и День космонавтики, я так нарочно родился. А это диплом: я принял картинку "
   "с МКС! Станция пролетала над нами и свистела в приёмник, а я записал. Подарок с орбиты. Бабушка испекла пирог-ракету. Почти ракету.",
   "April the twelfth is my birthday and Cosmonautics Day — I was born that way on purpose. And this is a "
   "certificate: I received a picture from the ISS! It flew over us whistling into my receiver, and I recorded "
   "it. A present from orbit. Granny baked a rocket pie. Almost a rocket."),
  months="4", on="04-12", stamp="b_iss")

B(A, 200, "postcard", "kolya", YAMADA,
  ("Коле на день рождения — бумажный журавлик из Японии.",
   "For his birthday Kolya gets a paper crane from Japan."),
  ("Ямада-сан помнит! Прислал журавлика, сложенного из карты Хоккайдо: «Двенадцатое апреля — день Гагарина и день Коли». "
   "Глеб Андреевич тоже поздравил, морзянкой, в эфире. А бабушка — пирогом. Это лучший день рождения. Опять.",
   "Yamada-san remembered! He sent a crane folded from a map of Hokkaido: 'April the twelfth — Gagarin's day and "
   "Kolya's day.' Gleb Andreyevich congratulated me too, in Morse, on the air. And Granny — with a pie. Best "
   "birthday ever. Again."),
  months="4", on="04-12", needs="kolya.gleb", stamp="b_crane_japan")

B(A, 200, "postcard", "kolya", BUREAU,
  ("Коле на день рождения пришли открытки от радиодрузей со всего света.",
   "Birthday cards for Kolya from radio friends all over the world."),
  ("Пятнадцать открыток! Хоккайдо, Манаус, Архангельск, «Седов», кордон. Разложил их на стене вокруг карты. "
   "Раньше там висела просто карта. А теперь на карте люди, и все меня поздравляют.",
   "Fifteen cards! Hokkaido, Manaus, Arkhangelsk, the Sedov, the cordon. I've pinned them on the wall round the "
   "map. It used to be just a map. Now there are people on it, and they're all wishing me happy birthday."),
  months="4", on="04-12", needs="kolya.gleb", stamp="b_qsl_bureau")

# =====================================================================================================
# NINA — Kolya's grandmother. Feeds everyone; worry and pride.
# =====================================================================================================
A = "nina"
KOLYA_G = ("Коля, Городок", "Kolya, Gorodok")

B(A, 5, "newspaper", "nina", ("«Сельская новь»", "The Village News"),
  ("В «Сельской нови» напечатали рецепт бабы Нины.",
   "The Village News printed Granny Nina's recipe."),
  ("Мой пирог напечатали! С капустой и яйцом, «от Нины Рябининой, Липовка». Только тесто перепутали: у меня на простокваше, "
   "а они — на кефире. На кефире! Люди испекут и на меня подумают. Садитесь, вот вам правильный, сравните.",
   "They printed my pie! Cabbage and egg, 'from Nina Ryabinina, Lipovka'. Only they got the dough wrong: mine's made "
   "with soured milk and they wrote kefir. Kefir! People will bake it and blame me. Sit down, here's the proper "
   "one, you compare."),
  gift="b_pie_cabbage")

B(A, 30, "postcard", "nina", YAMADA,
  ("Бабе Нине на день рождения — открытка из Японии!",
   "A birthday card from Japan for Granny Nina!"),
  ("Из Японии! Мне! «Дорогая Нина-сан». Это Колин японец, Ямада. Коля ему, оказывается, в эфире сказал, что у бабушки день "
   "рождения. Через полсвета! Я б ему пирог послала, да зачерствеет. Напишу хоть спасибо — Коля переведёт.",
   "From Japan! For me! 'Dear Nina-san.' It's Kolya's Japanese friend, Yamada. Turns out Kolya told him on the air "
   "it was his granny's birthday. Halfway round the world! I'd send him a pie, but it'd go stale. I'll write a "
   "thank-you at least — Kolya will translate."),
  months="12", on="12-08", needs="kolya.japan", reply="out", stamp="b_crane_japan")

B(A, 40, "letter", "nina", ("Валентина, Вологда", "Valentina, Vologda"),
  ("Бабе Нине пишет подруга молодости. Нина тревожится о Коле.",
   "An old friend writes to Granny Nina. Nina worries about Kolya."),
  ("Валя пишет, подружка моя, мы с ней сорок лет назад на ферме работали. Спрашивает, как Коля. А как Коля? Ночью в наушниках, "
   "стучит, глаза красные, с Японией разговаривает. А со мной — «ага» да «угу». Ну не со зла. Может, когда и мне по радио позвонит.",
   "Valya writes — we worked on the farm together forty years ago. She asks how Kolya is. How is he? Up at night "
   "in his headphones, tapping away, eyes red, talking to Japan. And to me it's 'uh-huh' and 'mm'. Not out of "
   "spite. Maybe one day he'll ring me on the radio too."),
  months="1,2,3", reply="out")

B(A, 40, "letter", "nina", ("Г. А. Туманов, Сосновый кордон", "G. A. Tumanov, Pine Cordon"),
  ("Метеоролог с кордона написал бабе Нине — спасибо за пироги.",
   "The meteorologist at the cordon thanks Granny Nina for her pies."),
  ("Глеб Андреевич пишет — мне! «Уважаемая бабушка Николая, ваши пирожки дошли, хоть и в виде сухарей, и были съедены с большим "
   "уважением». Выходит, я ему сухари послала. Теперь сушки пошлю, нарочно, им ничего не сделается. Вот, попробуйте.",
   "Gleb Andreyevich has written — to me! 'Dear Grandmother of Nikolai, your pies arrived, though as rusks, and "
   "were eaten with great respect.' So I sent the man rusks. Now I'll send sushki on purpose — nothing can happen "
   "to those. Here, try one."),
  months="4,5,6,7,8", needs="kolya.gleb", gift="b_sushki")

B(A, 40, "letter", "nina", ("Школа, Липовка", "Lipovka School"),
  ("Из школы бабе Нине — благодарность за внука.",
   "The school writes to thank Granny Nina for her grandson."),
  ("Из школы письмо. Думала — натворил. А там: «Благодарность бабушке за воспитание внука». Мне! Коля на физике про радио "
   "рассказывал, весь урок и ещё перемену, и дети слушали. Положу в комод, к его грамотам. Возьмите грибочков, от радости банку открыла.",
   "A letter from the school. I thought he'd done something. But it says: 'With thanks to his grandmother for "
   "raising him.' To me! Kolya talked about radio in physics, the whole lesson and the break, and the children "
   "listened. It's going in the drawer with his certificates. Have some mushrooms — I opened a jar for joy."),
  months="9,10,11", gift="b_nina_mushrooms")

B(A, 20, "letter", "nina", KOLYA_G,
  ("Баба Нина получила первое письмо Коли из колледжа.",
   "Granny Nina got Kolya's first letter from college."),
  ("Первое письмо! «Бабушка, кормят нормально». Нормально — значит плохо, я его знаю. Комната на троих: один храпит, второй тоже "
   "радио любит, хоть одна радость. Носки, пишет, надеваю. Врёт. Соберу посылку — пирожки, носки. Отнесёте завтра?",
   "His first letter! 'Granny, the food's all right.' All right means bad, I know him. Three to a room: one snores, "
   "the other loves radio too — that's one mercy. He says he's wearing his socks. He's lying. I'll pack a parcel — "
   "pies, socks. Will you take it tomorrow?"),
  months="9,10,11", needs="kolya.college", reply="out")

B(A, 30, "letter", "nina", KOLYA_G,
  ("Колю выбрали старостой радиокружка. Баба Нина печёт от волнения.",
   "Kolya's been made head of the radio club. Granny Nina bakes from nerves."),
  ("Старостой радиокружка выбрали! Тихоню моего. Пишет: «Бабушка, я на крыше колледжа антенну ставил, вся группа смотрела». "
   "На крыше! Я теперь не сплю. Ешьте пирог, яблочный. Я теперь всё время на нервах пеку.",
   "He's been made head of the radio club! My quiet boy. He writes: 'Granny, I put up an aerial on the college roof "
   "and the whole class watched.' On the roof! Now I can't sleep. Eat some pie, apple. I bake all the time now, from nerves."),
  months="10,11,12", gift="b_pie_apple")

B(A, 20, "parcel", "nina", KOLYA_G,
  ("Коля прислал бабушке подарок со своей первой стипендии.",
   "Kolya sent his grandmother a present from his first grant."),
  ("Со стипендии купил! Платок пуховый, тонкий — сквозь кольцо проходит, вот смотрите, проходит! Я ему писала: себе ботинки купи. "
   "А он — платок. Ну что с ним делать. Носить. А мой старый шарф возьмите, вам по морозу ходить.",
   "He bought it with his grant! A down shawl so fine it goes through a ring — look, it does! I wrote to him: buy "
   "yourself some boots. And he buys a shawl. What can you do with him. Wear it. And you take my old scarf — you're "
   "out in the frost all day."),
  months="12", on="12-08", gift="b_nina_scarf")

B(A, 40, "letter", "nina", KOLYA_G,
  ("Коля сдал сессию на пятёрки. Баба Нина читает письмо всей деревне.",
   "Kolya got top marks. Granny Nina reads his letter to the whole village."),
  ("Сессию сдал на пятёрки. Все пять пятёрок! Значит, не только в эфире сидит, учится. Директор, пишет, руку жал. Я письмо "
   "Зине носила, Михалычу носила, теперь вам прочту. Вы уж послушайте, я с выражением.",
   "Top marks in every exam. Five out of five! So he doesn't just sit on the air, he studies. The director shook "
   "his hand, he writes. I've taken the letter to Zina, to Mikhalych, and now I'll read it to you. Do listen, I'll "
   "read it with feeling."),
  months="1,2")

B(A, 40, "postcard", "nina", KOLYA_G,
  ("Коля едет домой на день рождения. Баба Нина уже печёт.",
   "Kolya is coming home for his birthday. Granny Nina is already baking."),
  ("Едет на день рождения, на все выходные! Тесто уже ставлю, хоть до приезда две недели — ничего, порепетирую. Антенну на "
   "берёзе подтянуть велел. А то, пишет, Глеб Андреевич без него скучает. Глеб скучает. А бабушка, видно, нет.",
   "He's coming for his birthday, the whole weekend! I'm setting the dough already, though it's two weeks off — "
   "never mind, I'll rehearse. He asked me to tighten the aerial on the birch. Otherwise, he writes, Gleb "
   "Andreyevich misses him. Gleb misses him. And Granny doesn't, apparently."),
  months="3,4", stamp="b_birch")

# =====================================================================================================
# LIDIA — the club and the library. A tired idealist with dry humour.
# =====================================================================================================
A = "lidia"
CULT = ("Отдел культуры района", "District Culture Department")
CLUBN = ("Клуб, Л. А. Белова", "The Club, L. A. Belova")

B(A, 4, "parcel", "lidia", ("Областной библиотечный коллектор", "Regional Library Supply"),
  ("Лидии Аркадьевне пришла посылка книг для библиотеки.",
   "A parcel of books for Lidia Arkadyevna's library."),
  ("Двенадцать книг. Три из них — один и тот же детектив, видимо, чтобы наверняка. Один «Справочник садовода» восемьдесят "
   "девятого года, новенький, нечитаный. Зато Паустовский. Ради него и живём. Детектив возьмите, у меня их теперь лишние два.",
   "Twelve books. Three of them are the same detective novel — to be on the safe side, I suppose. One gardener's "
   "handbook from 1989, brand new, unread. But there's Paustovsky. That's what we live for. Take the detective; I "
   "now have two to spare."),
  gift="b_detective", stamp="b_library")

B(A, 15, "notice", "zina", CLUBN,
  ("В клубе кино: «Девчата». Афиши разнесли по дворам.",
   "Film night at the club: 'The Girls'. Posters delivered round the village."),
  ("Кино в клубе, «Девчата»! Я их сто раз видела и в сто первый пойду. Лидия молодец, хоть кто-то нас из дому вытаскивает. "
   "Только бы проектор не погас, как в прошлый раз, на самом интересном. Мы тогда конец хором досказывали.",
   "A film at the club — 'The Girls'! I've seen it a hundred times and I'll go a hundred and first. Good for Lidia, "
   "someone has to drag us out of the house. If only the projector doesn't die like last time, right at the best "
   "bit. We finished the story out loud, all together."),
  months="10,11,12,1,2,3", stamp="b_film")

B(A, 1, "notice", "marina", CLUBN,
  ("Соколовых позвали в клубное кино.",
   "The Sokolovs are invited to the club film night."),
  ("Нас позвали в кино! В Москве мы ходили в кинотеатр в торговом центре и ели попкорн по цене крыла самолёта. Тут обещают "
   "семечки. Дима спросил, какой там дресс-код. Я сказала: валенки, Дима. Всегда валенки.",
   "We've been invited to the cinema! In Moscow we went to a multiplex in a shopping centre and ate popcorn priced "
   "like an aircraft wing. Here they promise sunflower seeds. Dima asked about the dress code. I said: felt boots, "
   "Dima. Always felt boots."))

B(A, 25, "letter", "lidia", ("И. Новикова, Калининград", "I. Novikova, Kaliningrad"),
  ("В библиотеку Липовки вернули книгу, взятую в 1987 году.",
   "A book borrowed from the Lipovka library in 1987 has been returned."),
  ("Вернули «Трёх мушкетёров», взятых в восемьдесят седьмом. Пишет: «Простите, увезла в чемодане, всю жизнь стыдно». Штраф "
   "прощаю. Формуляр её сохранился, почерк с завитушками. Отвечу: приезжайте, дам «Двадцать лет спустя». А янтарик — вам, она для почтальона вложила.",
   "The Three Musketeers, borrowed in 1987, returned. She writes: 'Forgive me, it went off in my suitcase, I've "
   "been ashamed all my life.' Fine forgiven. Her library card survived, all curly handwriting. I'll write back: "
   "come, I'll lend you Twenty Years After. The amber is yours — she put it in for the postman."),
  reply="out", gift="b_amber", stamp="b_baltic")

B(A, 25, "parcel", "lidia", ("Областной фильмофонд", "Regional Film Library"),
  ("Клубу прислали фильмы на всю зиму.",
   "The club has been sent films for the whole winter."),
  ("Фильмофонд расщедрился: тридцать фильмов. Половина комедии, половина про любовь, и один документальный — про трактор. "
   "Про трактор придёт Сергей Кузнецов. Будет поправлять диктора, я его знаю. Пожалуй, этот покажу последним.",
   "The film library's been generous: thirty films. Half comedies, half love stories, and one documentary about a "
   "tractor. Sergey Kuznetsov will come for the tractor. He'll correct the narrator, I know him. I think I'll show "
   "that one last."),
  months="11,12")

B(A, 20, "postcard", "lidia", ("Бывшие читатели", "Former readers"),
  ("У Лидии Аркадьевны день рождения — открытки от бывших читателей.",
   "It's Lidia Arkadyevna's birthday: cards from former readers."),
  ("Сколько мне — неважно: библиотекари не стареют, они переплетаются. Вот открытка от мальчика, которого я в пятом классе "
   "записала на «Таинственный остров». Теперь он капитан дальнего плавания. Говорит — из-за меня. Из-за Жюля Верна, конечно, но приятно.",
   "My age doesn't matter: librarians don't grow old, they just get rebound. Here's a card from a boy I signed up "
   "for The Mysterious Island in fifth grade. He's a sea captain now. He says it's because of me. Because of Jules "
   "Verne, of course, but it's nice."),
  months="1", on="01-25", stamp="b_birthday")

B(A, 20, "registered", "lidia", CULT,
  ("Заказное Лидии Аркадьевне: библиотеку в Липовке хотят закрыть.",
   "A registered letter for Lidia Arkadyevna: they want to close the library."),
  ("«В целях оптимизации сети». Библиотеку закрыть с сентября, фонд передать в Городок. Шесть тысяч книг. А Агафья Петровна "
   "за «Анной Карениной» в Городок на чём поедет? На оптимизации?.. Простите. Я, кажется, впервые за двадцать лет повысила голос.",
   "'In order to optimise the network.' The library to close in September, the stock to go to Gorodok. Six "
   "thousand books. And how is Agafya Petrovna to get to Gorodok for Anna Karenina? On optimisation?.. Forgive me. "
   "I think I've raised my voice for the first time in twenty years."),
  months="2,3,4", sets="lidia.closure")

PET = ("Л. А. Белова, библиотека", "L. A. Belova, the library")
B(A, 3, "notice", "mikhalych", PET,
  ("Лидия Аркадьевна просит Липовку писать письма в защиту библиотеки.",
   "Lidia Arkadyevna asks Lipovka to write letters to save the library."),
  ("Писать, значит, в район. Напишу. Я им так скажу: деревня без библиотеки — что рой без матки, разлетится. По-пчелиному "
   "напишу, пусть разбираются. Отнесёте?",
   "Write to the district, then. I will. I'll tell them: a village without a library is like a swarm without a "
   "queen — it scatters. I'll write it the bee way and let them work it out. Will you take it?"),
  reply="out")

B(A, 1, "notice", "zina", PET,
  ("Зина пишет в район в защиту библиотеки — с копией.",
   "Zina writes to the district to save the library — with a copy."),
  ("Библиотеку закрыть?! А где я журналы брать буду, что мне Лидия откладывает? Пишу. Я в своё время ревизию из Городка выгнала, "
   "и сейчас напишу. С копией! Слово-то какое — копия. Пусть боятся. Отнесёте?",
   "Close the library?! And where will I get the magazines Lidia puts by for me? I'm writing. I once saw off an "
   "auditor from Gorodok; I'll write now too. With a copy! What a word — copy. Let them tremble. Will you take it?"),
  reply="out")

B(A, 1, "notice", "nina", PET,
  ("Баба Нина пишет письмо в защиту библиотеки.",
   "Granny Nina writes a letter to save the library."),
  ("Коля в этой библиотеке всё про радио перечитал, с третьего класса. Так и напишу: внук мой там вырос, между полками. "
   "Красиво писать не умею, я пироги умею. Ничего, от сердца — тоже почерк. Отнесёте?",
   "Kolya read everything about radio in that library, from third grade on. That's what I'll write: my grandson "
   "grew up there, between the shelves. I can't write nicely, I can bake. Never mind — the heart has its own "
   "handwriting too. Will you take it?"),
  reply="out")

B(A, 1, "notice", "dima", PET,
  ("Дима Соколов пишет в защиту библиотеки — по пунктам.",
   "Dima Sokolov writes to save the library, in bullet points."),
  ("Петиция? Это мы умеем. Пишу по пунктам. Первое: в библиотеке тихо и тепло. Второе: Марина берёт там книжки про огород. "
   "Третье: огород у нас пока не получается. Вывод: книжек нужно больше, а не меньше. Логика безупречна. Отнесёте?",
   "A petition? That we can do. Bullet points. One: the library is quiet and warm. Two: Marina borrows gardening books "
   "there. Three: our garden isn't working yet. Conclusion: we need more books, not fewer. Flawless logic. Will you take it?"),
  reply="out")

B(A, 25, "letter", "lidia", CULT,
  ("В библиотеку Липовки едет комиссия из района.",
   "A commission from the district is coming to inspect the library."),
  ("Едут проверять. Комиссия, двое: посмотрят, «востребована ли». Покажу формуляры — на каждой книге по десять фамилий. "
   "И чайник поставлю. Нет, чайник — это подкуп. Поставлю чайник и уйду к стеллажам: это уже не подкуп, это гостеприимство.",
   "They're coming to inspect. A commission of two, to see whether we're 'in demand'. I'll show them the cards — "
   "ten names on every book. And I'll put the kettle on. No, a kettle is bribery. I'll put the kettle on and "
   "withdraw to the shelves: that's not bribery, that's hospitality."),
  months="3,4,5")

B(A, 20, "newspaper", "lidia", ("«Сельская новь»", "The Village News"),
  ("В «Сельской нови» напечатали письма Липовки о библиотеке.",
   "The Village News printed Lipovka's letters about the library."),
  ("Целая полоса: «Липовка пишет». Михалыч про пчёл, Зинаида с копией, Дима по пунктам, баба Нина — про внука между полками. "
   "Читаю, и… видите, очки запотели. Жарко здесь. Возьмите газету, у меня их десять: Зина скупила весь тираж.",
   "A whole page: 'Lipovka Writes'. Mikhalych about bees, Zinaida with her copy, Dima in bullet points, Granny Nina "
   "about her grandson between the shelves. I read it and… you see, my glasses have steamed up. It's hot in here. "
   "Take a paper, I've got ten — Zina bought up the whole print run."),
  months="4,5,6")

B(A, 25, "registered", "lidia", CULT,
  ("Библиотеку в Липовке оставили! Заказное из района.",
   "The Lipovka library is saved! A registered letter from the district."),
  ("«…учитывая многочисленные обращения жителей, библиотеку сохранить». Сохранить. Я двадцать лет здесь, и ни разу мне не "
   "приходило письмо с хорошим словом в конце. Пойду повешу на доску объявлений. А потом просто посижу среди книг.",
   "'…in view of numerous appeals from residents, the library is to be retained.' Retained. Twenty years I've been "
   "here, and never once has a letter ended with a good word. I'll pin it on the noticeboard. And then I'll just sit "
   "for a while among the books."),
  months="5,6,7", stamp="b_heart", sets="lidia.saved")

B(A, 30, "parcel", "lidia", ("Читатели со всей страны", "Readers from all over"),
  ("В библиотеку Липовки шлют книги со всей страны.",
   "Books are pouring into the Lipovka library from all over the country."),
  ("Посылки из Омска, Твери, Самары. Прочитали про нас и шлют: «Пусть стоят у вас, раз у вас за книги так держатся». Сорок томов. "
   "Возьмите эту, она в двух экземплярах. На почте в обед должно быть что почитать.",
   "Parcels from Omsk, Tver, Samara. People read about us and sent books: 'Let them live with you, since you hold "
   "on to books so hard.' Forty volumes. Take this one, there are two copies. A post office needs something to "
   "read at lunch."),
  months="7,8,9", gift="b_gift_book", stamp="b_letters")

B(A, 30, "notice", "mikhalych", CLUBN,
  ("Лидия Аркадьевна набирает актёров для «Морозко».",
   "Lidia Arkadyevna is casting for 'Morozko'."),
  ("Лидия Аркадьевна в Морозко меня зовёт. Говорит, борода своя, гримировать не надо. А что, согласен. Только посох пусть дадут: "
   "я без дымаря в руках стоять не умею, руки девать некуда.",
   "Lidia Arkadyevna wants me as Morozko, Father Frost. Says the beard's my own, no make-up needed. Well, why not. "
   "Only they'd better give me a staff: I can't stand without a smoker in my hand, I don't know what to do with my arms."),
  months="9,10,11")

B(A, 2, "notice", "marina", CLUBN,
  ("Марину попросили нарисовать декорации к «Морозко».",
   "Marina has been asked to paint the scenery for 'Morozko'."),
  ("Лидия Аркадьевна просит декорации: лес, избушку, сугробы. Я в Москве рисовала для книжек — двенадцать на восемнадцать "
   "сантиметров. А тут задник шесть метров. Дима говорит: рисуй, будто книжка очень большая. Это, кстати, помогает.",
   "Lidia Arkadyevna wants scenery: a forest, a hut, snowdrifts. In Moscow I drew for books — twelve by eighteen "
   "centimetres. This backdrop is six metres. Dima says: draw it as if the book were very big. It actually helps."))

B(A, 2, "notice", "kolya", CLUBN,
  ("Колю позвали в «Морозко» — на свет и звук.",
   "Kolya has been asked to do lights and sound for 'Morozko'."),
  ("Меня — на свет и звук! Метель сделаю: белый шум из приёмника, только громче. И прожектор синий, для мороза. Морозко будет "
   "Михалыч. Когда он в бороде и в синем свете — я его сам боюсь.",
   "Me — lights and sound! I'll make the blizzard: white noise from a receiver, only louder. And a blue spotlight "
   "for the frost. Mikhalych is Morozko. When he's in his beard under blue light, even I'm scared of him."))

B(A, 30, "notice", "zina", CLUBN,
  ("Афиша: «Морозко» в клубе, премьера двадцать восьмого.",
   "Poster: 'Morozko' at the club, opening on the twenty-eighth."),
  ("Премьера двадцать восьмого! Я в антракте чай разносить буду с пирожками. Лидия говорит: антракта нет. А я говорю: будет. "
   "Вот увидите, будет: всем же захочется обсудить Михалыча в бороде.",
   "Opening night on the twenty-eighth! I'll be serving tea and pies in the interval. Lidia says there's no "
   "interval. I say there will be. You'll see — everyone will want to talk about Mikhalych in his beard."),
  months="12")

B(A, 1, "notice", "nina", CLUBN,
  ("Баба Нина собирается на «Морозко» — внук делает метель.",
   "Granny Nina is going to 'Morozko': her grandson makes the blizzard."),
  ("Внук мой метель делает! И прожектор. Сяду в первый ряд, в платке. Если Михалыч басом заговорит — засмеюсь, наверно. "
   "Нельзя? Ну, я в платок. Нате вам рыбник, в клуб с собой не понесу, там Зина со своими пирожками.",
   "My grandson's making the blizzard! And the spotlight. I'll sit in the front row in my shawl. If Mikhalych "
   "starts booming, I'll laugh, I expect. Not allowed? Then I'll laugh into my shawl. Here, have a fish pie — I "
   "won't take it to the club, Zina's got her pies there."),
  months="12", gift="b_pie_fish")

B(A, 1, "notice", "dima", CLUBN,
  ("Дима Соколов идёт на «Морозко» — он держал стремянку.",
   "Dima Sokolov is going to 'Morozko' — he held the stepladder."),
  ("Марина три недели рисовала лес, а я держал стремянку. Это мой вклад в культуру: стремянка. На афише меня нет, но в каждой "
   "нарисованной ёлке есть немного моей стремянки.",
   "Marina painted the forest for three weeks and I held the stepladder. That's my contribution to culture: a "
   "stepladder. I'm not on the poster, but there's a little of my stepladder in every painted fir tree."),
  months="12", stamp="b_morozko")

B(A, 20, "letter", "lidia", ("Фотограф «Сельской нови»", "Village News photographer"),
  ("Лидии Аркадьевне прислали фотографии со спектакля.",
   "Lidia Arkadyevna received photos from the play."),
  ("Прислали фотографии со спектакля. Михалыч в бороде, Марфушенька ревёт, Колина метель — видно, как снег летит, а это "
   "пенопласт. Возьмите одну. Вот эту, где все кланяются. Тут и вы в зале, в третьем ряду.",
   "The photos from the play have come. Mikhalych in his beard, Marfushenka bawling, Kolya's blizzard — you can "
   "see the snow flying, and it's polystyrene. Take one. This one, where everyone's bowing. You're in it too, in "
   "the third row."),
  months="1,2", gift="b_morozko_photo")

B(A, 60, "letter", "lidia", ("Областной фильмофонд", "Regional Film Library"),
  ("Клубу разрешили летнее кино под открытым небом.",
   "The club may hold open-air film nights this summer."),
  ("Летнее кино под открытым небом, у реки. Экран — простыня: Зина пожертвовала лучшую, с вышивкой. Комары бесплатно. "
   "Пойдёт дождь — скажу, что это фильм про дождь, и никто не уйдёт. Я их знаю.",
   "Open-air films this summer, by the river. The screen is a sheet: Zina donated her best one, embroidered. "
   "Mosquitoes free of charge. If it rains, I'll say it's a film about rain, and nobody will leave. I know them."),
  months="6,7", stamp="b_film")

B(A, 90, "registered", "lidia", ("Областная библиотека", "Regional Library"),
  ("Библиотеку Липовки признали лучшей сельской библиотекой года.",
   "The Lipovka library has been named the region's best village library."),
  ("По итогам года: «Лучшая сельская библиотека области». Это мы. Те, кого хотели закрыть. Повешу грамоту рядом с тем письмом про оптимизацию — "
   "для симметрии. А вам спасибо. Вы тогда все письма носили, и туда, и обратно. Без вас бы не дошло.",
   "For the past year: 'Best village library in the region.' That's us. The ones they wanted to close. I'll hang the certificate next "
   "to that letter about optimisation — for symmetry. And thank you. You carried all those letters, there and back. "
   "Without you, none of it would have got through."),
  months="1,2,3", stamp="b_star_award")

# =====================================================================================================
# SOKOLOVY — Marina and Dima, from Moscow, learning the village. Funny and self-ironic.
# =====================================================================================================
A = "sokolovy"
DMUM = ("Мама, Москва", "Mum, Moscow")
SISTERS = ("Вера и Надя Ласточкины", "Vera and Nadya Lastochkina")
SEEDS = ("«Семена почтой»", "Seeds by Post")

B(A, 2, "parcel", "dima", DMUM,
  ("Диме Соколову посылка от мамы из Москвы: кофемашина.",
   "A parcel for Dima Sokolov from his mum in Moscow: a coffee machine."),
  ("Мама прислала кофемашину. Она уверена, что мы тут голодаем. Розетка на кухне у нас одна, и в ней чайник. Будем включать "
   "по очереди, как в коммуналке. Хотите эспрессо? Через полчаса. Когда чайник закипит.",
   "Mum sent a coffee machine. She's convinced we're starving out here. We have one socket in the kitchen and the "
   "kettle lives in it. We'll take turns, like in a communal flat. Fancy an espresso? In half an hour. After the kettle boils."))

B(A, 10, "letter", "marina", ("Катя, Москва", "Katya, Moscow"),
  ("Марине пишет московская подруга: когда вернётесь?",
   "Marina's Moscow friend writes: when are you coming back?"),
  ("Катя спрашивает: «Ну что, когда обратно?» Будто мы на даче. Пишу ей, что ночью у нас под окном кто-то вздыхал, а утром "
   "выяснилось — соседская корова. И что не вернёмся. Наверное. Отправите? Ей полезно знать про корову.",
   "Katya asks: 'So, when are you coming back?' As if we were at the dacha. I'm writing that something sighed "
   "under our window all night, and in the morning it turned out to be the neighbours' cow. And that we're not "
   "coming back. Probably. Will you send it? It'll do her good to know about the cow."),
  reply="out")

B(A, 10, "letter", "dima", ("В. Сухов, печник, Городок", "V. Sukhov, stove-maker, Gorodok"),
  ("Печник из Городка ответил Диме, почему дымит печь.",
   "A stove-maker in Gorodok told Dima why the stove smokes."),
  ("Я ему подробно описал проблему: три листа, схема, гипотезы. Он ответил одной строчкой: «Молодой человек, откройте задвижку». "
   "Открыл. Не дымит. У меня два высших. Задвижка. Марина второй час смеётся. Не говорите никому, пожалуйста.",
   "I described the problem in detail: three pages, a diagram, hypotheses. He replied in one line: 'Young man, "
   "open the damper.' I opened it. No smoke. I have two degrees. A damper. Marina's been laughing for two hours. "
   "Please don't tell anyone."),
  months="9,10,11,12,1,2,3", stamp="b_chimney")

B(A, 12, "parcel", "marina", ("Магазин «Валенки»", "The Felt Boot Shop"),
  ("Марине прислали валенки — сорок шестого размера.",
   "Marina's felt boots have arrived — in size forty-six."),
  ("Я заказала тридцать восьмой, прислали сорок шестой. Дима влез в них прямо в ботинках. Решили: будут семейные, за дровами "
   "ходим по очереди. А варежки в подарок тоже не того размера — возьмите, вам, может, впору.",
   "I ordered a thirty-eight; they sent a forty-six. Dima got into them with his shoes on. We've decided they're "
   "family boots: we take turns going for firewood. And the free mittens are the wrong size too — take them, they "
   "might fit you."),
  months="10,11,12,1,2", gift="b_big_mittens")

B(A, 12, "postcard", "marina", ("Арт-директор, Москва", "Art director, Moscow"),
  ("Марине открытка из Москвы про дедлайн. А в Липовке минус тридцать.",
   "A postcard from Moscow about a deadline. In Lipovka it's thirty below."),
  ("Арт-директор напоминает про дедлайн. А у нас минус тридцать, вода в ведре в сенях замёрзла, я рисую у печки в варежках. "
   "Знаете, что я поняла? Москва — это где дедлайн. А тут — где вода в ведре. И второе почему-то важнее.",
   "The art director is reminding me of a deadline. Here it's thirty below, the bucket in the porch has frozen, and "
   "I'm drawing by the stove in mittens. Do you know what I've realised? Moscow is where the deadline is. Here is "
   "where the bucket is. And somehow the bucket matters more."),
  months="12,1,2,3", stamp="b_frost", sets="sokolovy.winter1")

B(A, 12, "letter", "dima", ("IT-компания, Москва", "IT company, Moscow"),
  ("Диму зовут обратно в Москву — на хорошую зарплату.",
   "Dima's being offered a well-paid job back in Moscow."),
  ("Зовут обратно. Зарплата плюс сорок процентов, офис с видом на реку. У меня тоже вид на реку, правда, она подо льдом. "
   "Ответил: спасибо, у меня дрова не колоты. Они решили, что это сленг. Отнесёте? Пусть думают, что сленг.",
   "They want me back. Forty per cent more, an office with a river view. I have a river view too, though it's "
   "under ice. I replied: thank you, but my wood isn't chopped. They decided it was slang. Will you take it? Let "
   "them think it's slang."),
  months="1,2,3,4", reply="out")

B(A, 12, "parcel", "marina", SEEDS,
  ("Марина выписала семена — сорок сортов, включая артишоки.",
   "Marina has ordered seeds: forty kinds, artichokes included."),
  ("Сорок пакетиков! Артишоки, спаржа, японский шпинат, физалис. Баба Нина посмотрела и спросила: «А картошку?» Картошку я "
   "забыла. Ничего, огород будет как в журнале. Дима уже сделал таблицу с поливом по часам.",
   "Forty packets! Artichokes, asparagus, Japanese spinach, physalis. Granny Nina looked and asked, 'And potatoes?' "
   "I forgot potatoes. Never mind, our garden will be like a magazine. Dima has already made a spreadsheet with "
   "watering by the hour."),
  months="2,3,4,5", stamp="b_seeds")

B(A, 20, "letter", "marina", SISTERS,
  ("Сёстры Ласточкины согласны отдать Соколовым козочку.",
   "The Lastochkin sisters agree to give the Sokolovs a young goat."),
  ("Сёстры из Заречья пишут: козочку отдадут. Условие — доить два раза в день и при ней не ругаться. Писали вдвоём: строчка "
   "аккуратная, а поверх неё другой рукой: «Не слушайте Веру». Мы их уже любим. Обеих. И козу заранее.",
   "The sisters across the river write that they'll give us a goat. On condition we milk her twice a day and don't "
   "swear in front of her. They wrote it together: a neat line, and over it in another hand, 'Don't listen to "
   "Vera.' We love them already. Both. And the goat in advance."),
  months="3,4,5")

B(A, 20, "postcard", "dima", SISTERS,
  ("Ласточкины прислали Диме наставление про козу Ириску.",
   "The Lastochkins sent Dima instructions for Iriska the goat."),
  ("Инструкция по эксплуатации козы. «Ириска любит хлеб с солью, иву и разговоры. Не любит громкую музыку и мужчин в шляпах». "
   "Я снял шляпу. На всякий случай навсегда. Завтра её на лодке перевезут. Марина купила ей два колокольчика — один вам.",
   "An operating manual for a goat. 'Iriska likes bread with salt, willow and conversation. Dislikes loud music and "
   "men in hats.' I've taken off my hat. Forever, just in case. Tomorrow they'll bring her over by boat. Marina "
   "bought her two bells — one's for you."),
  months="4,5,6", gift="b_goat_bell", stamp="b_goat")

B(A, 20, "letter", "marina", ("Мама Димы, Москва", "Dima's mum, Moscow"),
  ("Мама Димы в ужасе: сын завёл козу.",
   "Dima's mum is horrified: her son has a goat."),
  ("Димина мама узнала про козу. Пишет: «Дима, ты с ума сошёл, у тебя два высших». Будто козе это важно. А Ириска Диму обожает: "
   "ходит за ним, как собака, и ест его шнурки. Он говорит, это и есть признание. В айти его так не ценили.",
   "Dima's mum has found out about the goat. She writes: 'Dima, have you lost your mind, you have two degrees.' As "
   "if the goat cares. Iriska adores Dima: follows him like a dog and eats his shoelaces. He says that's what "
   "recognition looks like. Nobody valued him like that in IT."),
  months="5,6")

B(A, 25, "letter", "dima", ("Журнал «Сад и огород»", "Garden & Allotment magazine"),
  ("Диме ответили из журнала садоводов. Огород не задался.",
   "A gardening magazine replied to Dima. The garden hasn't gone well."),
  ("Я написал в журнал: почему всё взошло и всё исчезло? Отвечают: «Проверьте, нет ли на участке козы». Есть. Её зовут Ириска, "
   "она съела артишоки, спаржу и, кажется, таблицу полива. Остался укроп. Его она, видимо, не уважает.",
   "I wrote to the magazine: why did everything come up and then vanish? They reply: 'Check whether there is a goat "
   "on your plot.' There is. Her name is Iriska, and she ate the artichokes, the asparagus and, I think, the "
   "watering spreadsheet. The dill survived. Apparently she has no respect for dill."),
  months="6,7")

B(A, 30, "letter", "marina", SEEDS,
  ("Марине ответили про артишоки: в Липовке они не растут.",
   "Marina's been told artichokes don't grow in Lipovka."),
  ("Ответ на мою жалобу: «Артишоки на вашей широте не вызревают». Спасибо, я заметила. Итог лета: один кабачок, огромный. "
   "Назвали Геннадием и съели всей улицей. Баба Нина сказала: на тот год картошку сажай, горе ты московское.",
   "The reply to my complaint: 'Artichokes do not ripen at your latitude.' Thank you, I'd noticed. The summer's "
   "harvest: one courgette, enormous. We named it Gennady and the whole street ate it. Granny Nina said: plant "
   "potatoes next year, you poor Moscow thing."),
  months="8,9")

B(A, 30, "letter", "marina", ("Мама, Москва", "Mum, Moscow"),
  ("Марине письмо от мамы. У Соколовых будет малыш!",
   "A letter from Marina's mum. The Sokolovs are expecting!"),
  ("Мама пишет: «Я так и знала». А мы ей только позавчера сказали — по телефону, с холма у водонапорной башни, где связь. Вы… "
   "ну, третьи, кто знает. После мамы и Ириски. Весной. Дима уже читает про отопление детских комнат и седеет.",
   "Mum writes: 'I knew it.' And we only told her the day before yesterday — by phone, from the hill by the water "
   "tower where there's signal. You're… well, the third to know. After Mum and Iriska. In spring. Dima is already "
   "reading about heating children's rooms and going grey."),
  months="9,10,11")

B(A, 25, "postcard", "dima", DMUM,
  ("Димина мама узнала про малыша и шлёт приданое.",
   "Dima's mum has heard about the baby and is sending supplies."),
  ("Мама предупреждает: следом идут три посылки с вязаным. Три. Я посчитал: если малыш будет носить по шапке в день, хватит "
   "до школы. Мама сказала, это минимум. Носки вот уже пришли, на взрослых тоже — возьмите. А про козу она передумала: козье молоко полезное.",
   "Mum warns that three parcels of knitting are on their way. Three. I've worked it out: if the baby wears a "
   "different hat every day, they'll last till school. Mum says that's the minimum. The socks have come already, "
   "grown-up ones too — take a pair. And she's changed her mind about the goat: goat's milk is good for you."),
  months="10,11,12,1", gift="b_knitted_socks")

B(A, 25, "parcel", "dima", ("Детская мебель почтой", "Nursery furniture by mail"),
  ("Соколовым пришла кроватка. Дима собирает её третий вечер.",
   "The Sokolovs' cot has come. Dima has been assembling it for three evenings."),
  ("Кроватка. Инструкция на шведском и в картинках. Собирал три вечера, осталось четыре лишних винта. Позвал Сергея Кузнецова: "
   "он посмотрел, сказал «ага» и за десять минут собрал так, что винтов не хватило. Как?! Спрашиваю. Говорит: руки.",
   "The cot. Instructions in Swedish and pictures. I spent three evenings on it and had four screws left over. I "
   "called Sergey Kuznetsov: he looked, said 'right', and in ten minutes built it so that there weren't enough "
   "screws. How?! I asked. He said: hands."),
  months="12,1,2,3")

B(A, 25, "parcel", "marina", SEEDS,
  ("Марина снова выписала семена — на этот раз картошку.",
   "Marina has ordered seeds again — potatoes this time."),
  ("Новый заказ: картошка, морковь, огурцы, укроп. Ни одного артишока. Баба Нина проверила список и сказала: «Вот теперь человек». "
   "А для Ириски построили забор. Дима строил по чертежу, а Сергей — по-нормальному. Стоит Серёжин.",
   "The new order: potatoes, carrots, cucumbers, dill. Not a single artichoke. Granny Nina checked the list and "
   "said, 'Now you're a person.' And we've built a fence for Iriska. Dima built his to a drawing; Sergey built his "
   "the normal way. Sergey's is the one still standing."),
  months="2,3,4", stamp="b_seeds")

B(A, 25, "letter", "dima", SISTERS,
  ("Ласточкины пишут Диме: Ириска ждёт козлят.",
   "The Lastochkins write to Dima: Iriska is expecting kids."),
  ("Сёстры пишут, что Ириска, кажется, тоже ждёт. Помните, они её зимой на неделю к себе забирали? Вот. Я спросил Марину, "
   "бывает ли, что коза и человек рожают в один месяц. Она в меня клубком бросила. У всех нервы.",
   "The sisters write that Iriska seems to be expecting too. Remember they took her for a week in winter? Well. I "
   "asked Marina whether a goat and a person can give birth in the same month. She threw a ball of wool at me. "
   "Everyone's on edge."),
  months="3,4")

B(A, 25, "telegram", "dima", ("Марина, роддом, Городок", "Marina, maternity ward, Gorodok"),
  ("У Соколовых родилась дочка! Телеграмма из Городка.",
   "The Sokolovs have a daughter! A telegram from Gorodok."),
  ("ДОЧЬ ТРИ ДВЕСТИ ВСЁ ХОРОШО ВЕЗИ ЖЁЛТУЮ ШАПОЧКУ НЕ ЗЕЛЁНУЮ. Дочь. Дочь! Еду. Жёлтая шапочка… их тут сорок, все от мамы. "
   "Эта горчичная — она жёлтая? Помогите, пожалуйста. Я сейчас не различаю цвета, я различаю только «дочь».",
   "DAUGHTER 3200 G ALL WELL BRING YELLOW HAT NOT GREEN. A daughter. A daughter! I'm going. The yellow hat… there are "
   "forty of them, all from Mum. This mustard one — is that yellow? Please help. I can't tell colours right now, "
   "all I can tell is 'daughter'."),
  months="4,5,6", stamp="b_baby_sun", sets="sokolovy.baby")

B(A, 20, "letter", "marina", ("Катя, Москва", "Katya, Moscow"),
  ("Марина с дочкой дома. Подруга зовёт в Москву «показать ребёнка».",
   "Marina and the baby are home. A friend wants them to visit Moscow."),
  ("Ася. Асенька. Спит под яблоней в коляске, а Ириска стоит рядом и сторожит — никого не подпускает, даже Диму. Катя зовёт "
   "в Москву «показать ребёнка цивилизации». Цивилизация подождёт. Вот, нарисовала вам открытку: Ася и коза.",
   "Asya. Little Asya. She sleeps in her pram under the apple tree, and Iriska stands guard beside her and lets no "
   "one near, not even Dima. Katya wants us to come to Moscow 'to show the baby to civilisation'. Civilisation can "
   "wait. Here — I drew you a card: Asya and the goat."),
  months="5,6,7,8", gift="b_asya_card")

B(A, 25, "newspaper", "dima", ("«Сельская новь»", "The Village News"),
  ("В «Сельской нови» — фото Диминого урожая.",
   "The Village News prints a photo of Dima's harvest."),
  ("Напечатали фото: я и огурцы. Подпись: «Москвич Дмитрий Соколов собрал первый урожай». Урожай — восемнадцать банок. "
   "Посчитал: с прошлогодними артишоками каждая обошлась в две тысячи. Но эта бесценна. Берите.",
   "They printed a photo: me and the cucumbers. Caption: 'Muscovite Dmitry Sokolov brings in his first harvest.' "
   "The harvest is eighteen jars. I worked it out: counting last year's artichokes, each one cost two thousand "
   "roubles. But this one is priceless. Take it."),
  months="8,9", gift="b_dima_pickles")

B(A, 20, "postcard", "marina", ("Из Москвы и из Липовки", "From Moscow and Lipovka"),
  ("У Марины день рождения — открытки из Москвы и от соседей.",
   "Marina's birthday: cards from Moscow and from the neighbours."),
  ("Открытки: из Москвы три, из Липовки девять. Девять! От Зинаиды Павловны, от бабы Нины, от Лидии Аркадьевны, Михалыч — с пчелой. "
   "Я считаю, это перепись. И перепись говорит: мы местные. Ася праздник проспала, как и положено.",
   "Cards: three from Moscow, nine from Lipovka. Nine! From Zinaida Pavlovna, Granny Nina, Lidia Arkadyevna, "
   "Mikhalych with a bee on his. I call that a census. And the census says: we're locals. Asya slept through the "
   "party, as she should."),
  months="10", on="10-03", stamp="b_rowan")

B(A, 30, "letter", "dima", ("Друзья, Москва", "Friends, Moscow"),
  ("Московские друзья Димы собрались к нему на шашлыки. В ноябре.",
   "Dima's Moscow friends want to come for a barbecue. In November."),
  ("Друзья хотят к нам на шашлыки. В ноябре. Пишу: ребята, у нас снег, дрова, младенец и коза. Они: «Класс, коза!» Ладно. Дрова я теперь "
   "колю с одного удара. Почти. С трёх. Возьмите яблок — с наших двух старых яблонь, единственное, что растёт само.",
   "Friends want to come for a barbecue. In November. I wrote: guys, we've got snow, firewood, a baby and a goat. They "
   "said: 'Cool, a goat!' Fine. I split logs with one blow now. Almost. Three. Have some apples — from our two old "
   "trees, the only thing that grows here by itself."),
  months="10,11", gift="b_apples", stamp="b_apple")

B(A, 60, "letter", "dima", ("Олег, Москва", "Oleg, Moscow"),
  ("Друг Димы съездил в Липовку и до сих пор оттаивает.",
   "Dima's friend visited Lipovka and still hasn't thawed out."),
  ("Олег приезжал на выходные и пишет, что до сих пор не отогрелся. Спрашивает: «Как вы там живёте?» Отвечаю: нормально, Олег. "
   "Это у тебя, наверное, задвижка не открыта. Я ждал этой шутки с первой зимы. Оно того стоило.",
   "Oleg came for the weekend and writes that he still hasn't warmed up. He asks: 'How do you live out there?' I "
   "replied: fine, Oleg. You've probably got your damper closed. I've been waiting to make that joke since our "
   "first winter. It was worth it."),
  months="12,1,2", stamp="b_frost")

B(A, 45, "letter", "marina", ("Мама Димы, Москва", "Dima's mum, Moscow"),
  ("Мама Димы хочет приехать на всё лето. А может, и насовсем.",
   "Dima's mum wants to come for the whole summer. Maybe for good."),
  ("Димина мама пишет: «Приеду на лето к Асеньке, а там посмотрим». «Посмотрим» — значит, она уже узнавала, не продаётся ли "
   "дом у реки. Дима побледнел. А я рада: она будет вязать, я — рисовать. Коза её полюбит. Коза всех любит, кроме мужчин в шляпах.",
   "Dima's mum writes: 'I'll come for the summer to be with Asya, and then we'll see.' 'We'll see' means she's "
   "already asked whether the house by the river is for sale. Dima went pale. I'm glad: she'll knit, I'll draw. The "
   "goat will love her. The goat loves everyone except men in hats."),
  months="2,3,4")

B(A, 35, "parcel", "dima", ("Детская обувь почтой", "Children's shoes by mail"),
  ("Асе пришли первые ботиночки. А первые шаги она уже сделала.",
   "Asya's first shoes have come. Her first steps came first."),
  ("Ботиночки пришли, первые, красные. А шаги она сделала вчера — по крыльцу, прямо к Ириске. Три шага — и плюх. Коза её "
   "обнюхала и стояла не шевелясь, пока Ася за неё держалась. Никогда я так не гордился козой.",
   "The shoes have come — her first, red ones. But she took her first steps yesterday, across the porch, "
   "straight to Iriska. Three steps and plop. The goat sniffed her and stood stock-still while Asya held on to "
   "her. I have never been so proud of a goat."),
  months="3,4,5")

B(A, 45, "letter", "marina", ("Агентство недвижимости, Москва", "Estate agency, Moscow"),
  ("Соколовы продали московскую квартиру. Остаются насовсем.",
   "The Sokolovs have sold their Moscow flat. They're staying for good."),
  ("Квартиру в Москве продали. Всё, мы местные. Корабли сожжены — ну, или как тут говорят, дрова наколоты. Дима копает грядки "
   "под картошку, без единого артишока. А это вам вербочки: Ася наломала. Ну, я держала, она ломала.",
   "The Moscow flat is sold. That's it, we're locals. We've burned our boats — or, as they say round here, the wood "
   "is chopped. Dima is digging beds for potatoes, not an artichoke in sight. And here's some pussy willow: Asya "
   "picked it. Well, I held her and she picked."),
  months="4,5,6", gift="b_willow", stamp="b_seeds", sets="sokolovy.stayed")

# =====================================================================================================
# MARINA_BOOK — Marina's picture book about Lipovka, starring the post-office cat Surguch.
# =====================================================================================================
A = "marina_book"
SINITSA = ("Издательство «Синица», Москва", "Blue Tit Books, Moscow")
KSENIA = ("Редактор Ксения, «Синица»", "Ksenia, editor, Blue Tit Books")

B(A, 50, "letter", "marina", SINITSA,
  ("Детское издательство заинтересовалось рисунками Марины.",
   "A children's publisher is interested in Marina's drawings."),
  ("Послала в издательство три картинки: наша улица, мельница, почта. Ответили: «Хотим книжку. Про что?» Не знаю пока. Про "
   "Липовку. Про то, как сюда приходят письма. Можно я вас нарисую? Со спины. Вы не любите, когда на вас смотрят, я заметила.",
   "I sent the publisher three pictures: our street, the mill, the post office. They replied: 'We want a book. "
   "About what?' I don't know yet. About Lipovka. About how letters come here. May I draw you? From behind. You "
   "don't like being looked at, I've noticed."),
  needs="sokolovy.winter1", reply="out", stamp="b_siskin")

B(A, 55, "letter", "marina", KSENIA,
  ("Редактор предлагает Марине сделать героем книжки кота.",
   "The editor suggests Marina's book should star a cat."),
  ("Ксения пишет: «Пусть героем будет кот». А у нас есть кот! Сургуч, на почте, спит на письмах. Зарисовываю его неделю — он "
   "не замечает, он спит. Книжка будет «Кот Сургуч и почта Липовки». Вы не против, что кот главнее вас?",
   "Ksenia writes: 'Let the hero be a cat.' And we have a cat! Surguch, at the post office, asleep on the letters. "
   "I've been sketching him for a week — he hasn't noticed, he's asleep. The book will be 'Surguch the Cat and the "
   "Lipovka Post'. You don't mind the cat outranking you?"))

B(A, 55, "registered", "marina", SINITSA,
  ("Марине пришёл договор на книжку про Липовку.",
   "Marina's contract for the book about Lipovka has come."),
  ("Договор. Настоящий, в двух экземплярах, с печатью. Срок сдачи — через год. Год! Дима сказал: за год в Липовке можно вырастить "
   "кабачок и ребёнка. Он, наверное, пошутил. Надеюсь. Нет, правда, надеюсь, что пошутил.",
   "A contract. A real one, two copies, with a seal. Deadline: a year from now. A year! Dima said that in a year in "
   "Lipovka you can grow a courgette and a child. He was joking, I expect. I hope. No, really, I hope he was joking."))

B(A, 60, "letter", "marina", KSENIA,
  ("Редактор жалуется Марине: в книжке про кота слишком много козы.",
   "The editor complains: there's too much goat in a book about a cat."),
  ("Ксения пишет: «Марина, на каждом развороте коза. Это книжка про кота». Пересчитала: коза на одиннадцати разворотах из "
   "двенадцати. А что делать, если Ириска всегда в кадре? Оставлю на трёх. На четырёх. Ладно, на пяти.",
   "Ksenia writes: 'Marina, there's a goat on every spread. This is a book about a cat.' I counted: the goat is on "
   "eleven spreads out of twelve. What can I do, Iriska is always in shot? I'll keep her on three. Four. Fine, five."))

B(A, 40, "letter", "marina", KSENIA,
  ("Марине продлили срок — «в связи с рождением соавтора».",
   "Marina's deadline is extended 'owing to the birth of a co-author'."),
  ("Ксения продлила срок на три месяца — «в связи с рождением соавтора». Это про Асю. Рисую одной рукой, второй качаю коляску. "
   "Ася уже ставит кляксы: одна попала Сургучу на хвост, и стало лучше. Оставим.",
   "Ksenia has given me three more months 'owing to the birth of a co-author'. That's Asya. I draw with one hand "
   "and rock the pram with the other. Asya already makes blots: one landed on Surguch's tail and it looked better. "
   "We'll keep it."),
  needs="sokolovy.baby")

B(A, 60, "parcel", "marina", SINITSA,
  ("Марине прислали вёрстку книжки про кота Сургуча.",
   "Marina has the proofs of her book about Surguch the cat."),
  ("Вёрстка! Всё собрано: мельница, магазин, клуб, пчёлы Михалыча, почта с синей крышей. И Сургуч спит на последнем письме. "
   "Посмотрите, похоже? Мне важно, чтобы вы сказали. Вы тут каждый день ходите.",
   "The proofs! It's all there: the mill, the shop, the club, Mikhalych's bees, the post office with its blue roof. "
   "And Surguch asleep on the last letter. Look — is it like? I need you to tell me. You walk here every day."),
  stamp="b_cat_post")

B(A, 50, "letter", "marina", KSENIA,
  ("Книжку Марины отправили в типографию: тираж пять тысяч.",
   "Marina's book has gone to print: five thousand copies."),
  ("Печатают! Пять тысяч. Пять тысяч котов Сургучей разъедутся по стране, а настоящий даже не проснулся, когда я ему сказала. "
   "Ксения просит фото автора. Я сфотографировалась с козой. Пусть теперь сама решает.",
   "They're printing it! Five thousand. Five thousand Surguches will travel all over the country, and the real one "
   "didn't even wake up when I told him. Ksenia wants an author photo. I had mine taken with the goat. Let her decide now."))

B(A, 50, "parcel", "marina", SINITSA,
  ("Марине пришли её книжки — «Кот Сургуч и почта Липовки».",
   "Marina's books have arrived: Surguch the Cat and the Lipovka Post."),
  ("Пришли! Пахнут краской. Первая — вам, подписала: «Тому, кто носит письма в Липовке, — от кота и автора». Кот поставил лапу: "
   "я обмакнула её в акварель, он не возражал, он спал. Вторую отдайте Сургучу. Пусть спит на ней.",
   "They've come! They smell of ink. The first is yours; I signed it: 'To the one who carries the letters in "
   "Lipovka — from the cat and the author.' The cat added his paw: I dipped it in watercolour and he didn't mind, "
   "he was asleep. Give the second one to Surguch. He can sleep on it."),
  gift="b_surguch_book", stamp="b_cat_post")

B(A, 45, "letter", "marina", ("2 «Б», школа № 7, Новосибирск", "Class 2B, School 7, Novosibirsk"),
  ("Дети из Новосибирска спрашивают Марину: Липовка правда есть?",
   "Children in Novosibirsk ask Marina: is Lipovka real?"),
  ("Второй «Б» из Новосибирска спрашивает: Липовка правда есть? И кот есть? И почтальон правда ходит пешком? Отвечаю: всё правда, "
   "кот спит, почтальон ходит — вот, прямо сейчас стоит у моей калитки. Подпишетесь? Им будет приятно.",
   "Class 2B in Novosibirsk asks: is Lipovka real? Is the cat real? Does the postman really walk everywhere? I'm "
   "answering: all true, the cat sleeps, the postman walks — and is standing at my gate right now. Will you sign "
   "too? They'd love that."),
  reply="out", stamp="b_letters")

B(A, 40, "letter", "marina", ("Л. А. Белова, библиотека", "L. A. Belova, the library"),
  ("Лидия Аркадьевна зовёт Марину на презентацию книжки в библиотеке.",
   "Lidia Arkadyevna invites Marina to launch her book at the library."),
  ("Лидия Аркадьевна устраивает презентацию моей книжки в библиотеке, в субботу. Пишет: «Будут дети, Зинаида с пирожками и кот, "
   "если удастся его разбудить». Волнуюсь больше, чем на защите диплома. Вы придёте? Вы же там на четвёртой странице.",
   "Lidia Arkadyevna is holding a launch for my book at the library on Saturday. She writes: 'There'll be children, "
   "Zinaida with pies, and the cat, if he can be woken.' I'm more nervous than at my degree defence. Will you come? "
   "You're on page four, after all."))


# =====================================================================================================
# output
# =====================================================================================================
def write(path, cols, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["\t".join(cols)]
    for r in rows:
        cells = [str(c) for c in r]
        for c in cells:
            assert "\t" not in c and "\n" not in c and "\r" not in c, c
        lines.append("\t".join(cells))
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def lint():
    for r in ROWS:
        d = dict(zip(ARC_COLS, r))
        where = f"{d['arc']}#{d['n']}"
        for k, lim in (("from", 40), ("brief", 80), ("news", 320)):
            for lang in ("ru", "en"):
                if len(d[f"{k}_{lang}"]) > lim:
                    print(f"  {where}: {k}_{lang} {len(d[f'{k}_{lang}'])} > {lim}")
    gifts = sum(1 for r in ROWS if r[15])
    stamps = sum(1 for r in ROWS if r[16])
    print(f"{len(ROWS)} beats, {gifts} gifts, {stamps} stamps")
    for arc in _n:
        print(f"  {arc}: {_n[arc]}")


def simulate():
    """Earliest delivery of every beat, for each start month (flags from these arcs only)."""
    order = ["mikhalych", "zina", "kolya", "lidia", "sokolovy", "nina", "marina_book"]
    by_arc = {}
    for r in ROWS:
        by_arc.setdefault(r[0], []).append(dict(zip(ARC_COLS, r)))
    for m in range(1, 13):
        start = dt.date(2027, m, 1)
        flags = {}
        spans = []
        for arc in order:
            t = start
            for b in by_arc[arc]:
                t = t + dt.timedelta(days=int(b["gap"]))
                for f in filter(None, b["needs"].split(",")):
                    t = max(t, flags.get(f, dt.date(2100, 1, 1)))
                months = {int(x) for x in b["months"].split(",")} if b["months"] else set(range(1, 13))
                while t.month not in months or (b["on"] and t.strftime("%m-%d") != b["on"]):
                    t += dt.timedelta(days=1)
                if b["sets"]:
                    flags[b["sets"]] = t
            spans.append(f"{arc}={(t - start).days / 365:.1f}")
        print(f"start {m:2d}: " + " ".join(spans))


if __name__ == "__main__":
    write(C / "arcs/b.tsv", ARC_COLS, ROWS)
    write(C / "items/b.tsv", ["key", "family", "variant", "name_ru", "name_en"], ITEMS)
    write(C / "stamps/b.tsv", ["key", "family", "bg", "value", "name_ru", "name_en", "series"],
          [(k, f, bg, str(v), ru, en, s) for k, f, bg, v, ru, en, s in STAMPS])
    lint()
    if "--sim" in sys.argv:
        simulate()
