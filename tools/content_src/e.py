"""Group E: letters addressed to the postman (to = me).

python tools/content_src/e.py  -> arcs/e.tsv, items/e.tsv, stamps/e.tsv
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
C = ROOT / "app/src/main/assets/content"

ARC_COLS = ["arc", "n", "gap", "months", "on", "needs", "kind", "to", "from_ru", "from_en", "brief_ru", "brief_en",
            "news_ru", "news_en", "reply", "gift", "stamp", "sets"]

ITEMS = []   # key, family, variant, name_ru, name_en
STAMPS = []  # key, family, bg, value, name_ru, name_en, series
ROWS = []
_n = {}


def item(key, family, variant, ru, en):
    ITEMS.append([key, family, variant, ru, en])


def stamp(key, family, bg, value, ru, en, series):
    STAMPS.append([key, family, bg, str(value), ru, en, series])


def B(arc, gap, months, needs, kind, fr, fe, br, be, nr, ne, gift="", stamp="", sets="", on=""):
    _n[arc] = _n.get(arc, 0) + 1
    ROWS.append([arc, str(_n[arc]), str(gap), months, on, needs, kind, "me", fr, fe, br, be, nr, ne, "", gift, stamp, sets])


DISTRICT_RU, DISTRICT_EN = "Районный узел связи", "District Post Office"

# ---------------------------------------------------------------- items
item("e_attic_key", "found", "key", "Латунный ключ неизвестно от чего", "A brass key to who knows what")
item("e_varya_daisies", "postcard", "flowers", "Варины ромашки (и пчела)", "Varya's daisies (and a bee)")
item("e_secret_leaves", "bouquet", "dried", "Осенние листья от Тайного друга", "Autumn leaves from a Secret Friend")
item("e_currant_jam", "jar", "jam", "Смородиновое варенье Кузнецовых", "The Kuznetsovs' blackcurrant jam")
item("e_porch_pie", "pie", "cabbage", "Пирог с капустой с крыльца", "A cabbage pie from the porch")
item("e_porch_mittens", "mittens", "patterned", "Варежки, левая длиннее", "Mittens, the left one longer")
item("e_zina_tea", "tea", "tin", "Чай в жестянке от Зины", "A tin of tea from Zina")
item("e_class_1979", "photo", "old", "4 класс на мостках, 1979", "Year 4 on the landing stage, 1979")
item("e_pigeon_whistle", "toy", "whistle", "Свистулька-голубь от Пети", "Petya's pigeon whistle")
item("e_ksenia_photo", "photo", "old", "Ксеня на Неве, 1959", "Ksenya by the Neva, 1959")
item("e_teacher_thermometer", "thermometer", "window", "Оконный градусник Лебедева", "Lebedev's window thermometer")
item("e_wax_candle", "candle", "honey", "Восковая свеча Михалыча", "Mikhalych's beeswax candle")
item("e_volga_card", "postcard", "ship", "Открытка с волжского теплохода", "A postcard from a Volga steamer")
item("e_ivan_tea", "tea", "herbs", "Уральский иван-чай", "Fireweed tea from the Urals")
item("e_ryzhiki", "jar", "mushrooms", "Солёные рыжики из Ключей", "Salted saffron milk caps from Klyuchi")
item("e_galina_newyear", "postcard", "winter", "Новогодняя открытка Галины", "Galina's New Year card")
item("e_goat_socks", "socks", "grey", "Носки из козьей шерсти", "Goat-wool socks")
item("e_jasper", "found", "pebble", "Яшма с Чусовой", "Jasper from the Chusovaya")
item("e_visit_photo", "photo", "group", "Галина у почты Липовки", "Galina at the Lipovka post office")
item("e_cedar_cones", "basket", "cones", "Кедровые шишки с Урала", "Cedar cones from the Urals")
item("e_bag_badge", "badge", "post", "Значок с новой почтовой сумки", "The badge from the new post bag")
item("e_gramota", "book", "red", "Почётная грамота в красной папке", "A certificate of honour in a red folder")
item("e_honour_badge", "badge", "medal", "«Почётный почтальон района»", "Honorary Postman of the District")
item("e_route_map", "map", "old", "Карта маршрутов 1961 года", "A 1961 map of the post rounds")
item("e_pestov_star", "badge", "star", "Звёздочка Пестова", "Pestov's star")
item("e_readers_card", "postcard", "city", "Открытка от читателей газеты", "A card from the newspaper's readers")
item("e_column_file", "book", "brown", "Подшивка «Записок почтальона»", "The bound “Notes of a Postman”")
item("e_bublik_pretzel", "bread", "pretzel", "Баранка для Бублика", "A pretzel for Bublik")
item("e_bublik_scarf", "scarf", "red", "Двухметровый шарф Бублика", "Bublik's two-metre scarf")

# ---------------------------------------------------------------- stamps
stamp("e_order47", "letter", "cream", 10, "Приказ № 47", "Order No. 47", "post")
stamp("e_daisies", "flower", "sky", 3, "Ромашки у синего забора", "Daisies by the blue fence", "lipovka")
stamp("e_felt_cat", "cat", "red", 1, "Сургуч фломастером", "Surguch in felt-tip", "post")
stamp("e_secret_friend", "letter", "violet", 8, "Тайный друг", "The Secret Friend", "post")
stamp("e_porch_snow", "snowflake", "blue", 6, "Крыльцо в снегу", "A porch in the snow", "seasons")
stamp("e_ledger", "book", "cream", 3, "Страничка из амбарной книги", "A page from the ledger", "lipovka")
stamp("e_flood", "boat", "sky", 8, "Паводок на Липке", "Flood on the Lipka", "seasons")
stamp("e_obs_telegram", "telegram", "night", 12, "Телеграмма с обсерватории", "A telegram from the observatory", "far")
stamp("e_pigeon", "bird", "sky", 5, "Голубиная почта", "Pigeon post", "post")
stamp("e_takeoff", "clock", "cream", 7, "Вылет в 7:40", "Take-off at 7:40", "post")
stamp("e_stamp_1958", "letter", "cream", 40, "Марка с конверта 1958 года", "A stamp off a 1958 envelope", "post")
stamp("e_showcase", "book", "violet", 25, "Витрина «Письма из Липовки»", "The Letters from Lipovka case", "gorodok")
stamp("e_minus27", "snowflake", "sky", 27, "Минус двадцать семь", "Minus twenty-seven", "seasons")
stamp("e_orion", "star", "night", 9, "Орион над Липкой", "Orion over the Lipka", "seasons")
stamp("e_phacelia", "flower", "violet", 6, "Фацелия", "Phacelia", "lipovka")
stamp("e_porch_bee", "bee", "gold", 8, "Пчела на почтовом крыльце", "A bee on the post office porch", "lipovka")
stamp("e_volga", "ship", "blue", 12, "Волга у Ярославля", "The Volga at Yaroslavl", "far")
stamp("e_astrakhan", "sun", "gold", 16, "Астрахань. Конец пути", "Astrakhan. The end of the line", "far")
stamp("e_ural", "mountain", "green", 10, "Урал. Река Чусовая", "The Urals. The Chusovaya", "far")
stamp("e_palma", "dog", "red", 6, "Пальма", "Palma", "far")
stamp("e_minus38", "snowflake", "night", 12, "Минус тридцать восемь", "Minus thirty-eight", "far")
stamp("e_malachite", "mountain", "sea", 20, "Малахит", "Malachite", "far")
stamp("e_mail_boat", "boat", "sea", 9, "Почта приплыла", "The post has sailed in", "far")
stamp("e_kerosene", "lantern", "night", 7, "Ночь при керосинке", "A night by the oil lamp", "far")
stamp("e_ski_race", "sled", "blue", 11, "Лыжня связистов", "The postal workers' ski race", "far")
stamp("e_galina_telegram", "telegram", "cream", 25, "«Выехала!»", "“On my way!”", "far")
stamp("e_invitation", "heart", "red", 30, "Приглашение в Ключи", "An invitation to Klyuchi", "far")
stamp("e_bridge", "bridge", "sky", 50, "Мост в Заречье", "The bridge to Zarechye", "zarechye")
stamp("e_district_ny", "fireworks", "night", 20, "С Новым годом, узел!", "Happy New Year from the district", "holidays")
stamp("e_honour", "bell", "gold", 99, "Почётный почтальон", "Honorary Postman", "post")
stamp("e_3000", "globe", "sky", 30, "Три тысячи километров", "Three thousand kilometres", "post")
stamp("e_editorial", "house", "red", 12, "Редакция «Сельской нови»", "The Village News office", "gorodok")
stamp("e_readers", "letter", "blue", 4, "Письма читателей", "Letters from readers", "gorodok")
stamp("e_holiday_issue", "fireworks", "red", 10, "Новогодний номер", "The New Year issue", "holidays")
stamp("e_vladivostok", "lighthouse", "sea", 40, "Владивосток", "Vladivostok", "far")
stamp("e_bublik_scarf", "dog", "red", 5, "Бублик в шарфе", "Bublik in a scarf", "lipovka")
stamp("e_reader214", "dog", "dusk", 3, "Читатель № 214", "Reader No. 214", "lipovka")

# ================================================================ me_welcome
A = "me_welcome"
B(A, 0, "", "", "registered", DISTRICT_RU, DISTRICT_EN,
  "Приказ о назначении: теперь вы — почтальон Липовки.",
  "The appointment order: you are now the postman of Lipovka.",
  "ПРИКАЗ № 47. Назначить почтальона отделения связи Липовка (участок: Липовка и далее по мере восстановления мостов). Приступить немедленно. Выдать: сумку почтовую — 1 шт., ключи от отделения — 1 связка, печать календарную — 1 шт. Кот на балансе отделения не числится, но проживает. Начальник районного узла связи В. Т. Пестов. P.S. От руки, не для приказа: участок у вас хороший, люди там пишут письма. Это теперь редкость. Берегите ноги.",
  "ORDER No. 47. A postman is hereby appointed to the Lipovka post office (round: Lipovka, and further as bridges are restored). To start at once. Issued: post bag, 1; office keys, 1 bunch; date stamp, 1. A cat is not on the office's books, but resides. V. T. Pestov, Head of the District Post Office. P.S. By hand, not for the order: it's a good round. People there still write letters, which is rare these days. Look after your feet.",
  stamp="e_order47")
B(A, 1, "", "", "letter", "Антонина Гавриловна (записка)", "Antonina Gavrilovna (a note)",
  "В ящике стола — записка от прежней почтальонши.",
  "A note from the previous postwoman, left in the desk drawer.",
  "Здравствуйте, кто бы вы ни были! Я тридцать один год носила эту сумку, теперь ваша очередь. Главное. Сургуч ест только из блюдца с синей каёмкой, из другого не станет, не уговаривайте. Спит на письмах — сгоняйте ласково, он обидчивый. Зелёный чайник в горошек ставьте на малый огонь: на большом он свистит фальшиво, и Сургуч уходит из дома. Ходики отстают на семь минут, не поправляйте — вся Липовка под них живёт. Агафье Петровне пенсию несите к одиннадцати, она к этому часу пироги ставит. Удачи. А. Г.",
  "Hello, whoever you are! I carried this bag for thirty-one years; now it's your turn. The main things. Surguch eats only from the saucer with the blue rim; he won't touch any other, so don't try. He sleeps on the letters: shoo him off gently, he takes offence. Put the green spotted kettle on a low flame: on a high one it whistles out of tune and Surguch leaves the house. The wall clock is seven minutes slow. Don't fix it, all Lipovka lives by it. Take Agafya Petrovna her pension by eleven, that's when she puts the pies in. Good luck. A. G.")
B(A, 2, "", "", "parcel", DISTRICT_RU, DISTRICT_EN,
  "Посылка из района: ключи, печать и ещё один ключ — неизвестно от чего.",
  "A parcel from the district: keys, a date stamp, and one mystery key.",
  "Опись вложения. Ключи от отделения Липовка: от входной двери — 1, от сейфа — 1, от почтового ящика у магазина — 1. Печать календарная «ЛИПОВКА» — 1. Ключ латунный старого образца, назначение неизвестно — 1 (обнаружен в деле отделения за 1958 год, возвращается по месту хранения). Оператор Л. Мошкина. Приписка: Валентин Тимофеевич говорит, что ключ «от чердака, наверное», но сам не помнит, а Антонина Гавриловна не знала. Если откроете им что-нибудь — сообщите, нам самим интересно.",
  "Packing list. Keys to the Lipovka office: front door, 1; safe, 1; the post box by the shop, 1. Date stamp LIPOVKA, 1. Brass key, old type, purpose unknown, 1 (found in the office's file for 1958, returned to where it belongs). Clerk L. Moshkina. A note: Valentin Timofeyevich says the key is “probably for the attic”, but he doesn't remember himself, and Antonina Gavrilovna never knew. If it opens anything, do tell us. We're curious too.",
  gift="e_attic_key")
B(A, 2, "", "", "postcard", "Варя Кузнецова", "Varya Kuznetsova",
  "Открытка от Вари: «Добро пожаловать» с ромашками и ошибками.",
  "A postcard from Varya: a welcome full of daisies and spelling mistakes.",
  "ЗДРАСТВУЙТЕ НОВЫЙ ПАЧТАЛЬОН! Добро пожаловать в Липовку. Я Варя мне 7 лет. Я живу где синий забор и трактор. Сургуч хороший кот, но он царапаица если гладить против шерсти. Я вам нарисовала цветы, это ромашки, а это не клякса а пчела. Пишите мне пожалуста, я умею читать уже почти всё. ВАРЯ",
  "HELO NEW POSTMAN! Welcome to Lipovka. I am Varya I am 7. I live where the blue fence and the tractor are. Surguch is a good cat but he scrachs if you stroke him the rong way. I drew you flowers, these are dasies and this is not a blot it is a bee. Please rite to me, I can read nearly everything now. VARYA",
  gift="e_varya_daisies", stamp="e_daisies")
B(A, 3, "", "", "notice", DISTRICT_RU, DISTRICT_EN,
  "Извещение из района о почтовой машине — с припиской не по форме.",
  "A notice from the district about the mail van, with an off-the-record note.",
  "Извещение. Почтовая машина прибывает в Липовку ежедневно в 7:15 (по ходикам отделения — в 7:08). Входящую корреспонденцию разбирать по ячейкам, исходящую сдавать водителю до 7:30. Посылки свыше 10 кг доставлять тачкой; тачка в сарае, колесо подкачать. — Не по форме: водитель Михаил очень любит, когда ему наливают чаю из зелёного чайника. Не отказывайте человеку: он вам весь район привозит. В. Т. П.",
  "Notice. The mail van arrives in Lipovka daily at 7:15 (7:08 by the office clock). Sort incoming mail into the pigeonholes; hand outgoing mail to the driver by 7:30. Parcels over 10 kg are to be delivered by wheelbarrow; the wheelbarrow is in the shed, pump up the tyre. Off the record: Mikhail the driver is very fond of a cup of tea from the green kettle. Don't refuse the man, he brings you the whole district. V. T. P.")
B(A, 7, "", "", "letter", "Антонина Гавриловна, Городок", "Antonina Gavrilovna, Gorodok",
  "Антонина Гавриловна из Городка спрашивает, как там Сургуч. И вы.",
  "Antonina Gavrilovna writes from Gorodok to ask about Surguch. And you.",
  "Здравствуйте! Пишу вам с пятого этажа, от сына. Тут лифт, горячая вода и ни одной собаки, которая бы меня знала. Просыпаюсь в шесть и не знаю, куда себя деть: ноги просятся на маршрут. Как вы там? Сургуч не похудел? Липовка вас приняла? Она сначала присматривается, а потом пироги несёт — это и значит, что приняла. Когда зовут чай пить, не отказывайтесь: это тоже работа почтальона, только её в приказах не пишут. Кланяйтесь от меня всем. И ходикам. Ваша А. Г.",
  "Hello! I'm writing from the fifth floor, at my son's. There's a lift, hot water, and not one dog who knows me. I wake at six and don't know what to do with myself: my feet want to go on the round. How are you getting on? Has Surguch lost weight? Has Lipovka taken to you? First it watches you, then it brings you pies, and that's how you know. When they ask you in for tea, don't say no: that's part of a postman's job too, it just isn't written in the orders. Give my regards to everyone. And to the clock. Yours, A. G.")

# ================================================================ me_autumn1: the Secret Friend (Varya)
A = "me_autumn1"
SF_RU, SF_EN = "Тайный друг", "A Secret Friend"
B(A, 3, "9", "", "letter", "Без обратного адреса", "No return address",
  "Письмо «Почтальону Липовки. Лично» — без подписи и без марки.",
  "A letter “To the Postman of Lipovka. Personal”, unsigned and unstamped.",
  "ПОЧТАЛЬОНУ ЛИПОВКИ. ЛИЧНО. Здравствуйте. Вам навернае никто не пишет, потому что вы всем носите письма, а вам никто. Это нисправедливо. Поэтому я буду вам писать. Кто я — секрет. Сегодня в Липовке осень, листья жёлтые и красные, а у клёна возле клуба уже голые ноги. Ответ кладите под камень у колодца. ТАЙНЫЙ ДРУГ",
  "TO THE POSTMAN OF LIPOVKA. PERSONAL. Hello. Probly nobody writes to you, because you bring everyone letters but nobody brings you any. That is unfare. So I will write to you. Who I am is a secret. Today it is autumn in Lipovka, the leaves are yellow and red, and the maple by the club has bare legs already. Put your answer under the stone by the well. A SECRET FRIEND")
B(A, 7, "9,10", "", "letter", SF_RU, SF_EN,
  "Тайный друг пишет снова, а марку рисует фломастером.",
  "The Secret Friend writes again, with a stamp drawn in felt-tip.",
  "ПОЧТАЛЬОНУ ЛИПОВКИ. Здравствуйте опять. Спасибо, что ответили под камнем, только камень тяжело поднимать. Марку я сама нарисовала фломастером, это Сургуч, он рыжий, потому что фломастер рыжий. Вопрос: вам не страшно ходить мимо гусей бабы Нины? Мне страшно. Я хожу мимо них портфелем вперёд. Сегодня в 9 часов я видела, как вы шли быстро, а у вас развязался шнурок. Завяжите. ТАЙНЫЙ ДРУГ",
  "TO THE POSTMAN OF LIPOVKA. Hello again. Thank you for answering under the stone, only the stone is heavy to lift. I drew the stamp myself, it's Surguch, he's ginger because the felt-tip is ginger. I'm a girl, that's all I'm telling. Question: aren't you scared walking past Granny Nina's geese? I am. I walk past them with my school bag in front. Today at 9 o'clock I saw you walking fast and your shoelace was undone. Tie it. A SECRET FRIEND",
  stamp="e_felt_cat")
B(A, 8, "9,10", "", "letter", SF_RU, SF_EN,
  "Тайный друг прислал осенние листья, засушенные в медицинской книге.",
  "The Secret Friend sends autumn leaves, pressed in a medical book.",
  "ПОЧТАЛЬОНУ ЛИПОВКИ. Посылаю вам осень. Это листья, я их сушила в толстой книге про болезни (оттуда ничего не заразное). Самый красный — с рябины у Анны, жёлтый — с липы у школы, а коричневый просто так. Вопрос: правда, что почтальоны знают все тайны, потому что носят все письма? Мама говорит, хороший почтальон чужих писем не читает. Тогда как вы узнаете, кто я? ТАЙНЫЙ ДРУГ",
  "TO THE POSTMAN OF LIPOVKA. I'm sending you autumn. These are leaves, I pressed them in a fat book about illnesses (nothing in it is catching). The reddest one is from Anna's rowan, the yellow one from the linden by the school, and the brown one is just because. Question: is it true postmen know all the secrets because they carry all the letters? Mum says a good postman never reads other people's letters. Then how will you find out who I am? A SECRET FRIEND",
  gift="e_secret_leaves")
B(A, 9, "10,11", "", "letter", SF_RU, SF_EN,
  "Тайный друг проговорился: папа, трактор и буква Я задом наперёд.",
  "The Secret Friend lets slip: a dad, a tractor and a back-to-front letter.",
  "ПОЧТАЛЬОНУ ЛИПОВКИ. Сегодня был первый иней, и папа сказал, что трактору тоже холодно. У нас в классе пять человек, я самая быстрая, кроме Мишки. Учительница поставила мне звёздочку за букву Я, раньше я писала её задом наперёд. Ой. Это была подсказка, но я её не стираю, потому что ластик ест бумагу. Вы уже догадались? Если догадались, никому не говорите. ТАЙНЫЙ ДРУГ",
  "TO THE POSTMAN OF LIPOVKA. Today was the first frost and Dad said the tractor is cold too. There are five of us in my class and I am the fastest except Mishka. The teacher gave me a star for my letter R, I used to write it back to front. Oops. That was a clue but I'm not rubbing it out because the rubber eats the paper. Have you guessed yet? If you have, don't tell anyone. A SECRET FRIEND")
B(A, 8, "10,11", "", "letter", SF_RU, SF_EN,
  "Тайный друг обещает скоро раскрыться и спрашивает про любимое варенье.",
  "The Secret Friend promises a reveal soon and asks your favourite jam.",
  "ПОЧТАЛЬОНУ ЛИПОВКИ. Я заметила, что вы стали ходить мимо нашего забора медленно и смотреть в окна. Это нечестно! Смотреть можно только в письма. Ладно. Скоро я раскроюсь, как в кино. Последний вопрос: какое у вас любимое варенье? Это нужно для дела. ТАЙНЫЙ ДРУГ. P.S. Гусей бабы Нины я больше не боюсь, я отдала им свой бутерброд.",
  "TO THE POSTMAN OF LIPOVKA. I noticed you've started walking past our fence slowly and looking at the windows. That's cheating! You can only look in letters. All right. Soon I will reveal myself like in a film. Last question: what is your favourite jam? It's needed for something. A SECRET FRIEND. P.S. I'm not scared of Granny Nina's geese any more, I gave them my sandwich.",
  stamp="e_secret_friend")
B(A, 7, "10,11", "", "letter", "Варя Кузнецова", "Varya Kuznetsova",
  "Тайна раскрыта: Тайный друг — это Варя Кузнецова. Зовут на чай!",
  "Mystery solved: the Secret Friend is Varya. You're invited to tea!",
  "ПОЧТАЛЬОНУ ЛИПОВКИ. Это я, Варя Кузнецова!!! Тайный друг — это была я! Вы, навернае, догадались из-за синего забора. Я писала, потому что всем приходят письма, а вам только от начальника, а это не считается. Мама сказала, что надо раскрыться и что я молодец, но в следующий раз марку надо клеить настоящую. Приходите в субботу на чай. Будет смородиновое варенье, потому что вы так и не ответили, какое любимое. ВАРЯ. P.S. Можно я буду писать дальше, только уже не тайно?",
  "TO THE POSTMAN OF LIPOVKA. It's me, Varya Kuznetsova!!! The Secret Friend was me! You probly guessed because of the blue fence. I wrote because everybody gets letters and you only get them from your boss, and that doesn't count. Mum said I have to reveal myself and that I'm clever, but next time I must use a real stamp. Come to tea on Saturday. There will be blackcurrant jam, because you never said what your favourite is. VARYA. P.S. Can I keep writing, only not secretly?")
B(A, 6, "10,11", "", "parcel", "Ольга Кузнецова, ФАП", "Olga Kuznetsova, medical post",
  "Ольга Кузнецова извиняется за Варины письма и шлёт варенье.",
  "Olga Kuznetsova apologises for Varya's letters and sends jam.",
  "Здравствуйте! Пишу коротко, у меня приём. Хочу извиниться: Варя полтора месяца таскала у меня конверты — оказалось, на «тайные письма». Я всё узнала, когда нашла в фельдшерском справочнике кленовые листья. Спасибо, что отвечали ей под камнем. Она стала писать почти без ошибок, учительница удивляется, а Варя важно говорит: «У меня переписка». Варенье передаю — раз уж вы так и не сказали, какое любимое. Ольга Кузнецова, ФАП Липовка",
  "Hello! A short note, I have patients waiting. I want to apologise: for six weeks Varya was pinching my envelopes, for “secret letters”, it turns out. I found out when I found maple leaves in my medical handbook. Thank you for answering her under the stone. She now writes almost without mistakes, the teacher is amazed, and Varya says importantly, “I have a correspondence.” Here's the jam, since you never did say which one is your favourite. Olga Kuznetsova, Lipovka medical post",
  gift="e_currant_jam", sets="me.autumn1")

# ================================================================ me_winter1: gifts on the porch (the whole village)
A = "me_winter1"
PORCH_RU, PORCH_EN = "Оставлено на крыльце", "Left on the porch"
B(A, 3, "12", "", "parcel", PORCH_RU, PORCH_EN,
  "На крыльце почты — тёплый пирог в полотенце и записка без подписи.",
  "On the post office porch: a warm pie in a towel and an unsigned note.",
  "На крыльце, в полотенце с петухами, — пирог с капустой, ещё тёплый. Под ним записка, печатными буквами, карандашом: «ПОЧТЕ. ЕШЬТЕ ГОРЯЧИМ. ПОЛОТЕНЦЕ ВЕРНИТЕ НА ПЕРИЛА». На снегу у ступенек — следы валенок, маленькие, и ведут они за угол, а там тропинку уже замело.",
  "On the porch, wrapped in a towel with cockerels on it: a cabbage pie, still warm. Under it a note in pencil capitals: “FOR THE POST. EAT IT HOT. LEAVE THE TOWEL ON THE RAILING.” In the snow by the steps, small felt-boot prints lead round the corner, where the path has already drifted over.",
  gift="e_porch_pie", stamp="e_porch_snow")
B(A, 6, "12,1", "", "parcel", PORCH_RU, PORCH_EN,
  "В ящике у двери — варежки с узором. Полотенце с перил исчезло.",
  "Patterned mittens in the box by the door. The towel on the railing is gone.",
  "В почтовом ящике у двери — варежки с узором, левая заметно длиннее правой. Записка, почерк уже другой, буквы круглые: «ПО НОЧАМ МИНУС ДВАДЦАТЬ, А ВЫ ХОДИТЕ В ПЕРЧАТОЧКАХ. СТЫДНО». Полотенце с петухами с перил исчезло. Сургуч сидит на подоконнике с видом, будто всё видел, но не скажет.",
  "In the box by the door: patterned mittens, the left one clearly longer than the right. A note, in different handwriting this time, round letters: “IT'S MINUS TWENTY AT NIGHT AND YOU GO ABOUT IN THOSE LITTLE GLOVES. FOR SHAME.” The cockerel towel has vanished from the railing. Surguch sits on the windowsill looking as if he saw everything but isn't telling.",
  gift="e_porch_mittens")
B(A, 7, "12,1", "", "parcel", PORCH_RU, PORCH_EN,
  "На ступеньке — клюква в сахаре и записка с учительским наклоном.",
  "Sugared cranberries on the step, and a note in a teacher's slanting hand.",
  "На ступеньке — банка клюквы в сахаре, завёрнутая в газету «Сельская новь» за прошлый четверг. Бумажка из тетради в клетку: «От простуды. По ложке утром, натощак». Почерк опять другой: с наклоном, ровный, как на школьной доске. Это уже третий человек. Или четвёртый, если считать того, кто унёс полотенце.",
  "On the step: a jar of sugared cranberries wrapped in last Thursday's Village News. A slip torn from a squared exercise book: “Against colds. A spoonful in the morning, before breakfast.” Different handwriting again, slanted and neat, like on a school blackboard. That's a third person. Or a fourth, if you count whoever took the towel.")
B(A, 7, "1,2", "", "letter", "Записка в дверной щели", "A note in the door crack",
  "Неизвестные просят не караулить у окна. Следы на снегу — разные.",
  "The unknown givers ask you not to keep watch. The prints in the snow vary.",
  "Записка в дверной щели: «НЕ КАРАУЛЬТЕ У ОКНА ДО ПОЛНОЧИ. ВСЁ РАВНО НЕ УВИДИТЕ, А СВЕТ ЖЖЁТЕ». Утром на крыльце — пихтовый веник, связанный бечёвкой («для пола», сказано на ярлычке), и на снегу целая выставка следов: валенки, сапоги сорок пятого размера, детские ботинки и, кажется, кошачьи. Кошачьи, впрочем, ведут к Сургучу.",
  "A note in the crack of the door: “DON'T WATCH AT THE WINDOW TILL MIDNIGHT. YOU WON'T SEE US ANYWAY, AND YOU'RE WASTING ELECTRICITY.” In the morning on the porch: a fir-branch broom tied with string (“for the floor”, says the label), and the snow holds a whole exhibition of prints: felt boots, size-eleven boots, a child's shoes and, it seems, a cat's. The cat's, admittedly, lead to Surguch.")
B(A, 8, "1,2", "", "parcel", PORCH_RU, PORCH_EN,
  "Под банкой мёда забыта страничка из амбарной книги. Это график!",
  "Under a jar of honey, a page from a ledger was left behind. It's a rota!",
  "На крыльце — банка тёмного гречишного мёда. А под банкой, видно второпях, забыта страничка, вырванная из амбарной книги: «…четв. — Михалыч (мёд). пятн. — Лебедев (клюква!). суб. — Кузнецовы, Варю не пускать одну. воскр. — Нина (пирог, не с капустой, с капустой уже было). Агафье — вторник, НЕ СПОРИТЬ. Не забыть: пол…» Дальше оторвано.",
  "On the porch: a jar of dark buckwheat honey. And under it, left in a hurry by the look of it, a page torn from a ledger: “…Thurs: Mikhalych (honey). Fri: Lebedev (cranberries!). Sat: the Kuznetsovs, don't let Varya go alone. Sun: Nina (pie, NOT cabbage, cabbage done already). Agafya: Tuesdays, NO ARGUING. Remember: the fl…” The rest is torn off.",
  stamp="e_ledger")
B(A, 6, "1,2", "", "letter", "Зинаида Павловна, магазин", "Zinaida Pavlovna, the shop",
  "Зинаида Павловна признаётся: подарки на крыльце — от всей Липовки.",
  "Zinaida Pavlovna owns up: the porch gifts are from all of Lipovka.",
  "Ну, раз уж вы нашли страничку… Это я. То есть мы все. Когда Антонина Гавриловна уезжала, зашла ко мне в магазин и сказала: «Первая зима на маршруте самая тяжкая. Приглядите». Ну я и завела тетрадку: кто в какой день. Желающих оказалось больше, чем дней в неделе, Агафья Петровна даже обиделась, что ей только вторник. Варежки, кстати, её: левая длиннее, потому что считала петли и заговорилась. Полотенце — Нинино, она его ищет, верните. Чай вот от меня. И не благодарите никого, а то все придут благодарить обратно. Зинаида П.",
  "Well, since you've found the page… It's me. That is, all of us. When Antonina Gavrilovna was leaving, she came into the shop and said, “The first winter on the round is the hardest. Keep an eye out.” So I started a notebook: who does which day. There were more volunteers than days in the week; Agafya Petrovna was even offended she only got Tuesdays. The mittens are hers, by the way: the left one's longer because she got chatting and lost count. The towel is Nina's, she's looking for it, give it back. The tea is from me. And don't go thanking anyone, or they'll all come round to thank you back. Zinaida P.",
  gift="e_zina_tea", sets="me.winter1")

# ================================================================ me_spring1: a bottle in the flood
A = "me_spring1"
B(A, 3, "4", "", "letter", "Бутылка у мостков", "A bottle by the landing stage",
  "Паводок вынес к мосткам бутылку с запиской 1979 года.",
  "The flood washed up a bottle with a note from 1979 by the landing stage.",
  "(Зелёная бутылка из-под лимонада, горлышко залито сургучом. Внутри — листок из тетради, совсем сухой.) Тому, кто найдёт! Это научный опыт. Мы, 4 класс Липовской школы, бросили 12 бутылок в Липку в паводок 14 апреля 1979 года. Сообщите, пожалуйста, где и когда вы нашли эту бутылку. Можно хоть в Каспийском море. Ответ пишите: Липовка, школа, Николаю Семёновичу. Заранее спасибо! Илья Ш., 4 кл.",
  "(A green lemonade bottle, the neck sealed with wax. Inside, a sheet from an exercise book, perfectly dry.) To whoever finds this! This is a scientific experiment. We, Year 4 of Lipovka school, threw 12 bottles into the Lipka in the flood of 14 April 1979. Please let us know where and when you found this bottle. Even if it's in the Caspian Sea. Write to: Lipovka, the school, Nikolai Semyonovich. Thank you in advance! Ilya Sh., Year 4",
  stamp="e_flood")
B(A, 4, "4,5", "", "letter", "Николай Семёнович Лебедев", "Nikolai Semyonovich Lebedev",
  "Учитель узнал свою бутылку: «Проплыла триста метров за сорок семь лет».",
  "The teacher knows the bottle: 300 metres in forty-seven years.",
  "Здравствуйте! Вы не представляете, что вы мне принесли. Двенадцать бутылок, апрель семьдесят девятого, мой первый «опыт по гидродинамике». Тогда нашлись три: одну выловили в Городке, вторую паромщик, а третья в восьмидесятом году написала нам с Волги — весь класс неделю ходил героями. Ваша — четвёртая. Проплыла триста метров за сорок семь лет. Где же она была всё это время? А Илья Ш. — тот самый Илья, что теперь на обсерватории звёзды считает. Я ему напишу. Н. С. Лебедев",
  "Hello! You can't imagine what you've brought me. Twelve bottles, April seventy-nine, my first “experiment in hydrodynamics”. Three were found back then: one fished out at Gorodok, one by the ferryman, and the third wrote to us from the Volga in 1980 — the whole class walked about like heroes for a week. Yours is the fourth. It travelled three hundred metres in forty-seven years. Where has it been all this time? And Ilya Sh. is that very Ilya who now counts stars at the observatory. I'll write to him. N. S. Lebedev")
B(A, 5, "4,5", "", "letter", "Фёдор Ильич, мельница", "Fyodor Ilyich, the mill",
  "Мельник знает, где сорок семь лет пряталась бутылка.",
  "The miller knows where the bottle hid for forty-seven years.",
  "Здравствуйте. Николай Семёнович рассказал мне про бутылку. Так я вам скажу, где она была. У меня под мельницей, в старом обводном лотке. Его заколотили ещё при отце, а этой весной вода поднялась выше досок, и всё, что там копилось, понесло: два ведра, калошу, бревно с гвоздями — и, выходит, вашу науку. Я ещё подумал: что-то звякнуло. Сорок семь лет у меня под полом опыт шёл, а я и не знал. Ф. И. Жуков",
  "Hello. Nikolai Semyonovich told me about the bottle. Well, I can tell you where it was. Under my mill, in the old bypass channel. It was boarded up in my father's day, and this spring the water rose above the boards and carried off everything that had collected there: two buckets, a galosh, a log full of nails — and, it seems, your science. I did think I heard something clink. Forty-seven years an experiment was running under my floor, and I never knew. F. I. Zhukov")
B(A, 5, "4,5", "", "telegram", "Илья, обсерватория", "Ilya, the observatory",
  "Телеграмма от астронома Ильи: «Бутылка моя».",
  "A telegram from Ilya the astronomer: “The bottle is mine.”",
  "ЛИПОВКА ПОЧТА ПОЧТАЛЬОНУ ТЧК БУТЫЛКА МОЯ ТЧК ТРИСТА МЕТРОВ ЗА СОРОК СЕМЬ ЛЕТ ЭТО ШЕСТЬ МЕТРОВ В ГОД ТЧК БЫСТРЕЕ МАТЕРИКОВ МЕДЛЕННЕЕ УЛИТКИ ТЧК ПЕРЕДАЙТЕ НИКОЛАЮ СЕМЁНОВИЧУ ОПЫТ СЧИТАЮ УДАЧНЫМ ТЧК ВЫВОД ТЧК НАУКА ВСЕГДА ДОПЛЫВАЕТ ТЧК СПАСИБО ВАМ ИЛЬЯ",
  "LIPOVKA POST FOR THE POSTMAN STOP THE BOTTLE IS MINE STOP THREE HUNDRED METRES IN FORTY SEVEN YEARS IS SIX METRES A YEAR STOP FASTER THAN CONTINENTS SLOWER THAN A SNAIL STOP TELL NIKOLAI SEMYONOVICH I CONSIDER THE EXPERIMENT A SUCCESS STOP CONCLUSION STOP SCIENCE ALWAYS GETS THERE STOP THANK YOU ILYA",
  stamp="e_obs_telegram")
B(A, 5, "4,5", "", "letter", "Николай Семёнович Лебедев", "Nikolai Semyonovich Lebedev",
  "Учитель прислал фото класса 1979 года: опыт продолжается.",
  "The teacher sends a 1979 class photo: the experiment goes on.",
  "Нашёл в шкафу фотографию того самого класса. Вот они, на мостках, держат бутылки, как букеты. Илья — второй слева, шапка набекрень. Оставьте карточку у себя: без вас это была бы просто бутылка. Мы с нынешним четвёртым классом решили: опыт продолжается. В субботу бросаем двенадцать новых. Обратный адрес на записках — ваш: Липовка, почта. Вы ведь не против? Н. С.",
  "I found a photograph of that very class in my cupboard. There they are on the landing stage, holding their bottles like bunches of flowers. Ilya is second from the left, cap askew. Keep the picture: without you it would have been just a bottle. The current Year 4 and I have decided the experiment goes on. On Saturday we launch twelve new ones. The return address on the notes is yours: Lipovka, the post office. You don't mind, do you? N. S.",
  gift="e_class_1979")
B(A, 6, "4,5", "", "letter", "Таисия Ивановна, паром в Борках", "Taisia Ivanovna, Borki ferry",
  "Паромщица из Борок нашла новую бутылку: сорок вёрст за девятнадцать дней.",
  "The Borki ferrywoman found a new bottle: forty versts in nineteen days.",
  "Здравствуйте, почта Липовки! Пишет Таисия Ивановна, паромщица из Борок, это ниже по Липке, сорок вёрст. Выловила вчера у причала бутылку с запиской: «4 класс, Липовка, опыт». Докладываю, как просили: нашла в семь утра, бутылка целая, записка сухая. Сорок вёрст за девятнадцать дней — передайте ребятам, хорошая скорость, не то что у некоторых. Я и сама в детстве бросала такие, да мне никто не ответил. Так что вы им ответьте обязательно. Т. И.",
  "Hello, Lipovka post! This is Taisia Ivanovna, the ferrywoman at Borki, forty versts down the Lipka. Yesterday by the jetty I fished out a bottle with a note: “Year 4, Lipovka, experiment.” Reporting as requested: found at seven in the morning, bottle intact, note dry. Forty versts in nineteen days — tell the children that's a good speed, not like some. I threw bottles like that myself as a girl, but nobody ever wrote back. So be sure you write back to them. T. I.",
  sets="me.spring1")

# ================================================================ me_summer1: pigeon post (Petya)
A = "me_summer1"
PG_RU, PG_EN = "Голубиная почта", "Pigeon post"
B(A, 3, "6", "", "letter", "Голубь (записка на лапке)", "A pigeon (a note on its leg)",
  "На крыльцо почты сел голубь с запиской на лапке.",
  "A pigeon landed on the post office porch with a note on its leg.",
  "(Сизый голубь с белым хвостом сел на крыльцо и не улетает, пока не снимешь с лапки трубочку. Внутри — бумажка, свёрнутая в десять раз.) ГОЛУБИНАЯ ПОЧТА. ДОСТАВКА № 1. Вылет 8:02. Проверка связи. Если долетело — ответ привяжите к лапке. Голубя зовут Гагарин. Кормить не надо, он на диете. Отправитель засекречен.",
  "(A grey pigeon with a white tail landed on the porch and won't fly off until you take the little tube from its leg. Inside, a scrap of paper folded ten times.) PIGEON POST. DELIVERY No. 1. Take-off 8:02. Testing the line. If this arrived, tie your answer to its leg. The pigeon is called Gagarin. Don't feed him, he's on a diet. Sender classified.",
  stamp="e_pigeon")
B(A, 5, "6,7", "", "letter", PG_RU, PG_EN,
  "Голубиная почта вызывает вас на соревнование: кто быстрее?",
  "The pigeon post challenges you to a race: who's faster?",
  "ГОЛУБИНАЯ ПОЧТА. ДОСТАВКА № 4. Вылет 7:40, прибыл (по вашему ответу) 7:43. Три минуты! А пешком от мельн… ой, от нас до вас двадцать минут. Значит, голубиная почта быстрее обычной. Предлагаю соревнование: в субботу я посылаю Гагарина, а вы несёте такое же письмо ногами. Кто проиграет, тот… не знаю. Придумайте сами. Засекреченный.",
  "PIGEON POST. DELIVERY No. 4. Take-off 7:40, arrived (by your reply) 7:43. Three minutes! And on foot from the mi… oops, from us to you it's twenty minutes. So pigeon post is faster than ordinary post. I propose a race: on Saturday I send Gagarin and you carry the same letter on foot. Whoever loses has to… I don't know. You think of something. Classified.",
  stamp="e_takeoff")
B(A, 6, "6,7", "", "letter", PG_RU, PG_EN,
  "Голубь проиграл гонку на крыше клуба. Отправитель требует ничью.",
  "The pigeon lost the race on the club roof. The sender demands a draw.",
  "ГОЛУБИНАЯ ПОЧТА. ДОСТАВКА № 7. Нечестно!!! Гагарин сел на крышу клуба и сидел там полчаса, потому что там голубки. Поэтому ничья. Но Гагарин всё равно лучше, потому что он не ходит по гостям и не пьёт чай. А вы пили чай у Агафьи Петровны, я всё видел с крыши… то есть с высоты. И ещё вам дали пирожок. Засекреченный.",
  "PIGEON POST. DELIVERY No. 7. Not fair!!! Gagarin landed on the club roof and sat there for half an hour because there were lady pigeons. So it's a draw. But Gagarin is still better, because he doesn't go visiting and doesn't drink tea. And you had tea at Agafya Petrovna's, I saw everything from the roof… I mean from a height. And they gave you a pie, too. Classified.")
B(A, 7, "7", "", "letter", PG_RU, PG_EN,
  "Голубиную почту использует взрослый: просит повлиять на внука.",
  "A grown-up uses the pigeon post: please talk sense into a grandson.",
  "ГОЛУБИНАЯ ПОЧТА. ДОСТАВКА № 9. Пишет не голубь и не тот, кто обычно. Уважаемая почта, прошу повлиять. Внук третий день не слезает с крыши мельницы, мука у него во всех карманах, а на ужин он теперь отвечает: «Вылет в девятнадцать ноль-ноль». Если голубиная почта будет вас обижать — пишите, я с ней поговорю. Дед засекреченного.",
  "PIGEON POST. DELIVERY No. 9. This is not the pigeon writing, nor the usual sender. Dear post office, I ask you to have a word. For three days my grandson hasn't come down off the mill roof, there's flour in all his pockets, and when called to supper he answers, “Take-off at nineteen hundred.” If the pigeon post gives you any trouble, write to me and I'll speak to it. The classified one's grandad.")
B(A, 7, "7,8", "", "letter", "Петя Жуков, мельница", "Petya Zhukov, the mill",
  "Отправитель раскрыт: это Петя, внук мельника, и его голубь Гагарин.",
  "The sender revealed: Petya, the miller's grandson, and Gagarin his pigeon.",
  "ГОЛУБИНАЯ ПОЧТА. ДОСТАВКА № 12. Ладно, раскрываюсь, дед всё равно всё выдал. Я Петя Жуков, мне десять лет, я из Вологды, а летом живу на мельнице. Гагарина мне подарил сосед дядя Слава, он голубятник, и сказал: голубь летит туда, где его кормят. Поэтому я в первые дни кормил его пшеном у вас на крыльце, пока вы были на маршруте. Чтобы он запомнил дорогу. Извините за пшено. И за перья. Петя",
  "PIGEON POST. DELIVERY No. 12. All right, I'm revealing myself, Grandad gave everything away anyway. I'm Petya Zhukov, I'm ten, I'm from Vologda, and in summer I live at the mill. Our neighbour Uncle Slava gave me Gagarin, he keeps pigeons, and he said a pigeon flies to where it gets fed. So in the first days I fed him millet on your porch while you were out on the round. So he'd learn the way. Sorry about the millet. And the feathers. Petya")
B(A, 7, "8", "", "letter", "Петя и Гагарин", "Petya and Gagarin",
  "Голубиная почта закрывается до следующего лета. Петя дарит свистульку.",
  "The pigeon post closes until next summer. Petya sends a whistle.",
  "ГОЛУБИНАЯ ПОЧТА. ДОСТАВКА № 15, последняя. Завтра мама увозит меня в Вологду, а Гагарин поедет со мной в корзинке. Он будет скучать по вашему крыльцу, это точно: вчера он просидел там до вечера и вас ждал. Дарю вам свистульку-голубя, я её купил на ярмарке на свои. Если свистнете — Гагарин, может, услышит даже в Вологде. Голубиная почта закрывается до следующего лета. Петя и Гагарин.",
  "PIGEON POST. DELIVERY No. 15, the last. Tomorrow Mum takes me back to Vologda, and Gagarin is coming with me in a basket. He'll miss your porch, that's for sure: yesterday he sat there till evening waiting for you. I'm giving you a pigeon whistle, I bought it at the fair with my own money. If you blow it, maybe Gagarin will hear it even in Vologda. The pigeon post is closed until next summer. Petya and Gagarin.",
  gift="e_pigeon_whistle", sets="me.summer1")

# ================================================================ me_autumn2: the trunk in the attic (1958)
A = "me_autumn2"
KS_RU, KS_EN = "К. Лучинина, Ленинград, 1958", "K. Luchinina, Leningrad, 1958"
B(A, 3, "9", "me.autumn1", "letter", "Чердак почты, сундук", "The post office attic, a trunk",
  "Старый латунный ключ подошёл к сундуку на чердаке. Там — письма.",
  "The old brass key fits a trunk in the attic. Inside: letters.",
  "(Латунный ключ из районной посылки подошёл — к сундуку на чердаке, под связками старых газет. В сундуке чернильница-непроливайка, медный колокольчик, а под ними — пачка писем, перевязанная почтовым шпагатом. Сверху записка.) «Кто найдёт — не выбрасывайте. Это не казённое, это моё. Почтальон отделения Липовка И. Д. Дорофеев, октябрь 1959 г.» Все письма адресованы ему. Обратный адрес везде один: Ленинград, общежитие педагогического института, К. Лучининой.",
  "(The brass key from the district parcel fits — a trunk in the attic, under bundles of old newspapers. In the trunk: a spill-proof inkwell, a brass bell, and beneath them a bundle of letters tied with postal twine. On top, a note.) “Whoever finds this, don't throw it away. It isn't government property, it's mine. I. D. Dorofeyev, postman of the Lipovka office, October 1959.” All the letters are addressed to him. The return address is always the same: Leningrad, the teachers' institute hostel, K. Luchinina.")
B(A, 6, "9,10,11", "me.autumn1", "letter", KS_RU, KS_EN,
  "Первое письмо из сундука: Ксеня из Озёрок пишет почтальону.",
  "The first letter from the trunk: Ksenya from Ozyorki writes to the postman.",
  "«Здравствуйте, Иван Дорофеевич! Вы, наверное, удивитесь. Это Ксеня из Озёрок — та, которой вы летом принесли вызов в институт и ждали у калитки, пока я прочитаю, а я ревела, и вы дали мне свой платок. Платок у меня, отдам, когда приеду. Ленинград огромный, а писем мне никто не пишет, кроме мамы. Можно, я буду писать вам? Вы ведь всё равно почтальон, вам письма носить не тяжело. К. Л., 2 сентября 1958 г.»",
  "“Dear Ivan Dorofeyevich! You'll probably be surprised. It's Ksenya from Ozyorki — the girl you brought the institute's acceptance to in the summer. You waited at the gate while I read it, and I cried, and you gave me your handkerchief. I still have it; I'll give it back when I come home. Leningrad is enormous, and nobody writes to me except Mum. May I write to you? You're a postman after all, letters aren't heavy for you to carry. K. L., 2 September 1958.”")
B(A, 7, "9,10,11", "me.autumn1", "letter", "К. Лучинина, Ленинград, 1959", "K. Luchinina, Leningrad, 1959",
  "Письмо 1959 года: сушёная липа в конверте и ленинградский дождь.",
  "A letter from 1959: dried linden in an envelope and Leningrad rain.",
  "«Иван Дорофеевич, вы опять прислали мне в конверте сушёную липу — вся комната пахнет Липовкой, девочки смеются. А я посылаю вам ленинградский дождь: вот, видите, буква расплылась. Вы спрашиваете, вернусь ли я учительствовать в район. Не знаю. Здесь Эрмитаж и Нева, а там — вы с вашей сумкой. Как это сравнивать? Никак нельзя сравнивать. Пишите чаще. Ваша К. 14 марта 1959 г.»",
  "“Ivan Dorofeyevich, you've sent me dried linden blossom in an envelope again — the whole room smells of Lipovka and the girls laugh at me. And I'm sending you Leningrad rain: look, there, that letter has run. You ask whether I'll come back to teach in the district. I don't know. Here there's the Hermitage and the Neva, and there — there's you with your bag. How can you compare them? You can't compare them at all. Write more often. Your K. 14 March 1959.”",
  stamp="e_stamp_1958")
B(A, 7, "9,10,11", "me.autumn1", "letter", "Софья Марковна, музей", "Sofia Markovna, the museum",
  "Музей в Городке знает про Ивана Дорофеевича. И про внучку Ксении.",
  "The museum knows of Ivan Dorofeyevich — and of Ksenya's granddaughter.",
  "Здравствуйте, коллега по почтовой истории — простите, но вы им теперь стали. Иван Дорофеевич Дорофеев служил почтальоном в Липовке с 1951 по 1989 год; у меня есть его фотография с велосипедом. Ксения Лучинина в 1960 году вышла замуж в Ленинграде и сорок лет учила детей литературе. Переписка их оборвалась летом 1959-го, почему — не знаю. Иван Дорофеевич так и не женился, зато вся округа звала его «наш Дорофеич». И вот что важно: у Ксении Андреевны есть внучка, Мария, она живёт в Петербурге. Адрес я нашла. Решать вам. С. М. Вайс",
  "Hello, my colleague in postal history — forgive me, but that's what you've become. Ivan Dorofeyevich Dorofeyev was the Lipovka postman from 1951 to 1989; I have a photograph of him with his bicycle. Ksenia Luchinina married in Leningrad in 1960 and taught children literature for forty years. Their letters broke off in the summer of 1959; I don't know why. Ivan Dorofeyevich never married, but the whole district called him “our Dorofeich”. And here is the important thing: Ksenia Andreyevna has a granddaughter, Maria, who lives in St Petersburg. I've found the address. It's up to you. S. M. Weiss")
B(A, 9, "9,10,11", "me.autumn1", "letter", "Мария, Санкт-Петербург", "Maria, St Petersburg",
  "Внучка Ксении нашла у бабушки жестяную коробку с письмами из Липовки.",
  "Ksenya's granddaughter found her grandmother's tin of letters from Lipovka.",
  "Здравствуйте! Ваше письмо я прочитала три раза, а потом полезла на антресоли. У бабушки была жестяная коробка из-под монпансье, трогать её нам не разрешали. В ней сорок одно письмо из Липовки, все подписаны «И. Д.», и мужской клетчатый платок. Когда я была маленькая, бабушка говорила: «Самые красивые письма на свете пишут деревенские почтальоны». Я думала, это она так, к слову. Теперь знаю, что не к слову. Можно, я приеду? Мария",
  "Hello! I read your letter three times and then climbed up to the top cupboard. My grandmother had a tin that once held fruit drops, and we were never allowed to touch it. Inside: forty-one letters from Lipovka, all signed “I. D.”, and a man's checked handkerchief. When I was little, Grandma used to say, “The most beautiful letters in the world are written by village postmen.” I thought it was just a saying. Now I know it wasn't. May I come and visit? Maria")
B(A, 8, "9,10,11", "me.autumn1", "letter", "Мария, Санкт-Петербург", "Maria, St Petersburg",
  "Мария прислала фото Ксении и последнее письмо Ивана Дорофеевича.",
  "Maria sends a photo of Ksenya and Ivan Dorofeyevich's last letter.",
  "Посылаю вам фотографию бабушки: 1959 год, Нева, она в берете и смеётся. И последнее письмо Ивана Дорофеевича, вот оно целиком: «Ксеня. Оставайтесь в Ленинграде. Там Нева и ваши будущие ученики, а Липовка никуда не денется, она вас подождёт в письмах. Я буду носить чужие и радоваться за вас. Платок не возвращайте. И. Д.» Бабушкина жизнь была очень счастливой, правда. А платок все эти годы лежал в коробке, выглаженный. Мария",
  "I'm sending you a photo of my grandmother: 1959, the Neva, she's in a beret and laughing. And Ivan Dorofeyevich's last letter, here it is in full: “Ksenya. Stay in Leningrad. There's the Neva and your future pupils there, and Lipovka isn't going anywhere; it will wait for you in letters. I'll carry other people's and be glad for you. Don't return the handkerchief. I. D.” Grandma's life was a very happy one, truly. And all those years the handkerchief lay in the tin, ironed. Maria",
  gift="e_ksenia_photo")
B(A, 8, "9,10,11", "me.autumn1", "letter", "Софья Марковна, музей", "Sofia Markovna, the museum",
  "В музее открылась витрина «Письма из Липовки»: обе пачки вместе.",
  "The museum opens a “Letters from Lipovka” case: both bundles together.",
  "Дорогие мои… простите, привычка. Вчера в музее открылась маленькая витрина «Письма из Липовки». Слева — письма Ксении из вашего сундука, справа — письма Ивана Дорофеевича из жестяной коробки. Шестьдесят семь лет они пролежали в разных городах, а теперь лежат в одной витрине, через стекло друг от друга. Мария приезжала, стояла долго, а потом сказала: «Ну вот. Договорили». Чернильницу Ивана Дорофеевича оставьте себе, она по праву ваша: маршрут-то тот же. С. М. Вайс",
  "My dears… forgive me, it's a habit. Yesterday the museum opened a small display case, “Letters from Lipovka”. On the left, Ksenya's letters from your trunk; on the right, Ivan Dorofeyevich's letters from the tin. For sixty-seven years they lay in different cities, and now they're in one case, a pane of glass apart. Maria came and stood there a long time, and then she said, “There. They've finished their conversation.” Keep Ivan Dorofeyevich's inkwell: it's yours by right, the round is the same. S. M. Weiss",
  stamp="e_showcase")

# ================================================================ me_winter2: weather reports in the door (the teacher)
A = "me_winter2"
WX_RU, WX_EN = "Сводка в дверной щели", "A report in the door crack"
B(A, 3, "12", "me.winter1", "letter", WX_RU, WX_EN,
  "В дверной щели — сводка погоды «для почтальона». Кто её пишет?",
  "In the door crack: a weather report “for the postman”. Who writes it?",
  "СВОДКА ДЛЯ ПОЧТАЛЬОНА. 6:00. Минус 19, ясно, ветер северо-западный, 3 м/с. Давление растёт. На маршруте: у моста гололёд, у фермы позёмка, у магазина Зинаида Павловна с новостями (задержка до 15 мин.). Рекомендация: шарф поверх воротника, а не под. (Почерк ровный, с наклоном, единицы измерения выписаны аккуратно. Подписи нет.)",
  "REPORT FOR THE POSTMAN. 6:00. Minus 19, clear, wind north-westerly, 3 m/s. Pressure rising. On the round: black ice by the bridge, drifting snow by the farm, Zinaida Pavlovna with news by the shop (delay up to 15 min). Advice: scarf over the collar, not under. (Neat, slanting handwriting, the units carefully written in. No signature.)")
B(A, 5, "12,1", "me.winter1", "letter", WX_RU, WX_EN,
  "Новая сводка: минус двадцать семь, и кто-то записывает, как вы одеты.",
  "A new report: minus twenty-seven, and someone notes what you're wearing.",
  "СВОДКА ДЛЯ ПОЧТАЛЬОНА. 6:00. Минус 27. Тихо. Дым из труб стоит столбом — к морозу дня на три. Видимость отличная, до водонапорной башни. Рекомендация: варежки двойные, пирог в сумку, на крыльце у Сорокиной подолгу не стоять — там сквозит. Замечание: вчера в 8:12 вы вышли без шапки. Записано.",
  "REPORT FOR THE POSTMAN. 6:00. Minus 27. Still. Chimney smoke standing straight up: frost for about three days. Visibility excellent, as far as the water tower. Advice: double mittens, a pie in the bag, don't linger on Sorokina's porch, it's draughty. Note: yesterday at 8:12 you went out without a hat. This has been recorded.",
  stamp="e_minus27")
B(A, 6, "12", "me.winter1", "letter", WX_RU, WX_EN,
  "Праздничная сводка: снег хлопьями, Орион над рекой и Сириус левее.",
  "A holiday report: big snowflakes, Orion over the river, Sirius to the left.",
  "СВОДКА ДЛЯ ПОЧТАЛЬОНА, ПРАЗДНИЧНАЯ. Минус 8, снег крупный, хлопьями — к тёплому году. В праздничную ночь ожидается: хлопушки над клубом, Дед Мороз у Кузнецовых (усы опять отклеятся), над рекой — Орион во всей красе, а левее и ниже — Сириус, ярче всех. Рекомендация: посмотрите вверх хотя бы раз. Небо бесплатное, его тоже доставляют каждый вечер. С наступающим.",
  "REPORT FOR THE POSTMAN, HOLIDAY EDITION. Minus 8, big flaky snow: a sign of a warm year. Expected on the festive night: crackers over the club, Ded Moroz at the Kuznetsovs' (his moustache will come unstuck again), Orion in all his glory over the river, and lower left, Sirius, the brightest of all. Advice: look up at least once. The sky is free; it gets delivered every evening too. Happy New Year.",
  stamp="e_orion")
B(A, 8, "1,2", "me.winter1", "letter", WX_RU, WX_EN,
  "Неизвестный синоптик отвечает на вопрос «Кто вы?». Почти отвечает.",
  "The unknown forecaster answers the question “Who are you?” Almost.",
  "СВОДКА ДЛЯ ПОЧТАЛЬОНА. 6:00. Минус 14, облачно, к обеду снег. Отвечаю на ваш вопрос, оставленный в щели: «Кто вы?» Ответ: метеослужба Липовки, внештатная. Барометр у неё 1961 года выпуска и ни разу не ошибся, в отличие от радио. Рекомендация: не дежурить в сенях в шесть утра. В сенях минус пять, а метеослужба всё равно ходит огородами.",
  "REPORT FOR THE POSTMAN. 6:00. Minus 14, overcast, snow by lunchtime. In answer to your question left in the crack, “Who are you?”: the Lipovka weather service, freelance. Its barometer was made in 1961 and has never once been wrong, unlike the radio. Advice: do not lie in wait in the porch at six in the morning. It's minus five in there, and the weather service comes the back way through the gardens anyway.")
B(A, 7, "1,2", "me.winter1", "letter", WX_RU, WX_EN,
  "Оттепель в сводке и подсказка в виде школьной задачи.",
  "A thaw in the report, and a clue set out like a school problem.",
  "СВОДКА ДЛЯ ПОЧТАЛЬОНА. 6:00. Оттепель, плюс один. С крыш капает, у колодца лужа под ледком — обходить слева. Рекомендация: валенки — нет, сапоги — да. Наблюдение: Сургуч в 6:05 вышел на крыльцо, понюхал воздух и вернулся в дом. Кот тоже синоптик, только не записывает. P.S. Дано: почерк с наклоном, барометр, Орион. Найти: метеослужбу. Решение — за вами.",
  "REPORT FOR THE POSTMAN. 6:00. Thaw, plus one. Dripping from the roofs, a puddle under thin ice by the well: go round on the left. Advice: felt boots, no; rubber boots, yes. Observation: at 6:05 Surguch came out onto the porch, sniffed the air and went back in. The cat is a forecaster too, he just doesn't keep notes. P.S. Given: slanting handwriting, a barometer, Orion. Find: the weather service. The solution is up to you.")
B(A, 7, "2", "me.winter1", "letter", "Николай Семёнович Лебедев", "Nikolai Semyonovich Lebedev",
  "Метеослужба раскрыта: сводки писал Николай Семёнович. Дарит градусник.",
  "The weather service unmasked: Nikolai Semyonovich. He sends a thermometer.",
  "Ну что ж, раскрываюсь, хотя вы, по-моему, давно всё поняли. Сорок лет я вёл дневник погоды — для уроков, для ребят, для себя. Школа теперь обходится без меня, а дневник без меня не может. Вот я и подумал: кому сводка нужнее всех? Тому, кто первым выходит из дома. Барометр не отдам, он мне как родня, а оконный градусник — держите. Повесьте с северной стороны, не на солнце, иначе он будет вам льстить. И не выходите больше без шапки: я всё записываю. Н. С. Лебедев",
  "Well then, I'll own up, though I think you worked it out long ago. For forty years I kept a weather diary — for lessons, for the children, for myself. The school manages without me now, but the diary can't. So I thought: who needs a forecast most? The one who leaves the house first. I won't part with the barometer, it's like family, but here's the window thermometer. Hang it on the north side, out of the sun, or it will flatter you. And don't go out without a hat again: I write everything down. N. S. Lebedev",
  gift="e_teacher_thermometer")

# ================================================================ me_spring2: seeds by post (Mikhalych)
A = "me_spring2"
WW_RU, WW_EN = "Доброжелатель", "A Well-Wisher"
B(A, 3, "3", "me.spring1", "letter", "Конверт без марки", "An envelope with no stamp",
  "Кто-то прислал семена и просит посеять их у почтового крыльца.",
  "Someone sends seeds and asks you to sow them by the post office porch.",
  "(Конверт без марки, внутри бумажный кулёчек с семенами, мелкими, как мак. Конверт почему-то пахнет воском.) Посейте у крыльца, с солнечной стороны. Когда снег сойдёт и земля станет как пирог — тёплая и рассыпчатая. Глубоко не закапывайте, им надо свет видеть. Доброжелатель.",
  "(An envelope with no stamp; inside, a paper twist of seeds as tiny as poppy seeds. The envelope, for some reason, smells of wax.) Sow these by the porch, on the sunny side. When the snow's gone and the earth is like a pie, warm and crumbly. Don't bury them deep, they need to see the light. A Well-Wisher.")
B(A, 8, "3,4", "me.spring1", "letter", WW_RU, WW_EN,
  "Второй кулёк от Доброжелателя: фацелия. Конверт снова пахнет воском.",
  "A second twist from the Well-Wisher: phacelia. Wax smell again.",
  "Это фацелия. Если пойдёте спрашивать у Зинаиды Павловны, что такое фацелия, — не надо, она потом всем расскажет, и пропадёт сюрприз. Сейте полосой вдоль забора, редко. Конверт пахнет воском — не обращайте внимания, это у меня руки такие. Доброжелатель.",
  "This is phacelia. If you're thinking of asking Zinaida Pavlovna what phacelia is — don't, she'll tell everyone and the surprise will be spoilt. Sow it in a strip along the fence, thinly. The envelope smells of wax: pay no attention, that's just my hands. A Well-Wisher.",
  stamp="e_phacelia")
B(A, 8, "4,5", "me.spring1", "letter", WW_RU, WW_EN,
  "Третий кулёк: донник и медуница — «для ранних». Для каких ранних?",
  "A third twist: melilot and lungwort, “for the early ones”. Which early ones?",
  "Третий кулёк — донник. Вырастет высокий, жёлтый, пахнет сеном. И медуница — это для ранних, у них тоже работа. Спросите: для каких ранних? Узнаете. Поливать вечером, когда солнце ушло: днём вода землю обжигает. Доброжелатель. P.S. Сургуча от грядки гоните, он её копает и думает, что это для него.",
  "The third twist is melilot. It'll grow tall and yellow and smell of hay. And lungwort, that's for the early ones; they have work to do too. You'll ask: which early ones? You'll find out. Water in the evening, once the sun's gone: in the daytime water scorches the soil. A Well-Wisher. P.S. Keep Surguch off the bed, he digs it up and thinks it's for him.")
B(A, 8, "4,5", "me.spring1", "letter", WW_RU, WW_EN,
  "Доброжелатель видел всходы через забор и шлёт белый клевер.",
  "The Well-Wisher saw the seedlings over the fence and sends white clover.",
  "Взошло? Я видел — взошло. Шёл мимо, смотрел через забор. Хорошо взошло, густо. Теперь главное — не полоть то, чего не знаете. Что не знаете, то, может, и есть самое нужное. Посылаю ещё клевер белый, на дорожку к калитке. Ходить по нему можно, он не обижается, только крепче становится. Д.",
  "Has it come up? I saw — it has. I was walking by and looked over the fence. Good and thick. Now the main thing is not to weed out what you don't recognise. What you don't recognise may be just what's needed most. Here's some white clover too, for the path to the gate. You can walk on it, it doesn't mind; it only grows stronger. W.")
B(A, 8, "5", "me.spring1", "letter", WW_RU, WW_EN,
  "Доброжелатель предупреждает: скоро у крыльца будут гости в полоску.",
  "The Well-Wisher warns: soon there'll be striped guests at the porch.",
  "Почти пора. Скоро у вашего крыльца будет столовая. Не пугайтесь гостей: они в полосатой форме, но по делу. Руками не машите, варенье на крыльце в полдень не ешьте. Они вежливые, если с ними вежливо. А если какая сядет на рукав — постойте, она посмотрит на вас и полетит дальше. Вы ей не интересны, ей интересна фацелия. Д.",
  "Nearly time. Soon there'll be a canteen by your porch. Don't be alarmed by the guests: they wear striped uniforms, but they're here on business. Don't wave your arms about, and don't eat jam on the porch at midday. They're polite if you're polite to them. And if one lands on your sleeve, just stand still: she'll take a look at you and fly on. It's not you she's interested in, it's the phacelia. W.",
  stamp="e_porch_bee")
B(A, 8, "5", "me.spring1", "parcel", "Пётр Михайлович, пасека", "Pyotr Mikhailovich, the apiary",
  "Доброжелатель — Михалыч: у почты теперь пчелиная столовая.",
  "The Well-Wisher is Mikhalych: the post office now runs a bee canteen.",
  "Ну, будет прятаться. Это я, Михалыч. От моей пасеки до вашей почты пчеле лететь через всю Липовку, а по пути, кроме Агафьиной сирени, есть нечего. Вот я и устроил у вашего крыльца столовую на полдороге. Вы для них теперь вроде почтового отделения: прилетели, заправились — и дальше с грузом. Тоже доставка, только сладкая. Свечку восковую посылаю, а с вашей фацелии будет первый мёд — обещаю, банка ваша. Пётр Михайлович, пасечник",
  "All right, no more hiding. It's me, Mikhalych. From my apiary to your post office a bee has to fly right across Lipovka, and on the way there's nothing to eat but Agafya's lilac. So I set up a halfway canteen by your porch. To them you're a kind of post office now: fly in, fill up, and off again with the load. Deliveries too, only sweet ones. Here's a beeswax candle, and the first honey from your phacelia will be yours, I promise you the jar. Pyotr Mikhailovich, beekeeper",
  gift="e_wax_candle")

# ================================================================ me_summer2: postcards down the Volga (Antonina)
A = "me_summer2"
B(A, 3, "6", "me.summer1", "postcard", "Открытка, Ярославль", "A postcard, Yaroslavl",
  "Открытка с Волги «Почтальону Липовки», без подписи. Почерк знакомый.",
  "An unsigned Volga postcard to the postman. The hand looks familiar.",
  "Почтальону Липовки. Ярославль. Волга здесь шире, чем всё, что вы видели, — шире нашей Липки раз в сорок. Пароход гудит так, что чай в стакане дрожит. Погода хорошая, ноги отдыхают, а голова — нет, голова всё думает: доставят ли эту открытку вовремя? (Без подписи. Почерк круглый, с завитушкой у «д» — где-то вы его уже видели.)",
  "To the Postman of Lipovka. Yaroslavl. The Volga here is wider than anything you've seen, forty times wider than our Lipka. The steamer hoots so loud the tea shakes in the glass. Fine weather; my feet are resting, but my head isn't: it keeps wondering whether this card will be delivered on time. (Unsigned. A round hand with a curl on the “d” — you've seen it somewhere before.)",
  stamp="e_volga")
B(A, 6, "6,7", "me.summer1", "postcard", "Открытка, Кострома", "A postcard, Kostroma",
  "Вторая открытка с Волги: полотенце с петухами и почта без кота.",
  "A second Volga card: a towel with cockerels and a post office with no cat.",
  "Почтальону Липовки. Кострома. Купила льняное полотенце с петухами — точно такое, как у одной нашей общей знакомой. Заходила на здешнюю почту: крыльцо высокое, весы новые, а кота нет. Непорядок. Как можно разбирать письма, если на них никто не спит?",
  "To the Postman of Lipovka. Kostroma. I bought a linen towel with cockerels on it, just like one belonging to a friend we have in common. Looked in at the post office here: a tall porch, new scales, and no cat. Not right at all. How can you sort letters if nobody's sleeping on them?")
B(A, 6, "7", "me.summer1", "postcard", "Открытка, Нижний Новгород", "A postcard, Nizhny Novgorod",
  "Третья открытка: огромная лестница и вопрос про блюдце с синей каёмкой.",
  "A third card: a huge staircase and a question about the blue-rimmed saucer.",
  "Почтальону Липовки. Нижний Новгород. Здесь лестница от Волги наверх, ступенек под шестьсот. Молодёжь пыхтит, а я поднялась и не запыхалась: тридцать один год на маршруте ногам даром не прошли. Как там блюдце с синей каёмкой? Не разбилось? Без него он есть не станет, помните.",
  "To the Postman of Lipovka. Nizhny Novgorod. There's a staircase here from the Volga to the top, nearly six hundred steps. The young ones puff and pant, but I climbed it without losing my breath: thirty-one years on the round weren't wasted on these legs. How's the saucer with the blue rim? Not broken? He won't eat without it, remember.")
B(A, 6, "7,8", "me.summer1", "postcard", "Открытка, Казань", "A postcard, Kazan",
  "Открытка из Казани: впервые в жизни отправлять, а не разносить.",
  "A card from Kazan: for the first time in her life, sending, not delivering.",
  "Почтальону Липовки. Казань. Ела чак-чак — он как наш мёд, только в узелках. Рецепт попрошу для Михалыча, пусть удивится. Пишу вам и понимаю: первый раз в жизни я открытки отправляю, а не разношу. Оказывается, это так же приятно. Даже приятнее: не надо думать, кусается ли у адресата собака.",
  "To the Postman of Lipovka. Kazan. I ate chak-chak; it's like our honey, only tied in knots. I'll ask for the recipe for Mikhalych, let him be surprised. Writing to you, I realise: for the first time in my life I'm sending postcards instead of delivering them. It turns out to be just as nice. Nicer, even: no need to wonder whether the addressee's dog bites.")
B(A, 6, "8", "me.summer1", "postcard", "Открытка, Астрахань", "A postcard, Astrakhan",
  "Последняя открытка с Волги подписана: «А. Г.»",
  "The last Volga postcard is signed: “A. G.”",
  "Почтальону Липовки. Астрахань, конец пути. Дальше Волга уходит в море, а мне пора домой. Знаете, что я поняла за этот месяц? Почтальон — это человек, которого всегда кто-то ждёт. А пенсионер — это человек, который сам всех ждёт. Так вот: я решила не быть пенсионером. Ждите. А. Г.",
  "To the Postman of Lipovka. Astrakhan, the end of the line. From here the Volga runs into the sea, and it's time I went home. Do you know what I've understood this month? A postman is someone people are always waiting for. A pensioner is someone who does all the waiting. Well then: I've decided not to be a pensioner. Expect me. A. G.",
  stamp="e_astrakhan")
B(A, 6, "8", "me.summer1", "letter", "Антонина Гавриловна, Городок", "Antonina Gavrilovna, Gorodok",
  "Открытки с Волги слала Антонина Гавриловна. Приедет в сентябре.",
  "The Volga cards were from Antonina Gavrilovna. She'll visit in September.",
  "Ну, вы, конечно, сразу поняли — по блюдцу. Это я. Сын подарил мне на юбилей путёвку на теплоход: «Мама, ты всю жизнь носила чужие открытки, поезди теперь сама». Вот я и поездила. А писать решила вам, потому что Липовке я отслужила, а вы теперь и есть Липовка. Последнюю открытку, с теплоходом, посылаю в конверте — пусть у вас висит. Приеду в сентябре, на один день. Ставьте зелёный чайник. На малый огонь, помните? Ваша А. Г.",
  "Well, of course you guessed straight away, from the saucer. It's me. For my birthday my son gave me a river cruise: “Mum, all your life you've carried other people's postcards, now go and travel yourself.” So I did. And I decided to write to you, because I've done my service to Lipovka, and now you are Lipovka. Here's the last card, the one with the steamer, in an envelope; put it up on your wall. I'll come in September for a day. Put the green kettle on. On a low flame, remember? Yours, A. G.",
  gift="e_volga_card")

# ================================================================ me_penpal: Galina from Verkhnie Klyuchi
A = "me_penpal"
GA_RU, GA_EN = "Галина Ершова, Верхние Ключи", "Galina Yershova, Verkhnie Klyuchi"
B(A, 21, "", "", "letter", GA_RU, GA_EN,
  "Письмо с Урала: почтальон из Верхних Ключей предлагает переписку.",
  "A letter from the Urals: a village postwoman wants to correspond.",
  "Здравствуйте, коллега из Липовки! Пишет вам Галина Ершова, почтальон села Верхние Ключи — это Урал, река Чусовая. В нашей газете «Связист» в рубрике «Новости участков» было две строчки: в Липовку назначен новый почтальон, почта там с синей крышей и котом. А у нас крыша зелёная и собака. Вот я и подумала: все пишут всем, а почтальонам никто. Давайте писать друг другу — от сельской почты к сельской. Про маршруты, про погоду, про что угодно. Если неохота — не отвечайте, я не обижусь. Ну, обижусь немножко. Галина",
  "Hello, colleague in Lipovka! This is Galina Yershova, the postwoman of the village of Verkhnie Klyuchi — that's the Urals, on the Chusovaya river. In our trade paper, The Signalman, under “News from the Rounds”, there were two lines: a new postman has been appointed to Lipovka, where the post office has a blue roof and a cat. Ours has a green roof and a dog. So I thought: everyone writes to everyone, but nobody writes to postmen. Let's write to each other, from one village post to another. About rounds, weather, anything. If you don't feel like it, don't answer, I won't be offended. Well, only a little. Galina",
  stamp="e_ural")
B(A, 18, "", "", "letter", GA_RU, GA_EN,
  "Галина рассказывает про свою собаку Пальму и свой маршрут.",
  "Galina tells you about her dog Palma and her round.",
  "Ответ ваш получила и прочитала вслух Пальме. Пальма — моя собака: рыжая, вислоухая, ходит со мной по участку с четырнадцатого года и знает, кому газета, а кому пенсия. Где пенсия — там она садится и ждёт, потому что там дают сушку. Маршрут у меня четырнадцать километров: село, потом лесом до Ключиков, потом через брод на Заимку, где три дома и бабушка Шура с козой. Летом на велосипеде «Урал», зимой на лыжах. А у вас сколько? И как ваш кот относится к собакам? Галина",
  "I got your answer and read it aloud to Palma. Palma's my dog: ginger, floppy-eared, she's walked the round with me since 2014 and knows who gets a newspaper and who gets a pension. Where there's a pension she sits down and waits, because that's where they give her a biscuit. My round is fourteen kilometres: the village, then through the woods to Klyuchiki, then across the ford to Zaimka, where there are three houses and Granny Shura with her goat. In summer on a Ural bicycle, in winter on skis. How long is yours? And how does your cat feel about dogs? Galina",
  stamp="e_palma")
B(A, 25, "12,1,2", "", "letter", GA_RU, GA_EN,
  "У Галины минус тридцать восемь и рецепт пельменей со снегом.",
  "Minus thirty-eight at Galina's, and a pelmeni recipe with snow in it.",
  "У нас зима всерьёз. Вчера минус тридцать восемь, у меня ресницы склеились, пока дошла до Заимки. Сумку в такую погоду держу под тулупом, а то газеты ломаются, как вафли. Пальма ходит в попоне, которую бабушка Шура сшила ей из старого пальто, — вид у неё как у генерала. Посылаю рецепт наших пельменей: фарш из трёх мяс, лук не крутить, а рубить, и щепотку снега в фарш — для сочности, честное слово. Лепите всей деревней, так быстрее. Как у вас, метёт? Галина",
  "Winter's serious here. Yesterday it was minus thirty-eight; my eyelashes froze together on the way to Zaimka. In weather like that I keep the bag under my sheepskin, or the newspapers snap like wafers. Palma wears a dog coat Granny Shura made her out of an old overcoat; she looks like a general. Here's the recipe for our pelmeni: three kinds of meat, the onion chopped not minced, and a pinch of snow in the filling for juiciness, honestly. Make them with the whole village, it's quicker. How about you, is it blowing a blizzard? Galina",
  stamp="e_minus38")
B(A, 20, "1,2,3", "", "letter", GA_RU, GA_EN,
  "Обмен марками: Галина шлёт камни Урала и паровозы.",
  "A stamp swap: Galina sends Ural gemstones and steam engines.",
  "Вспомнила: вы писали, что собираете марки с писем. А мой муж Гена полжизни их собирал, а потом бросил, альбомы на антресолях. Я их сняла и три вечера разбирала. Посылаю вам дубли: камни Урала — малахит, яшма, аметист, они у нас тут как дома. И пару с паровозами: Гена сказал, у вас там «Кукушка» ходит, пусть будет ей компания. Если у вас есть лишние с котами — шлите, у меня внучка Настя по котам с ума сходит. Галина",
  "I remembered you wrote that you collect stamps off letters. Well, my husband Gena collected them for half his life and then gave up; the albums are on top of the wardrobe. I got them down and spent three evenings sorting. Here are the duplicates: Ural stones — malachite, jasper, amethyst, they're at home here. And a couple with steam engines: Gena says you have a little train, the Cuckoo, so it can have some company. If you have spare ones with cats, send them; my granddaughter Nastya is mad about cats. Galina",
  stamp="e_malachite")
B(A, 25, "4,5", "", "letter", GA_RU, GA_EN,
  "Половодье на Чусовой: пенсию возили на лодке. Пальма ждёт щенков.",
  "Flood on the Chusovaya: the pension went by boat. Palma expects puppies.",
  "Половодье у нас! Чусовая вышла из берегов, брод на Заимку стал морем. Бабушке Шуре пенсию я везла на лодке: Гена грёб, а Пальма сидела на носу, как капитан. Шура вышла на крыльцо в сапогах и говорит: «Почта приплыла!» Расписалась в ведомости прямо в лодке. И новость: Пальма ждёт щенков. От кого — не говорит. Подозревают Тузика с лесопилки, но у него алиби. Галина",
  "We've got the spring flood! The Chusovaya's burst its banks and the ford to Zaimka is a sea. I took Granny Shura her pension by boat: Gena rowed and Palma sat in the bow like a captain. Shura came out onto her porch in her boots and said, “The post has sailed in!” She signed the register right there in the boat. And news: Palma is expecting puppies. She won't say who the father is. Suspicion falls on Tuzik from the sawmill, but he has an alibi. Galina",
  stamp="e_mail_boat")
B(A, 20, "5,6", "", "parcel", GA_RU, GA_EN,
  "Пятеро щенков, рассада на почтовом окне и уральский иван-чай.",
  "Five puppies, seedlings on the post office window, and Ural fireweed tea.",
  "Щенков пятеро! Трое рыжие, в маму, двое пятнистые — так что с алиби Тузика всё ясно. Разобрали по дворам за неделю: почтальону раздавать щенков легко, я же знаю, кто без собаки скучает. А у меня на окнах рассада, на всех подоконниках, даже на почтовом, так что посетители расписываются в квитанциях между помидорами. Посылаю наш иван-чай: сама собирала в прошлом июле, сама сушила. Заваривайте в вашем зелёном чайнике, в горошек. Галина",
  "Five puppies! Three ginger like their mum and two spotted, so that settles Tuzik's alibi. They all went to homes within a week: it's easy for a postwoman to give away puppies, I know who's lonely without a dog. And my windows are full of seedlings, every sill, even at the post office, so customers sign their receipts between the tomatoes. Here's our fireweed tea: I picked it myself last July and dried it myself. Brew it in your green spotted kettle. Galina",
  gift="e_ivan_tea")
B(A, 25, "7,8", "", "letter", GA_RU, GA_EN,
  "Сенокос в Ключах. Внучка Настя носит почтовую сумку.",
  "Haymaking in Klyuchi. Granddaughter Nastya carries the post bag.",
  "Сенокос. Гена косит, я после маршрута ворошу, а Настя приехала на каникулы и ходит со мной по участку — носит мою сумку через плечо, гордая. В Ключиках бабки суют ей конфеты, а она серьёзно: «Не положено, я на службе». Вся в меня. Пальма от счастья помолодела. Земляника отошла, черника пошла. Рецепт варенья по-ключевски: ягоду не мыть, а продувать, сахару поровну и варить три раза по пять минут, остужая. Тогда ягодка целая. Галина",
  "Haymaking. Gena mows, I turn the hay after my round, and Nastya's come for the holidays and walks the round with me, carrying my bag over her shoulder, very proud. In Klyuchiki the old ladies push sweets at her and she says, very serious, “Not allowed, I'm on duty.” Takes after me. Palma's grown young again with happiness. The wild strawberries are over, the bilberries have started. Jam the Klyuchi way: don't wash the berries, blow on them; equal sugar; boil three times for five minutes, cooling in between. Then each berry stays whole. Galina")
B(A, 20, "8,9", "", "letter", GA_RU, GA_EN,
  "Бессонная ночь: гроза, Пальма убежала, Галина пишет вам при керосинке.",
  "A sleepless night: a storm, Palma ran off, Galina writes to you by oil lamp.",
  "Пишу ночью, в три часа. Не спится: гроза была страшная, Пальма испугалась грома и убежала, я до полуночи звала её по огородам с фонарём. Не нашла. Сижу теперь на крыльце, жду, пишу вам при керосинке — свет, конечно, выбило. И думаю: мы с вами ни разу не виделись, а вы первое, кому мне захотелось это рассказать. Странное дело — письма. …Пять утра. Пришла! Мокрая, в репьях и ужасно довольная, а в зубах чья-то рукавица. Всё. Спать. Галина",
  "Writing at three in the morning. I can't sleep: there was a terrible storm, Palma was frightened by the thunder and ran off, and I was calling her round the gardens with a torch till midnight. Couldn't find her. Now I'm sitting on the porch, waiting, writing to you by the oil lamp, because of course the power's out. And I'm thinking: we've never once met, yet you're the first one I wanted to tell. Funny things, letters. …Five a.m. She's back! Soaked, full of burrs and terribly pleased with herself, with someone's mitten in her mouth. That's it. Bed. Galina",
  stamp="e_kerosene")
B(A, 25, "9,10", "", "parcel", GA_RU, GA_EN,
  "Грибной год на Урале: Галина шлёт баночку солёных рыжиков.",
  "A mushroom year in the Urals: Galina sends a jar of salted milk caps.",
  "Грибы! Старики говорят, таких лет не было с восемьдесят шестого. Иду по маршруту и всё время в кювет смотрю: рыжики, грузди, белые. Почту теперь ношу с корзиной: в сумке газеты, в корзине обед на зиму. Начальница в районе пошутила, что надо ввести в отчёт новую графу: «Доставлено писем — 40, найдено груздей — 112». Посылаю вам баночку солёных рыжиков. К ним нужна горячая картошка и чтобы никто не мешал. Галина",
  "Mushrooms! The old folk say there hasn't been a year like it since eighty-six. I walk my round and keep looking into the ditches: saffron milk caps, milk mushrooms, ceps. I carry the post with a basket now: newspapers in the bag, winter dinners in the basket. My boss in the district joked that the report needs a new column: “Letters delivered: 40. Milk mushrooms found: 112.” Here's a jar of salted milk caps for you. They want hot potatoes and nobody to disturb you. Galina",
  gift="e_ryzhiki")
B(A, 25, "10,11", "", "letter", GA_RU, GA_EN,
  "Год переписки: письма ваши уже не помещаются в коробку из-под валенок.",
  "A year of letters: yours no longer fit in the felt-boot box.",
  "Сегодня посчитала: мы пишем друг другу почти год. Письма ваши лежат у меня в коробке из-под валенок, и коробка уже не закрывается. Гена говорит, пора заводить вторую. У нас лёг снег, в октябре, как положено. Съездила последний раз на велосипеде до Заимки, с завтрашнего дня — лыжи. Скажите честно: как вы? Не устали? Первый год на участке самый трудный. Потом ноги привыкают, а голова — нет: каждое утро думает, а вдруг сегодня принесу кому хорошую новость. И ведь приносишь. Галина",
  "I counted today: we've been writing to each other for almost a year. Your letters are in a felt-boot box and the lid won't shut any more. Gena says it's time for a second box. Our snow has come, in October, as it should. I took the bicycle to Zaimka one last time; from tomorrow it's skis. Tell me honestly: how are you? Not worn out? The first year on a round is the hardest. Then your feet get used to it, but your head never does: every morning it thinks, maybe today I'll bring someone good news. And you know, you do. Galina")
B(A, 25, "12", "", "postcard", GA_RU, GA_EN,
  "Новогодняя открытка от Галины: ёлка на почте наряжена конвертами.",
  "A New Year card from Galina: the post office tree is decked with envelopes.",
  "С наступающим, коллега! Желаю вам в новом году лёгкой сумки, сухих ног, добрых собак и чтобы все адресаты были дома. У нас ёлку поставили прямо на почте, и Настя нарядила её конвертами — пустыми, но с марками, очень красиво. Пальма спит под ёлкой, как подарок. Ваша Галина и вся почта Верхних Ключей",
  "Happy New Year, colleague! For the year ahead I wish you a light bag, dry feet, kind dogs, and every addressee at home. We've put the tree up right in the post office and Nastya decorated it with envelopes — empty, but with stamps on, very pretty. Palma sleeps under it like a present. Your Galina, and the whole Verkhnie Klyuchi post office",
  gift="e_galina_newyear")
B(A, 25, "1,2", "", "parcel", GA_RU, GA_EN,
  "Галина — серебро на лыжных гонках связистов. И носки из козьей шерсти.",
  "Galina takes silver at the postal ski race. And sends goat-wool socks.",
  "Хвастаюсь: на районных лыжных соревнованиях связистов я заняла второе место в своей возрастной группе! Пять километров с почтовой сумкой через плечо (это для смеха, но сумку дали настоящую, с газетами). Грамоту повесила на почте над весами. А у вас лыжи есть? Если нет — приезжайте, у нас лишние. Носки посылаю из козьей шерсти, от Шуриной козы. Колются, зато в них хоть в сугроб. Галина",
  "Showing off: at the district postal workers' ski races I came second in my age group! Five kilometres with a post bag over my shoulder (that was for fun, but they gave us a real bag, with newspapers in it). I've hung the certificate in the post office above the scales. Do you have skis? If not, come here, we've spare ones. I'm sending you socks of goat wool, from Shura's goat. They prickle, but in them you could stand in a snowdrift. Galina",
  gift="e_goat_socks", stamp="e_ski_race")
B(A, 30, "3,4", "", "letter", GA_RU, GA_EN,
  "Галина решилась: в июле отпуск — к вам в Липовку!",
  "Galina has decided: her July holiday will be in Lipovka!",
  "Решилась! В отпуск в июле — к вам. Гене сказала, он засмеялся: «Почтальон в отпуск едет к почтальону. Профессиональная болезнь». Ну и пусть. Хочу посмотреть на ваш маршрут, на мельницу, на Сургуча, на зелёный чайник — на всё, про что вы писали. Ехать двое суток: автобус, потом поезд, потом ваш Городок. Это ничего, я в поезде вяжу. Скажите, что вам привезти с Урала? Только не пишите «ничего». Галина",
  "I've made up my mind! My July holiday — to you. I told Gena and he laughed: “A postwoman going on holiday to see a postman. Occupational disease.” Let him laugh. I want to see your round, the mill, Surguch, the green kettle, everything you've written about. Two days' journey: a bus, then the train, then your Gorodok. That's nothing, I knit on trains. Tell me, what should I bring you from the Urals? Only don't write “nothing”. Galina")
B(A, 25, "5,6", "", "letter", GA_RU, GA_EN,
  "Билеты куплены. Галина везёт пельмени и волнуется: какие вы?",
  "Tickets bought. Galina is bringing pelmeni and wonders what you're like.",
  "Вы написали «ничего не надо», я так и знала. Поэтому привезу всё: рыжики, иван-чай, пельмени в сумке-холодильнике (Гена говорит, не довезу, а я довезу) и камушек для девочки, которая писала вам тайные письма. Билеты взяла на середину июля. Сменщица Люба обещала разнести мою почту, Пальма остаётся на Гене. Сплю плохо, всё думаю: какие вы? Я вас по письмам вижу, а по письмам все хорошие. Галина",
  "You wrote “nothing, really”, I knew you would. So I'll bring everything: milk caps, fireweed tea, pelmeni in a cool bag (Gena says they won't survive the trip, but they will), and a pebble for the girl who wrote you secret letters. I've booked tickets for mid-July. Lyuba, my relief, has promised to do my round, and Gena's in charge of Palma. I'm sleeping badly, wondering what you're like. I can see you in your letters, but in letters everyone is lovely. Galina")
B(A, 20, "6,7", "", "letter", GA_RU, GA_EN,
  "Поездка отменяется: Ключи нельзя оставить без почты.",
  "The trip is off: Klyuchi can't be left without post.",
  "Неприятность. Любу, мою сменщицу, забрали в район на курсы на всё лето, а больше разносить некому. Ключики без почты — это как без воды: пенсии, лекарства из аптеки, газеты бабушке Шуре. Не могу я их бросить. Вы ведь меня понимаете, как никто. Билеты сдала. Поплакала немножко, Пальма меня утешала, лизала нос. Ничего. Не в этом году — так в следующем. Пельмени уже налепила, съели с Геной за ваше здоровье. Не обижайтесь. Галина",
  "Bad luck. Lyuba, my relief, has been sent to the district on a course for the whole summer, and there's nobody else to do the round. Klyuchiki without post is like being without water: pensions, the chemist's parcels, Granny Shura's papers. I can't leave them. You understand that better than anyone. I've returned the tickets. I cried a little; Palma comforted me and licked my nose. Never mind. If not this year, then next. I'd already made the pelmeni; Gena and I ate them to your health. Don't be cross. Galina")
B(A, 25, "7,8", "", "parcel", GA_RU, GA_EN,
  "Раз Галина не приехала, к вам приехал кусочек Урала — яшма с Чусовой.",
  "Instead of Galina, a piece of the Urals comes: Chusovaya jasper.",
  "Раз уж я не приехала, пусть к вам приедет кусочек Урала. Это яшма с Чусовой. Я её нашла у брода в свою первую осень на участке, и все эти годы она лежала у меня на почте на столе, прижимала квитанции. Теперь пусть прижимает ваши. Полейте её водой — увидите, какая она внутри красная, как закат над Ключиками. Не вздумайте отказываться. Галина",
  "Since I couldn't come, let a piece of the Urals come to you. This is jasper from the Chusovaya. I found it by the ford in my first autumn on the round, and all these years it's sat on my desk at the post office holding down the receipts. Now let it hold down yours. Pour some water on it and you'll see how red it is inside, like sunset over Klyuchiki. Don't you dare refuse it. Galina",
  gift="e_jasper")
B(A, 30, "9,10", "", "letter", GA_RU, GA_EN,
  "Гена построил на почте крыльцо, и там теперь читают ваши письма.",
  "Gena built a porch at the post office, and now your letters get read there.",
  "Гена мой построил на почте новое крыльцо, с навесом и скамейкой: «Чтобы бабки, пока пенсию ждут, не на ступеньках сидели». Теперь у нас на крыльце клуб. Сидят, обсуждают — и знаете кого? Вас. Я ведь читаю им ваши письма, не целиком, только про Липовку. Бабушка Шура про вашу Агафью Петровну спрашивает: как вязание, не мёрзнет ли. Они теперь как будто знакомы. Вот так почта людей и сводит, через тысячу вёрст. Галина",
  "My Gena's built a new porch at the post office, with a roof and a bench: “So the old girls don't sit on the steps while they wait for their pensions.” Now our porch is a club. They sit and discuss things — and who do you think? You. I read them your letters, not all of them, just the bits about Lipovka. Granny Shura asks after your Agafya Petrovna: how's the knitting, does she keep warm. They're practically acquainted now. That's how the post brings people together, across a thousand versts. Galina")
B(A, 30, "11,12", "dog", "letter", GA_RU, GA_EN,
  "Пальма поседела и теперь провожает Галину только до брода.",
  "Palma has gone grey and now only walks Galina as far as the ford.",
  "Пальма у меня поседела, вся морда белая. Ей двенадцать. На Заимку теперь не ходит: провожает до брода, ложится у старой берёзы и ждёт, пока я вернусь. Иду обратно — а она уже хвостом стучит, издалека слышно. Гена говорит: «Пенсионерка». Нет, говорю, она теперь на полставки, как я скоро буду. А ваш Бублик ещё молодой. Ходите с ним больше, пока ноги у обоих бегут. Галина",
  "Palma's gone grey, her whole muzzle's white. She's twelve. She doesn't go to Zaimka any more: she sees me as far as the ford, lies down by the old birch and waits for me to come back. On my way home I can hear her tail thumping from far off. Gena says, “A pensioner.” No, I tell him, she's part-time now, like I'll be soon. Your Bublik is still young. Walk with him lots, while both your legs still run. Galina")
B(A, 25, "12,1", "", "letter", GA_RU, GA_EN,
  "Галина снова загадывает на Новый год одно и то же: приехать.",
  "For New Year Galina makes the same wish again: to come and visit.",
  "Опять Новый год, и опять я вам пишу. Знаете, что я загадала в прошлом году? Приехать. Не сбылось. В этом загадываю то же самое, только громче. У нас минус сорок один, занятия в школе отменили, а дети катаются с горки — какая учёба в такой мороз! Посылаю вам рисунок, Настя рисовала: это наша почта, это я, это Пальма, а это — вы. Почему вы с крыльями — не знаю. Настя говорит, почтальоны летают. Галина",
  "New Year again, and again I'm writing to you. Do you know what I wished for last year? To come. It didn't happen. This year I'm wishing the same thing, only louder. It's minus forty-one here, school's cancelled, and the children are sledging — who could study in a frost like this! I'm sending a picture Nastya drew: this is our post office, this is me, this is Palma, and this is you. Why you have wings I don't know. Nastya says postmen fly. Galina")
B(A, 30, "2,3", "", "letter", GA_RU, GA_EN,
  "Галина нашла свою первую ведомость и вспоминает, кого боялась.",
  "Galina found her very first register and remembers what she was afraid of.",
  "Разбирала старый шкаф и нашла свою первую ведомость, девяносто восьмой год. Мне было двадцать шесть, и я боялась всего: собак, гусей, начальницы и бабушки Шуры — она тогда была не бабушка, а грозная тётка с коромыслом. Теперь Шура мне как мама, а я никого не боюсь, кроме гусей. Гусей бояться — это не стыдно, это опыт. А вы кого в Липовке боялись поначалу? Признавайтесь. Галина",
  "I was clearing out an old cupboard and found my first register, from ninety-eight. I was twenty-six and afraid of everything: dogs, geese, my boss and Granny Shura, who back then wasn't a granny but a fearsome woman with a yoke and two buckets. Now Shura's like a mother to me and I'm not afraid of anyone except geese. Being afraid of geese is nothing to be ashamed of; it's experience. And who were you afraid of in Lipovka at first? Own up. Galina")
B(A, 30, "4,5", "", "letter", GA_RU, GA_EN,
  "В этот раз точно: Галина нашла замену и снова собирается в Липовку.",
  "This time for sure: Galina has found a stand-in and is coming to Lipovka.",
  "В этом году — точно. Слышите? ТОЧНО. Договорилась с племянницей Лидой: она студентка, летом свободна, участок знает с детства — я её в десять лет на раме велосипеда возила. Начальница подписала мне отпуск ещё в марте, пока не передумала. Гена тоже собрался, но потом сказал, что кто-то должен остаться с Пальмой и с огурцами. Так что еду одна, как настоящая путешественница. Галина",
  "This year, for certain. Do you hear? FOR CERTAIN. I've arranged it with my niece Lida: she's a student, free in summer, and she's known the round since she was little — I used to carry her on my bicycle crossbar when she was ten. My boss signed my leave back in March, before she could change her mind. Gena was going to come too, but then he said someone has to stay with Palma and the cucumbers. So I'm travelling alone, like a real explorer. Galina")
B(A, 30, "6,7", "", "telegram", "Телеграмма, Верхние Ключи", "Telegram, Verkhnie Klyuchi",
  "Телеграмма от Галины: «Выехала. Встречайте автобус из Городка».",
  "A telegram from Galina: “On my way. Meet the bus from Gorodok.”",
  "ЛИПОВКА ПОЧТА ТЧК ВЫЕХАЛА ТЧК ВСТРЕЧАЙТЕ ЧЕТВЕРГ АВТОБУС ИЗ ГОРОДКА ОДИННАДЦАТЬ ДВАДЦАТЬ ТЧК ПЕЛЬМЕНИ СО МНОЙ ТЧК ВОЛНУЮСЬ КАК В ПЕРВЫЙ ДЕНЬ НА УЧАСТКЕ ТЧК ГАЛИНА",
  "LIPOVKA POST STOP ON MY WAY STOP MEET THURSDAY BUS FROM GORODOK ELEVEN TWENTY STOP PELMENI WITH ME STOP NERVOUS AS MY FIRST DAY ON THE ROUND STOP GALINA",
  stamp="e_galina_telegram")
B(A, 10, "6,7,8", "dog", "letter", GA_RU, GA_EN,
  "Галина пишет из поезда: неделя в Липовке пролетела как один день.",
  "Galina writes from the train: the week in Lipovka flew by like a day.",
  "Пишу из поезда, трясёт, простите почерк. Неделя у вас пролетела как один день. Всё было как в письмах, только лучше: ходики отстают, Сургуч спал на моей сумке, Агафья Петровна связала мне носки за два вечера, мельник показал колесо, а Бублик проводил меня до самого автобуса и сидел, пока не уехали. Я прошла с вами весь маршрут и, знаете, ноги не устали совсем. Устало сердце — от радости. Галина",
  "Writing from the train, it's shaking, forgive the handwriting. The week with you flew by like a single day. Everything was as in your letters, only better: the clock's slow, Surguch slept on my bag, Agafya Petrovna knitted me socks in two evenings, the miller showed me his wheel, and Bublik walked me all the way to the bus and sat there until it left. I walked your whole round with you and, you know, my feet weren't tired at all. My heart was — with happiness. Galina")
B(A, 14, "7,8,9", "", "parcel", GA_RU, GA_EN,
  "Галина дома и шлёт фотографию: она и вы у почты Липовки.",
  "Galina is home and sends a photo: the two of you at the Lipovka post office.",
  "Дома. Пальма обиделась на меня на два дня, а потом простила и теперь ходит следом даже в огород, чтобы опять не уехала. Варя прислала фотографию, где мы с вами у вашей почты, под синей крышей, а на крыльце Сургуч делает вид, что он не с нами. Я заказала две копии. Одну — вам, вот она. Свою повесила над весами, рядом с лыжной грамотой. Бабки на крыльце разглядывают и говорят: «Похожи». На кого, на кого похожи — не говорят. Галина",
  "Home. Palma sulked at me for two days, then forgave me, and now she follows me even into the vegetable patch, in case I leave again. Varya sent the photo of the two of us at your post office under the blue roof, with Surguch on the porch pretending he's not with us. I had two copies made. One's for you, here it is. I've hung mine over the scales, next to the skiing certificate. The old girls on the porch study it and say, “Alike.” Alike to whom, they won't say. Galina",
  gift="e_visit_photo")
B(A, 30, "9,10", "", "parcel", GA_RU, GA_EN,
  "Посылка с Урала: кедровые шишки. Можно щёлкать, можно сажать.",
  "A parcel from the Urals: cedar cones. Crack them, or plant them.",
  "Рассказала всем Ключам про Липовку. Бабушка Шура спросила: «А кедр у них растёт?» Я говорю: нет. Она: «Так пошли им шишек, пусть посадят». Посылаю. Кедровые шишки с орехами, их можно щёлкать долгими вечерами, а можно посадить у почты. Гена говорит, через сорок лет будут свои шишки. Подождём? Мы с вами терпеливые, мы почтальоны: всё, что отправлено, рано или поздно доходит. Галина",
  "I told all of Klyuchi about Lipovka. Granny Shura asked, “Do they have cedars there?” I said no. She said, “Then send them some cones and let them plant them.” So here they are. Siberian cedar cones, full of nuts: you can crack them on long evenings, or plant them by the post office. Gena says in forty years you'll have your own cones. Shall we wait? We're patient, you and I, we're postmen: everything that's sent arrives sooner or later. Galina",
  gift="e_cedar_cones")
B(A, 30, "12", "", "letter", GA_RU, GA_EN,
  "Официальное приглашение от почты Верхних Ключей: теперь ваша очередь.",
  "An official invitation from the Verkhnie Klyuchi post office: your turn now.",
  "С Новым годом! И вот вам мой подарок — не в посылке, а в письме. Приглашение. Официальное: «Почта села Верхние Ключи приглашает почту деревни Липовка в гости, в любое время года, лучше летом, но можно и зимой — лыжи есть». Подписали: я, Гена, бабушка Шура, Настя и Пальма (лапой, в чернилах, полчаса потом отмывали). Теперь ваша очередь ехать. А не приедете — я снова сама приеду. Ваша Галина",
  "Happy New Year! And here's my present — not in a parcel but in a letter. An invitation. An official one: “The post office of the village of Verkhnie Klyuchi invites the post office of the village of Lipovka to visit, at any time of year, preferably summer, but winter will do — there are skis.” Signed by me, Gena, Granny Shura, Nastya and Palma (with her paw, in ink; it took half an hour to wash off). Now it's your turn to travel. And if you don't come, I'll come again myself. Your Galina",
  stamp="e_invitation")

# ================================================================ me_postmaster: milestone letters from the district
A = "me_postmaster"
B(A, 3, "", "km10", "letter", DISTRICT_RU, DISTRICT_EN,
  "Район отмечает ваши первые десять километров.",
  "The district takes note of your first ten kilometres.",
  "Почтальону отделения связи Липовка. По данным учёта, вами пройдены первые 10 (десять) километров по участку. Отмечаем добросовестное начало работы. Обувь берегите, новая по смете не раньше следующего квартала. Начальник РУС В. Т. Пестов. — От руки: Не подумайте, что мы тут считаем каждый ваш шаг. Считаем, конечно. Но с уважением.",
  "To the postman of the Lipovka post office. According to our records, you have covered your first 10 (ten) kilometres on the round. A conscientious start is hereby noted. Look after your shoes: new ones are not in the budget until next quarter. V. T. Pestov, Head of the District Post Office. By hand: Don't think we sit here counting your every step. We do, of course. But respectfully.")
B(A, 5, "", "km25", "letter", DISTRICT_RU, DISTRICT_EN,
  "Ответ района на незаданный вопрос о велосипеде.",
  "The district answers a question you never asked, about a bicycle.",
  "На ваш запрос о выделении велосипеда сообщаем… Запроса не было? Тогда отвечаем на будущий: велосипед по штату отделению Липовка не положен. Положены ноги. Пройдено 25 км, что соответствует норме и даже несколько её превышает. В. Т. Пестов. — От руки: Я в ваши годы ходил участок Сосновка, двенадцать вёрст в одну сторону, и велосипеда тоже не дали. Зато я знаю там каждую собаку по имени. Ноги — лучше.",
  "With regard to your request for a bicycle… There was no request? Then we are answering the future one: a bicycle is not on the Lipovka office's establishment. Legs are. 25 km covered, which meets the norm and even exceeds it somewhat. V. T. Pestov. By hand: At your age I walked the Sosnovka round, twelve versts each way, and they didn't give me a bicycle either. But I know every dog there by name. Legs are better.")
B(A, 10, "", "km50", "letter", DISTRICT_RU, DISTRICT_EN,
  "Мост в Заречье официально принят. В районе шутят, что это ваша заслуга.",
  "The Zarechye bridge is official. The district jokes it's your doing.",
  "Сообщаем: мост через р. Липку в Заречье принят комиссией районной администрации в эксплуатацию. Почтовое сообщение с Заречьем восстановлено официально. — Внутренняя приписка: комиссия приехала, когда по мосту уже месяц ходят, — порядок такой. У нас на узле шутят, что мост починили благодаря вам: вы его, мол, «выходили». Пусть шутят. Только ходите посерединке: перила покрашены, а прикручены пока не все. В. Т.",
  "We hereby inform you that the bridge over the Lipka to Zarechye has been accepted into service by the district administration's commission. Postal service to Zarechye is officially restored. Internal note: the commission arrived when people had been walking over the bridge for a month — that's procedure. At the office they joke that the bridge was mended thanks to you: you “walked it back to health”. Let them joke. Only keep to the middle: the railings are painted, but not all of them are bolted on yet. V. T.",
  stamp="e_bridge")
B(A, 10, "", "km100", "parcel", DISTRICT_RU, DISTRICT_EN,
  "За сто километров — новая сумка с латунным значком «Почта».",
  "For a hundred kilometres: a new bag with a brass Post badge.",
  "Распоряжение. В связи с прохождением 100 (ста) километров выдать почтальону отделения Липовка сумку почтовую новую, кожаную, с латунным значком «Почта». Старую сумку сдать на склад узла. В. Т. Пестов. — От руки: Старую не сдавайте. Антонина свою тоже не сдала, я в курсе. Повесьте на гвоздь у двери — пусть висит, ей заслуженно.",
  "Directive. In view of 100 (one hundred) kilometres covered, the postman of the Lipovka office is to be issued a new leather post bag with a brass Post badge. The old bag is to be returned to the district stores. V. T. Pestov. By hand: Don't return the old one. Antonina didn't return hers either, I know all about it. Hang it on the nail by the door. Let it hang there, it's earned it.",
  gift="e_bag_badge")
B(A, 20, "", "km250", "registered", DISTRICT_RU, DISTRICT_EN,
  "Почётная грамота района — с одной буквой, вписанной от руки.",
  "A district certificate of honour, with one letter written in by hand.",
  "ПОЧЁТНАЯ ГРАМОТА. Награждается почтальон отделения связи Липовка за образцовую доставку корреспонденции в любую погоду и 250 (двести пятьдесят) километров пройденного пути. Начальник РУС В. Т. Пестов. — От руки: Грамоту печатали три раза. Принтер на узле упорно писал «Лиловка». В третий раз я вписал букву ручкой. Не взыщите: зато видно, что от души.",
  "CERTIFICATE OF HONOUR. Awarded to the postman of the Lipovka post office for exemplary delivery of mail in all weathers and 250 (two hundred and fifty) kilometres of road walked. V. T. Pestov, Head of the District Post Office. By hand: We printed this three times. The office printer insisted on “Lilovka”. The third time I put the letter in with a pen. Don't hold it against us: at least you can see it's heartfelt.",
  gift="e_gramota")
B(A, 30, "", "km500", "parcel", DISTRICT_RU, DISTRICT_EN,
  "Пятьсот километров: вам выдана форменная фуражка «на вырост».",
  "Five hundred kilometres: you're issued a uniform cap “to grow into”.",
  "Распоряжение. За 500 (пятьсот) километров безупречной службы выдать почтальону отделения Липовка фуражку форменную, одну. Размер в личном деле не указан, поэтому выдаётся размер «на вырост», согласно положению. В. Т. Пестов. — От руки: Подложите под ободок газету. «Сельскую новь» — она толще. И фуражку носите по праздникам, а в будни шапку: мне про шапку уже докладывали.",
  "Directive. For 500 (five hundred) kilometres of impeccable service, the postman of the Lipovka office is to be issued one uniform cap. Size not stated in the personnel file, therefore issued in size “to grow into”, as per regulations. V. T. Pestov. By hand: Fold a newspaper under the band. The Village News, it's thicker. And wear the cap on holidays and a warm hat on weekdays: I've had reports about the hat.")
B(A, 60, "12", "", "postcard", DISTRICT_RU, DISTRICT_EN,
  "Новогоднее поздравление от узла связи и мандарины от водителя.",
  "New Year greetings from the district office, and tangerines from the driver.",
  "Коллектив районного узла связи поздравляет вас с Новым годом! Мы тут подсчитали: в этом году Липовка отправила писем больше, чем Городок за весь март. Липовка пишет! Желаем вам в новом году ровной дороги, тёплой погоды и чтобы ходики отставали не больше чем на семь минут. — Водитель Михаил просит передать, что мандарины в ящике от него, а не от узла. Узел мандарины не выдаёт.",
  "The staff of the District Post Office wish you a Happy New Year! We've done some counting: this year Lipovka sent more letters than Gorodok did in the whole of March. Lipovka writes! We wish you smooth roads in the new year, warm weather, and a clock no more than seven minutes slow. Mikhail the driver asks us to say that the tangerines in the box are from him, not from the office. The office does not issue tangerines.",
  stamp="e_district_ny")
B(A, 20, "", "km1000", "registered", DISTRICT_RU, DISTRICT_EN,
  "Вам присвоено звание «Почётный почтальон района». Значок из сейфа.",
  "You are made Honorary Postman of the District. The badge was in the safe.",
  "Решением районного узла связи почтальону отделения Липовка за 1000 (тысячу) километров пройденного пути присвоено звание «Почётный почтальон района». Значок прилагается. За всю историю узла этот значок получали четыре человека, последний — И. Д. Дорофеев, отделение Липовка, 1979 год. Вы пятый. В. Т. Пестов. — От руки: Я этот значок все годы, что здесь начальником, держал в сейфе. Думал, никому уже не понадобится. Ошибся. Рад, что ошибся.",
  "By decision of the District Post Office, the postman of the Lipovka office, for 1000 (one thousand) kilometres walked, is awarded the title of Honorary Postman of the District. Badge enclosed. In the whole history of the office only four people have received this badge, the last being I. D. Dorofeyev, Lipovka office, 1979. You are the fifth. V. T. Pestov. By hand: I've kept this badge in the safe all the years I've been in charge here. I thought nobody would ever need it again. I was wrong. Glad to be wrong.",
  gift="e_honour_badge", stamp="e_honour")
B(A, 30, "", "km2000", "parcel", DISTRICT_RU, DISTRICT_EN,
  "Из архива узла — карта почтовых маршрутов 1961 года.",
  "From the district archive: a 1961 map of the post rounds.",
  "Архив узла переезжает в новое здание, а одну вещь выбросить рука не поднялась. Карта почтовых маршрутов района, 1961 год, составлена И. Д. Дорофеевым от руки, цветными карандашами. Посмотрите: ваш маршрут — тот же, что шестьдесят с лишним лет назад, только мост новый. Две тысячи километров вы прошли. Это, между прочим, от Липовки до Урала, где ваша знакомая почтальонша. Да, на узле все знают: письма ведь через нас идут. В. Т. Пестов",
  "The office archive is moving to a new building, and there was one thing I couldn't bring myself to throw out. A map of the district's post rounds, 1961, drawn by hand in coloured pencils by I. D. Dorofeyev. Look: your round is the same as it was sixty-odd years ago, only the bridge is new. You've walked two thousand kilometres. That, incidentally, is from Lipovka to the Urals, where your friend the postwoman is. Yes, the whole office knows: the letters go through us, after all. V. T. Pestov",
  gift="e_route_map")
B(A, 30, "", "km3000", "letter", "Валентин Тимофеевич Пестов", "Valentin Timofeyevich Pestov",
  "Пестов пишет не как начальник: он уходит на пенсию и дарит свою звёздочку.",
  "Pestov writes not as your boss: he's retiring, and gives you his star.",
  "Пишу не как начальник, а просто. В конце года ухожу на пенсию: буду выращивать огурцы и, наверное, писать письма, теперь моя очередь. Три тысячи километров вы прошли — это до Байкала. За сорок лет я подписал тысячи приказов, а самым удачным считаю № 47, про вас. Посылаю свою звёздочку «Отличник связи», 1984 год. Наград мне больше не нужно, а вам она пригодится: к ней привыкаешь, и стыдно потом плохо работать. Валентин Тимофеевич. Просто.",
  "I'm writing not as your boss, just as myself. At the end of the year I retire: I'll grow cucumbers and probably write letters — my turn now. You've walked three thousand kilometres; that's to Lake Baikal. In forty years I signed thousands of orders, and I count No. 47, the one about you, as the best. I'm sending my “Excellence in Communications” star, from 1984. I don't need any more awards, but it'll be useful to you: you get used to wearing it, and then you'd be ashamed to do a bad job. Valentin Timofeyevich. Just that.",
  gift="e_pestov_star", stamp="e_3000")

# ================================================================ me_column: Notes of a Postman in the Village News
A = "me_column"
PS_RU, PS_EN = "Павел Сергеевич, «Сельская новь»", "Pavel Sergeyevich, Village News"
B(A, 7, "", "d5", "letter", PS_RU, PS_EN,
  "Редактор «Сельской нови» предлагает вам вести рубрику в газете.",
  "The editor of the Village News offers you a column in the paper.",
  "Здравствуйте! Пишет вам редактор «Сельской нови» Павел Сергеевич Редькин. Про вас мне рассказали трое за одну неделю: Зинаида Павловна (по телефону, сорок минут), Софья Марковна из музея и наш водитель Михаил. Когда про человека рассказывают трое, газете пора с ним поговорить. Предлагаю рубрику «Записки почтальона». Раз в месяц, полполосы, о чём хотите — о маршруте, о погоде, о коте. Гонорар скромный, слава районная. Подумайте. П. С.",
  "Hello! This is Pavel Sergeyevich Redkin, editor of the Village News. Three people told me about you in a single week: Zinaida Pavlovna (by phone, forty minutes), Sofia Markovna from the museum, and our driver Mikhail. When three people talk about someone, it's time the paper had a word with them. I propose a column: “Notes of a Postman”. Once a month, half a page, about whatever you like: the round, the weather, the cat. A modest fee, district-wide fame. Think it over. P. S.",
  stamp="e_editorial")
B(A, 21, "", "", "newspaper", "«Сельская новь», Городок", "The Village News, Gorodok",
  "Вышли первые «Записки почтальона». Тираж разошёлся к обеду.",
  "The first “Notes of a Postman” is out. The issue sold out by lunchtime.",
  "Вышел номер! «Записки почтальона», колонка первая, на третьей полосе, между прогнозом погоды и объявлением о продаже козы. Тираж разошёлся к обеду — такого в Городке не было с юбилея района. Высылаю вам пять экземпляров: один вам, один Сургучу, остальные кому сочтёте нужным. Опечатку в третьем абзаце не ищите, я её уже нашёл: «почтальён». Наборщица говорит, так душевнее. П. С.",
  "The issue is out! “Notes of a Postman”, column one, page three, between the weather forecast and an advert for a goat for sale. It sold out by lunchtime: Gorodok hasn't seen the like since the district's jubilee. I'm sending you five copies: one for you, one for Surguch, the rest for whoever you see fit. Don't hunt for the misprint in the third paragraph, I've found it already: “postmun”. The typesetter says it's homelier that way. P. S.")
B(A, 30, "", "", "letter", PS_RU, PS_EN,
  "Пошли письма читателей: про ходики, про кота и про собаку.",
  "Readers' letters are coming in: about the clock, the cat, and a dog.",
  "Пошли письма! Первое — от бабушки из Заполья, восемьдесят лет: пишет, что к ним в шестидесятые тоже ходил почтальон с котом и что она всплакнула, читая про ходики. Второе — от школьника из Городка: «А почтальону правда дают собаку?» Третье — от нашего же наборщика, просит больше про Сургуча. Пересылаю все. Отвечать необязательно, но если ответите — напечатаю. П. С.",
  "The letters have started! The first is from a granny in Zapolye, eighty years old: she writes that in the sixties they had a postman with a cat too, and she shed a tear reading about the wall clock. The second is from a schoolboy in Gorodok: “Do postmen really get given a dog?” The third is from our own typesetter, asking for more about Surguch. I'm forwarding them all. You needn't answer, but if you do, I'll print it. P. S.",
  stamp="e_readers")
B(A, 30, "", "", "letter", "Тимур, 9 лет (через редакцию)", "Timur, 9 (via the newspaper)",
  "Письмо от мальчика из Городка: он тоже хочет быть почтальоном.",
  "A letter from a boy in Gorodok: he wants to be a postman too.",
  "Здраствуйте! Я прочитал вашу колонку. Я тоже хочу быть почтальоном когда вырасту, но мама говорит, что сейчас все пишут в телефоне. Это правда? Сколько надо ходить? Я хожу в школу 1 км. Это много или мало? Можно я вам пришлю письмо по-настоящему? Вот оно. Это оно и есть. Тимур, 3 «Б»",
  "Helo! I read your column. I want to be a postman too when I grow up but Mum says that now everyone writes on their phones. Is that true? How much do you have to walk? I walk 1 km to school. Is that a lot or a little? Can I send you a real letter? Here it is. This is it. Timur, class 3B")
B(A, 35, "", "", "letter", PS_RU, PS_EN,
  "Сургучу пишут больше, чем редактору. Это статистика.",
  "Surguch gets more letters than the editor. That's a statistic.",
  "Сургучу пишут больше, чем мне. Это не шутка, это статистика: за месяц одиннадцать писем на имя кота. Одна читательница из Борок связала ему коврик, другая прислала рецепт «кошачьего пирога» — мы проверили, это пирог с рыбой, вполне человеческий, редакция съела за обедом. Коврик пересылаю. Рецепт тоже, раз уж пирога не осталось. Ваш редактор, слегка обиженный. П. С.",
  "Surguch gets more letters than I do. That's not a joke, it's a statistic: eleven letters addressed to the cat this month. One reader in Borki knitted him a rug, another sent a recipe for “cat pie” — we checked, it's a fish pie, perfectly human; the editorial office ate it at lunch. I'm forwarding the rug. And the recipe, since there's no pie left. Your slightly offended editor. P. S.")
B(A, 40, "", "", "letter", PS_RU, PS_EN,
  "Редактор сам прошёл ваш маршрут. Тираж вырос на сорок экземпляров.",
  "The editor walked your round himself. Circulation is up forty copies.",
  "Признаюсь: в субботу я сам прошёл ваш маршрут, от почты до мельницы и обратно, с блокнотом. Шесть километров, два чаепития, одна гусыня бабы Нины, которая посмотрела на меня с презрением. Теперь я понимаю, почему в «Записках» так мало жалоб и так много чая. Тираж вырос на сорок экземпляров. Сорок! Для районки это как полёт в космос. П. С.",
  "I confess: on Saturday I walked your round myself, from the post office to the mill and back, with a notebook. Six kilometres, two tea parties and one of Granny Nina's geese, who looked at me with contempt. Now I understand why the “Notes” have so few complaints and so much tea. Circulation is up by forty copies. Forty! For a district paper that's a space flight. P. S.")
B(A, 30, "12", "", "newspaper", "«Сельская новь», Городок", "The Village News, Gorodok",
  "Новогодний номер: читатели пишут пожелания почтальону Липовки.",
  "The New Year issue: readers send wishes to the postman of Lipovka.",
  "В новогоднем номере вместо «Записок» — ваши читатели. Мы попросили написать, чего они желают почтальону Липовки. Пришло сто четыре открытки. Желают: сухих ног (37 раз), тёплых варежек (21), чтобы Сургуч не толстел (9), хорошего начальства (1, подпись неразборчива, почерк похож на Пестова), а один читатель из Озёрок — «чтобы вы никогда от нас не уезжали». Последнее я поставил крупно. Самую красивую открытку пересылаю. С Новым годом! П. С.",
  "In the New Year issue, instead of the “Notes”: your readers. We asked them to write what they wish the postman of Lipovka. We received a hundred and four cards. They wish you: dry feet (37 times), warm mittens (21), a Surguch who doesn't get fat (9), good bosses (1, signature illegible, handwriting resembles Pestov's), and one reader in Ozyorki wrote “that you never leave us”. That one I printed large. I'm forwarding the prettiest card. Happy New Year! P. S.",
  gift="e_readers_card", stamp="e_holiday_issue")
B(A, 40, "", "", "letter", PS_RU, PS_EN,
  "Ваши «Записки» читают во Владивостоке. Растёт ли липа у школы?",
  "Your “Notes” are read in Vladivostok. Is the school linden still there?",
  "Пересылаю письмо из Владивостока. Пишет женщина, Елена: сестра вырезает «Записки» из газеты и посылает ей через всю страну. Елена пишет: «Я выросла в деревне под Городком, тридцать лет её не видела, а читаю вас — и чувствую запах печки и мокрого забора». Она спрашивает, растёт ли ещё большая липа у школы. Я обещал, что вы ответите. Растёт же? П. С.",
  "I'm forwarding a letter from Vladivostok. It's from a woman called Elena: her sister cuts the “Notes” out of the paper and posts them to her right across the country. Elena writes: “I grew up in a village near Gorodok and haven't seen it in thirty years, but when I read you I can smell the stove and the wet fence.” She asks whether the big linden by the school is still growing. I promised you'd answer. It is, isn't it? P. S.",
  stamp="e_vladivostok")
B(A, 60, "", "", "parcel", PS_RU, PS_EN,
  "Год «Запискам почтальона»: редактор прислал подшивку в переплёте.",
  "A year of “Notes of a Postman”: the editor sends a bound volume.",
  "Год «Запискам почтальона»! Я переплёл все номера в одну подшивку: в типографии, в коричневую обложку с золотым тиснением, как полагается солидным изданиям. Это вам. Второй экземпляр отдал Софье Марковне в музей. Она сказала, что через сто лет по вашим запискам будут изучать, как мы тут жили. Я сказал: пусть изучают, только с чаем. Продолжаем? Продолжаем. П. С.",
  "A year of “Notes of a Postman”! I've had every issue bound into one volume at the printer's, in a brown cover with gold lettering, as befits a serious publication. This one is yours. The second copy I gave to Sofia Markovna for the museum. She said that in a hundred years people will study your notes to learn how we lived here. I said, let them study, but with tea. Shall we carry on? We carry on. P. S.",
  gift="e_column_file")

# ================================================================ me_dog: Bublik
A = "me_dog"
B(A, 5, "", "dog", "parcel", "Зинаида Павловна, магазин", "Zinaida Pavlovna, the shop",
  "Зинаида Павловна докладывает: Бублик вынес из магазина баранку.",
  "Zinaida Pavlovna reports: Bublik walked out of the shop with a pretzel.",
  "Довожу до вашего сведения: ваш Бублик сегодня в 9:20 вошёл в магазин вместе с вами, а вышел без вас и с баранкой. Баранку записала в тетрадку на ваш счёт: пять рублей. Шучу, не записала. Но в следующий раз пусть ждёт на крыльце, как воспитанный пёс. А это ему ещё одна — чтобы не думал, что я жадная. Зинаида П.",
  "For your information: today at 9:20 your Bublik came into the shop with you and left without you, carrying a pretzel. I've put the pretzel on your tab: five roubles. Only joking, I haven't. But next time he can wait on the porch like a well-brought-up dog. And here's another one for him, so he doesn't think I'm stingy. Zinaida P.",
  gift="e_bublik_pretzel")
B(A, 14, "", "", "letter", "Варя Кузнецова", "Varya Kuznetsova",
  "Варя считает, что Бублику нужна форма, и берётся вязать шарф.",
  "Varya thinks Bublik needs a uniform and is going to knit him a scarf.",
  "Здраствуйте! Бублик у вас в какой должности? Я думаю, он помошник почтальона. Тогда ему нужна форма. Я буду вязать ему шарф, бабушка Агафья научила меня набирать петли. Какой у него любимый цвет? Я думаю, красный, потому что он рыжий, а рыжим идёт красный, как Сургучу. Только не говорите ему, это сюрприз. ВАРЯ",
  "Helo! What is Bublik's job at your post office? I think he is the postman's asistant. Then he needs a uniform. I'm going to knit him a scarf, Granny Agafya taught me to cast on. What is his favourite colour? I think red, because he's ginger and red suits ginger, like Surguch. Only don't tell him, it's a surprise. VARYA")
B(A, 20, "", "", "letter", "Баба Нина", "Granny Nina",
  "Баба Нина рассказывает, как Бублик с Сургучом сторожили почту.",
  "Granny Nina tells how Bublik and Surguch guarded the post office.",
  "Здравствуйте! Хочу вам сказать про вашего пса. Вчера вы ушли на дальний конец, а он остался у почты. Лёг на крыльцо и до вечера никого не пускал, даже Михалыча с банкой. Только Сургуча пустил: тот ему на спину сел, и так они вдвоём и сторожили. Мой Коля говорит, это называется «пост сдал — пост принял». Покормила его котлетой. Не ругайтесь. Баба Нина",
  "Hello! I wanted to tell you about your dog. Yesterday you went off to the far end and he stayed by the post office. He lay on the porch and wouldn't let anyone past till evening, not even Mikhalych with his jar. Only Surguch was allowed: he sat on Bublik's back and the two of them stood guard together. My Kolya says that's called “changing of the guard”. I gave him a meatball. Don't scold me. Granny Nina")
B(A, 30, "11,12,1,2", "", "parcel", "Варя Кузнецова", "Varya Kuznetsova",
  "Варя довязала Бублику шарф. Длина — два метра.",
  "Varya has finished Bublik's scarf. It is two metres long.",
  "Вот шарф для Бублика!!! Я вязала его три месяца. Он получился длинный, два метра, потому что я не умею остановиться. Бабушка Агафья сказала, что можно намотать два раза и ещё на хвост останется. Красный, как обещала. Если Бублику не понравится, можете носить сами, вам тоже пойдёт красный. ВАРЯ",
  "Here is Bublik's scarf!!! I knitted it for three months. It came out long, two metres, because I don't know how to stop. Granny Agafya says you can wind it round twice and there will still be some left for his tail. Red, like I promised. If Bublik doesn't like it, you can wear it yourself, red will suit you too. VARYA",
  gift="e_bublik_scarf", stamp="e_bublik_scarf")
B(A, 40, "", "", "letter", "Лидия Аркадьевна, клуб", "Lidia Arkadyevna, the club",
  "Бублик записан в библиотеку: читатель № 214, ходит на кино по четвергам.",
  "Bublik has joined the library: reader No. 214, comes to Thursday films.",
  "Сообщаю официально: в библиотеку при клубе записан новый читатель. Формуляр № 214, имя — Бублик. Причина: он третий четверг подряд приходит на кинопоказ, ложится под первую скамейку и не уходит до титров. На «Каштанке» вздыхал, в конце вилял хвостом. Книг на дом пока не берёт, но правила библиотеки знает: не лает. Если будете искать его по четвергам в семь — он у нас. Л. А. Белова",
  "I hereby inform you officially that the club library has a new reader. Card No. 214, name: Bublik. Reason: for the third Thursday running he's come to the film night, lain down under the front bench and stayed till the credits. During Kashtanka he sighed, and at the end he wagged his tail. He doesn't borrow books yet, but he knows the library rules: no barking. If you're looking for him on Thursdays at seven, he's with us. L. A. Belova",
  stamp="e_reader214")


# ================================================================ write
def write(path, cols, rows):
    for r in rows:
        for c in r:
            assert "\t" not in c and "\n" not in c and "\r" not in c, c
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(r) + "\n")


if __name__ == "__main__":
    write(C / "arcs/e.tsv", ARC_COLS, ROWS)
    write(C / "items/e.tsv", ["key", "family", "variant", "name_ru", "name_en"], ITEMS)
    write(C / "stamps/e.tsv", ["key", "family", "bg", "value", "name_ru", "name_en", "series"], STAMPS)
    print(f"{len(ROWS)} beats, {len(ITEMS)} items, {len(STAMPS)} stamps")
