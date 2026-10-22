"""Group A content: the Lipovka core (Anna, Fyodor Ilyich, Agafya Petrovna, the teacher, the Kuznetsovs).

python tools/content_src/a.py   -> writes arcs/a.tsv, items/a.tsv, stamps/a.tsv and prints a pacing report.
"""
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
C = ROOT / "app/src/main/assets/content"

ARCS = []  # (arc, [beats])


def B(gap, months, kind, to, frm, brief, news, *, on="", needs="", reply="", gift="", stamp="", sets=""):
    return dict(gap=gap, months=months, on=on, needs=needs, kind=kind, to=to, frm=frm, brief=brief, news=news,
                reply=reply, gift=gift, stamp=stamp, sets=sets)


def arc(name, *beats):
    ARCS.append((name, list(beats)))


# ---------------------------------------------------------------- items
ITEMS = [
    # key, family, variant, ru, en
    ("a_pie_fish", "pie", "fish", "Рыбник Анны", "Anna's fish pie"),
    ("a_shell", "found", "shell", "Ракушка с Соловков", "A shell from the Solovki"),
    ("a_rowan", "bouquet", "rowan", "Ветка рябины", "A sprig of rowan"),
    ("a_photo_wedding", "photo", "wedding", "Свадьба под рябиной", "The wedding under the rowan"),
    ("a_jar_lingon", "jar", "lingonberry", "Брусника из Вытегры", "Lingonberries from Vytegra"),
    ("a_scarf_check", "scarf", "check", "Шарф из «Рябинки»", "A scarf from the Ryabinka"),
    ("a_photo_baby", "photo", "baby", "Алёнка, первая карточка", "Alyonka's first photo"),
    ("a_toy_boat", "toy", "boat", "Кораблик Степана", "Stepan's little boat"),
    ("a_mill_key", "found", "key", "Ключ от мельницы", "A key to the mill"),
    ("a_photo_mill", "photo", "landscape", "Колесо пошло", "The wheel turning"),
    ("a_bread_loaf", "bread", "loaf", "Горбушка субботнего хлеба", "The heel of a Saturday loaf"),
    ("a_kalach", "bread", "kalach", "Калач с мельницы", "A kalach from the mill"),
    ("a_whistle", "toy", "whistle", "Ивовый свисток Пети", "Petya's willow whistle"),
    ("a_photo_petya", "photo", "group", "Дед и внук у колеса", "Grandpa and grandson at the wheel"),
    ("a_mittens", "mittens", "patterned", "Варежки с узором", "Patterned mittens"),
    ("a_socks_grey", "socks", "grey", "Серые шерстяные носки", "Grey woollen socks"),
    ("a_jar_cloudberry", "jar", "cloudberry", "Морошка из Карелии", "Cloudberries from Karelia"),
    ("a_pie_berry", "pie", "berry", "Черничный пирог", "Bilberry pie"),
    ("a_tea_linden", "tea", "herbs", "Липовый цвет", "Linden blossom tea"),
    ("a_photo_sisters", "photo", "old", "Сёстры на Липке", "Two sisters by the Lipka"),
    ("a_cornflowers", "bouquet", "cornflowers", "Васильки", "Cornflowers"),
    ("a_map_star", "map", "star", "Подвижная карта неба", "A rotating star map"),
    ("a_postcard_space", "postcard", "space", "Туманность из Архыза", "A nebula from Arkhyz"),
    ("a_book_memoir", "book", "blue", "«Сорок выпусков»", "Forty Graduations"),
    ("a_photo_reunion", "photo", "group", "Вечер встречи", "The reunion night"),
    ("a_plant_lemon", "plant", "lemon", "Лимон учителя", "The teacher's lemon tree"),
    ("a_drawing", "postcard", "winter", "Рисунок Вари", "Varya's drawing"),
    ("a_bell_sleigh", "bell", "sleigh", "Колокольчик из Устюга", "A bell from Ustyug"),
    ("a_gingerbread", "bread", "gingerbread", "Пряник для Бублика", "Bublik's gingerbread"),
    ("a_pumice", "found", "pebble", "Пемза с Камчатки", "Pumice from Kamchatka"),
    ("a_fish_smoked", "fish", "smoked", "Камчатский кижуч", "Kamchatka coho salmon"),
    ("a_photo_friends", "photo", "portrait", "Варя и Уля", "Varya and Ulya"),
    ("a_pie_apple", "pie", "apple", "Именинный пирог", "Birthday pie"),
    ("a_tea_herbs", "tea", "tin", "Чай с чабрецом", "Thyme tea"),
    ("a_plant_aloe", "plant", "aloe", "Отросток алоэ", "An aloe cutting"),
    ("a_tea_rosehip", "tea", "rosehip", "Шиповник от доктора", "Rosehip from the doctor"),
    ("a_fish_dried", "fish", "dried", "Треска из Мурманска", "Cod from Murmansk"),
    ("a_horseshoe", "found", "horseshoe", "Дедова подкова", "Grandad's horseshoe"),
    ("a_pretzel", "bread", "pretzel", "Именинный крендель", "A birthday pretzel loaf"),
    ("a_eggs", "basket", "eggs", "Яйца с «Урала»", "Eggs from the Ural"),
]

# ---------------------------------------------------------------- stamps
STAMPS = [
    # key, family, bg, value, ru, en, series
    ("a_onega", "ship", "sea", 12, "Теплоход «Онега»", "MV Onega", "far"),
    ("a_lighthouse", "lighthouse", "dusk", 8, "Маяк Белого моря", "A White Sea lighthouse", "far"),
    ("a_seagull", "bird", "sea", 6, "Чайка над Соловками", "A gull over the Solovki", "far"),
    ("a_white_night", "sun", "night", 15, "Белая ночь", "White night", "seasons"),
    ("a_rowan_stamp", "berry", "red", 4, "Рябина", "Rowan", "lipovka"),
    ("a_telegram", "telegram", "cream", 10, "Телеграмма", "Telegram", "post"),
    ("a_lace", "flower", "cream", 25, "Вологодское кружево", "Vologda lace", "far"),
    ("a_heart", "heart", "red", 20, "Сердце", "A heart", "holidays"),
    ("a_ferry", "boat", "sky", 7, "Паром у Перевоза", "The ferry at Perevoz", "lipovka"),
    ("a_cow", "cow", "green", 3, "Липовская ферма", "The Lipovka dairy", "lipovka"),
    ("a_moon", "moon", "night", 12, "Колыбельная", "Lullaby", "seasons"),
    ("a_mill", "mill", "sky", 5, "Водяная мельница", "The watermill", "lipovka"),
    ("a_mill_gold", "mill", "gold", 50, "Памятник техники", "A monument of engineering", "lipovka"),
    ("a_fir", "fir", "night", 3, "Новогодняя ёлка", "New Year fir", "holidays"),
    ("a_onego", "lake", "blue", 14, "Онежское озеро", "Lake Onega", "far"),
    ("a_cloudberry", "berry", "gold", 9, "Морошка", "Cloudberry", "far"),
    ("a_linden", "tree", "green", 2, "Липа", "Linden", "lipovka"),
    ("a_cup", "kettle", "blue", 3, "Чай у Агафьи", "Tea at Agafya's", "lipovka"),
    ("a_observatory", "star", "night", 30, "Обсерватория", "The observatory", "far"),
    ("a_school_bell", "bell", "gold", 1, "Первый звонок", "The first bell", "holidays"),
    ("a_knight", "horse", "cream", 11, "Шахматы по почте", "Chess by post", "post"),
    ("a_icebreaker", "ship", "blue", 40, "Ледокол", "Icebreaker", "far"),
    ("a_book", "book", "green", 6, "Сорок выпусков", "Forty Graduations", "lipovka"),
    ("a_school", "house", "red", 4, "Липовская школа", "Lipovka school", "lipovka"),
    ("a_comet", "star", "dusk", 60, "Комета", "The comet", "far"),
    ("a_stars", "star", "violet", 18, "Кассиопея", "Cassiopeia", "far"),
    ("a_globe", "globe", "blue", 30, "Глобус с вмятиной", "The dented globe", "lipovka"),
    ("a_ustyug", "snowflake", "blue", 10, "Великий Устюг", "Veliky Ustyug", "holidays"),
    ("a_sleigh", "sled", "night", 5, "Сани Деда Мороза", "Ded Moroz's sleigh", "holidays"),
    ("a_xmas_star", "star", "gold", 13, "Новогодняя звезда", "New Year star", "holidays"),
    ("a_dog", "dog", "cream", 4, "Бублик", "Bublik", "lipovka"),
    ("a_cat", "cat", "cream", 3, "Сургуч", "Surguch", "post"),
    ("a_volcano", "mountain", "dusk", 40, "Авачинская сопка", "Avachinsky volcano", "far"),
    ("a_salmon", "fish", "sea", 22, "Кижуч", "Coho salmon", "far"),
    ("a_plane", "plane", "sky", 35, "Рейс на материк", "Flight to the mainland", "far"),
    ("a_autumn", "tree", "gold", 2, "Осень", "Autumn", "seasons"),
    ("a_aurora", "star", "green", 28, "Северное сияние", "Northern lights", "far"),
    ("a_anchor", "anchor", "sea", 16, "Мурманский порт", "Murmansk port", "far"),
    ("a_radio", "radio", "cream", 12, "Ламповый приёмник", "Valve radio", "radio"),
    ("a_birthday", "fireworks", "violet", 8, "С днём рождения", "Happy birthday", "holidays"),
    ("a_snow", "snowflake", "sky", 1, "Первый снег", "First snow", "seasons"),
    ("a_rain", "rain", "sky", 2, "Осенний дождь", "Autumn rain", "seasons"),
    ("a_swallow", "swallow", "sky", 5, "Ласточки вернулись", "The swallows are back", "seasons"),
    ("a_letter", "letter", "cream", 7, "Письмо", "A letter", "post"),
    ("a_clinic", "house", "cream", 9, "Амбулатория", "The village clinic", "lipovka"),
    ("a_clock", "clock", "cream", 6, "Ходики", "Wall clock", "post"),
    ("a_rainbow", "rainbow", "sky", 10, "Радуга над Липкой", "Rainbow over the Lipka", "seasons"),
    ("a_camera", "camera", "cream", 20, "Фотокарточка", "A photograph", "post"),
]

# ---------------------------------------------------------------- senders
STEPAN = ("Степан, т/х «Онега»", "Stepan, MV Onega")
VALYA = ("Валентина Сергеевна, Вытегра", "Valentina Sergeyevna, Vytegra")
LENA = ("Лена, Вологда", "Lena, Vologda")
PETYA = ("Петя, Вологда", "Petya, Vologda")
KROTOV = ("С. И. Кротов, Кириллов", "S. I. Krotov, Kirillov")
KLAVA = ("Клавдия, Петрозаводск", "Klavdia, Petrozavodsk")
FEDOR = ("Ф. И. Жуков, мельница", "F. I. Zhukov, the mill")
AGAFYA = ("А. П. Сорокина", "A. P. Sorokina")
ILYA = ("Илья Ковалёв, Архыз", "Ilya Kovalyov, Arkhyz")
TEACHER = ("Н. С. Лебедев, Городок", "N. S. Lebedev, Gorodok")
CHESS = ("А. Л. Гринберг, Томск", "A. L. Grinberg, Tomsk")
ZUEVA = ("М. Зуева, Вологда", "M. Zueva, Vologda")
MOROZ = ("Дед Мороз, Великий Устюг", "Ded Moroz, Veliky Ustyug")
MURZILKA = ("Журнал «Мурзилка»", "Murzilka magazine")
ULYA = ("Уля, Петропавловск-Камч.", "Ulya, Petropavlovsk-Kamch.")
UNI = ("Медуниверситет, Ярославль", "Medical University, Yaroslavl")
KOSTYA = ("Костя, Мурманск", "Kostya, Murmansk")
ME_TEACHER = ("Н. С. Лебедев, Городок", "N. S. Lebedev, Gorodok")

# ================================================================ ANNA
arc("anna",
    B(2, "", "letter", "anna", STEPAN,
      ("Анне письмо от Степана с «Онеги».", "A letter for Anna from Stepan on the Onega."),
      ("От Стёпы. Они в Архангельске, грузят лес. Пишет, что вся палуба пахнет смолой, как у нас баня в субботу, "
       "и что он от этого запаха чуть не заплакал. Ой. Это я зря вслух. Вы ведь никому не скажете?",
       "From Styopa. They're in Arkhangelsk, loading timber. He says the whole deck smells of resin, like our "
       "bathhouse on a Saturday, and the smell nearly made him cry. Oh. I shouldn't have read that out. "
       "You won't tell anyone, will you?"),
      stamp="a_onega"),
    B(12, "", "postcard", "anna", ("Степан, Кандалакша", "Stepan, Kandalaksha"),
      ("Степан прислал Анне открытку с маяком.", "Stepan sent Anna a postcard with a lighthouse."),
      ("Опять маяк. Он всегда выбирает с маяками, у меня над машинкой их уже одиннадцать, целое побережье. "
       "А сзади три слова: «Жив. Скучаю. Ешь». «Ешь» — это он в маму. Она тоже всех кормит письменно.",
       "Another lighthouse. He always picks ones with lighthouses; there are eleven over my sewing machine now, "
       "a whole coastline. And three words on the back: 'Alive. Miss you. Eat.' The 'eat' is his mother in him. "
       "She feeds everyone by letter too."),
      stamp="a_lighthouse"),
    B(18, "", "parcel", "anna", ("Текстиль почтой, Иваново", "Textiles by Post, Ivanovo"),
      ("Анне пришла посылка с тканью из Иванова.", "Anna has a parcel of fabric from Ivanovo."),
      ("Лён, серый, как Липка в октябре. Стёпе рубашку шью, по ночам, после фермы: на его плечи в магазине "
       "ничего нет, он у нас как шкаф с якорем. Только ему не говорите. Пусть думает, что купила.",
       "Linen, grey as the Lipka in October. I'm making Styopa a shirt, at night, after my shift at the dairy; "
       "the shops have nothing for his shoulders, he's built like a wardrobe with an anchor. Don't tell him, though. "
       "Let him think I bought it."),
      stamp="a_cow"),
    B(20, "", "letter", "anna", STEPAN,
      ("Степан пишет Анне про шторм и про крыльцо.", "Stepan writes to Anna about a storm and a porch."),
      ("Три дня штормило у Канина Носа. Пишет, что не боялся, а сам нарисовал на полях крыльцо, со столбиками "
       "и скамейкой. «Анюта, не смейся, это я так держался». Я не смеюсь. Хорошее крыльцо. Под рябину как раз встанет.",
       "Three days of storm off Kanin Nos. He says he wasn't scared, but in the margin he's drawn a porch, with "
       "posts and a bench. 'Anyuta, don't laugh, that's how I held on.' I'm not laughing. It's a good porch. "
       "It'll fit right under the rowan.")),
    B(25, "", "letter", "anna", VALYA,
      ("Мама Степана прислала Анне рецепт рыбника.", "Stepan's mother sent Anna a fish pie recipe."),
      ("Будущая свекровь. Рецепт рыбника, на четырёх страницах, а в конце: «Стёпа с детства упрямый, но отходчивый. "
       "Тесто тоже». Я теперь этого рыбника боюсь больше, чем свадьбы. В субботу испеку. Если выйдет — "
       "вам первый кусок.",
       "My future mother-in-law. A fish pie recipe, four pages long, and at the end: 'Styopa's been stubborn since "
       "he was small, but he softens. So does the dough.' Now I'm more afraid of this pie than of the wedding. "
       "I'll bake it on Saturday. If it works, you get the first slice.")),
    B(21, "", "postcard", "anna", STEPAN,
      ("Наконец-то: Степан прислал Анне открытку.", "At last: a postcard from Stepan for Anna."),
      ("Три недели ни строчки, и вот: «Были без связи, всё хорошо». Без связи! А я, знаете, на вас сердилась, "
       "будто это вы его письма в сумке держите. Простите. Вот, возьмите рыбника. Получился, представляете? "
       "С первого раза.",
       "Three weeks without a line, and now: 'We were out of contact, all well.' Out of contact! And I was cross "
       "with you, you know, as if you were keeping his letters in your bag. I'm sorry. Here, have some fish pie. "
       "It came out, can you imagine? First try."),
      gift="a_pie_fish"),
    B(30, "", "letter", "anna", ("Степан, Соловки", "Stepan, the Solovki"),
      ("Степан прислал с Белого моря две ракушки.", "Stepan sent two shells from the White Sea."),
      ("С Соловков, две ракушки. Одна мне, а про другую написано: «Отдай почтальону, который носит мои письма. "
       "Пусть знает, что море настоящее». Держите. Он вас ни разу не видел, а уже благодарит. Он такой.",
       "From the Solovki, two shells. One is mine, and about the other he writes: 'Give it to the postman who "
       "carries my letters. Let them know the sea is real.' Here. He's never once seen you and he's already "
       "thanking you. That's him."),
      gift="a_shell", stamp="a_seagull"),
    B(25, "", "letter", "anna", ("Степан, Архангельск", "Stepan, Arkhangelsk"),
      ("Степан пишет из дока. Анна шьёт ему жилет.", "Stepan writes from the dry dock. Anna sews him a waistcoat."),
      ("Встали в док, в Архангельске, на ремонт. Пишет, в доке сквозняк, как в трубе: «Мёрзну, как налим». Налим, "
       "между прочим, не мёрзнет. Я ему жилет на вате сшила, ночью. Отправите? И пусть только попробует не носить.",
       "They're in dry dock in Arkhangelsk for repairs. He says the dock's as draughty as a chimney: 'Freezing like a "
       "burbot.' Burbot don't freeze, for the record. I sewed him a quilted waistcoat last night. Will you send it? "
       "And he'd better wear it."),
      reply="out"),
    B(30, "", "letter", "anna", STEPAN,
      ("Степан обещает Анне быть дома к Покрову.", "Stepan promises Anna he'll be home by Pokrov."),
      ("Контракт до осени, пишет, а к Покрову — на берег, честное морское. Я ответила: не приедешь к Покрову — "
       "выйду за Фёдора Ильича. Шучу, конечно. Фёдор Ильич первый бы испугался. Но Стёпе об этом знать не обязательно.",
       "His contract runs till autumn, he writes, and then he's ashore by Pokrov, a sailor's word. I wrote back: if "
       "you're not here by Pokrov, I'll marry Fyodor Ilyich. Joking, of course. Fyodor Ilyich would be the first to "
       "run. But Styopa doesn't need to know that."),
      reply="out"),
    B(30, "", "postcard", "anna", STEPAN,
      ("Степан считает дни до берега.", "Stepan is counting the days to shore."),
      ("Считает дни. Пишет: «Вахта — четыре часа, а день без тебя — сто». Это он у кого-то списал, точно. Стёпа так "
       "красиво не умеет. Но всё равно спасибо тому, у кого списал.",
       "He's counting the days. Writes: 'A watch is four hours, and a day without you is a hundred.' He copied that "
       "from someone, I'm sure. Styopa can't put things that prettily. But thanks all the same to whoever he copied "
       "it from.")),
    B(30, "8,9", "letter", "anna", STEPAN,
      ("Степан списывается на берег: будет к Покрову.", "Stepan is signing off: home by Pokrov."),
      ("Всё. Списывается. «Буду к Покрову, Анюта, топи баню». Рябина у меня покраснела, видите? Значит, правда осень. "
       "Значит, правда скоро. Возьмите веточку, а то у вас на почте одни конверты. Пусть будет красиво.",
       "That's it. He's signing off. 'Home by Pokrov, Anyuta, fire up the bathhouse.' My rowan's gone red, see? "
       "So it really is autumn. So it really is soon. Take a sprig; you've nothing but envelopes at the post office. "
       "Let it be pretty."),
      gift="a_rowan", stamp="a_rowan_stamp"),
    B(14, "10", "telegram", "anna", ("Степан, Архангельск", "Stepan, Arkhangelsk"),
      ("Телеграмма Анне: Степан едет домой.", "A telegram for Anna: Stepan is coming home."),
      ("«ВСТРЕЧАЙ ПЯТНИЦУ АВТОБУС ГОРОДКА ЦЕЛУЮ СТЕПАН». Пятница — это же послезавтра. А у меня руки в муке, "
       "и голова в муке, и крыльца нет, и... Ничего. Крыльцо он сам построит. Он обещал. На полях.",
       "'MEET FRIDAY GORODOK BUS KISSES STEPAN.' Friday is the day after tomorrow. And my hands are floury, "
       "and my hair's floury, and there's no porch, and... Never mind. He'll build the porch himself. "
       "He promised. In the margin."),
      stamp="a_telegram", sets="anna.home"),
    B(20, "10,11", "postcard", "anna", VALYA,
      ("Мама Степана пишет Анне: теперь он ваш.", "Stepan's mother writes to Anna: he's yours now."),
      ("Стёпа дома, третью неделю! Чинит всё подряд, даже то, что не сломано. А мама его пишет: «Теперь он ваш, "
       "Анечка, держите крепче, он скользкий, как налим». Опять налим. У них, видно, вся семья налимы. "
       "Летом распишемся. Ой. Я это вслух сказала?",
       "Styopa's home, three weeks now! He mends everything, even things that aren't broken. And his mother writes: "
       "'He's yours now, Anechka, hold on tight, he's slippery as a burbot.' The burbot again. They must all be burbot "
       "in that family. We'll marry in the summer. Oh. Did I say that out loud?")),
    )

INVITE = ("Анна и Степан", "Anna and Stepan")
INVITE_BRIEF = ("{} — приглашение на свадьбу Анны и Степана.", "{}: an invitation to Anna and Stepan's wedding.")


def invite(to, who_ru, who_en, ru, en, gap=2, stamp=""):
    return B(gap, "6", "notice", to, INVITE,
             (INVITE_BRIEF[0].format(who_ru), INVITE_BRIEF[1].format(who_en)), (ru, en), stamp=stamp)


arc("anna_wedding",
    B(30, "1,2,3", "parcel", "anna", ("Текстиль почтой, Иваново", "Textiles by Post, Ivanovo"),
      ("Анне пришёл крепдешин — на свадебное платье.", "Crêpe de Chine for Anna's wedding dress."),
      ("Крепдешин, цвета топлёного молока. Белое мне не идёт, я в белом как сметана. Шить буду сама, чужим рукам "
       "такое не доверю. Стёпе ни слова. Он думает, что жениху платье видеть нельзя, а я думаю — он просто не заметит.",
       "Crêpe de Chine, the colour of baked milk. White doesn't suit me, in white I look like sour cream. "
       "I'll sew it myself; I wouldn't trust anyone else's hands with this. Not a word to Styopa. He thinks the groom "
       "mustn't see the dress; I think he just won't notice it."),
      needs="anna.home"),
    B(25, "2,3,4", "parcel", "anna", VALYA,
      ("Мама Степана прислала Анне бабушкино кружево.", "Stepan's mother sent Anna a grandmother's lace."),
      ("Кружево вологодское, бабушкино. Сто лет, а ни одной дырочки. Пишет: «Пришей к вороту, Анечка, на счастье, "
       "оно у нас трёх невест видело». Трёх! Я, выходит, четвёртая. Руки трясутся, а мне ещё рукава вшивать.",
       "Vologda lace, Stepan's grandmother's. A hundred years old and not a single hole. She writes: 'Sew it to the "
       "collar, Anechka, for luck; it's seen three brides in our family.' Three! So I'm the fourth. My hands are "
       "shaking, and I still have the sleeves to set in."),
      stamp="a_lace"),
    B(20, "5,6", "registered", "anna", ("Отдел ЗАГС, Городок", "Registry Office, Gorodok"),
      ("Анне и Степану назначили день свадьбы.", "Anna and Stepan have a wedding date."),
      ("Назначили: июль, суббота, одиннадцать утра. Стёпа прочёл и пошёл доделывать крыльцо — невесту, говорит, "
       "без крыльца в дом не вносят, споткнёшься. Я спрашиваю: а без бани можно? Задумался. Теперь и баню строит.",
       "It's set: July, a Saturday, eleven in the morning. Styopa read it and went off to finish the porch; you can't "
       "carry a bride in without a porch, he says, you'll trip. I asked, and without a bathhouse? He thought about it. "
       "Now he's building a bathhouse too."),
      stamp="a_heart"),
    invite("agafya", "Агафье Петровне", "Agafya Petrovna",
           "На свадьбу зовут! Ну, Анюта, дождалась. Терпенье и труд всё перетрут. Платок голубой надену, он у меня "
           "для праздника лежит, давно лежит. А вы придёте? Приходите. Только зонт возьмите: на свадьбу дождь — к богатству.",
           "They're inviting me to the wedding! Well, Anyuta, she waited and she got him. Patience and work wear "
           "everything down. I'll wear my blue headscarf, it's been put by for a holiday, a long while now. And you'll "
           "come? Do. Just bring an umbrella: rain at a wedding means a rich life."),
    invite("fedor", "Фёдору Ильичу", "Fyodor Ilyich",
           "Приду. Галстук бы найти. Был где-то, с девяносто какого-то года. Анне скажите: мука на пироги — с меня. "
           "Сколько надо, столько и смелю.",
           "I'll come. Need to find a tie. Had one somewhere, from the nineties. Tell Anna the flour for the pies is "
           "on me. However much she needs, I'll grind."),
    invite("teacher", "Николаю Семёновичу", "Nikolai Semyonovich",
           "Анна Ветрова, выпуск шестнадцатого года. По физике твёрдая четвёрка, в законе Ома путалась, но платье "
           "на выпускной сшила такое, что директор забыл речь. Приду непременно. Подарю утюг: это ведь тоже, в сущности, физика.",
           "Anna Vetrova, class of 2016. A solid B in physics, muddled Ohm's law, but sewed herself a graduation dress "
           "that made the headmaster forget his speech. I'll certainly come. I'll give her an iron. That too is physics, "
           "in essence."),
    invite("olga", "Кузнецовым", "The Kuznetsovs",
           "Зовут нас троих, и Варю отдельной строчкой: «и Варвару Сергеевну». Варя теперь ходит важная и спрашивает, "
           "кто понесёт шлейф. Говорю: шлейфа нет. «Значит, сошьют», — говорит. И ведь Анна сошьёт.",
           "All three of us are invited, and Varya on a line of her own: 'and Varvara Sergeyevna'. Now Varya walks about "
           "looking important and asks who'll carry the train. There's no train, I tell her. 'Then they'll sew one,' "
           "she says. And Anna would, too."),
    invite("zina", "Зинаиде Павловне", "Zinaida Pavlovna",
           "А я знала! Ещё в мае знала: Анна у меня шесть катушек белых ниток взяла, а кто ж столько берёт без свадьбы? "
           "Пряников на всю деревню закажу. Да не смотрите вы так. Я не сплетничаю, я предвижу.",
           "I knew it! I knew back in May: Anna bought six reels of white thread from me, and who buys that many without "
           "a wedding? I'll order gingerbread for the whole village. Don't look at me like that. I don't gossip, I foresee."),
    B(2, "6", "letter", "me", INVITE,
      ("Анна и Степан зовут почтальона на свадьбу.", "Anna and Stepan invite the postman to their wedding."),
      ("Дорогой наш почтальон! Приходите к нам на свадьбу — в субботу, в два часа, к нам во двор, под рябину. "
       "Это вы весь год носили мне Стёпины письма: и длинные, и короткие, и те, которых я ждала, а их всё не было. "
       "Я тогда на вас сердилась, а вы всё равно приходили. Без вас мы бы не дотерпели. Стёпа говорит, что посадит вас "
       "рядом с капитаном. Капитан у нас, если что, он сам. Приходите обязательно, и без подарка — подарок вы уже сделали. "
       "Анна и Степан.",
       "Dear postman! Come to our wedding: Saturday at two, in our yard, under the rowan. All year it was you who "
       "brought me Styopa's letters: the long ones, the short ones, and the ones I waited for that never came. I was "
       "cross with you then, and you kept coming anyway. Without you we'd never have held out. Styopa says he'll seat "
       "you next to the captain. The captain, for the record, is him. Do come, and no present: you've given yours "
       "already. Anna and Stepan."),
      stamp="a_letter"),
    B(20, "7", "telegram", "anna", ("Экипаж т/х «Онега»", "The crew of MV Onega"),
      ("Анну и Степана поздравил весь экипаж «Онеги».", "The whole crew of the Onega congratulates Anna and Stepan."),
      ("«ПОЗДРАВЛЯЕМ МОЛОДЫХ ГОРЬКО ЭКИПАЖ ОНЕГИ». Стёпа читал и отворачивался, будто ему мошка в глаз. Вот, "
       "возьмите карточку со свадьбы. Тут и вы есть, с краю, за Фёдором Ильичом. Ну, половина вас.",
       "'CONGRATULATIONS TO THE COUPLE KISS KISS CREW OF THE ONEGA.' Styopa read it and turned away, as if he had a "
       "midge in his eye. Here, take a photo from the wedding. You're in it, at the edge, behind Fyodor Ilyich. "
       "Well, half of you is."),
      gift="a_photo_wedding", stamp="a_onega", sets="anna.married"),
    B(30, "8,9", "parcel", "anna", VALYA,
      ("Свекровь прислала Анне брусники.", "Anna's mother-in-law sent lingonberries."),
      ("Брусника, шесть банок, и записка: «Одну — почтальону. Не жадничай». Я и не жадничаю, видите, сразу отдаю. "
       "Она теперь всех нас кормит из Вытегры. Стёпа говорит: у мамы наконец полный экипаж.",
       "Lingonberries, six jars, and a note: 'One for the postman. Don't be stingy.' I'm not, see, I'm handing it "
       "straight over. She feeds all of us from Vytegra now. Styopa says his mum finally has a full crew."),
      gift="a_jar_lingon"),
    )

arc("anna_home",
    B(30, "8,9", "letter", "anna", ("Речной техникум, Вологда", "River College, Vologda"),
      ("Степана приняли на курсы судоводителей.", "Stepan has been accepted for a skipper's course."),
      ("Стёпу приняли на заочные курсы, на капитана парома. Сидит вечерами с лоцией, бормочет про створные знаки, "
       "а я шью. Так и живём: он про фарватер, я про вытачки. Иногда путаемся.",
       "Styopa's been accepted on a correspondence course to skipper a ferry. He sits up evenings with the pilot "
       "book, muttering about leading marks, and I sew. That's how we live: him about fairways, me about darts. "
       "Sometimes we mix them up."),
      needs="anna.married"),
    B(25, "9,10,11", "parcel", "anna", ("«Швейный мир», Москва", "Sewing World, Moscow"),
      ("Анне пришёл оверлок — для мастерской.", "An overlocker for Anna's workshop."),
      ("Оверлок! Два года копила, ещё до свадьбы начала. Стёпа отдаёт мне летнюю кухню: пусть, говорит, будет "
       "мастерская, а варенье и в доме сварим. Вывеску хочу: «Рябинка». Скромно, но с характером. Как я.",
       "An overlocker! I saved for two years, I started before the wedding. Styopa's giving me the summer kitchen: "
       "let it be a workshop, he says, we'll make jam in the house. I want a sign: 'Ryabinka', little rowan. Modest, "
       "but with character. Like me.")),
    B(20, "", "letter", "anna", ("Л. Мохова, Городок", "L. Mokhova, Gorodok"),
      ("У «Рябинки» первый заказ из Городка.", "The Ryabinka's first order from Gorodok."),
      ("Первый заказ из Городка! Женщина была у нас на свадьбе, тётя Стёпиного друга, и платье моё запомнила. "
       "Хочет внучкам-двойняшкам школьные сарафаны. Двойняшки — это ведь два раза одно и то же, а ошибиться нельзя ни разу.",
       "My first order from Gorodok! The woman was at our wedding, an aunt of Styopa's friend, and she remembered my "
       "dress. She wants school pinafores for her twin granddaughters. Twins means the same thing twice, and you can't "
       "get it wrong even once.")),
    B(20, "10,11,12", "parcel", "anna", VALYA,
      ("Свекровь прислала Анне фланели. Анна краснеет.", "Anna's mother-in-law sent flannel. Anna blushes."),
      ("Фланель. Мягкая, в мелкий цветочек, на... ну, на всякое маленькое. Мы ещё никому не говорили, а свекровь уже "
       "знает, она всегда всё знает первой. Вы ведь тоже никому? Отнесите Агафье Петровне записочку. Она поймёт.",
       "Flannel. Soft, with a tiny flower print, for... well, for small things. We haven't told anyone yet, but my "
       "mother-in-law knows already; she always knows first. You won't tell either? Take this note to Agafya Petrovna. "
       "She'll understand."),
      reply="agafya"),
    B(30, "12,1,2", "registered", "anna", ("Речной техникум, Вологда", "River College, Vologda"),
      ("Степан сдал экзамены: он судоводитель.", "Stepan passed his exams: he's a qualified skipper."),
      ("Сдал! Диплом судоводителя, с печатью. Стёпа хочет повесить его над крыльцом, а там моя вывеска. Договорились: "
       "над баней. Вот, возьмите шарф, из обрезков, первая вещь «Рябинки». У вас шея вечно голая, я давно смотрю.",
       "He passed! A skipper's certificate, with a stamp. Styopa wants to hang it over the porch, but that's where my "
       "sign is. We agreed: over the bathhouse. Here, take this scarf, made from offcuts, the Ryabinka's first piece. "
       "Your neck is always bare; I've been noticing."),
      gift="a_scarf_check"),
    B(20, "1,2,3", "parcel", "anna", AGAFYA,
      ("Агафья Петровна прислала Анне посылку. Через три дома.", "Agafya Petrovna sent Anna a parcel. From three doors down."),
      ("Пинетки, от Агафьи Петровны. По почте, хотя живёт через три дома. Записка: «Через порог не передают, вот и шлю». "
       "Голубые и розовые, на всякий случай. Говорит, кто родится, тому и впору.",
       "Bootees, from Agafya Petrovna. By post, though she lives three doors down. A note: 'Things aren't handed over "
       "a threshold, so I'm posting them.' Blue ones and pink ones, just in case. Whoever's born, she says, they'll fit.")),
    B(20, "3,4", "letter", "anna", ("Переправа «Перевоз»", "Perevoz Ferry Crossing"),
      ("Степана назначили капитаном парома.", "Stepan has been made skipper of the ferry."),
      ("Капитан парома у Перевоза, с первой воды. Двенадцать вёрст от дома, а не двенадцать тысяч. Каждый вечер дома, "
       "представляете? Я даже не знаю, что с ним делать. Привыкла, что муж — это письма.",
       "Skipper of the ferry at Perevoz, from the first open water. Twelve versts from home, not twelve thousand. Home "
       "every evening, can you imagine? I don't quite know what to do with him. I'd got used to a husband being letters."),
      stamp="a_ferry"),
    B(30, "4,5,6", "telegram", "anna", VALYA,
      ("У Анны и Степана родилась дочка.", "Anna and Stepan have a baby daughter."),
      ("«ПОЗДРАВЛЯЮ ВНУЧКОЙ ВЫЕЗЖАЮ МАМА». Уже едет. А это — Алёнка. Три двести, кричит, как пароходный гудок, вся в отца. "
       "Стёпа всем говорит: «У меня экипаж». Вот, возьмите карточку, первую. Она тут сердитая, но красивая.",
       "'CONGRATULATIONS ON GRANDDAUGHTER COMING MUM.' She's on her way. And this is Alyonka. Three kilos two hundred, "
       "she bellows like a ship's horn, her father all over. Styopa tells everyone, 'I've got a crew.' Here, take a "
       "photo, the very first. She's cross in it, but beautiful."),
      gift="a_photo_baby", stamp="a_moon", sets="anna.baby"),
    B(40, "6,7,8", "letter", "anna", ("Степан, паром «Перевоз»", "Stepan, the Perevoz ferry"),
      ("Степан пишет Анне с парома — хотя каждый вечер дома.", "Stepan writes to Anna from the ferry, though he's home every night."),
      ("«Анюта, ночи светлые, видел цаплю. Целуй Алёнку, расскажи ей про цаплю». Каждый вечер дома, а всё равно пишет. "
       "Привык. Вот, это он вам кораблик вырезал, второй — Алёнке. Говорит, почтальону без кораблика нельзя.",
       "'Anyuta, the nights are light, I saw a heron. Kiss Alyonka, tell her about the heron.' Home every evening and he "
       "still writes. He's used to it. Here, he carved you a little boat; the other is Alyonka's. He says a postman "
       "can't do without a boat."),
      gift="a_toy_boat", stamp="a_white_night"),
    )

# ================================================================ FEDOR
arc("fedor",
    B(5, "", "letter", "fedor", LENA,
      ("Фёдору Ильичу письмо от дочери из Вологды.", "A letter for Fyodor Ilyich from his daughter in Vologda."),
      ("Лена. Пишет: «Папа, не лазай на колесо». А кто полезет. Вал треснул. Дубовый, ещё отец ставил. "
       "Скрипит теперь, как я по утрам. Ничего. Дуб найдём.",
       "Lena. She writes, 'Dad, don't climb on the wheel.' And who else will? The shaft's cracked. Oak, my father put it "
       "in. Creaks now, like me in the mornings. Never mind. We'll find oak.")),
    B(18, "", "newspaper", "fedor", ("Общество мельничных мастеров", "Society of Millwrights"),
      ("Фёдору Ильичу пришёл бюллетень «Жернов».", "Fyodor Ilyich has a newsletter: The Millstone."),
      ("Мельники. Целое общество, в Кириллове. Бюллетень «Жернов», восемь страниц, и всё про колёса. Я думал, нас двое "
       "осталось: я да ветер. Напишу им. Отнесёте? Тут размеры вала и чертёж. Криво, но понятно.",
       "Millers. A whole society, in Kirillov. A newsletter, The Millstone, eight pages, all about wheels. I thought "
       "there were two of us left: me and the wind. I'll write to them. Will you post it? The shaft's measurements are "
       "in there, and a drawing. Crooked, but clear."),
      reply="out", stamp="a_mill"),
    B(30, "", "letter", "fedor", KROTOV,
      ("Мастер Кротов ответил Фёдору Ильичу про вал.", "Master Krotov answers Fyodor Ilyich about the shaft."),
      ("Савва Игнатьевич Кротов. Восемьдесят один год, сорок мельниц поставил. Пишет: дуб на вал рубят зимой и сушат "
       "три года. Трёх лет у меня нет. Дальше: «Не горюй, Фёдор, поищем старый». Фёдор. Будто мы в одной артели. "
       "Может, и в одной.",
       "Savva Ignatyevich Krotov. Eighty-one, built forty mills. He says oak for a shaft is felled in winter and "
       "dried three years. I haven't got three years. Then: 'Don't fret, Fyodor, we'll find an old one.' Fyodor. As if "
       "we were in the same crew. Maybe we are.")),
    B(30, "", "letter", "fedor", KROTOV,
      ("Кротов прислал Фёдору Ильичу чертёж.", "Krotov has sent Fyodor Ilyich a drawing."),
      ("Колесо стоит, и я при нём стою. Кротов шлёт чертёж, как шипы резать. Красиво рисует, старик. Вот, держите "
       "ключ от мельницы, запасной. Промокнете или замёрзнете на обходе — заходите, там печка. Не спорьте.",
       "The wheel's standing, and I stand by it. Krotov sends a drawing of how to cut the tenons. Draws beautifully, "
       "the old man. Here, take this key to the mill, the spare. If you get soaked or frozen on your round, come in, "
       "there's a stove. Don't argue."),
      gift="a_mill_key"),
    B(25, "", "newspaper", "fedor", ("Общество мельничных мастеров", "Society of Millwrights"),
      ("В «Жернове» написали про мельницу Фёдора Ильича.", "The Millstone has written about Fyodor Ilyich's mill."),
      ("Написали про нас. «Последняя действующая водяная мельница района». Последняя. Утешили. Фотография моя, "
       "сорокалетней давности, с усами. Усы я потом сбрил. Зря, пожалуй.",
       "They've written about us. 'The last working watermill in the district.' The last. That's a comfort. A photo "
       "of me, forty years old, with a moustache. I shaved it off later. A mistake, maybe.")),
    B(30, "", "letter", "fedor", KROTOV,
      ("Кротов нашёл для Фёдора Ильича сухой дуб.", "Krotov has found seasoned oak for Fyodor Ilyich."),
      ("Нашёл! Под Белозерском амбар разбирали, а там матица дубовая, сорок лет сохла. Пишет: «Летом пришлём "
       "с попутной». Слышите, как Липка шумит у плотины? Это она радуется. И я.",
       "He's found it! They were taking down a granary near Belozersk, and there was an oak beam, forty years drying. "
       "He writes, 'We'll send it in summer with a lorry going your way.' Hear the Lipka rushing at the dam? "
       "That's the river being glad. Me too.")),
    B(30, "6,7,8", "notice", "fedor", ("Транспортная контора, Белозерск", "Freight Office, Belozersk"),
      ("Фёдору Ильичу привезли дубовое бревно.", "An oak log has arrived for Fyodor Ilyich."),
      ("Бревно приехало. Шесть метров, лежит, как кит на берегу. Сергей с трактором обещал, без него не сдюжить. "
       "Кротов в записке: «Береги, Фёдор, это последний такой дуб в моей жизни». И в моей.",
       "The log's here. Six metres, lying there like a whale on a beach. Sergey's promised his tractor; can't manage "
       "without him. Krotov's note says, 'Look after it, Fyodor, it's the last oak like this in my life.' "
       "And in mine.")),
    B(20, "7,8,9", "parcel", "fedor", KROTOV,
      ("Кротов прислал Фёдору Ильичу своё тесло.", "Krotov has sent Fyodor Ilyich his own adze."),
      ("Тесло. Его. Семьдесят лет, рукоять вытерта до блеска, по ладони. Пишет: «Мне уже не держать, а тебе "
       "в самый раз». Ну. Стою вот. Не знаю, что сказать. Вы идите, у вас сумка тяжёлая.",
       "An adze. His. Seventy years old, the handle worn to a shine, to the shape of a palm. He writes, 'I can't hold "
       "it any more; it's just right for you.' Well. Here I stand. Don't know what to say. You go on, your bag's "
       "heavy.")),
    B(30, "8,9,10", "letter", "fedor", ("Общество мельничных мастеров", "Society of Millwrights"),
      ("Колесо мельницы пошло. Общество просит фотографию.", "The mill wheel turns again. The society wants a photo."),
      ("Колесо пошло. Во вторник, в шесть утра. Я сел на мостках и слушал. Час сидел, как мальчишка. Кротов просит "
       "карточку для «Жернова». Сергей снял, вышло две. Одну им, одну вам. Колесо на ней смазано. Это оно крутится.",
       "The wheel's going. Tuesday, six in the morning. I sat on the boards and listened. Sat an hour, like a boy. "
       "Krotov wants a photo for The Millstone. Sergey took them, two came out. One for them, one for you. The wheel's "
       "blurred. That's it turning."),
      gift="a_photo_mill", stamp="a_camera"),
    B(30, "10,11", "letter", "fedor", ("Надежда, пекарня, Кириллов", "Nadezhda, bakery, Kirillov"),
      ("Фёдору Ильичу пишет пекарь из Кириллова.", "A baker from Kirillov writes to Fyodor Ilyich."),
      ("Племянница Кротова, Надежда. Пекарня у неё. Пишет: на муке с камней хлеб живой, не то что фабричный. Предлагает "
       "печь. Печь у меня есть, русская, от отца. Отец в ней по субботам пёк. Я в ней валенки сушу. Непорядок.",
       "Krotov's niece, Nadezhda. Has a bakery. She writes that bread from stone-ground flour is alive, not like "
       "factory stuff. Says I should bake. I've an oven, a Russian stove, my father's. Father baked in it on Saturdays. "
       "I dry my felt boots in it. Not right.")),
    B(30, "12,1,2", "parcel", "fedor", ("Надежда, пекарня, Кириллов", "Nadezhda, bakery, Kirillov"),
      ("Фёдору Ильичу прислали по почте живую закваску.", "Fyodor Ilyich has received a live sourdough starter by post."),
      ("Закваска. Живая, в банке. По почте ехала, как барыня. Надежда велит кормить каждый день, мукой и водой. "
       "Как кошку. Назвал Марфой. Вы не смейтесь, она слышит.",
       "A starter. Alive, in a jar. Travelled by post like a lady. Nadezhda says feed it every day, flour and water. "
       "Like a cat. I've named her Marfa. Don't laugh, she can hear you.")),
    B(40, "2,3,4", "letter", "fedor", KROTOV,
      ("Фёдор Ильич испёк первый субботний хлеб.", "Fyodor Ilyich has baked his first Saturday bread."),
      ("Испёк. Первый. Корка трещит, мякиш дышит, Марфа довольна. Кротов пишет: «Пришли попробовать, а то не поверю». "
       "Отправлю. А вам горбушка, пока тёплая. Горбушка — лучшее. Не всякому даю.",
       "Baked it. The first. The crust crackles, the crumb breathes, Marfa's pleased. Krotov writes, 'Send me some, "
       "or I won't believe it.' I'll send it. And the heel's for you, while it's warm. The heel's the best part. "
       "I don't give it to just anyone."),
      reply="out", gift="a_bread_loaf", sets="fedor.bread"),
    B(40, "5,6,7,8", "newspaper", "fedor", ("«Сельская новь»", "Village News"),
      ("В «Сельской нови» написали про хлеб с мельницы.", "The Village News has written about the mill's bread."),
      ("В газете: «Субботний хлеб Фёдора Жукова». Теперь по субботам очередь с шести утра, из Городка едут. Пеку сорок "
       "буханок. Сорок первую не пеку, принцип. Вот, калач вам. Это не буханка, это сверх принципа.",
       "In the paper: 'Fyodor Zhukov's Saturday Bread'. Now there's a queue on Saturdays from six in the morning; "
       "people drive from Gorodok. I bake forty loaves. Not a forty-first: principle. Here, a kalach for you. "
       "That's not a loaf, that's beyond principle."),
      gift="a_kalach"),
    B(50, "1,2,3", "letter", "fedor", KROTOV,
      ("Кротов передал Фёдору Ильичу свой значок.", "Krotov has passed his badge to Fyodor Ilyich."),
      ("Кротов. Пишет, общество теперь на молодых, ему пора на лавочку. А мне — значок, «Почётный мельник», свой, "
       "пятьдесят седьмого года. Не по чину мне. А вернуть — обидеть. Приколю по субботам.",
       "Krotov. Says the society's for the young ones now, it's time he sat on a bench. And he's sent me a badge, "
       "'Honoured Miller', his own, from fifty-seven. Above my rank. But sending it back would offend him. "
       "I'll wear it on Saturdays.")),
    B(60, "9,10,11", "registered", "fedor", ("Областной центр наследия", "Regional Heritage Centre"),
      ("Мельницу Фёдора Ильича признали памятником.", "Fyodor Ilyich's mill has been declared a monument."),
      ("Памятник. Мельница теперь памятник техники, с табличкой. Я живой, а мельница уже памятник. Студенты приедут "
       "мерить. Пусть меряют. А хлеб по субботам — это не по их части. Это по моей.",
       "A monument. The mill's a monument of engineering now, with a plaque. I'm alive and the mill's already a "
       "monument. Students are coming to measure it. Let them. But Saturday bread isn't their department. "
       "That's mine."),
      stamp="a_mill_gold"),
    )

arc("fedor_petya",
    B(25, "", "letter", "fedor", PETYA,
      ("Петя прислал деду рисунок мельницы.", "Petya has sent his grandpa a drawing of the mill."),
      ("Внук. Петька. Нарисовал мельницу по памяти. Колесо у него почему-то с ушами. А похоже. Спрашивает, починили ли "
       "вал. Напишу: чиним.",
       "My grandson. Petya. Drew the mill from memory. For some reason the wheel has ears. Still, it's like. Asks if "
       "the shaft's mended. I'll write: we're mending it.")),
    B(30, "5,6,7", "telegram", "fedor", LENA,
      ("Телеграмма: Петя едет к деду на лето.", "A telegram: Petya is coming to his grandpa for the summer."),
      ("«ВСТРЕЧАЙ ПЕТЮ СУББОТУ АВТОБУС ЛЕНА». Едет. На всё лето. Раскладушку надо с чердака. И сахару. Петька без сахару "
       "не человек. И мышей на чердаке предупредить.",
       "'MEET PETYA SATURDAY BUS LENA.' He's coming. For the whole summer. Need the camp bed down from the loft. "
       "And sugar. Petya's not human without sugar. And warn the mice in the loft."),
      stamp="a_telegram"),
    B(20, "6,7,8", "letter", "fedor", LENA,
      ("Лена напоминает Пете про панаму.", "Lena reminds Petya about his sun hat."),
      ("Лена Петьке пишет: носи панаму. Панама у нас на пугале в огороде. Петька сам надел, сказал — вороне голову "
       "печёт. Ворона, кстати, не улетает. Уважает.",
       "Lena writes to Petya: wear your sun hat. The sun hat's on the scarecrow in the garden. Petya put it there "
       "himself, said the crow's head gets hot. The crow doesn't fly off, by the way. Respects it.")),
    B(25, "8,9", "postcard", "fedor", PETYA,
      ("Петя доехал до Вологды и уже скучает.", "Petya is back in Vologda and already misses the mill."),
      ("«Дед, я доехал. Скучаю по колесу и по тебе. Колесо на первом месте, но ты не обижайся». Честный. В меня. "
       "Дома тихо стало. Слишком.",
       "'Grandpa, I'm home. I miss the wheel and you. The wheel comes first, but don't be offended.' Honest. Takes "
       "after me. It's quiet in the house now. Too quiet.")),
    B(40, "10,11,12", "parcel", "fedor", PETYA,
      ("Петя прислал деду модель мельницы.", "Petya has sent his grandpa a model of the mill."),
      ("Модель. Сам клеил, из спичек и картона, колесо крутится, если дуть. Учительница поставила пять и спросила: "
       "«Где ты видел такую мельницу?» А он: «У деда». Вот так. У деда.",
       "A model. Glued it himself, from matches and card; the wheel turns if you blow on it. His teacher gave him "
       "top marks and asked, 'Where did you see a mill like this?' And he said, 'At Grandpa's.' There you are. "
       "At Grandpa's."),
      stamp="a_mill"),
    B(30, "12,1", "postcard", "fedor", PETYA,
      ("Новогодняя открытка от Пети.", "A New Year card from Petya."),
      ("«Дед, с Новым годом. Я вырос на четыре сантиметра. Колесо ещё не перерос». Перерастёт. Года через три. "
       "Тогда пусть сам на него и лезет, а я снизу покричу.",
       "'Happy New Year, Grandpa. I've grown four centimetres. Haven't outgrown the wheel yet.' He will. In about "
       "three years. Then he can climb it himself, and I'll shout from below."),
      stamp="a_fir"),
    B(30, "2,3", "letter", "fedor", PETYA,
      ("Петя поздравил деда с днём рождения.", "Petya wishes his grandpa a happy birthday."),
      ("Петька с днём рождения поздравляет. Пишет: «Дед, ты не старый, ты просто давно». Давно — это верно. "
       "Лена приписала, что летом опять пришлёт. Пришлёт. Куда она денется. Тут колесо.",
       "Petya's wishing me happy birthday. Writes, 'Grandpa, you're not old, you've just been around a long time.' "
       "A long time, that's true. Lena's added that she'll send him again in summer. She will. Where else? "
       "The wheel's here.")),
    B(40, "5,6", "letter", "fedor", PETYA,
      ("Петя просится к деду в помощники.", "Petya asks to be his grandpa's assistant."),
      ("Просится на работу: «Дед, возьми помощником, зарплату можно мукой». Мукой. Возьму. Только пусть ведро сам "
       "носит, а не рассказывает, как его носить.",
       "He's asking for a job: 'Grandpa, take me on as your assistant, you can pay me in flour.' In flour. I'll take "
       "him. As long as he carries the bucket himself and doesn't just explain how it's carried.")),
    B(30, "7,8", "parcel", "fedor", LENA,
      ("Лена прислала Пете журналы «Юный техник».", "Lena has sent Petya a bundle of Young Technician magazines."),
      ("Лена журналы прислала, Петьке. Читает вслух, про турбины. Я ему: колесо — та же турбина, только честная, "
       "всё на виду. Спорим вечерами. Вот, он вам свисток из ивы вырезал. Свистит. Громче, чем спорит.",
       "Lena's sent magazines for Petya. He reads them aloud, about turbines. I tell him a wheel's the same as a "
       "turbine, only honest, everything in plain sight. We argue in the evenings. Here, he's carved you a willow "
       "whistle. It whistles. Louder than he argues."),
      gift="a_whistle"),
    B(40, "9,10,11", "letter", "fedor", PETYA,
      ("Петя занял первое место на областном конкурсе.", "Petya has won first prize in a regional contest."),
      ("Грамота. Областной конкурс, первое место: «Водяная мельница: как она работает». Про мою. Жюри спросило, откуда "
       "он всё знает. «Дед показал». Вот, пишет. Дед. Ну.",
       "A certificate. A regional contest, first place: 'The Watermill: How It Works'. About mine. The judges asked "
       "him how he knew it all. 'Grandpa showed me.' There, he writes it. Grandpa. Well.")),
    B(40, "12,1,2", "letter", "fedor", PETYA,
      ("Петя печёт в Вологде хлеб на дедовой закваске.", "Petya is baking in Vologda with his grandpa's starter."),
      ("Я Петьке кусок Марфы послал, в банке. Пишет: «Дед, у меня Марфа поднимается хуже, наверно, скучает». "
       "Скучает, конечно. Она деревенская. Пошлю муки своей. На своей поднимется.",
       "I posted Petya a bit of Marfa, in a jar. He writes, 'Grandpa, my Marfa doesn't rise as well, she must be "
       "homesick.' Of course she is. She's a village girl. I'll send some of my flour. She'll rise on her own."),
      needs="fedor.bread", reply="out"),
    B(40, "5,6", "letter", "fedor", PETYA,
      ("Петя решил стать инженером-гидротехником.", "Petya has decided to be a hydraulic engineer."),
      ("Едет на всё лето. И сообщает: решил, будет инженером-гидротехником. Плотины строить. Напишу ему: начни "
       "с нашей. Она течёт.",
       "He's coming for the whole summer. And announces he's decided to be a hydraulic engineer. To build dams. "
       "I'll write back: start with ours. It leaks.")),
    B(40, "8,9", "postcard", "fedor", PETYA,
      ("Петя просит деда никогда не продавать мельницу.", "Petya asks his grandpa never to sell the mill."),
      ("«Дед, мельницу не продавай, я её потом сам». Продавай. Кто её купит. Хотя теперь уж точно не продам. Лена "
       "карточку прислала: мы с Петькой у колеса. Он мне уже по ухо. Берите, у меня вторая есть.",
       "'Grandpa, don't sell the mill, I'll take it on later.' Sell it. Who'd buy it? Though now I certainly won't. "
       "Lena sent a photo: Petya and me at the wheel. He comes up to my ear now. Take it, I've a second one."),
      gift="a_photo_petya", stamp="a_camera"),
    )

# ================================================================ AGAFYA
arc("agafya",
    B(1, "", "notice", "agafya", ("Пенсионный фонд", "Pension Fund"),
      ("Агафье Петровне — пенсия и казённая бумага.", "Agafya Petrovna's pension and an official paper."),
      ("Пенсия — это хорошо, спасибо. А писем-то и нет. Одни казённые бумажки, будто я учреждение. Погрейтесь, "
       "погрейтесь. Руки-то какие холодные! Почтальону мёрзнуть, как воробью на заборе, — дело ли?",
       "The pension, good, thank you. But letters there are none. Only official papers, as though I were an "
       "institution. Warm yourself, do. Such cold hands! A postman freezing like a sparrow on a fence — is that right?")),
    B(12, "", "notice", "agafya", ("Энергосбыт", "Electricity Company"),
      ("Агафье Петровне пришёл счёт за свет.", "An electricity bill for Agafya Petrovna."),
      ("Опять за свет. Я одну лампочку жгу, на кухне, а пишут, будто тут завод. Ну, копейка рубль бережёт, заплачу. "
       "Вы мне только скажите честно: письма-то люди ещё пишут? Или одни счета остались?",
       "The electricity again. I burn one bulb, in the kitchen, and they write as if I ran a factory. Well, look after "
       "the kopecks; I'll pay. Only tell me honestly: do people still write letters? Or is it just bills now?")),
    B(14, "", "letter", "agafya", ("Возврат: «адресат выбыл»", "Returned: addressee moved"),
      ("Письмо Агафьи Петровны сестре вернулось назад.", "Agafya Petrovna's letter to her sister came back."),
      ("Вернулось. «Адресат выбыл». Это я Клаве писала, сестре, в Кондопогу. Тридцать лет не писала, гордые мы обе, "
       "а тут собралась. А её там нет. Вы не знаете, как людей ищут? Спросите на почте. Не за себя прошу. За Клаву.",
       "It's come back. 'Addressee moved.' I wrote to Klava, my sister, in Kondopoga. Thirty years I didn't write, "
       "we're both proud, and then I made up my mind. And she's not there. Do you know how people are found? Ask at "
       "the post office. I'm not asking for me. For Klava."),
      stamp="a_letter"),
    B(10, "", "parcel", "agafya", ("Пряжа почтой, Ярославль", "Yarn by Post, Yaroslavl"),
      ("Агафье Петровне пришла пряжа.", "Agafya Petrovna's yarn has arrived."),
      ("Пряжа пришла, овечья. А это вам — варежки, с узором. Не спорьте: зима спросит, что летом припасено. "
       "И про Клаву не забудьте, ладно? Я по ночам думаю: может, ей там холодно, а я и не знаю.",
       "My yarn's come, sheep's wool. And these are for you: mittens, patterned. Don't argue; winter will ask what "
       "summer put by. And don't forget about Klava, will you? At night I keep thinking: maybe she's cold there, "
       "and I don't even know."),
      gift="a_mittens"),
    B(14, "", "letter", "me", ("Адресное бюро, Кондопога", "Address Bureau, Kondopoga"),
      ("Почтальону ответили из Кондопоги про Клавдию.", "Kondopoga has answered the postman about Klavdia."),
      ("Уважаемый почтальон! На ваш запрос сообщаем: Хуттунен (урождённая Мальцева) Клавдия Петровна, 1952 г. р., "
       "выбыла из г. Кондопога в 2009 году. Новое место жительства в нашей картотеке не указано. Рекомендуем обратиться "
       "в адресно-справочную службу Республики Карелия. С уважением, инспектор Н. Р. Лукина. P. S. От себя: напишите "
       "соседям по старому адресу. Соседи всегда знают больше картотеки.",
       "Dear postman, in reply to your enquiry: Huttunen (née Maltseva), Klavdia Petrovna, born 1952, left the town "
       "of Kondopoga in 2009. Her new place of residence is not recorded in our files. We recommend contacting the "
       "address bureau of the Republic of Karelia. Yours, Inspector N. R. Lukina. P.S. A word of my own: write to the "
       "neighbours at the old address. Neighbours always know more than the files.")),
    B(20, "", "letter", "agafya", ("Г. Ойнонен, Кондопога", "G. Oinonen, Kondopoga"),
      ("Агафье Петровне ответила бывшая соседка Клавдии.", "Klavdia's old neighbour has written to Agafya Petrovna."),
      ("Соседка Клавина ответила, Галина. Помнит! Клава, пишет, уехала к сыну в Петрозаводск, и кота забрала, рыжего. "
       "Кот-то мне зачем... А всё равно приятно, что рыжий. Язык до Киева доведёт, а письмо, видно, — до Петрозаводска.",
       "Klava's neighbour wrote back, Galina. She remembers! Klava, she says, moved to her son's in Petrozavodsk, and "
       "took the cat, a ginger one. What do I want with a cat... Still, it's nice that he's ginger. Ask your way and "
       "you'll get to Kiev, they say; and a letter, it seems, gets to Petrozavodsk.")),
    B(21, "", "letter", "me", ("Адресная служба, Петрозаводск", "Address Bureau, Petrozavodsk"),
      ("Из Петрозаводска: письмо Агафьи Петровны передали сестре.", "Petrozavodsk: Agafya Petrovna's letter has reached her sister."),
      ("Уважаемый почтальон! Сообщить адрес гражданки Хуттунен К. П. мы не вправе. Однако вложенное в ваш запрос "
       "письмо от Агафьи Петровны Сорокиной я отнесла адресату лично, после работы, — живёт она недалеко от меня. "
       "Так не положено, но я давно в этой службе, а у меня тоже есть сестра. Клавдия Петровна прочла при мне "
       "и долго молчала. Ждите ответа. Инспектор Е. Корпела.",
       "Dear postman, we are not permitted to give out the address of Citizen K. P. Huttunen. However, I took the "
       "letter from Agafya Petrovna Sorokina enclosed with your enquiry to the addressee myself, after work; she lives "
       "near me. It's not the procedure, but I've been in this job a long time, and I have a sister too. Klavdia "
       "Petrovna read it in front of me and was silent a long while. Expect a reply. Inspector E. Korpela.")),
    B(18, "", "letter", "agafya", KLAVA,
      ("Агафье Петровне пришло письмо от сестры Клавдии.", "A letter for Agafya Petrovna from her sister Klavdia."),
      ("Клава. Клавочка. Пишет: «Гаша, я думала, тебя давно нет, а ты вон какая — с почерком». С почерком! "
       "Вы садитесь. Нет, стойте, я чайник... Вы только не уходите сразу. Одна я это сейчас не дочитаю, глаза не видят.",
       "Klava. My Klavochka. She writes, 'Gasha, I thought you were long gone, and look at you, with handwriting and "
       "all.' Handwriting! Sit down. No, wait, the kettle... Just don't leave straight away. I can't finish it alone "
       "just now, my eyes won't see."),
      stamp="a_onego", sets="agafya.found"),
    B(14, "", "letter", "agafya", KLAVA,
      ("Клавдия прислала сестре свою фотографию.", "Klavdia has sent her sister a photograph."),
      ("Карточку прислала. Вот она, Клава. Нос наш, мальцевский, никуда не делся. А шляпка — это её Карелия испортила, "
       "у нас так не носят. Говорят, лучше поздно, чем никогда. Да кто так говорит — тот, видно, не ждал.",
       "She's sent a photo. There she is, Klava. Our nose, the Maltsev nose, it hasn't gone anywhere. The hat's "
       "Karelia's doing, we don't wear them like that here. Better late than never, they say. Whoever says so never "
       "had to wait, I reckon."),
      reply="out"),
    B(30, "11,12,1,2,3", "letter", "agafya", KLAVA,
      ("У Клавдии в Петрозаводске зима.", "It's winter in Klavdia's Petrozavodsk."),
      ("Пишет, Онего у них подо льдом, ветер с озера шапку снимает. А носков шерстяных у неё нет! В Карелии живёт — и нет. "
       "Свяжу к пятнице, отправите? И вам пару, серые. Берите, говорю, у вас ноги вечно мокрые.",
       "She writes that Onega's under ice, the wind off the lake takes your hat clean off. And she has no woollen socks! "
       "Lives in Karelia and has none. I'll knit some by Friday; will you post them? And a pair for you, grey. Take "
       "them, I say; your feet are forever wet."),
      reply="out", gift="a_socks_grey", stamp="a_snow"),
    B(30, "", "parcel", "agafya", KLAVA,
      ("Клавдия прислала сестре морошки.", "Klavdia has sent her sister cloudberries."),
      ("Морошка! Клава прислала, три банки. Сама собирала, на болоте, с внучкой. В семьдесят с лишним — по болоту! "
       "Мальцевская порода. Возьмите банку. Мне одной столько не съесть, а вам — от простуды.",
       "Cloudberries! Klava's sent three jars. Picked them herself, on the bog, with her granddaughter. Past seventy "
       "and out on a bog! That's Maltsev stock. Take a jar. I can't eat all that alone, and it's good for your colds."),
      gift="a_jar_cloudberry", stamp="a_cloudberry"),
    B(30, "", "letter", "agafya", KLAVA,
      ("Клавдия вспоминает мамину голубую чашку.", "Klavdia remembers their mother's blue cup."),
      ("Клава вспоминает мамину чашку, голубую, с отбитым краем. Думала, разбилась давно. А вот она, гляньте. "
       "Я из неё сорок лет чай пью, отбитым краем от себя. Нарисую ей. Пусть знает, что ничего не пропало.",
       "Klava remembers Mother's cup, the blue one with the chipped rim. She thought it broke long ago. And here it is, "
       "look. I've drunk my tea from it for forty years, chipped side away from me. I'll draw it for her. Let her know "
       "nothing's been lost."),
      stamp="a_cup"),
    B(30, "1,2,3,4,5", "letter", "agafya", KLAVA,
      ("Клавдия хочет летом приехать к сестре.", "Klavdia wants to visit her sister in the summer."),
      ("Летом приехать хочет. Ко мне! А у меня потолок закоптился, крыльцо скрипит, занавески с прошлой жизни. "
       "Знаю, знаю, не за занавесками едет. Ну, не красна изба углами, а красна пирогами. Пирогов напеку.",
       "She wants to come in summer. To me! And my ceiling's sooty, the porch creaks, the curtains are from another "
       "life. I know, I know, she's not coming for the curtains. Well, a house isn't fine for its corners but for its "
       "pies. I'll bake pies.")),
    B(40, "6,7", "telegram", "agafya", KLAVA,
      ("Телеграмма Агафье Петровне: Клавдия выезжает.", "A telegram for Agafya Petrovna: Klavdia is on her way."),
      ("«ВЫЕЗЖАЮ ПОНЕДЕЛЬНИК ПОЕЗДОМ ВСТРЕЧАЙ КЛАВА». В понедельник! Ох, руки трясутся, как у молоденькой. "
       "Сергей обещал до станции довезти. Хороший он, Сергей. Все хорошие, все. И вы. А шарф где ваш?",
       "'LEAVING MONDAY BY TRAIN MEET ME KLAVA.' Monday! Oh, my hands are shaking like a girl's. Sergey's promised to "
       "drive me to the station. He's a good man, Sergey. Everyone's good, everyone. You too. And where's your scarf?"),
      stamp="a_telegram"),
    B(25, "7,8", "letter", "agafya", KLAVA,
      ("Клавдия уехала домой и уже пишет.", "Klavdia is home and already writing."),
      ("Доехала Клава. Пишет: «Гаша, я дома, а всё пахнет твоей печкой». Две недели проговорили, а главного так "
       "и не сказали. Значит, ещё приедет. Вот, пирог черничный, с проводов остался. Ешьте, ешьте.",
       "Klava's home. She writes, 'Gasha, I'm home, and everything smells of your stove.' Two weeks of talking and we "
       "never said the main thing. So she'll come again. Here, bilberry pie, left over from seeing her off. "
       "Eat, eat."),
      gift="a_pie_berry"),
    B(30, "8,9,10", "parcel", "agafya", KLAVA,
      ("Клавдия прислала книгу карельских узоров.", "Klavdia has sent a book of Karelian knitting patterns."),
      ("Клава книжку прислала, узоры карельские. Глаз не оторвать. Лидия Аркадьевна говорит, в клубе по четвергам "
       "свободно. Может, девчонок поучить? Руки пока помнят. Глаза боятся, а руки делают.",
       "Klava's sent a book of Karelian patterns. You can't take your eyes off them. Lidia Arkadyevna says the club's "
       "free on Thursdays. Maybe I could teach the girls? My hands still remember. The eyes are afraid, but the hands "
       "get on with it.")),
    B(21, "10,11", "notice", "agafya", ("Клуб, Л. А. Белова", "The club, L. A. Belova"),
      ("Агафье Петровне прислали афишу вязального кружка.", "Agafya Petrovna has the poster for her knitting circle."),
      ("Лидия Аркадьевна афишку прислала, показать. «Вязальный кружок «Петелька». Ведёт А. П. Сорокина». Ведёт! "
       "Как будто я трактор. Ну, раз веду — поведу. Варю Кузнецову первой запишу, у неё глаз хороший.",
       "Lidia Arkadyevna's sent me the poster to look at. 'Knitting circle: The Little Loop. Led by A. P. Sorokina.' "
       "Led! As if I were a tractor. Well, if I'm leading, I'll lead. I'll sign up Varya Kuznetsova first; she has "
       "a good eye.")),
    B(25, "11", "postcard", "agafya", KLAVA,
      ("Клавдия поздравила сестру с днём рождения.", "Klavdia sends her sister birthday wishes."),
      ("Клава поздравляет. Пишет: «Гаша, я тебя всю жизнь догоняю и не догоню». А это отнесите Варе: варежки, "
       "в синюю полоску, первые кружковые. Правая чуть длиннее. Под радио вязала, заслушалась. Пусть не обижается.",
       "Klava's sent birthday wishes. She writes, 'Gasha, I've chased you all my life and never caught up.' And take "
       "these to Varya: mittens, blue-striped, the circle's first. The right one's a bit longer. I was knitting to the "
       "radio and got carried away. Tell her not to mind."),
      on="11-26", reply="varya", stamp="a_birthday", sets="agafya.mittens"),
    B(40, "", "letter", "agafya", KLAVA,
      ("Клавдия пишет: в телефон не поплачешь.", "Klavdia writes: you can't cry into a phone."),
      ("Внучка Клаве телефон подарила, с картинками. А Клава пишет: «В телефон, Гаша, не поплачешь, а в письмо можно». "
       "И правда. Вон, пятнышко на строчке. Это не дождь. Вы же видите, что не дождь.",
       "Klava's granddaughter gave her a phone, with pictures. And Klava writes, 'You can't cry into a phone, Gasha, "
       "but you can into a letter.' It's true. Look, a spot on the line. That's not rain. You can see it's not rain.")),
    B(40, "4,5,6", "letter", "agafya", KLAVA,
      ("Клавдия посадила у себя во дворе липу.", "Klavdia has planted a linden in her yard."),
      ("Клава у себя во дворе липу посадила. «Чтобы и у меня была Липовка, маленькая». Пока с карандаш. Липа долго "
       "растёт, зато долго и живёт. Как мы с ней. Возьмите липового цвету, у меня мешок с прошлого лета.",
       "Klava's planted a linden in her yard. 'So I'll have a Lipovka too, a little one.' It's the size of a pencil "
       "for now. Lindens grow slowly, but they live long. Like the two of us. Take some linden blossom; I've a whole "
       "sack from last summer."),
      gift="a_tea_linden", stamp="a_linden"),
    B(50, "8,9,10", "parcel", "agafya", KLAVA,
      ("Клавдия нашла старую карточку двух сестёр.", "Klavdia has found an old photo of the two sisters."),
      ("Клава карточку нашла, шестьдесят первого года. Мы на Липке: я с косой, она с бантом, обе босые. Две напечатала. "
       "Одну мне, а другую, пишет, «почтальону, который нас нашёл». Это вам. Не спорьте. Это вы нас нашли.",
       "Klava found a photo from 1961. Us by the Lipka: me with a plait, her with a bow, both barefoot. She had two "
       "printed. One for me, and the other, she writes, 'for the postman who found us'. It's yours. Don't argue. "
       "You found us."),
      gift="a_photo_sisters", stamp="a_camera"),
    )

arc("agafya_fedor",
    B(45, "", "parcel", "agafya", FEDOR,
      ("Агафье Петровне — посылка с мельницы.", "A parcel from the mill for Agafya Petrovna."),
      ("С мельницы. Мука ржаная, два кило, и записка: «Агафья Петровна. Свежий помол. Денег не надо. Ф. Ж.» "
       "Денег не надо... Сорок лет мимо ходил, шапку снимал, а тут — мука. Ну, в долгу не останусь.",
       "From the mill. Rye flour, two kilos, and a note: 'Agafya Petrovna. Fresh-ground. No money needed. F. Zh.' "
       "No money needed... Forty years he walked past and raised his cap, and now: flour. Well, I won't stay "
       "in his debt."),
      needs="agafya.found"),
    B(3, "", "parcel", "fedor", AGAFYA,
      ("Фёдору Ильичу — носки от Агафьи Петровны.", "Socks from Agafya Petrovna for Fyodor Ilyich."),
      ("Носки. Мне. Размер откуда знает? Глаз, видно. Тёплые. Скажите ей... Нет, ничего не говорите. Сам скажу. Потом.",
       "Socks. For me. How does she know my size? A good eye, must be. Warm. Tell her... No, don't tell her anything. "
       "I'll tell her myself. Later.")),
    B(40, "3,4", "letter", "agafya", FEDOR,
      ("Фёдор Ильич зовёт Агафью Петровну смотреть ледоход.", "Fyodor Ilyich invites Agafya Petrovna to watch the ice go."),
      ("«Лёд пойдёт на днях. С плотины видно лучше всего. Приходите. Ф.» Одна строчка, а сколько он бумаги извёл — "
       "видите, нажим разный, переписывал. Пойти, что ли? Пойду. В голубом платке.",
       "'The ice will go any day now. You see it best from the dam. Come. F.' One line, and look how much paper he "
       "used up; the pressure's different, he rewrote it. Should I go? I'll go. In my blue headscarf.")),
    B(30, "", "postcard", "fedor", KLAVA,
      ("Фёдору Ильичу пришла открытка из Петрозаводска.", "A postcard from Petrozavodsk for Fyodor Ilyich."),
      ("Из Петрозаводска. Сестра её. Пишет: «Фёдор Ильич, берегите Гашу, она у нас одна». Беречь. Я и так... Ну. "
       "Берегу. Ледоход вот вместе смотрели. Это считается?",
       "From Petrozavodsk. Her sister. Writes, 'Fyodor Ilyich, take care of Gasha, she's the only one we've got.' "
       "Take care. I already... Well. I do. We watched the ice go together. Does that count?")),
    B(30, "9,10,11", "postcard", "agafya", PETYA,
      ("Петя, внук мельника, пишет Агафье Петровне.", "Petya, the miller's grandson, writes to Agafya Petrovna."),
      ("Петя, Фёдора Ильича внук, из Вологды: «Бабушка Агафья, спасибо за носки, я в них в школу хожу». Бабушка! "
       "Своих внуков не довелось, а тут — бабушка. В моих носках в школу ходит. Свяжу ещё, на вырост.",
       "Petya, Fyodor Ilyich's grandson, from Vologda: 'Granny Agafya, thank you for the socks, I wear them to "
       "school.' Granny! I never had grandchildren of my own, and now: granny. Going to school in my socks. "
       "I'll knit more, a size up.")),
    B(40, "11,12,1,2", "letter", "agafya", FEDOR,
      ("Фёдор Ильич написал Агафье Петровне письмо. Настоящее.", "Fyodor Ilyich has written Agafya Petrovna a real letter."),
      ("Письмо, на двух листах. «Агафья Петровна, пишу, потому что вслух у меня не выходит. Весной картошку сажать "
       "вдвоём сподручнее». Это он что ж — сватается? Под восемьдесят — картошкой? Ох. Постойте рядом, не уходите.",
       "A letter, two pages. 'Agafya Petrovna, I'm writing because out loud it won't come. Planting potatoes in spring "
       "goes easier with two.' What's this, is he courting? Nearly eighty, and with potatoes? Oh. Stand here a minute, "
       "don't go."),
      stamp="a_heart"),
    B(5, "", "letter", "fedor", AGAFYA,
      ("Агафья Петровна ответила Фёдору Ильичу.", "Agafya Petrovna has answered Fyodor Ilyich."),
      ("Ответила. «Картошку — согласная. А там поглядим». Согласная. На картошку. Это, по-нашему, уже много. "
       "Вы идите. Я тут посижу.",
       "She's answered. 'The potatoes: I'm agreed. And then we'll see.' Agreed. To the potatoes. Around here, that's "
       "a great deal. You go on. I'll sit here a while.")),
    B(40, "5,6", "letter", "agafya", LENA,
      ("Агафье Петровне пишет дочь Фёдора Ильича.", "Fyodor Ilyich's daughter writes to Agafya Petrovna."),
      ("Лена, дочка Фёдора Ильича. Пишет: «Папа написал, что картошку вы посадили вдвоём. Он за десять лет первый раз "
       "написал больше трёх строк — и все про вас». Что ж он там про меня? Не пишет. И правильно.",
       "Lena, Fyodor Ilyich's daughter. She writes, 'Dad wrote that you planted the potatoes together. In ten years "
       "that's the first time he's written more than three lines, and all of them about you.' What did he say about "
       "me? She doesn't write. Quite right too.")),
    B(40, "6,7", "letter", "agafya", KLAVA,
      ("Клавдия написала сразу двоим: Агафье и Фёдору.", "Klavdia has written to both of them: Agafya and Fyodor."),
      ("Гляньте на конверт: «Ф. И. Жукову и А. П. Сорокиной». Обоим! Клава летом приедет — «к вам обоим». "
       "Уже и в Петрозаводске знают, а я сама ещё не знаю. Вот, васильков нарвала. Сегодня раздавать хочется.",
       "Look at the envelope: 'To F. I. Zhukov and A. P. Sorokina.' Both of us! Klava's coming in summer, 'to you "
       "both'. They know in Petrozavodsk already, and I don't know myself yet. Here, I picked cornflowers. Today I "
       "feel like giving things away."),
      gift="a_cornflowers", stamp="a_rainbow"),
    )

# ================================================================ TEACHER
arc("teacher",
    B(4, "", "letter", "teacher", ILYA,
      ("Николаю Семёновичу письмо от ученика-астронома.", "A letter for Nikolai Semyonovich from a pupil who became an astronomer."),
      ("Илья Ковалёв, выпуск девяносто восьмого. По поведению — двойка, по всему остальному — неприлично хорошо. "
       "Теперь астроном, в горах. Снег у них в мае, зеркало шесть метров. Я ему когда-то говорил, что в Липовке звёзды "
       "не хуже. Соврал, конечно. Но педагогически.",
       "Ilya Kovalyov, class of ninety-eight. Conduct: poor. Everything else: indecently good. An astronomer now, in "
       "the mountains. Snow in May, a six-metre mirror. I once told him the stars in Lipovka are no worse. A lie, of "
       "course. But a pedagogical one."),
      stamp="a_observatory"),
    B(15, "", "postcard", "teacher", ("Т. Белова, Калининград", "T. Belova, Kaliningrad"),
      ("Ученица семьдесят девятого года пишет учителю.", "A pupil from the class of '79 writes to her teacher."),
      ("Таня Белова, семьдесят девятый год. «Вы мне поставили тройку по физике, а я тридцать лет проработала "
       "на электростанции». Вот видите. Тройка — тоже путёвка в жизнь. Иногда даже прямее пятёрки: человеку есть "
       "что доказывать.",
       "Tanya Belova, class of seventy-nine. 'You gave me a C in physics, and I worked thirty years at a power "
       "station.' There you are. A C is a ticket into life as well. Sometimes a more direct one than an A: "
       "the person has something to prove.")),
    B(20, "", "letter", "teacher", ("Г. Сычёв, Череповец", "G. Sychov, Cherepovets"),
      ("Бывший ученик признался учителю в старой проделке.", "A former pupil confesses an old prank to his teacher."),
      ("Геннадий Сычёв, главный инженер. Признаётся, что лягушку в мой стол в восемьдесят пятом посадил он, и просит "
       "прощения. Сорок лет совесть мучила. Я знал, Гена. Я всегда знал. Лягушку звали Ньютон, и она была лучшей "
       "ученицей в том классе.",
       "Gennady Sychov, chief engineer. He confesses that he put the frog in my desk in eighty-five, and asks "
       "forgiveness. Forty years his conscience has troubled him. I knew, Gena. I always knew. The frog was called "
       "Newton, and she was the best pupil in that class.")),
    B(10, "8,9,10", "postcard", "teacher", ("Липовская школа", "Lipovka School"),
      ("Николая Семёновича зовут в школу на праздник.", "Nikolai Semyonovich is invited to a school celebration."),
      ("Школа зовёт на праздник. Восьмой год обходятся без меня, и всё-таки зовут. Пойду. Галстук у меня тот же, "
       "что в восемьдесят втором. Он уже сам знает дорогу.",
       "The school has invited me to their celebration. For eight years now they've managed without me, and "
       "still they invite me. I'll go. My tie is the same one as in eighty-two. It knows the way by itself."),
      stamp="a_school_bell"),
    B(30, "", "parcel", "teacher", ILYA,
      ("Илья прислал учителю карту звёздного неба.", "Ilya has sent his teacher a star map."),
      ("Илья прислал подвижную карту неба. Две! Одну, пишет, вам, «а другую отдайте тому, кто в Липовке раньше всех "
       "встаёт». Раньше всех у нас встаёте вы, это проверено. Держите. Повернёте круг на число и час — и небо ваше.",
       "Ilya's sent a rotating star map. Two! One, he writes, is mine, 'and give the other to whoever gets up "
       "earliest in Lipovka.' That's you, it's been verified. Here. Turn the disc to the date and hour, and the sky "
       "is yours."),
      gift="a_map_star"),
    B(30, "", "letter", "teacher", ZUEVA,
      ("Бывшая ученица уговаривает учителя писать мемуары.", "A former pupil urges the teacher to write a memoir."),
      ("Марина Зуева, выпуск девяносто первого, теперь редактор. Требует воспоминаний: «Сорок выпусков — сорок глав». "
       "Я посчитал: сорок одна. В девяносто четвёртом выпуск был из одного человека. Он теперь ветеринар и до сих пор "
       "единственный отличник в своём классе.",
       "Marina Zueva, class of ninety-one, an editor now. She demands a memoir: 'Forty graduations, forty chapters.' "
       "I counted: forty-one. In ninety-four the graduating class was one person. He's a vet now, and still the only "
       "straight-A pupil in his class.")),
    B(30, "", "parcel", "teacher", ILYA,
      ("Илья нашёл ленту для старой пишущей машинки.", "Ilya has found a ribbon for the old typewriter."),
      ("Лента для машинки! Моей «Москве» шестьдесят лет, лент к ней не делают с прошлого века, а Илья нашёл. "
       "Стучу теперь по вечерам. Агафья Петровна через забор спрашивает, не завёлся ли у меня дятел. Завёлся. "
       "Мемуарный.",
       "A typewriter ribbon! My Moskva is sixty years old, nobody's made ribbons for it since the last century, and "
       "Ilya found one. Now I tap away in the evenings. Agafya Petrovna asks over the fence whether I've got a "
       "woodpecker. I have. A memoir woodpecker.")),
    B(25, "", "letter", "teacher", ("В. Ершова, Сокол", "V. Yershova, Sokol"),
      ("Учителю пишет его самый первый выпуск.", "The teacher's very first class writes to him."),
      ("Валентина Ершова, мой первый выпуск, семьдесят восьмой. Вспоминает, что я их боялся больше, чем они меня. "
       "Правда. Мне было двадцать три, им семнадцать, а у Вали коса до пояса и взгляд инспектора. Будет первая глава. "
       "Называется «Страх».",
       "Valentina Yershova, my first class, seventy-eight. She remembers that I was more afraid of them than they "
       "were of me. True. I was twenty-three, they were seventeen, and Valya had a plait to her waist and the look "
       "of an inspector. That's chapter one. It's called 'Fear'.")),
    B(30, "", "letter", "teacher", CHESS,
      ("Учитель продолжает шахматную партию по почте.", "The teacher's chess game by post goes on."),
      ("Аркадий Львович из Томска. Мы с ним с семьдесят четвёртого играем по почте. Сто двенадцатая партия. Пишет: "
       "«Конь f3». Я так и знал. Он всегда так ходит, когда у него спина болит. Отвечу через неделю, пусть поволнуется.",
       "Arkady Lvovich from Tomsk. We've played chess by post since seventy-four. Game one hundred and twelve. He "
       "writes: 'Knight f3.' I knew it. He always plays that when his back hurts. I'll answer in a week; let him "
       "fret."),
      reply="out", stamp="a_knight"),
    B(30, "3,4", "letter", "teacher", ILYA,
      ("Илья пишет учителю о новой комете.", "Ilya writes to his teacher about a new comet."),
      ("Илья пишет: открыли комету, через год подлетит к нам, будет видна даже в бинокль. Обещает приехать с телескопом. "
       "Прислал туманности, открытки. Одну возьмите. Подожду. Комета летела тысячи лет, я уж год как-нибудь потерплю.",
       "Ilya writes that a comet's been discovered; in a year it'll come close enough to see even with binoculars. "
       "He promises to come with a telescope. He sent postcards of nebulae; take one. I'll wait. The comet's been "
       "flying for thousands of years; I can manage a year."),
      gift="a_postcard_space"),
    B(30, "", "letter", "teacher", ("Л. Шапошников, ледокол", "L. Shaposhnikov, icebreaker"),
      ("Учителю пишет ученик — капитан ледокола.", "A pupil who became an icebreaker captain writes to the teacher."),
      ("Лёня Шапошников, капитан ледокола. Пишет из Арктики: «Николай Семёнович, полярное сияние — это не только "
       "ионизация». Конечно, не только. Ещё и красиво. В восемьдесят девятом я им этого не сказал, не по программе было. "
       "Говорю теперь.",
       "Lyonya Shaposhnikov, icebreaker captain. He writes from the Arctic: 'Nikolai Semyonovich, the aurora isn't "
       "only ionisation.' Of course not. It's beautiful too. In eighty-nine I didn't tell them that; it wasn't on the "
       "syllabus. I'm telling them now."),
      stamp="a_icebreaker"),
    B(30, "", "registered", "teacher", ZUEVA,
      ("Рукопись учителя вернулась от редактора.", "The teacher's manuscript is back from the editor."),
      ("Рукопись вернулась. Зуева исправила мне запятые. Красным! Сорок лет я исправлял красным. Сижу, смотрю: "
       "справедливо, все до одной. Ученики растут, а учителя, как видите, учатся.",
       "The manuscript's back. Zueva has corrected my commas. In red! For forty years I corrected in red. I sit and "
       "look: fair, every last one. Pupils grow up, and teachers, as you see, learn.")),
    B(30, "6,7,8", "letter", "teacher", CHESS,
      ("Шахматный соперник из Томска сдался.", "The chess rival in Tomsk has resigned."),
      ("Аркадий Львович сдался. Пятьдесят лет, сто двенадцать партий, и я впереди на одно очко. Пишет: «Играем сто "
       "тринадцатую, в отместку». Я ответил: e2–e4. Как в семьдесят четвёртом. Пусть думает, что это ностальгия. "
       "А это дебют.",
       "Arkady Lvovich has resigned. Fifty years, a hundred and twelve games, and I'm ahead by one point. He writes, "
       "'Game one hundred and thirteen, for revenge.' I replied: e2–e4. As in seventy-four. Let him think it's "
       "nostalgia. It's an opening."),
      reply="out", stamp="a_knight"),
    B(40, "9,10,11", "parcel", "teacher", ZUEVA,
      ("Вышла книга учителя — «Сорок выпусков».", "The teacher's book is out: Forty Graduations."),
      ("Книга. «Сорок выпусков», триста экземпляров, синяя обложка. Пахнет типографией, как новый учебник. Это вам, "
       "подписал: «Почтальону Липовки, который приносил мне мои выпуски». Не читайте сразу. Прочтите зимой.",
       "The book. Forty Graduations, three hundred copies, a blue cover. It smells of the printing house, like a new "
       "textbook. This one's yours, I've signed it: 'To the postman of Lipovka, who brought me my graduates.' Don't "
       "read it at once. Read it in winter."),
      gift="a_book_memoir", stamp="a_book", sets="teacher.book"),
    B(30, "", "letter", "teacher", ("В. Гусев, Тотьма", "V. Gusev, Totma"),
      ("Бывший ученик обиделся, что его нет в книге.", "A former pupil is hurt not to be in the book."),
      ("Витя Гусев обиделся, что его нет в книге. Есть! Страница сто двенадцать: «один ученик с рогаткой». Не узнал себя. "
       "Значит, исправился. Отвечу, что исправившихся по фамилии не называют. Из педагогических соображений.",
       "Vitya Gusev is hurt that he isn't in the book. He is! Page one hundred and twelve: 'a certain pupil with a "
       "catapult'. He didn't recognise himself. So he's reformed. I'll reply that the reformed are never named. "
       "For pedagogical reasons."),
      reply="out"),
    B(30, "", "letter", "teacher", ("Соня, Тверь", "Sonya, Tver"),
      ("Учителю написала внучка его ученика.", "A pupil's granddaughter writes to the teacher."),
      ("Пишет девочка из Твери, Соня, одиннадцать лет. Дедушка читал ей мою книгу и показал Полярную звезду, как я его "
       "учил в семьдесят девятом. Ковш, две крайние звезды, отложить пять раз. «Работает», пишет Соня. Работает. "
       "Почти полвека.",
       "A girl from Tver writes, Sonya, eleven. Her grandfather read her my book and showed her the Pole Star the way "
       "I taught him in seventy-nine. The Dipper, the two end stars, five times the distance. 'It works,' Sonya "
       "writes. It does. For nearly half a century.")),
    )

arc("teacher_gorodok",
    B(30, "11,12,1", "letter", "teacher", ("Липовская школа", "Lipovka School"),
      ("Учителя зовут почётным гостем на вечер встречи.", "The teacher is invited as guest of honour to the reunion."),
      ("Вечер встречи выпускников, первая суббота февраля, а в этот раз ещё и юбилей школы. «Ждём вас как почётного "
       "гостя». А я им кто, стенгазета? Пойду, конечно. Сорок одна глава, все приглашены.",
       "The alumni reunion, the first Saturday in February, and this time the school's jubilee too. 'We await you as "
       "our guest of honour.' And what am I to them, a wall newspaper? I'll go, of course. Forty-one chapters, "
       "all invited."),
      needs="teacher.book", stamp="a_school"),
    B(14, "1,2", "telegram", "teacher", ILYA,
      ("Илья едет на вечер встречи с телескопом.", "Ilya is coming to the reunion with a telescope."),
      ("«ПРИЕДУ ВЕЧЕР ВСТРЕЧИ ВЕЗУ ТЕЛЕСКОП ПРОГНОЗ ЯСНО ИЛЬЯ». В восьмом классе он так же писал на контрольной: "
       "«Ответ ясен», а решения не было. Надеюсь, теперь будет и решение, и небо.",
       "'COMING TO REUNION BRINGING TELESCOPE FORECAST CLEAR ILYA.' In year eight he wrote in a test, 'The answer is "
       "clear,' and there was no working. I hope this time there'll be the working and the sky."),
      stamp="a_telegram"),
    B(10, "2,3", "letter", "teacher", ("Выпуск 1988 года", "The class of 1988"),
      ("Выпускники благодарят учителя за вечер встречи.", "Former pupils thank the teacher for the reunion."),
      ("Благодарят, сорок подписей. А пришло сто сорок, в школу на сто двадцать мест. Стояли в коридоре, как на перемене, "
       "и кто-то, клянусь, курил за котельной. Я сделал вид, что не вижу: сорок лет тренировался. Вот, фото, их три.",
       "A thank-you, forty signatures. And a hundred and forty came, to a school built for a hundred and twenty. They "
       "stood in the corridor as if at break, and someone, I swear, smoked behind the boiler house. I pretended not to "
       "see: forty years' practice. Here, a photo; they sent three."),
      gift="a_photo_reunion"),
    B(20, "2,3", "parcel", "teacher", ILYA,
      ("Илья оставил учителю телескоп и прислал окуляры.", "Ilya left his telescope with the teacher and sent eyepieces."),
      ("Илья оставил телескоп у меня, а теперь прислал окуляры и карту: комета будет в апреле, низко на западе, после "
       "заката. Велит наблюдать и записывать. Записывать я умею. Смотреть, оказывается, разучился. Будем учиться "
       "вдвоём с Варей Кузнецовой.",
       "Ilya left the telescope with me and now he's sent eyepieces and a chart: the comet will be up in April, low in "
       "the west after sunset. He wants me to observe and record. Recording I can do. Looking, it turns out, I've "
       "forgotten how. Varya Kuznetsova and I will learn together.")),
    B(25, "4,5", "letter", "teacher", ILYA,
      ("Учитель и Варя видели комету.", "The teacher and Varya have seen the comet."),
      ("Видели! С бугра у водокачки. Варя сказала, что у кометы причёска, как у Лидии Аркадьевны. Научно не подтверждаю, "
       "но и не опровергаю. Илье отписал наблюдения по форме. Последней строкой — про причёску. Пусть знает.",
       "We saw it! From the hill by the water tower. Varya said the comet has a hairdo like Lidia Arkadyevna's. "
       "Scientifically I neither confirm nor deny. I sent Ilya the observations in due form. The last line was about "
       "the hairdo. He ought to know."),
      stamp="a_comet"),
    B(10, "4,5,6", "letter", "varya", ILYA,
      ("Варе пришло письмо от настоящего астронома.", "Varya has a letter from a real astronomer."),
      ("Мне написал настоящий астроном! Илья Андреевич. Я спросила, куда комета летит, а он пишет — от Солнца, и вернётся "
       "через три тысячи лет. Я подсчитала: я столько не проживу. Зато я её видела. А про причёску это не я. Это "
       "Николай Семёнович.",
       "A real astronomer wrote to me! Ilya Andreyevich. I asked where the comet's going, and he says away from the "
       "Sun, and it'll come back in three thousand years. I worked it out: I won't live that long. But I saw it. And "
       "the hairdo thing wasn't me. That was Nikolai Semyonovich.")),
    B(30, "5,6,7", "letter", "teacher", ("Людмила, Городок", "Lyudmila, Gorodok"),
      ("Дочь зовёт Николая Семёновича к себе в Городок.", "His daughter asks Nikolai Semyonovich to move to Gorodok."),
      ("Дочь зовёт к себе в Городок. «Папа, у нас лифт и внуки». Лифт — аргумент слабый: по лестнице я пока быстрее. "
       "Внуки — аргумент сильный. Обещал подумать до осени. Думать долго я умею, сорок лет учил.",
       "My daughter wants me to move to her in Gorodok. 'Dad, we've a lift and grandchildren.' The lift is a weak "
       "argument: I'm still faster on the stairs. The grandchildren are a strong one. I promised to think until "
       "autumn. I know how to think slowly; I taught it for forty years.")),
    B(30, "7,8", "letter", "teacher", ("Людмила, Городок", "Lyudmila, Gorodok"),
      ("Николай Семёнович решил переезжать в Городок.", "Nikolai Semyonovich has decided to move to Gorodok."),
      ("Решил. Людмила нашла мне комнату с балконом на юг, для телескопа. Против балкона на юг я бессилен. А лимон мой "
       "в машину не влезет, ему двадцать лет. Возьмите его вы. Поливать раз в неделю и разговаривать. Он любит про погоду.",
       "I've decided. Lyudmila found me a room with a south-facing balcony, for the telescope. Against a south-facing "
       "balcony I'm powerless. But my lemon tree won't fit in the car; it's twenty years old. You take it. Water it "
       "once a week, and talk to it. It likes talk about the weather."),
      gift="a_plant_lemon"),
    B(20, "8,9", "letter", "teacher", ("Липовская школа", "Lipovka School"),
      ("Кабинет физики назовут именем Николая Семёновича.", "The physics room will bear Nikolai Semyonovich's name."),
      ("Школа пишет: кабинет физики назовут моим именем. При жизни! Неловко, как в новом костюме. Приборы свои оставлю "
       "им, и маятник, и глобус с вмятиной от Сычёва. Пусть дети видят: глобус помять можно. Землю — не надо.",
       "The school writes that the physics room will be named after me. In my lifetime! Awkward, like a new suit. "
       "I'll leave them my instruments, the pendulum, and the globe with Sychov's dent in it. Let the children see: "
       "you may dent a globe. Not the Earth."),
      stamp="a_globe"),
    B(30, "9,10,11", "letter", "me", TEACHER,
      ("Николай Семёнович написал почтальону из Городка.", "Nikolai Semyonovich writes to the postman from Gorodok."),
      ("Здравствуйте, дорогой почтальон. Пишу вам с балкона на юг. Городок шумный, фонари гасят звёзды, зато телескоп "
       "стоит хорошо, и внуки делают вид, что им интересно. По Липовке скучаю больше, чем полагается человеку с лифтом. "
       "Будьте добры, проверьте мою калитку: кажется, я её закрыл, а кажется — нет. Передайте Агафье Петровне, что "
       "дятел уехал, но книгу дописал. И как там мой лимон? Говорите с ним о погоде. Ваш Н. С. Лебедев.",
       "Hello, dear postman. I write to you from the south-facing balcony. Gorodok is noisy, the street lamps put out "
       "the stars, but the telescope stands well, and the grandchildren pretend to be interested. I miss Lipovka more "
       "than is proper for a man with a lift. Kindly check my garden gate: I think I shut it, and I think I didn't. "
       "Tell Agafya Petrovna the woodpecker has moved away, but finished his book. And how is my lemon tree? Talk to it "
       "about the weather. Yours, N. S. Lebedev."),
      stamp="a_autumn"),
    B(30, "11,12,1", "letter", "varya", TEACHER,
      ("Николай Семёнович прислал Варе задание из Городка.", "Nikolai Semyonovich sends Varya a task from Gorodok."),
      ("Николай Семёнович прислал задание: найти Кассиопею. Это буква «W», только на небе. И написать, в какую сторону "
       "она повернулась. Найду — пять. Я сказала маме, что у меня теперь школа и в Городке тоже. Мама сказала: "
       "«Только шапку надень».",
       "Nikolai Semyonovich sent me a task: find Cassiopeia. It's a letter W, only in the sky. And write which way "
       "it's turned. If I find it, I get top marks. I told Mum I've got school in Gorodok now too. Mum said, "
       "'Just put your hat on.'"),
      stamp="a_stars"),
    B(40, "2,3,4", "letter", "me", TEACHER,
      ("Николай Семёнович снова пишет почтальону.", "Nikolai Semyonovich writes to the postman again."),
      ("Дорогой почтальон! При музее у нас нашёлся кружок любителей астрономии: Софья Марковна пускает нас на крышу. "
       "Мне доверили вести. Видите, как бывает: сорок один выпуск, и вот сорок второй — шесть пенсионеров и один "
       "пятиклассник. Пятиклассник лучший. Варя прислала Кассиопею: нашла, и повернулась та, как положено. "
       "Пишите мне иногда. Учителю тоже нужно получать письма, а не только ставить отметки. Н. С. Лебедев.",
       "Dear postman! There's an amateur astronomy circle at the museum here: Sofia Markovna lets us up on the roof. "
       "They've asked me to lead it. You see how things go: forty-one graduating classes, and now a forty-second, six "
       "pensioners and one fifth-former. The fifth-former is the best. Varya sent me Cassiopeia: she found it, turned "
       "just as it should be. Write to me sometimes. A teacher needs letters too, not only to give marks. "
       "N. S. Lebedev."),
      stamp="a_letter"),
    )

# ================================================================ VARYA
arc("varya_moroz",
    B(5, "11,12", "newspaper", "varya", MURZILKA,
      ("Варе пришёл «Мурзилка» с адресом Деда Мороза.", "Varya's Murzilka has Ded Moroz's address in it."),
      ("Тут адрес Деда Мороза! Я уже написала: «Дорогой Дедушка Мароз, мне нужен щенок или хотябы хомяк. И чтобы у папы "
       "трактор не ломался, а то он грусный». Мама проверила, только «хотябы» не исправила, сказала — он поймёт. "
       "Отнесёте?",
       "Ded Moroz's address is in here! I've already written: 'Dear Granpa Frost, I need a puppy or at leest a "
       "hamster. And for Dad's tracter not to brake, it makes him sad.' Mum checked it, only she didn't fix 'at "
       "leest', she said he'll understand. Will you take it?"),
      reply="out"),
    B(10, "12,1", "letter", "varya", MOROZ,
      ("Варе ответил сам Дед Мороз из Великого Устюга.", "Ded Moroz himself has answered Varya from Veliky Ustyug."),
      ("Ответил! Пишет, что щенков по почте не посылают: в конверте им темно и скучно. А хомяк — это, говорит, к маме, "
       "у мамы полномочия. Мама говорит, полномочия — это когда «нет». А про трактор обещал. Папа, слышишь? Обещал!",
       "He answered! He says puppies can't go by post: it's dark and boring for them in an envelope. And the hamster, "
       "he says, is up to Mum; Mum has the authority. Mum says authority is when it's 'no'. But he promised about the "
       "tractor. Dad, do you hear? He promised!"),
      stamp="a_ustyug"),
    B(14, "1,2", "postcard", "varya", MOROZ,
      ("Ещё одна открытка Варе из Устюга.", "Another postcard for Varya from Ustyug."),
      ("Ещё открытка, с его теремом! А это вам, я нарисовала: это вы идёте с сумкой, это сугроб, а это кот Сургуч на "
       "крыше почты. Он не на крыше, я знаю, но так красивее. Повесьте над кроватью. Или над чайником, если над "
       "кроватью занято.",
       "Another postcard, with his tower house! And this is for you, I drew it: that's you walking with your bag, that's "
       "a snowdrift, and that's Surguch the cat on the post office roof. He isn't on the roof, I know, but it's "
       "prettier. Hang it over your bed. Or over the kettle, if over the bed is taken."),
      gift="a_drawing", stamp="a_cat"),
    B(250, "11,12", "notice", "varya", ("Вотчина Деда Мороза", "Ded Moroz's Estate"),
      ("Варя устраивает Деду Морозу проверку.", "Varya is putting Ded Moroz to the test."),
      ("Катя Гусева говорит, что Деда Мороза нет. Вот я и проверю. Написала ему проверочный вопрос: какого цвета "
       "у меня варежки, которые баба Агафья связала? Если он есть — знает. Отнесёте? Только не подсказывайте.",
       "Katya Guseva says Ded Moroz isn't real. So I'm going to check. I've written him a test question: what colour "
       "are the mittens Granny Agafya knitted me? If he's real, he'll know. Will you take it? Just don't give him any "
       "hints."),
      needs="agafya.mittens", reply="out"),
    B(10, "12,1", "letter", "varya", MOROZ,
      ("Дед Мороз прошёл Варину проверку.", "Ded Moroz has passed Varya's test."),
      ("ЗНАЕТ. «Варежки у тебя в синюю полоску, и правая чуть длиннее: Агафья Петровна вязала её под радио». Вы ему "
       "сказали? Нет? И баба Агафья говорит — нет. Значит, есть. Только вы так на меня не смотрите, а то я опять "
       "сомневаться начну.",
       "HE KNOWS. 'Your mittens are blue-striped, and the right one's a bit longer: Agafya Petrovna knitted it to the "
       "radio.' Did you tell him? No? Granny Agafya says no too. So he's real. Only don't look at me like that, or I'll "
       "start doubting again."),
      stamp="a_xmas_star"),
    B(7, "12,1", "parcel", "varya", MOROZ,
      ("Дед Мороз прислал Варе колокольчики.", "Ded Moroz has sent Varya sleigh bells."),
      ("Посылка! Два колокольчика и письмо: «Варе — на санки, а второй — почтальону, который несёт мои письма через "
       "сугробы». Это вам! Он про вас знает. Я же писала. Привяжите на сумку, будет звенеть, и все будут знать, что вы идёте.",
       "A parcel! Two bells and a letter: 'One for Varya's sledge, and the other for the postman who carries my letters "
       "through the snowdrifts.' That's for you! He knows about you. I did write. Tie it to your bag; it'll jingle and "
       "everyone will know you're coming."),
      gift="a_bell_sleigh", stamp="a_sleigh"),
    B(40, "2,3", "letter", "varya", MOROZ,
      ("Варин рисунок повесили в тереме Деда Мороза.", "Varya's drawing is hanging in Ded Moroz's house."),
      ("Мой рисунок висит у Деда Мороза в тереме! Между Мурманском и Сочи, он пишет. Я рисовала Липовку: почту, мельницу, "
       "Бублика и вас. Значит, вы теперь тоже в тереме висите. Поздравляю.",
       "My drawing's hanging in Ded Moroz's house! Between Murmansk and Sochi, he writes. I drew Lipovka: the post "
       "office, the mill, Bublik and you. So now you're hanging in his house too. Congratulations."),
      needs="dog"),
    B(250, "11", "newspaper", "varya", MURZILKA,
      ("Варя пишет Деду Морозу за Бублика.", "Varya writes to Ded Moroz on Bublik's behalf."),
      ("Мне в этом году ничего не надо, я уже большая. Я пишу за Бублика, он сам не умеет: «Дорогой Дед Мороз, я Бублик. "
       "Хочу, чтобы почтальон ходил помедленнее, а то лапы не успевают. Гав». «Гав» я сама придумала, для подлинности.",
       "I don't need anything this year, I'm big now. I'm writing for Bublik, he can't do it himself: 'Dear Grandfather "
       "Frost, I am Bublik. I wish the postman would walk slower, my paws can't keep up. Woof.' I made up the 'woof' "
       "myself, so it's authentic."),
      needs="dog", reply="out"),
    B(10, "12,1", "letter", "varya", MOROZ,
      ("Дед Мороз ответил Бублику.", "Ded Moroz has answered Bublik."),
      ("Дед Мороз ответил Бублику! «Почтальону ходить медленнее нельзя, письма ждут. Но я попрошу почаще "
       "останавливаться у калиток». И пряник прислал, для Бублика. Только Бублику сладкое нельзя. Так что вам. "
       "Ему не говорите.",
       "Ded Moroz answered Bublik! 'The postman can't walk slower, the letters are waiting. But I'll ask them to stop "
       "at garden gates more often.' And he sent gingerbread, for Bublik. Only Bublik's not allowed sweets. So it's "
       "yours. Don't tell him."),
      gift="a_gingerbread", stamp="a_dog"),
    B(20, "1,2", "letter", "varya", MOROZ,
      ("Дед Мороз зовёт Варю в помощники.", "Ded Moroz asks Varya to be his helper."),
      ("Дед Мороз зовёт меня в помощники! Отвечать малышам из Липовки, если они ему напишут. Мне! Я теперь как вы, "
       "только зимой. Почерк надо исправить. А «хотя бы» я теперь пишу раздельно. Давно уже, между прочим.",
       "Ded Moroz is asking me to be his helper! To answer the little ones in Lipovka if they write to him. Me! I'm "
       "like you now, only in winter. I'll have to fix my handwriting. And I spell 'at least' properly now. Have for "
       "ages, for the record."),
      stamp="a_ustyug"),
    )

arc("varya_kamchatka",
    B(30, "", "letter", "varya", ULYA,
      ("Варе написала девочка с Камчатки.", "A girl from Kamchatka has written to Varya."),
      ("Мне написала девочка с Камчатки! Уля. Нашла мой адрес в «Мурзилке», где «Давай дружить». У неё из окна вулкан, "
       "а у меня из окна баба Агафья. Ну, это тоже хорошо. Мы ровесницы, только Уля на два месяца старше и умеет свистеть.",
       "A girl from Kamchatka wrote to me! Ulya. She found my address in Murzilka, on the pen-pal page. Out of her "
       "window there's a volcano, and out of mine there's Granny Agafya. Well, that's good too. We're the same age, "
       "only Ulya's two months older and can whistle."),
      stamp="a_volcano"),
    B(25, "", "postcard", "varya", ULYA,
      ("Уля пишет Варе: у них дымила сопка.", "Ulya writes that their volcano was smoking."),
      ("Уля пишет: «У нас сегодня сопка дымила». Сопка — это гора. Гора, которая дымит, как папа, когда трактор не "
       "заводится. А я ей отправлю липовый листок, засушенный в книжке. Пусть знает, почему Липовка.",
       "Ulya writes, 'Our sopka was smoking today.' A sopka is a mountain. A mountain that smokes, like Dad when the "
       "tractor won't start. And I'll send her a linden leaf, pressed in a book. So she knows why it's called "
       "Lipovka."),
      reply="out"),
    B(30, "", "parcel", "varya", ULYA,
      ("Уля прислала Варе вулканический пепел.", "Ulya has sent Varya volcanic ash."),
      ("Посылка с Камчатки! Пепел вулкана в спичечном коробке, мама сказала — не нюхать. И камень, который плавает. "
       "Пемза! Их два. Вот один — вам. Положите в таз, сами увидите. У нас в Липке камни сразу тонут, я проверяла.",
       "A parcel from Kamchatka! Volcano ash in a matchbox; Mum said not to sniff it. And a stone that floats. Pumice! "
       "There are two. Here's one for you. Put it in a basin and see. In our Lipka stones sink straight away, "
       "I've checked."),
      gift="a_pumice"),
    B(20, "12,1", "postcard", "varya", ULYA,
      ("Новогодняя открытка Варе с Камчатки.", "A New Year card for Varya from Kamchatka."),
      ("У Ули Новый год наступает, когда у нас ещё обед. Девять часов разницы! Значит, она живёт в будущем. Я ей "
       "написала: «Как там, в будущем? Снег есть?» Мама смеётся, а я серьёзно спрашиваю.",
       "Ulya's New Year comes when we're still having lunch. Nine hours' difference! So she lives in the future. I "
       "wrote to her: 'What's it like in the future? Is there snow?' Mum laughs, but I'm asking seriously."),
      stamp="a_fir"),
    B(40, "3,4,5", "letter", "varya", ULYA,
      ("У Ули на Камчатке ещё зима.", "It's still winter for Ulya in Kamchatka."),
      ("У Ули снег до мая, они в школу на лыжах ходят! А у нас Липка уже тронулась и ласточки прилетели. Я ей написала, "
       "что у нас весна. Пусть завидует. Хотя у неё вулкан. Ладно. Мы квиты.",
       "Ulya has snow till May, they go to school on skis! And our Lipka's already broken up and the swallows are "
       "back. I wrote and told her it's spring here. Let her be jealous. Though she has a volcano. All right. "
       "We're even."),
      stamp="a_swallow"),
    B(40, "7,8", "letter", "varya", ULYA,
      ("Уля видела медведя на рыбалке.", "Ulya has seen a bear fishing."),
      ("Уля видела медведя! На реке, он ловил рыбу лапой, как кот. Её папа рыбак и говорит, что медведь ловит лучше. "
       "Я спросила папу, ловит ли он лучше медведя. Папа сказал: «Я лучше медведя чиню трактор». Это правда.",
       "Ulya saw a bear! At the river, catching fish with his paw like a cat. Her dad's a fisherman and says the bear "
       "catches better. I asked my dad if he catches better than a bear. Dad said, 'I fix tractors better than a "
       "bear.' That's true.")),
    B(30, "9,10", "letter", "varya", ULYA,
      ("Варя и Уля теперь во втором классе.", "Varya and Ulya are in the second year of school now."),
      ("Мы обе теперь во втором классе! Уля пишет, что у них учительница громкая. А наша Антонина Павловна совсем не "
       "кричит, она смотрит. Это страшнее. Я Уле так и написала: смотрит — это хуже.",
       "We're both in second year now! Ulya writes that their teacher is loud. Our Antonina Pavlovna never shouts, "
       "she looks at you. That's scarier. I told Ulya so: looking is worse.")),
    B(40, "11,12,1", "parcel", "varya", ULYA,
      ("Улин папа прислал Кузнецовым рыбу.", "Ulya's dad has sent the Kuznetsovs some fish."),
      ("Улин папа рыбу прислал, копчёного кижуча. Мама сказала: «Почтальону — хвост». Это она шутит. Вот, возьмите кусок "
       "из середины, там вкуснее. Кижуч — это лосось, только камчатский. Я теперь про рыб всё знаю.",
       "Ulya's dad sent fish, smoked coho. Mum said, 'The postman gets the tail.' She's joking. Here, take a piece "
       "from the middle, it's tastier. Coho is a salmon, only from Kamchatka. I know everything about fish now."),
      gift="a_fish_smoked", stamp="a_salmon"),
    B(60, "3,4,5", "letter", "varya", ULYA,
      ("Уля летит летом «на материк» — может, и в Липовку.", "Ulya is flying 'to the mainland' this summer, maybe to Lipovka."),
      ("Уля летом летит «на материк», к бабушке в Ярославль! А от Ярославля до нас — мама посмотрела — всего день ехать. "
       "Всего! С Камчатки девять часов лететь. Я уже придумала, что ей показать: мельницу, бабу Агафью и вас.",
       "Ulya's flying 'to the mainland' this summer, to her granny in Yaroslavl! And from Yaroslavl to us, Mum looked "
       "it up, is only a day's drive. Only! From Kamchatka it's nine hours' flying. I've already planned what to show "
       "her: the mill, Granny Agafya and you."),
      stamp="a_plane"),
    B(40, "7,8", "postcard", "varya", ("Уля, Ярославль", "Ulya, Yaroslavl"),
      ("Уля погостила у Вари и пишет из Ярославля.", "Ulya has visited Varya and writes from Yaroslavl."),
      ("Уля у нас три дня жила! Комары ей не понравились, а баба Агафья понравилась. Пишет: «Варя, у вас речка тихая, "
       "а у нас океан громкий. Я буду скучать по тихому». Вот, папа нас у мельницы снял. Это вам.",
       "Ulya stayed with us three days! She didn't like the mosquitoes but she liked Granny Agafya. She writes, 'Varya, "
       "your river's quiet and our ocean's loud. I'll miss the quiet.' Here, Dad took a picture of us at the mill. "
       "This one's yours."),
      gift="a_photo_friends"),
    B(60, "10,11,12", "letter", "varya", ULYA,
      ("Варя и Уля придумали шифр.", "Varya and Ulya have invented a cipher."),
      ("Мы с Улей придумали шифр: каждая буква — следующая по алфавиту. Смотрите: «Гбса — лпмпттбмэоба». Не понимаете? "
       "И не надо. Ну ладно: «Варя — колоссальная». Так Уля написала. Колоссальная — значит очень большая. Я согласна.",
       "Ulya and I made up a cipher: every letter is the next one in the alphabet. Look: 'Wbszb jt dpmpttbm.' Don't "
       "get it? You don't need to. Oh, all right: 'Varya is colossal.' That's what Ulya wrote. Colossal means very "
       "big. I agree.")),
    )

arc("varya",
    B(12, "", "letter", "varya", ("Бабушка Галя, Череповец", "Granny Galya, Cherepovets"),
      ("Варе пришло первое собственное письмо.", "Varya has her very own first letter."),
      ("Это мне! Не маме, а мне, вот: «Варваре Кузнецовой, лично». Бабушка Галя пишет. Я сама прочитала, за двадцать "
       "минут, только слово «непременно» мама помогла. Непременно — это когда точно. Бабушка непременно приедет летом.",
       "It's for me! Not Mum, me, look: 'To Varvara Kuznetsova, personally.' Granny Galya wrote it. I read it myself, "
       "in twenty minutes, Mum only helped with the word 'without fail'. Without fail means for sure. Granny's coming "
       "in the summer without fail.")),
    B(10, "6", "parcel", "varya", ("Бабушка Галя, Череповец", "Granny Galya, Cherepovets"),
      ("Варе исполнилось восемь лет.", "Varya has turned eight."),
      ("Мне восемь! Восемь — это два раза по четыре и почти десять. Бабушка прислала скакалку и книжку про звёзды. "
       "А мама испекла яблочный пирог. Вот вам кусок, с краю, где корочка. Краешек — самое вкусное, это все знают.",
       "I'm eight! Eight is two fours and nearly ten. Granny sent a skipping rope and a book about stars. And Mum "
       "baked an apple pie. Here's a piece for you, from the edge, where the crust is. The edge is the best bit, "
       "everyone knows that."),
      on="06-01", gift="a_pie_apple", stamp="a_birthday"),
    B(30, "8,9", "postcard", "varya", ("Н. С. Лебедев", "N. S. Lebedev"),
      ("Николай Семёнович поздравил Варю с началом учёбы.", "Nikolai Semyonovich wishes Varya a good school year."),
      ("Николай Семёнович прислал открытку: «Варваре — с началом учебного года. Физики ждать ещё долго, а на звёзды "
       "можно смотреть уже сейчас». Варваре! Как взрослой. Буду смотреть на звёзды. Только меня в девять спать гонят.",
       "Nikolai Semyonovich sent a card: 'To Varvara, for the new school year. Physics is a long way off, but you can "
       "look at the stars now.' Varvara! Like a grown-up. I'll look at the stars. Only they send me to bed at nine."),
      stamp="a_school_bell"),
    B(30, "10,11", "notice", "varya", ("Библиотека, Л. А. Белова", "Library, L. A. Belova"),
      ("Варе выписали собственный читательский билет.", "Varya has been issued her own library card."),
      ("Мне пришёл читательский билет! Свой, с фамилией. Теперь я читатель, официально. Лидия Аркадьевна написала, что мне "
       "можно брать три книжки, а не две, потому что я аккуратная. Я правда аккуратная. Только одну книжку уронила в Липку, "
       "но её не считали.",
       "My library card's come! My own, with my surname on it. I'm a reader now, officially. Lidia Arkadyevna wrote that "
       "I'm allowed three books, not two, because I'm careful. I really am. I only dropped one book in the Lipka, but "
       "that one didn't count.")),
    B(60, "2,3", "registered", "varya", ("Районный Дом культуры", "District House of Culture"),
      ("Варя заняла третье место в районном конкурсе рисунка.", "Varya has won third place in a district drawing contest."),
      ("Грамота! Третье место в районе, конкурс «Моя деревня». Я нарисовала почту, и вас, и кота. Первое — у мальчика "
       "из Городка, у него трактор с крыльями. Трактор с крыльями — это не деревня, я считаю. Это сказка. "
       "Но я не обижаюсь. Почти.",
       "A certificate! Third place in the district, the 'My Village' contest. I drew the post office, and you, and the "
       "cat. First place went to a boy from Gorodok, he did a tractor with wings. A tractor with wings isn't a village, "
       "I think. It's a fairy tale. But I'm not upset. Almost.")),
    B(60, "6", "letter", "varya", KOSTYA,
      ("Дядя Костя из Мурманска поздравил Варю с девятилетием.", "Uncle Kostya in Murmansk wishes Varya a happy ninth birthday."),
      ("Мне девять! Дядя Костя из Мурманска пишет: «Варька, у нас солнце не садится, так что спать ложись сама, без "
       "команды». А я и так сама. Почти всегда. И фотографию прислал, северного сияния. Зимнюю. Летом у них сияния нет, "
       "солнце мешает.",
       "I'm nine! Uncle Kostya in Murmansk writes, 'Varka, the sun doesn't set here now, so go to bed by yourself, "
       "without being told.' I do anyway. Nearly always. And he sent a photo of the northern lights. A winter one. "
       "There aren't any in summer, the sun gets in the way."),
      on="06-01", stamp="a_aurora"),
    B(30, "9,10", "newspaper", "varya", ("«Сельская новь»", "Village News"),
      ("Варино стихотворение напечатали в газете.", "Varya's poem has been printed in the newspaper."),
      ("Меня напечатали в газете! Стихотворение «Осень в Липовке»: «Листья падают в реку, / Река несёт их к морю, / "
       "А почтальон несёт письма, / И всё когда-нибудь доходит». Мама сказала, последняя строчка не рифмуется. "
       "А я сказала: зато правда.",
       "They printed me in the newspaper! A poem, 'Autumn in Lipovka': 'Leaves are falling in the river, / The river "
       "takes them to the sea, / The postman carries letters, / And everything gets there one day.' Mum said the last "
       "line doesn't rhyme. And I said: but it's true."),
      stamp="a_autumn"),
    B(60, "6", "parcel", "varya", ("Бабушка Галя, Череповец", "Granny Galya, Cherepovets"),
      ("Варе исполнилось десять.", "Varya has turned ten."),
      ("Мне десять. Двузначное число! Бабушка прислала взрослую книжку про звёзды, без картинок, а папа подарил фонарик "
       "с красным светом, чтобы глаза не портить, — это Николай Семёнович научил. А мама испекла крендель. Вот вам "
       "кусочек. Изюм я не выковыривала, честно.",
       "I'm ten. Two digits! Granny sent a grown-up book about stars, with no pictures, and Dad gave me a torch with a red "
       "light, so it doesn't spoil your eyes; Nikolai Semyonovich taught us that. And Mum baked a birthday pretzel loaf. "
       "Here's a bit for you. I didn't pick the raisins out, honest."),
      on="06-01", gift="a_pretzel"),
    B(40, "7,8,9", "letter", "me", ("Варя Кузнецова, Липовка", "Varya Kuznetsova, Lipovka"),
      ("Варя написала письмо самому почтальону.", "Varya has written a letter to the postman."),
      ("Дорогой почтальон! Пишу вам письмо, потому что вы всем приносите, а вам никто. Это несправедливо. Мне десять лет, "
       "пишу почти без ошибок, только «что бы» иногда отдельно. Спасибо за все письма: от Деда Мороза, от Ули, от бабушки "
       "и даже за те, где «оплатить до 25-го», маме они тоже нужны. Бублику привет. Не ходите по лужам. Ваша Варя. "
       "P. S. Ответ можно положить в наш ящик. Я проверяю каждый день.",
       "Dear postman! I'm writing you a letter because you bring everyone letters and nobody writes to you. That's not "
       "fair. I'm ten, I write almost without mistakes, only sometimes I spell 'all right' as 'alright'. Thank you for "
       "all the letters: from Ded Moroz, from Ulya, from Granny, and even the ones that say 'pay by the 25th', Mum needs "
       "those too. Say hello to Bublik. Don't walk through puddles. Love, Varya. P.S. You can put the answer in our "
       "letterbox. I check it every day."),
      stamp="a_letter"),
    )

# ================================================================ OLGA
PHARM = ("Аптечный склад, Городок", "Pharmacy Depot, Gorodok")
CRB = ("Районная больница, Городок", "District Hospital, Gorodok")
arc("olga",
    B(6, "", "parcel", "olga", PHARM,
      ("Ольге пришли лекарства для медпункта.", "Medicines for Olga's medical post have arrived."),
      ("Опять прислали йода на полк, а таблеток от давления три пачки. У меня полдеревни на давлении, и все говорят: "
       "«Ерунда, само пройдёт». Буду писать заявку заново, четвёртый раз. Заявки я теперь пишу красивее, чем стихи.",
       "They've sent iodine for a regiment again, and three packets of blood pressure pills. Half the village has blood "
       "pressure, and everyone says, 'Nonsense, it'll pass.' I'll write the request again, the fourth time. I write "
       "requests more beautifully than poetry now.")),
    B(10, "11,12,1,5,6", "registered", "olga", UNI,
      ("Ольгу вызывают на сессию.", "Olga is summoned to her exam session."),
      ("Справка-вызов. Снова в Ярославль, на две недели сессии. Четвёртый курс, учусь на врача заочно... ну, почти "
       "заочно: днём медпункт, ночью учебник. Варя остаётся с Серёжей, значит, две недели макарон с тушёнкой. "
       "Переживут. Они это любят.",
       "My summons. Back to Yaroslavl for two weeks of exams. Fourth year, studying to be a doctor by "
       "correspondence... well, nearly: the medical post by day, the textbook by night. Varya stays with Seryozha, "
       "which means two weeks of pasta and tinned stew. They'll survive. They love it.")),
    B(20, "1,2,6,7", "letter", "olga", ("Ира, однокурсница", "Ira, a fellow student"),
      ("Ольга сдала фармакологию на пятёрку.", "Olga got top marks in pharmacology."),
      ("Ира пишет: я одна сдала фармакологию на пять с первого раза. Это не я умная. Это пятнадцать лет на трёх деревнях "
       "и Агафья Петровна, которая всё лечит малиной и спорит со мной про таблетки. Я у неё многому научилась. "
       "Спорить, например.",
       "Ira writes that I was the only one to pass pharmacology with top marks first time. It's not that I'm clever. "
       "It's fifteen years covering three villages, and Agafya Petrovna, who treats everything with raspberries and "
       "argues with me about pills. I've learnt a lot from her. Arguing, for one.")),
    B(40, "4,5,6,7", "parcel", "olga", PHARM,
      ("Ольге прислали вакцину от клещей.", "Olga has received tick vaccine."),
      ("Вакцина от клещей, в термосумке, как мороженое. Клещи проснулись раньше нас всех, я уже двоих сняла: с Михалыча "
       "и с козы. Так что записывайтесь. И вы тоже. Почтальону по кустам — в первую очередь.",
       "Tick vaccine, in a cool bag, like ice cream. The ticks woke up before any of us; I've already taken off two: "
       "one from Mikhalych and one from a goat. So sign up. You too. A postman cutting through bushes comes first.")),
    B(30, "5,6,7,8", "letter", "olga", ("Е. Миронова, Москва", "E. Mironova, Moscow"),
      ("Ольге пишет благодарная дачница.", "A grateful summer visitor writes to Olga."),
      ("Дачница прошлогодняя пишет. Сыну её я крючок из пальца доставала: ловил окуня, поймал себя. Прислала спасибо "
       "и чай с чабрецом. Мне столько не выпить. Возьмите пачку. Чабрец — от усталости в ногах. Это медицина, "
       "а не бабушкины сказки.",
       "Last year's summer visitor is writing. I got a fishhook out of her son's finger: he was fishing for perch and "
       "caught himself. She sent thanks and thyme tea. I can't drink all that. Take a packet. Thyme is for tired legs. "
       "That's medicine, not old wives' tales."),
      gift="a_tea_herbs"),
    B(30, "", "letter", "olga", UNI,
      ("Ольга закрыла сессию.", "Olga has passed her exams."),
      ("Сессию закрыла. Хирургию сдавала профессору, у него руки, как у Фёдора Ильича: большие и спокойные. "
       "Сказал: «Кузнецова, у вас пальцы рабочие, это видно». Лучший комплимент в моей жизни. Серёжа чуть-чуть обиделся.",
       "Exams done. I took surgery with a professor whose hands are like Fyodor Ilyich's: big and calm. He said, "
       "'Kuznetsova, you have working fingers, it shows.' The best compliment of my life. Seryozha was a tiny bit "
       "offended.")),
    B(40, "8,9,10", "letter", "olga", CRB,
      ("Главврач пишет Ольге о будущем медпункта.", "The head doctor writes to Olga about the medical post's future."),
      ("Главврач пишет: как получу диплом, медпункт сделают врачебной амбулаторией. С врачом. Со мной, то есть. Ещё два "
       "года. Я пока никому не говорю. Ну, кроме вас. Вы как сейф, только с сумкой.",
       "The head doctor writes that once I have my diploma, the medical post will become a clinic. With a doctor. Me, "
       "that is. Two more years. I'm not telling anyone yet. Well, except you. You're like a safe, only with a bag.")),
    B(25, "9,10,11", "parcel", "olga", PHARM,
      ("Ольге привезли прививки от гриппа.", "The flu vaccines have arrived for Olga."),
      ("Прививки от гриппа. Градусник внутри — плюс пять, как положено, везли как младенца. Агафья Петровна уже "
       "записалась первой и придёт с вязанием, «чтоб не зря сидеть». Вам место держу. Не отпирайтесь: у вас самая "
       "простудная работа в деревне.",
       "The flu jabs. The thermometer inside says plus five, as it should; they were carried like a baby. Agafya "
       "Petrovna's signed up first and will bring her knitting, 'so as not to sit for nothing'. I'm keeping a place for "
       "you. Don't refuse: you have the coldest job in the village."),
      stamp="a_rain"),
    B(30, "11,12,1", "parcel", "olga", CRB,
      ("В медпункт прислали кардиограф.", "An ECG machine has arrived for the medical post."),
      ("Кардиограф! Свой, в медпункте. Раньше всех в Городок возили, по кочкам. Фёдор Ильич пришёл первым и сказал: "
       "«Пиши, что всё в порядке». Написала. У него и правда всё в порядке. Только пульс частит, когда Агафья "
       "Петровна в окне.",
       "An ECG machine! Our own, at the post. We used to take everyone to Gorodok, over the potholes. Fyodor Ilyich "
       "came first and said, 'Write that everything's fine.' I did. Everything really is fine. Only his pulse races "
       "when Agafya Petrovna's in the window."),
      stamp="a_heart"),
    B(30, "12,1", "registered", "olga", UNI,
      ("Ольгу снова вызывают на сессию. Пятый курс.", "Olga is summoned to exams again. Fifth year."),
      ("Опять вызов. Пятый курс. Варя спросила, когда я перестану учиться. Я сказала: никогда, профессия такая. Она "
       "подумала и говорит: «Тогда я тоже буду врачом. Чтобы мы вместе не переставали». Ну вот. Довела ребёнка.",
       "Another summons. Fifth year. Varya asked when I'll stop studying. Never, I said, it's that kind of job. She "
       "thought and said, 'Then I'll be a doctor too. So we can not stop together.' There you are. I've driven the "
       "child to it.")),
    B(40, "2,3", "letter", "olga", ("Р. Г. Ахмедова, Городок", "R. G. Akhmedova, Gorodok"),
      ("Ольга будет проходить практику в Городке.", "Olga will do her hospital placement in Gorodok."),
      ("Практику буду проходить в Городке, у Раисы Гусейновны. Говорят, строгая, как зимний ветер, и лучше неё диагноз "
       "никто не ставит. Пишет: «Приезжайте к восьми. К восьми — это не к восьми ноль пяти». Мне нравится. "
       "С такими учиться.",
       "I'll do my placement in Gorodok, with Raisa Guseinovna. They say she's as strict as a winter wind and nobody "
       "makes a better diagnosis. She writes, 'Come at eight. Eight does not mean five past.' I like that. Those are "
       "the people to learn from.")),
    B(50, "5,6", "parcel", "olga", ("Р. Г. Ахмедова, Городок", "R. G. Akhmedova, Gorodok"),
      ("Раиса Гусейновна прислала Ольге свои учебники.", "Raisa Guseinovna has sent Olga her old textbooks."),
      ("Раиса Гусейновна свои учебники прислала, целую коробку. С пометками на полях: «чушь», «проверено», «так не "
       "бывает, но бывает». Это дороже любого учебника. Я теперь читаю не книги, а её поля.",
       "Raisa Guseinovna sent her textbooks, a whole box. With notes in the margins: 'nonsense', 'tested', 'this never "
       "happens, but it does'. That's worth more than any textbook. Now I'm not reading the books, I'm reading her "
       "margins.")),
    B(40, "9,10", "parcel", "olga", PHARM,
      ("Снова осень, снова прививки у Ольги.", "Autumn again, and flu jabs again at Olga's."),
      ("Опять прививки. Этой осенью без очереди: все уже знают, что не больно, если смотреть на мою герань. Вот, возьмите "
       "отросток алоэ, у меня три горшка. От порезов, от ожогов и от плохого настроения. Последнее не научно, "
       "но работает.",
       "Flu jabs again. No queue this autumn: everyone knows it doesn't hurt if you look at my geranium. Here, take an "
       "aloe cutting; I have three pots. For cuts, for burns and for a bad mood. The last isn't scientific, "
       "but it works."),
      gift="a_plant_aloe"),
    B(30, "12,1", "registered", "olga", UNI,
      ("Ольге утвердили тему дипломной работы.", "Olga's diploma thesis topic has been approved."),
      ("Тему диплома утвердили: «Сельский медпункт: врач на расстоянии вытянутой руки». Это я придумала. Руководитель "
       "сказал, что слишком поэтично, потом подумал и оставил. Пишу ночами. Варя носит мне чай и говорит: «Держись, доктор».",
       "My thesis topic's approved: 'The Village Medical Post: A Doctor Within Arm's Reach.' I came up with it. My "
       "supervisor said it was too poetic, then thought about it and kept it. I write at night. Varya brings me tea "
       "and says, 'Hang in there, doctor.'")),
    B(50, "3,4,5", "letter", "olga", CRB,
      ("Ольгу зовут работать в Городок. Она отказывается.", "Olga is offered a job in Gorodok. She says no."),
      ("Зовут в районную больницу. Ординатура, квартира, зарплата. Я ответила: спасибо, нет. У меня тут Агафья Петровна "
       "с давлением, Фёдор Ильич с пульсом, Михалыч с пчёлами и полдеревни, которая без меня таблетки пить не будет. "
       "Отправите?",
       "They want me at the district hospital. A residency, a flat, a salary. I replied: thank you, no. I have Agafya "
       "Petrovna with her blood pressure here, Fyodor Ilyich with his pulse, Mikhalych with his bees, and half a village "
       "that won't take its pills without me. Will you post it?"),
      reply="out"),
    B(40, "6,7", "telegram", "sergey", ("Ольга, Ярославль", "Olga, Yaroslavl"),
      ("Телеграмма Сергею от Ольги: экзамены сданы.", "A telegram from Olga for Sergey: the exams are passed."),
      ("От Оли. «СДАЛА ВСЁ ЕДУ ДОМОЙ ДОКТОР КУЗНЕЦОВА». Доктор! Слышите? Варя, неси краску, табличку будем переписывать. "
       "Где моя тонкая кисть... Нет. Сначала побреюсь. Доктора встречаем.",
       "From Olya. 'PASSED EVERYTHING COMING HOME DOCTOR KUZNETSOVA.' Doctor! Do you hear? Varya, fetch the paint, we're "
       "redoing the sign. Where's my fine brush... No. First I'll shave. We're meeting a doctor."),
      stamp="a_telegram", sets="olga.doctor"),
    B(30, "7,8,9", "registered", "olga", CRB,
      ("Липовский медпункт стал врачебной амбулаторией.", "Lipovka's medical post is now a doctor's clinic."),
      ("Приказ: «Липовский медпункт преобразовать во врачебную амбулаторию. Заведующая — врач О. Н. Кузнецова». Врач. "
       "Я три раза прочитала, а потом пошла и вымыла крыльцо. Не знаю зачем. Надо было что-то сделать руками.",
       "An order: 'The Lipovka medical post is to become a doctor's clinic. Head: Dr O. N. Kuznetsova.' Doctor. I read "
       "it three times and then went and scrubbed the porch. I don't know why. I had to do something with my hands."),
      stamp="a_clinic"),
    B(30, "8,9,10", "postcard", "olga", ("Р. Г. Ахмедова, Городок", "R. G. Akhmedova, Gorodok"),
      ("Раиса Гусейновна назвала Ольгу коллегой.", "Raisa Guseinovna calls Olga a colleague."),
      ("«Поздравляю, коллега». Коллега! Пятнадцать лет была «Олечка, глянь», а теперь коллега. Варя нарисовала табличку: "
       "«Доктор. Стучать громко. Не открывают — она у Агафьи Петровны». Так и повесим. Вот, шиповник, от простуды. "
       "Доктор велит.",
       "'Congratulations, colleague.' Colleague! Fifteen years of 'Olechka, take a look', and now colleague. Varya drew "
       "a sign for the door: 'Doctor. Knock loudly. If no answer, she's at Agafya Petrovna's.' We'll hang it just like "
       "that. Here, rosehip, for colds. Doctor's orders."),
      gift="a_tea_rosehip"),
    )

# ================================================================ SERGEY
arc("sergey",
    B(8, "", "parcel", "sergey", ("Агрозапчасть, Вологда", "Agro Parts, Vologda"),
      ("Сергею пришла запчасть для трактора.", "A tractor part has arrived for Sergey."),
      ("Насос шестерёнчатый. Месяц ждал. Пока ждал, починил Агафье Петровне ходики, Николаю Семёновичу калитку, "
       "Зинаиде Павловне весы. Всем, кроме трактора. Теперь и трактору.",
       "A gear pump. Waited a month. While I waited I fixed Agafya Petrovna's wall clock, Nikolai Semyonovich's gate "
       "and Zinaida Pavlovna's scales. Everyone's but the tractor. Now the tractor's too."),
      stamp="a_clock"),
    B(7, "11,12,1,2,3", "letter", "sergey", KOSTYA,
      ("Сергею пишет брат из Мурманска.", "Sergey's brother writes from Murmansk."),
      ("Костя, брат. Пишет, у них зимой ночь сорок дней, а он всё равно в шесть встаёт, привычка с детства. Сияние вчера было "
       "зелёное, как наш трактор. Это он мне комплимент сделал, вы не думайте.",
       "Kostya, my brother. Says in winter it's night for forty days up there, and he still gets up at six, a habit since he "
       "was a boy. The aurora yesterday was green, like our tractor. He meant that as a compliment, don't you think "
       "otherwise."),
      stamp="a_aurora"),
    B(25, "", "parcel", "sergey", ("Частное лицо, Самара", "Private seller, Samara"),
      ("Сергей нашёл лампы для старого приёмника учителя.", "Sergey has found valves for the teacher's old radio."),
      ("Лампы. Николай Семёнович попросил отцовский «Рекорд» починить, сорок восьмого года, а таких ламп не делают "
       "с моего рождения. Нашёл у деда в Самаре, по объявлению. Дед пишет: «Пусть играет, жалко, если замолчит». "
       "Заиграет.",
       "Valves. Nikolai Semyonovich asked me to mend his father's Rekord radio, from forty-eight, and they haven't made "
       "valves like these since I was born. Found them with an old man in Samara, through an ad. He writes, 'Let it "
       "play, it'd be a shame if it went silent.' It'll play."),
      stamp="a_radio"),
    B(30, "", "letter", "sergey", KOSTYA,
      ("Братья Кузнецовы задумали собрать дедов мотоцикл.", "The Kuznetsov brothers plan to rebuild their grandad's motorbike."),
      ("Костя спрашивает, цел ли дедов «Урал». Цел, в сарае, под брезентом, куры на нём сидят. Мы с Костей пацанами на "
       "нём падать учились. Решили: соберём. Он — запчастями, я — руками. Возьмите яиц. Куры с «Урала» несутся лучше.",
       "Kostya's asking whether Grandad's Ural is still in one piece. It is, in the shed, under a tarp, with the hens "
       "sitting on it. Kostya and I learned to fall off on it as boys. We've decided: we'll rebuild it. Him with parts, "
       "me with my hands. Take some eggs. Hens lay better on an Ural."),
      gift="a_eggs"),
    B(30, "", "parcel", "sergey", KOSTYA,
      ("Костя прислал карбюратор для «Урала».", "Kostya has sent a carburettor for the Ural."),
      ("Карбюратор из Ирбита. Костя прислал, последний такой, говорит, на складе. Завернул в мурманскую газету, чтобы "
       "я не забывал, откуда помощь. А я, пока кур из сарая выгонял, дедову подкову нашёл. Берите. На счастье.",
       "A carburettor from Irbit. Kostya sent it, the last one in the warehouse, he says. Wrapped it in a Murmansk "
       "newspaper so I don't forget where the help came from. And while I was chasing the hens out of the shed, I found "
       "Grandad's horseshoe. Take it. For luck."),
      gift="a_horseshoe"),
    B(30, "6,7", "telegram", "sergey", KOSTYA,
      ("Брат Сергея едет в гости с треской.", "Sergey's brother is coming to visit, with cod."),
      ("«БУДУ ВТОРНИК ВЕЗУ ТРЕСКУ КОСТЯ». Треску везёт. Через всю страну, в сумке-холодильнике, как дипломат. Оля, "
       "освобождай морозилку. Варя, прячь хомяка. Шучу, хомяка у нас нет. Пока нет.",
       "'ARRIVING TUESDAY BRINGING COD KOSTYA.' He's bringing cod. Right across the country, in a cool bag, like a "
       "diplomat. Olya, clear the freezer. Varya, hide the hamster. Joking, we haven't got a hamster. Not yet."),
      stamp="a_telegram"),
    B(25, "7,8,9", "letter", "sergey", KOSTYA,
      ("Костя уехал и уже пишет про «Урал».", "Kostya's gone home and is already writing about the Ural."),
      ("Костя уехал, письмо уже прислал: «Серёга, «Урал» без меня не заводить». Мы его при нём завели, но не считается: "
       "через минуту заглох. Вот, трески сушёной возьмите, Костя мешок оставил. Под чай — милое дело.",
       "Kostya's gone, and he's already written: 'Seryoga, don't start the Ural without me.' We did start it while he "
       "was here, but it doesn't count: it stalled after a minute. Here, have some dried cod, Kostya left a sack. "
       "Lovely with tea."),
      gift="a_fish_dried"),
    B(30, "9,10,11", "parcel", "sergey", ("Швейная фурнитура, Подольск", "Sewing Parts, Podolsk"),
      ("Сергей чинит Анне швейную машинку.", "Sergey is mending Anna's sewing machine."),
      ("Челнок для «Подольской» семидесятого года. Анне Ветровой чиню. Она без машинки как без рук, а я без челнока — "
       "тоже как без рук. Две пары рук ждали одну железку. Дождались.",
       "A shuttle for a 1970 Podolsk machine. I'm mending Anna Vetrova's. She's helpless without her machine, and I was "
       "helpless without the shuttle. Two pairs of hands waiting on one bit of metal. Done waiting now.")),
    B(40, "1,2,3", "letter", "sergey", KOSTYA,
      ("Костя женится — на крановщице.", "Kostya is getting married, to a crane operator."),
      ("Костя женится! На крановщице, Наташе. Познакомились на высоте сорок метров, по рации: она ему «вира», он ей "
       "«майна», и вот. Свадьба летом, в Мурманске. В самый сенокос. Как нарочно.",
       "Kostya's getting married! To a crane operator, Natasha. They met forty metres up, over the radio: she said "
       "'hoist', he said 'lower', and there you are. The wedding's in summer, in Murmansk. Right in haymaking. As if on "
       "purpose."),
      stamp="a_heart"),
    B(40, "4,5", "registered", "sergey", ("Управление сельского хозяйства", "District Agriculture Office"),
      ("Сергей стал лучшим механизатором района.", "Sergey has been named the district's best machine operator."),
      ("Грамота. «Лучший механизатор района». Это за то, что я в посевную пять чужих тракторов поднял, а свой не сломал. "
       "Оля хочет повесить в медпункте, «для поднятия духа пациентов». Не знаю, как у них от меня дух поднимется.",
       "A certificate. 'Best machine operator in the district.' That's for getting five other people's tractors going "
       "at sowing time without breaking my own. Olya wants to hang it in the medical post, 'to raise the patients' "
       "spirits'. Can't see how I'd raise anyone's spirits.")),
    B(30, "6,7", "letter", "sergey", KOSTYA,
      ("Костя зовёт брата на свадьбу. Но сенокос.", "Kostya invites his brother to the wedding. But it's haymaking."),
      ("Приглашение, красивое, с якорем. А у нас сенокос, трава ждать не будет. Отправлю подарок: коптильню, сам сделал "
       "из старого бидона. Наташа, говорит Костя, рыбу любит. Отнесёте на почту? Тяжёлая, предупреждаю.",
       "The invitation, a fine one, with an anchor. But we're haymaking here; the grass won't wait. I'll send a "
       "present: a smoker, I made it myself from an old milk churn. Natasha loves fish, Kostya says. Will you take it "
       "to the post? It's heavy, I'm warning you."),
      reply="out", stamp="a_anchor"),
    B(30, "8,9", "letter", "sergey", KOSTYA,
      ("Костя прислал свадебную фотографию.", "Kostya has sent a wedding photo."),
      ("Свадебная карточка: Костя в костюме, Наташа в каске, это она на работе так снялась, для смеха. Коптильня работает, "
       "пишут, весь двор в дыму и в соседях. Зовут нас на будущее лето. Поедем. На «Урале», говорит Варя. Посмотрим.",
       "A wedding photo: Kostya in a suit, Natasha in a hard hat; she had it taken at work for a laugh. The smoker works, "
       "they write; the whole yard's full of smoke and neighbours. They're inviting us next summer. We'll go. On the "
       "Ural, says Varya. We'll see.")),
    B(40, "5,6,7", "letter", "sergey", KOSTYA,
      ("Дедов «Урал» наконец завёлся.", "Grandad's Ural has finally started."),
      ("Костя пишет: «Ну что, завёлся?» Завёлся! С третьего раза, как дед заводил. Варю в коляску, Оля ругается, а сама "
       "смеётся. Сфотографировал, Косте отправлю, пусть завидует. Отнесёте? Конверт бензином пахнет. Это от счастья.",
       "Kostya writes, 'Well, has it started?' It has! Third go, the way Grandad used to start it. Varya in the sidecar, "
       "Olya scolding and laughing at the same time. I took a picture, I'll send it to Kostya, let him be jealous. Will "
       "you take it? The envelope smells of petrol. That's happiness."),
      reply="out"),
    B(30, "7,8,9", "letter", "sergey", KOSTYA,
      ("Костя собирается на пенсии переехать в Липовку.", "Kostya plans to move to Lipovka when he retires."),
      ("Костя пишет: выйдет на пенсию — к нам, в Липовку. Наташа согласна, хочет туда, где ночь бывает каждый день, "
       "а не раз в году. Это когда ещё будет. А я уже дом присматриваю, через два от нас. Сарай там крепкий. "
       "Для второго «Урала».",
       "Kostya writes that when he retires, he's coming here, to Lipovka. Natasha agrees; she wants to live where night "
       "comes every day, not once a year. That's a long way off. But I'm already eyeing a house, two down from us. "
       "It has a solid shed. For a second Ural.")),
    )


# ================================================================ output
def clean(s):
    assert "\t" not in s and "\n" not in s and "\r" not in s, s
    return s


def main():
    arc_cols = ["arc", "n", "gap", "months", "on", "needs", "kind", "to", "from_ru", "from_en", "brief_ru", "brief_en",
                "news_ru", "news_en", "reply", "gift", "stamp", "sets"]
    lines = ["\t".join(arc_cols)]
    warn = []
    seen = set()
    for name, beats in ARCS:
        assert name not in seen, name
        seen.add(name)
        for n, b in enumerate(beats, 1):
            row = [name, str(n), str(b["gap"]), b["months"], b["on"], b["needs"], b["kind"], b["to"],
                   b["frm"][0], b["frm"][1], b["brief"][0], b["brief"][1], b["news"][0], b["news"][1],
                   b["reply"], b["gift"], b["stamp"], b["sets"]]
            lines.append("\t".join(clean(x) for x in row))
            lim = 700 if b["to"] == "me" else 320
            for lang, i in (("ru", 0), ("en", 1)):
                if len(b["news"][i]) > lim:
                    warn.append(f"{name}#{n} news_{lang} {len(b['news'][i])}")
                if len(b["brief"][i]) > 80:
                    warn.append(f"{name}#{n} brief_{lang} {len(b['brief'][i])}")
                if len(b["frm"][i]) > 40:
                    warn.append(f"{name}#{n} from_{lang} {len(b['frm'][i])}")
    (C / "arcs").mkdir(exist_ok=True)
    (C / "arcs/a.tsv").write_bytes(("\n".join(lines) + "\n").encode("utf-8"))

    lines = ["\t".join(["key", "family", "variant", "name_ru", "name_en"])]
    lines += ["\t".join(clean(x) for x in it) for it in ITEMS]
    (C / "items").mkdir(exist_ok=True)
    (C / "items/a.tsv").write_bytes(("\n".join(lines) + "\n").encode("utf-8"))

    lines = ["\t".join(["key", "family", "bg", "value", "name_ru", "name_en", "series"])]
    lines += ["\t".join(clean(str(x)) for x in st) for st in STAMPS]
    (C / "stamps").mkdir(exist_ok=True)
    (C / "stamps/a.tsv").write_bytes(("\n".join(lines) + "\n").encode("utf-8"))

    used_g = {b["gift"] for _, bs in ARCS for b in bs if b["gift"]}
    used_s = {b["stamp"] for _, bs in ARCS for b in bs if b["stamp"]}
    for k, *_ in ITEMS:
        if k not in used_g:
            warn.append(f"unused item {k}")
    for k, *_ in STAMPS:
        if k not in used_s:
            warn.append(f"unused stamp {k}")
    for g in used_g - {k for k, *_ in ITEMS}:
        warn.append(f"undefined item {g}")
    for s in used_s - {k for k, *_ in STAMPS}:
        warn.append(f"undefined stamp {s}")

    total = sum(len(bs) for _, bs in ARCS)
    gifts = sum(1 for _, bs in ARCS for b in bs if b["gift"])
    stamps = sum(1 for _, bs in ARCS for b in bs if b["stamp"])
    print(f"{total} beats, {gifts} gifts, {stamps} stamps")
    for name, bs in ARCS:
        print(f"  {name}: {len(bs)}")
    for w in warn:
        print("WARN", w)
    pacing()


# ---------------------------------------------------------------- pacing simulation
CHAINS = [["anna", "anna_wedding", "anna_home"], ["fedor"], ["fedor_petya"], ["agafya"], ["agafya_fedor"],
          ["teacher", "teacher_gorodok"], ["varya_moroz"], ["varya_kamchatka"], ["varya"], ["olga"], ["sergey"]]


def simulate(beats, start, t0=0):
    """Days from game start (start = date) until each beat is delivered, ignoring cross-arc flags."""
    t = t0
    out = []
    for i, b in enumerate(beats):
        t = t + b["gap"] if (i or t0 == 0) else t + 1
        months = {int(m) for m in b["months"].split(",")} if b["months"] else None
        while True:
            d = start + datetime.timedelta(days=t)
            if (months is None or d.month in months) and (not b["on"] or d.strftime("%m-%d") == b["on"]):
                break
            t += 1
        out.append(t)
        t += 1  # delivered the day it arrives
    return out


def pacing():
    arcs = dict(ARCS)
    print("pacing (years until the last beat, by start month 1..12):")
    for chain in CHAINS:
        row = []
        for m in range(1, 13):
            start = datetime.date(2030, m, 1)
            t = 0
            for name in chain:
                ts = simulate(arcs[name], start, t)
                t = ts[-1]
            row.append(t / 365)
        print(f"  {'+'.join(chain):34s} " + " ".join(f"{y:.1f}" for y in row))


if __name__ == "__main__":
    main()
