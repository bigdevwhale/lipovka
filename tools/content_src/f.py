# -*- coding: utf-8 -*-
"""Group F: the everyday mail that keeps Lipovka alive forever.

Writes app/src/main/assets/content/templates.tsv, fillers.tsv, events.tsv and stamps/f.tsv.
Run: python tools/content_src/f.py  (then python tools/check_content.py)
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "app/src/main/assets/content"

STAMPS, TEMPLATES, FILLERS, EVENTS = [], [], [], []


def S(key, family, bg, value, ru, en, series):
    STAMPS.append([key, family, bg, str(value), ru, en, series])


def T(key, every, day, months, to, kind, frm, brief, stamp, variants):
    TEMPLATES.append(dict(key=key, every=every, day=day, months=months, to=to, kind=kind,
                          frm=frm, brief=brief, stamp=stamp, variants=variants))


def F(tags, frm, brief, news):
    FILLERS.append((tags, frm, brief, news))


def E(key, start, end, district, look, name, notice, brief, stamp):
    EVENTS.append((key, start, end, str(district), look, name, notice, brief, stamp))


# --------------------------------------------------------------------------- stamps
S("f_news", "book", "cream", 3, "«Сельская новь»", "The Village News", "gorodok")
S("f_pension", "kettle", "gold", 10, "Чай с пенсии", "Pension-day tea", "post")
S("f_science", "star", "night", 6, "Наука и жизнь", "Science and Life", "far")
S("f_bees", "bee", "gold", 4, "Медосбор", "Honey harvest", "lipovka")
S("f_radio", "radio", "sky", 12, "Эфир", "On the air", "radio")
S("f_sewing", "flower", "blue", 3, "Ситец в васильки", "Cornflower chintz", "lipovka")
S("f_knit", "heart", "red", 5, "Тёплые петли", "Warm stitches", "lipovka")
S("f_kids", "cat", "violet", 2, "Кот-почтальон", "The postcat", "post")
S("f_world", "globe", "blue", 15, "Вокруг света", "Around the world", "far")
S("f_garden", "flower", "green", 4, "Космея", "Cosmos", "seasons")
S("f_rail", "train", "dusk", 8, "Перегон 118", "Stretch 118", "station")
S("f_art", "rainbow", "cream", 5, "Палитра", "The palette", "ozerki")
S("f_tech", "rocket", "night", 10, "Техника — молодёжи", "Tech for the young", "far")
S("f_fish", "fish", "sea", 6, "Лещ на горох", "Bream on peas", "ozerki")
S("f_history", "clock", "cream", 20, "Почта-телеграф", "Post and telegraph", "post")
S("f_seeds", "sun", "green", 3, "Февральские семена", "February seeds", "seasons")
S("f_bill", "lantern", "cream", 1, "Лампочка Ильича", "The village bulb", "lipovka")
S("f_shop", "house", "red", 2, "Сельмаг", "The village shop", "lipovka")
S("f_library", "book", "red", 7, "Библиотека", "The library", "lipovka")
S("f_bday", "heart", "gold", 10, "С днём рождения", "Happy birthday", "holidays")
S("f_twins", "goat", "green", 7, "Две козы", "Two goats", "zarechye")
S("f_bday_kid", "horse", "red", 5, "Лошадка", "Little horse", "holidays")
S("f_ny_fir", "fir", "night", 10, "Ёлочка", "Little fir", "holidays")
S("f_ny_snow", "snowflake", "blue", 5, "Снежинка", "Snowflake", "holidays")
S("f_ny_sled", "sled", "cream", 4, "Санки", "The sled", "holidays")
S("f_ny_fireworks", "fireworks", "night", 15, "Салют", "Fireworks", "holidays")
S("f_mar8", "flower", "gold", 8, "Мимоза", "Mimosa", "holidays")
S("f_bell", "bell", "gold", 7, "Первый звонок", "The first bell", "holidays")
S("f_teacher", "book", "green", 10, "Учителю", "To the teacher", "holidays")
S("f_oldny", "moon", "night", 6, "Старый Новый год", "Old New Year", "holidays")
S("f_spring", "sun", "sky", 3, "Первый день весны", "First day of spring", "seasons")
S("f_elders", "kettle", "cream", 9, "Чай с вареньем", "Tea with jam", "holidays")
S("f_radioday", "radio", "red", 7, "День радио", "Radio Day", "radio")
# events
S("f_fair", "horse", "red", 12, "Покровская ярмарка", "The Pokrov fair", "lipovka")
S("f_cranes", "crane", "dusk", 9, "Журавли улетают", "Cranes leaving", "seasons")
S("f_firstsnow", "snowflake", "sky", 3, "Первый снег", "First snow", "seasons")
S("f_freeze", "lake", "blue", 5, "Ледостав", "The river freezes", "seasons")
S("f_frost", "star", "night", 4, "Мороз и звёзды", "Frost and stars", "seasons")
S("f_clubtree", "fir", "green", 6, "Ёлка в клубе", "The club tree", "lipovka")
S("f_carols", "lantern", "night", 5, "Колядки", "Carollers", "holidays")
S("f_maslenitsa", "sun", "gold", 8, "Масленица", "Maslenitsa", "holidays")
S("f_icebreak", "bridge", "sea", 6, "Ледоход", "The ice goes out", "seasons")
S("f_swallows", "swallow", "sky", 4, "Ласточки", "Swallows", "seasons")
S("f_lilac", "flower", "violet", 5, "Сирень", "Lilac", "seasons")
S("f_lastbell", "bell", "green", 3, "Последний звонок", "The last bell", "lipovka")
S("f_hay", "cow", "green", 4, "Сенокос", "Haymaking", "seasons")
S("f_kupala", "flower", "night", 9, "Цвет папоротника", "Fern flower", "holidays")
S("f_berries", "berry", "red", 3, "Земляника", "Wild strawberries", "seasons")
S("f_mushrooms", "mushroom", "green", 5, "Боровик", "The cep", "seasons")
S("f_apples", "apple", "gold", 6, "Яблочный Спас", "Apple Saviour Day", "seasons")
S("f_railday", "train", "blue", 11, "День железнодорожника", "Railway Day", "station")
S("f_fishday", "boat", "sea", 10, "День рыбака", "Fishermen's Day", "ozerki")
S("f_forestday", "tree", "green", 8, "День леса", "Forest Day", "kordon")
S("f_townday", "fireworks", "violet", 14, "День Городка", "Gorodok Day", "gorodok")
S("f_starfall", "star", "dusk", 7, "Звездопад", "Falling stars", "seasons")
S("f_indian", "birch", "gold", 4, "Бабье лето", "Indian summer", "seasons")
S("f_icefish", "fish", "blue", 5, "Подлёдный лов", "Ice fishing", "ozerki")
S("f_potato", "sun", "cream", 2, "Копка картошки", "Potato digging", "lipovka")
S("f_cheese", "goat", "cream", 6, "Сырный день", "Cheese day", "zarechye")


# --------------------------------------------------------------------------- templates: the newspaper
PAPER_TO = "teacher,zina,fedor,erofey,grisha,tamara,matvei,timofei"
PAPER_FROM = ("«Сельская новь»", "The Village News")
PAPER_BRIEF = ("Четверг: по деревне разошлась «Сельская новь».", "Thursday: the Village News went round the village.")

T("paper_winter", "weekly", "4", "12,1,2", PAPER_TO, "newspaper", PAPER_FROM, PAPER_BRIEF, "f_news", [
    ("В Борках вырастили лимон на подоконнике — сорок лимонов! А у меня алоэ третий год решает, цвести ему или нет.",
     "In Borki someone grew a lemon tree on a windowsill — forty lemons! My aloe has spent three years deciding whether to flower."),
    ("Кроссворд опять с подвохом: «Северная птица, пять букв». Вот и вся неделя занята. Только не подсказывайте!",
     "The crossword's being sly again: “northern bird, five letters”. There goes the whole week. Don't tell me!"),
    ("Пишут, грейдер дойдёт до нас к среде. В прошлом году писали так же, а дошёл он к Масленице.",
     "They say the snowplough will reach us by Wednesday. They said that last year too, and it reached us by Maslenitsa."),
    ("В Городке конкурс снеговиков. Победил снеговик с самоваром вместо головы. Вот это фантазия у людей.",
     "A snowman contest in Gorodok. The winner had a samovar for a head. Now that's imagination."),
    ("Объявление: «Отдам котят в добрые руки, рыжие, к лотку приучены». Сургучу только не говорите — обидится.",
     "An ad: “Kittens to a good home, ginger, house-trained.” Don't tell Surguch, he'll take it personally."),
    ("Гороскоп на последней странице: «Ждите важного письма». А вы как раз с письмом. Сбывается!",
     "The horoscope on the back page says: “Expect an important letter.” And here you are with one. It's coming true!"),
    ("Автобус до Городка теперь в 7:15, а не в 7:10. Пять минут — а вся деревня волнуется, как перед свадьбой.",
     "The Gorodok bus now leaves at 7:15, not 7:10. Five minutes, and the whole village is fretting like before a wedding."),
    ("На Озёрках из-подо льда вытащили щуку на девять кило. Фотография есть, щука на ней очень недовольная.",
     "At Ozyorki someone pulled a nine-kilo pike out from under the ice. There's a photo. The pike looks deeply unimpressed."),
    ("Статья про валенки: оказывается, в Москве их снова носят. Мы-то их и не снимали.",
     "An article about felt boots: apparently Moscow is wearing them again. We never took ours off."),
    ("Потерялась коза в Сосновке, белая, с бубенчиком. Услышите в лесу звон — не пугайтесь, это коза.",
     "A goat's gone missing in Sosnovka, white, with a little bell. If you hear ringing in the woods, don't be scared, it's the goat."),
    ("Спрашивают, почему зимой хлеб черствеет быстрее. Отвечает агроном. Длинно. Хлеб за это время зачерствел.",
     "Someone asks why bread goes stale faster in winter. An agronomist replies. At length. The bread went stale meanwhile."),
    ("Детская загадка к Новому году — а над ней вся деревня бьётся. Ответ на шестой странице, вверх ногами. Не смотрим!",
     "A New Year riddle for children, and the whole village is stuck on it. The answer's on page six, upside down. No peeking!"),
    ("Лыжная гонка в Городке: первым пришёл дедушка семидесяти лет. Молодёжь, пишут, «остановилась попить чаю».",
     "The ski race in Gorodok: first across the line was a man of seventy. The young ones, it says, “stopped for a cup of tea”."),
    ("Советуют подкармливать синиц салом, только несолёным. Синицы, видно, на диете. Ну, сало-то у нас есть.",
     "They advise feeding the tits lard, only unsalted. The birds must be on a diet. Well, lard we've got."),
    ("Пишут про зимнюю дорогу по льду Липки: «не рекомендуется». А ею вся деревня ходит.",
     "A piece about the winter road across the Lipka ice: “not recommended”. The whole village uses it."),
    ("Фотография: метель в Городке, и в метели — почтальонша с сумкой. Подпись: «Почта приходит всегда». Это и про вас.",
     "A photo: a blizzard in Gorodok and a post-woman with her bag. The caption: “The post always comes.” That's about you too."),
    ("В библиотеке Городка теперь «вечера настольных игр». У нас лото по вечерам испокон веку — только без объявлений.",
     "Gorodok library has started “board game evenings”. We've had lotto evenings forever, just without a notice in the paper."),
    ("«Наши долгожители»: бабушке из Ракитного сто лет, сама топит печь. Секрет, говорит, — не садиться.",
     "Our Long-Livers: a woman in Rakitnoye is a hundred and lights her own stove. The secret, she says, is never sit down."),
    ("Прогноз на неделю: «местами метель». Это про нас. Мы как раз и есть эти места.",
     "The weekly forecast: “blizzards in places”. That's us. We're the places."),
])

T("paper_spring", "weekly", "4", "3,4,5", PAPER_TO, "newspaper", PAPER_FROM, PAPER_BRIEF, "f_news", [
    ("Фотография ледохода такая, что кажется — льдина сейчас вылезет из газеты прямо на стол.",
     "The photo of the ice breaking up is so good you'd think the floe will climb out of the paper onto the table."),
    ("Объявление: «Продаю рассаду помидоров, недорого, с разговорами». С разговорами — это они честно предупреждают.",
     "An ad: “Tomato seedlings for sale, cheap, conversation included.” At least they're honest about the conversation."),
    ("Конкурс «Лучший скворечник района». Жюри ещё думает, а скворцы уже выбрали — заселились в школьный.",
     "The district's Best Starling House contest. The jury's still thinking, but the starlings have chosen: they've moved into the school's."),
    ("Пишут, в мае пустят второй автобус до Городка. По субботам. Если дорогу не размоет. Её размоет.",
     "They say a second Gorodok bus starts in May. Saturdays. If the road doesn't wash out. It will."),
    ("Про Липку написали: «живописная река с прозрачной водой». В апреле не видели, когда она по огородам течёт.",
     "They wrote about our Lipka: “a picturesque river with clear water”. They've not seen it in April, running through the gardens."),
    ("В Городке открыли кружок скандинавской ходьбы, с палками. Вы без всяких палок столько вёрст отходили — и никакого кружка.",
     "Gorodok has opened a Nordic walking club, with poles. You've walked miles without any poles, and nobody gave you a club."),
    ("Женщина из Ольховки пишет: курица три дня подряд несёт яйца с двумя желтками. Редакция поздравляет. Курицу, видимо.",
     "A woman from Olkhovka writes that her hen has laid double-yolkers three days running. The editors offer congratulations. To the hen, presumably."),
    ("Напечатали, когда сажать огурцы по луне. Сосед сажает по луне, а мы — по соседу. Урожай одинаковый.",
     "They've printed when to sow cucumbers by the moon. The neighbour sows by the moon, we sow by the neighbour. Same harvest."),
    ("Субботник у школы, фотография: все с граблями, а Васька Ершов — с гармошкой. Тоже нужное дело.",
     "The school clean-up day, with a photo: everyone with rakes, and Vaska Yershov with an accordion. Somebody has to."),
    ("В Городок завезли калоши «весёленькой расцветки». Весёленькой! Калоши! Дожили до праздника.",
     "Gorodok has got galoshes “in cheerful colours”. Cheerful! Galoshes! What a time to be alive."),
    ("«Ушёл гусь, серый, откликается на Борю, по характеру строгий». Если встретите Борю — обходите стороной.",
     "“Goose gone, grey, answers to Borya, strict by nature.” If you meet Borya, walk round him."),
    ("Опечатка: вместо хора «Рябинушка» напечатали «Рыбинушка». Теперь всем любопытно, не про рыбу ли они поют.",
     "A misprint: the Little Rowan choir came out as the Little Roach choir. Now everyone wonders if they sing about fish."),
    ("Пишут, жаворонки прилетели раньше срока. Торопыги. Сидят теперь в поле, мёрзнут и поют — гордые.",
     "The larks are back early, it says. Hasty things. Now they sit in the field, freezing and singing, too proud to admit it."),
    ("Кроссворд: «Весенний первоцвет, восемь букв». Подснежник не лезет, мать-и-мачеха не лезет. Что за цветок такой?",
     "The crossword: “early spring flower, eight letters”. Crocus is too short, snowdrop… snowdrop! No, the third letter's a K."),
    ("На второй странице школьные сочинения «Моя деревня». Одно — про нашу почту! Про кота, который спит на письмах!",
     "On page two, children's essays called My Village. One is about our post office! About the cat who sleeps on the letters!"),
    ("Колонка садовода: «Не торопитесь снимать укрытие с роз». Да мы и не торопимся. У нас роз нет.",
     "The gardening column: “Do not hurry to uncover your roses.” We're in no hurry at all. We haven't got any roses."),
    ("В Городке будут красить мост — в голубой. Жители спорят: несерьёзно. А по-моему, весной в самый раз.",
     "They're painting the Gorodok bridge blue. People argue blue isn't serious. Seems just right for spring to me."),
    ("Объявление: «Куплю старый самовар, можно с вмятинами, вмятины — это история». Хорошо сказано.",
     "An ad: “Will buy an old samovar, dents welcome, dents are history.” Nicely put."),
    ("Анекдот на последней странице такой старый, что его ещё мой дед рассказывал. Всё равно смешно.",
     "The joke on the back page is so old my grandfather used to tell it. Still funny."),
])

T("paper_summer", "weekly", "4", "6,7,8", PAPER_TO, "newspaper", PAPER_FROM, PAPER_BRIEF, "f_news", [
    ("Клубника в Ольховке, пишут, с куриное яйцо. А на фото — с горошину. Фотограф, видно, далеко стоял.",
     "The strawberries in Olkhovka are as big as hen's eggs, it says. In the photo they're the size of peas. The photographer must have stood far off."),
    ("Районный рекорд: дед Пантелеев за день скосил гектар. Ему восемьдесят. Косу, пишут, отбивал сам и никому не давал.",
     "A district record: old Panteleyev mowed a hectare in a day. He's eighty. He sharpened the scythe himself, it says, and let no one touch it."),
    ("«Пропала коза, рыжая, звать Мила, любит сушки». У кого в кармане сушки — оглянитесь, не за вами ли она ходит.",
     "“Goat missing, ginger, name of Mila, fond of bagel rings.” If you've got bagel rings in your pocket, look behind you."),
    ("Пишут, комаров в этом году меньше. Кто это писал — тот в Городке сидел, к нам не заезжал.",
     "It says there are fewer mosquitoes this year. Whoever wrote that sat in Gorodok and never came out here."),
    ("Кино на площади в Городке — опять «Девчата». В пятидесятый раз. И пойдут, и смеяться будут на тех же местах.",
     "An open-air film in Gorodok: The Girls again. For the fiftieth time. People will go and laugh in all the same places."),
    ("От жары советуют пить воду и сидеть в тени. Совет простой, а приятно, что о тебе подумали.",
     "For the heat they advise drinking water and sitting in the shade. Simple advice, but it's nice that somebody thought of you."),
    ("Конкурс палисадников: победила хозяйка с мальвами в два метра. Стоят у неё мальвы, как сторожа у калитки.",
     "The front-garden contest went to a woman with two-metre hollyhocks. They stand by her gate like watchmen."),
    ("Кроссворд: «Болотная ягода, восемь букв». Морошка — семь, клюква — шесть… Голубика! Думали, на неделю, а вышло на минуту.",
     "The crossword: “bog berry, nine letters”. Cloudberry's ten… cranberry! That was meant to last the week and lasted a minute."),
    ("В Сосновке молния ударила в старый дуб, а он стоит, только дымком попахивает. Крепкий. Как наши старики.",
     "Lightning struck the old oak in Sosnovka, and it's still standing, just smells a bit smoky. Tough. Like our old folk."),
    ("В Городке открылось кафе-мороженое «Пломбир-сити». Сити! А мороженое, говорят, всё равно как в детстве.",
     "An ice-cream café called Plombir City has opened in Gorodok. City! But the ice cream, they say, tastes like childhood all the same."),
    ("Объявление: «Меняю мотоцикл «Урал» на корову. Корова — с характером, мотоцикл — тоже».",
     "An ad: “Will swap Ural motorcycle for a cow. The cow has character. So does the motorcycle.”"),
    ("Опечатка в программе праздника: «конкурс пирогов с капустником». Теперь и пекут, и спектакль ставят.",
     "A misprint in the fête programme: “a pie-and-sketch-show contest”. So now they're baking and putting on a play."),
    ("Старым липам у нашего клуба, пишут, под двести лет. «Охраняемые». Их и так пчёлы охраняют, всё лето гудят.",
     "The old limes by our club are nearly two hundred, it says. “Protected.” The bees protect them already, humming all summer."),
    ("Пишут, ночью будет звездопад. Будем смотреть. Если комары позволят.",
     "There'll be falling stars tonight, it says. We'll watch. If the mosquitoes allow."),
    ("Гороскоп обещает «неожиданную встречу у воды». У воды каждое утро одна и та же цапля. Вполне ожидаемая.",
     "The horoscope promises “an unexpected meeting by the water”. Every morning by the water there's the same heron. Fully expected."),
    ("Совет: зелень хранить в банке с водой, как букет. Смешно, а работает. Укроп теперь стоит, будто на свидание собрался.",
     "A tip: keep herbs in a jar of water, like a bouquet. Silly, but it works. The dill looks like it's off on a date."),
    ("На Озёрках видели лося: переплыл озеро и ушёл в лес, не обернулся. Гордый.",
     "An elk was seen at Ozyorki: swam the lake and walked into the woods without looking back. Proud beast."),
    ("Конкурс кваса: победил дед, который рецепт не раскрыл. Так и напечатали: «рецепт засекречен».",
     "The kvass contest went to an old man who wouldn't reveal his recipe. They printed it just so: “recipe classified”."),
    ("В объявлениях: «Отдам котёнка, характер золотой, когти — тоже».",
     "In the small ads: “Kitten free to good home, heart of gold, claws to match.”"),
])

T("paper_autumn", "weekly", "4", "9,10,11", PAPER_TO, "newspaper", PAPER_FROM, PAPER_BRIEF, "f_news", [
    ("В Ракитном вырастили кабачок на двенадцать кило. На фото — кабачок и хозяин. Хозяин помельче будет.",
     "In Rakitnoye someone grew a twelve-kilo marrow. The photo shows the marrow and its owner. The owner is the smaller one."),
    ("На выставке урожая — тыква на сто три кило. Привезли на тракторе. По фотографии не поймёшь, кто кого привёз.",
     "At the harvest show, a pumpkin of a hundred and three kilos. It came on a tractor. From the photo you can't tell who brought whom."),
    ("Над Озёрками, пишут, пролетел клин журавлей в двести птиц. Считали всей школой, и у каждого вышло по-разному.",
     "Two hundred cranes flew over Ozyorki, it says. The whole school counted them and everyone got a different number."),
    ("Белый гриб на три кило нашли в Сосновке. На фото он стоит на табуретке, как на пьедестале.",
     "A three-kilo cep was found in Sosnovka. In the photo it stands on a stool like a statue on a plinth."),
    ("Расписание на зиму: последний автобус в 17:40. Значит, в кино в Городок только днём. Или пешком, как вы.",
     "The winter timetable: the last bus is at 5:40. So only matinees in Gorodok. Or you walk, like you do."),
    ("Рецепт квашеной капусты с клюквой. Кто ж капусту по рецепту квасит — её по памяти квасят. Но вырежу.",
     "A recipe for sauerkraut with cranberries. Nobody makes sauerkraut from a recipe, you make it from memory. I'll cut it out anyway."),
    ("«Найдены очки в футляре у автостанции». Наверняка кто-то из наших. У нас полдеревни ищет очки, а они на лбу.",
     "“Glasses in a case found at the bus station.” Must be one of ours. Half the village hunts for glasses that are on their forehead."),
    ("На Покровской ярмарке, пишут, был калач в два метра. Несли вчетвером, съели вдесятером.",
     "At the Pokrov fair, it says, there was a two-metre kalach. Four people carried it, ten ate it."),
    ("Спрашивают, можно ли хранить морковь в песке. Можно. Бабушки это знали, но приятно, когда газета согласна.",
     "Someone asks whether carrots keep in sand. They do. Grandmothers knew, but it's nice when the paper agrees."),
    ("Школьники в Городке посадили аллею из сорока лиственниц. Лет через сорок будет красота. Подождём.",
     "Schoolchildren in Gorodok have planted forty larches. In forty years it'll be beautiful. We'll wait."),
    ("«Пропал пёс, рыжий, хвост бубликом, откликается на всё съедобное». Под это описание подходят все собаки района.",
     "“Dog missing, ginger, curly tail, answers to anything edible.” That describes every dog in the district."),
    ("Интервью со старейшей почтальонкой района: сорок лет с сумкой. Говорит, страшнее собак — калитки. Правда ведь?",
     "An interview with the district's longest-serving post-woman: forty years with the bag. She says gates are worse than dogs. Is it true?"),
    ("Опечатка: «курсы компьютерной грамотности» напечатали как «компотной». Вот на эти записались бы всей деревней.",
     "A misprint: “computer literacy classes” came out as “compote literacy”. Those the whole village would sign up for."),
    ("Первый снег, пишут, ожидается к середине ноября. Снег газету не читает. Придёт, когда захочет.",
     "First snow is expected by mid-November, it says. Snow doesn't read the paper. It'll come when it likes."),
    ("Конкурс названий для новой улицы в Городке: «Солнечная», «Садовая». Скучно. Надо бы «Улица Сургуча».",
     "A contest to name a new street in Gorodok: Sunny Street, Garden Street. Boring. It ought to be Surguch Street."),
    ("На последней полосе закат над Озёрками, «фото читателя». Снимали, видно, с лодки и уронили шапку: на снимке плывёт шапка.",
     "On the back page, a sunset over Ozyorki, “a reader's photo”. Taken from a boat, with a dropped hat: there's a hat floating in the picture."),
    ("В Городке выставка «Сто лет районной почте»: и сумка, и велосипед, и валенки почтальона. Сходите, вам интересно будет.",
     "Gorodok has an exhibition, A Hundred Years of the District Post: the bag, the bicycle, the postman's felt boots. Do go."),
    ("Советуют сажать чеснок под зиму в октябре. А наш в сентябре сажен. Чеснок газет не читает, он и так знает.",
     "They advise planting winter garlic in October. Ours went in in September. Garlic doesn't read the papers, it just knows."),
    ("Конкурс варенья: первое место — крыжовник с орехом, «царское». Мы такое тоже варим, просто не хвастаемся.",
     "The jam contest: first prize to gooseberry with walnuts, “the royal one”. We make that too, we just don't boast."),
])

# --------------------------------------------------------------------------- templates: the pension
T("pension_w", "monthly", "4", "", "agafya,nina,vera,nadya,sofia", "registered",
  ("Пенсионный фонд", "Pension Fund"),
  ("Принесли пенсию — в нескольких домах сегодня чай с конфетами.", "The pension came: a few houses are having tea with sweets tonight."),
  "f_pension", [
    ("Пересчитаю при вас, не обижайтесь: так меня мама учила. Всё верно. Вот, возьмите «Мишку на Севере».",
     "I'll count it in front of you, don't be offended, it's how my mother taught me. All correct. Here, have a chocolate."),
    ("Куплю наконец новый чайник. Старый свистит так, что соседский петух ему отвечает. Жалко, привыкла я к ним обоим.",
     "I'll finally buy a new kettle. The old one whistles so loud the neighbour's cockerel answers. A shame, I'm used to them both."),
    ("Половину — внукам на подарки, четверть — в кубышку, а остальное на шерсть. Носков всем надо.",
     "Half for the grandchildren's presents, a quarter in the piggy bank, the rest on wool. Everyone needs socks."),
    ("В этом месяце побалую себя: пастилы куплю, белёвской, в коробочке. Раз в месяц можно, правда же?",
     "This month I'll spoil myself: a box of Belyov pastila. Once a month is allowed, isn't it?"),
    ("Прибавили? На сорок рублей. Ну, сорок рублей — это две буханки и разговор с продавщицей. Тоже немало.",
     "A rise? Forty roubles. Well, forty roubles is two loaves and a chat with the shop-woman. Not nothing."),
    ("Коплю на поездку к внучке. Третий месяц — уже на билет в одну сторону хватает. Обратно, может, и не захочется.",
     "I'm saving to visit my granddaughter. Three months now: enough for a one-way ticket. Maybe I won't want to come back."),
    ("Калоши новые куплю. Нет, валенки. Нет, калоши — валенки ещё походят. Пока до магазина дойду, решу.",
     "I'll buy new galoshes. No, felt boots. No, galoshes, the boots have a winter left. I'll decide on the way to the shop."),
    ("Разменяю мелочью: внуки приедут — будем в лото на копеечки. Они проигрывают и сердятся, а я выигрываю и радуюсь.",
     "I'll get it in change: the grandchildren are coming, we'll play lotto for kopecks. They lose and sulk, I win and gloat."),
    ("Пересчитала — сошлось. Каждый месяц сходится, а я каждый раз волнуюсь, как на экзамене.",
     "Counted it, it adds up. It adds up every month, and every month I'm as nervous as at an exam."),
    ("Схожу в парикмахерскую, сделаю укладку. Будет соседям на что посмотреть, а то всё платок да платок.",
     "I'll go to the hairdresser's and have it set. Give the neighbours something to look at; it's always a headscarf otherwise."),
    ("Кофе натурального баночку возьму. Пью раз в год, на день рождения, а тут думаю: чего ждать?",
     "I'll get a jar of real coffee. I drink it once a year, on my birthday, but then I thought, why wait?"),
    ("Внук пишет: «Ба, не трать на меня». А я уже потратила — на пряжу. Свитер-то сама свяжу, а пряжа денег стоит!",
     "My grandson writes, “Gran, don't spend it on me.” Too late, it went on yarn. I'll knit the jumper myself, but yarn costs money!"),
    ("Первым делом — конверты. Двадцать штук, с марками. Писать есть кому, пусть и вам работа будет.",
     "Envelopes first. Twenty, with stamps. I've people to write to, and it'll give you some work too."),
    ("Хотела вам десятку на мороженое дать — вижу, не возьмёте. Тогда яблоко. От яблока не отказываются.",
     "I wanted to give you ten roubles for an ice cream, but I can see you won't take it. An apple, then. Nobody refuses an apple."),
    ("Это всё на краску. Забор у меня серый, как ноябрь. Выкрашу в голубой — пусть люди удивляются.",
     "This all goes on paint. My fence is as grey as November. I'll paint it blue and let people wonder."),
    ("Внучке на сапожки пошлю. Она пишет, что растёт по сантиметру в месяц. Пенсия так не растёт.",
     "I'll send some to my granddaughter for boots. She writes she grows a centimetre a month. The pension doesn't."),
    ("Пойду за дрожжами. Пирогов напеку — пенсия, как-никак, праздник.",
     "I'm off for yeast. I'll bake pies: pension day's a holiday, after all."),
    ("Купон на семена положили. Значит, весной будут астры — целая клумба, от Пенсионного фонда.",
     "They put in a coupon for seeds. So in spring there'll be asters, a whole bed of them, courtesy of the Pension Fund."),
])

T("pension_m", "monthly", "4", "", "fedor,teacher,mikhalych,erofey,matvei", "registered",
  ("Пенсионный фонд", "Pension Fund"),
  ("Пенсия пришла: старики сегодня при деньгах и при планах.", "The pension came: the old men are flush with money and plans."),
  "f_pension", [
    ("Пересчитаю, не обессудьте. Не вам не верю — себе. Всё точно, копейка в копейку.",
     "I'll count it, don't mind me. It's not you I don't trust, it's myself. All correct, to the kopeck."),
    ("Куплю наконец новый рубанок. Старому сорок лет, ворчит, как я. Пусть отдохнёт.",
     "I'll finally buy a new plane. The old one is forty and grumbles like me. It's earned a rest."),
    ("Первым делом — батарейки к приёмнику. Без новостей я проживу, а без прогноза погоды — нет.",
     "Batteries for the radio first. I can live without the news, but not without the weather forecast."),
    ("Табак бросил двадцать лет назад. Беру теперь мятные леденцы, коробку. И дешевле, и пахнет лучше.",
     "Gave up tobacco twenty years ago. Now I buy a tin of mint sweets instead. Cheaper and smells nicer."),
    ("Отложу на сапоги к весне. Старые прохудились — шёл вчера по лужам и чувствовал каждую.",
     "I'll put some by for new boots for spring. The old ones leak; yesterday I felt every puddle."),
    ("Прибавили? Как раз на банку краски. Подкрашу крыльцо — будет как жених.",
     "A rise? Just enough for a tin of paint. I'll paint the porch, it'll look like a bridegroom."),
    ("Схожу в Городок, в книжный. Ничего не куплю, но постою, полистаю. Это тоже удовольствие, и бесплатное.",
     "I'll go to the bookshop in Gorodok. I won't buy anything, but I'll stand and leaf through. That's a pleasure too, and free."),
    ("Внукам на мороженое отложу. Они не просят, а я помню: дед давал мне пятак — и я был богачом на целый день.",
     "Some for the grandchildren's ice cream. They don't ask, but I remember: Grandad gave me five kopecks and I was rich all day."),
    ("Очки новые закажу. В этих газета мелкая стала. Или газета мельчает, или я.",
     "I'll order new glasses. The paper's got small in these. Either the paper's shrinking or I am."),
    ("Спасибо, что принесли, не трястись в Городок. За это — чаю, с чабрецом, своим.",
     "Thank you for bringing it, saves me the bumpy ride to Gorodok. You'll have tea for that, with my own thyme."),
    ("Половина — на хозяйство, вторая — тоже на хозяйство. На себя тратить неловко. Хотя… шляпу бы новую.",
     "Half for the house, the other half for the house too. Feels wrong spending on myself. Though… a new hat would be nice."),
    ("Вы мне в следующий раз марок принесите, штук десять, с птицами. Раз пенсия пришла, будем письма писать.",
     "Next time bring me some stamps, ten or so, with birds on. Now the pension's here, we'll write some letters."),
    ("Кильки в томате банку и хлеба чёрного. Сяду у окна — вот тебе и ресторан.",
     "A tin of sprats in tomato and some black bread. Sit by the window and there's your restaurant."),
    ("Куплю поросёнка. Нет, не куплю: привяжусь, назову Борькой, и пиши пропало. Куплю лучше гвоздей.",
     "I'll buy a piglet. No, I won't: I'll get attached, call him Borka, and that's that. I'll buy nails instead."),
    ("Гармонь куплю. Шучу. Струн для гитары куплю. Тоже шучу — гитары нет. Чаю куплю.",
     "I'll buy an accordion. Joking. Guitar strings, then. Joking again, I haven't got a guitar. I'll buy tea."),
    ("Лески новой куплю, ноль три. Старую рыба уже наизусть знает.",
     "I'll buy new fishing line, point-three. The fish know the old one by heart."),
    ("Гвоздей, олифы, а остальное — внучке на книжки. Пусть читает, раз дед читать обленился.",
     "Nails, linseed oil, and the rest for my granddaughter's books. Let her read, since her grandad's gone lazy about it."),
    ("Вот так каждый месяц: деньги вы приносите, а радуюсь я не деньгам — разговору.",
     "Every month the same: you bring the money, and it's not the money I'm glad of, it's the chat."),
])


# --------------------------------------------------------------------------- templates: magazines (monthly)
T("mag_science", "monthly", "10", "", "teacher", "newspaper", ("Журнал «Наука и жизнь»", "Science and Life magazine"),
  ("Учителю пришла «Наука и жизнь» — в окне до ночи будет гореть лампа.", "Science and Life came for the teacher: his lamp will burn late tonight."),
  "f_science", [
    ("Статья про чёрные дыры. Пишут, они не такие уж чёрные. С людьми так же — сорок лет в школе мне это доказывали.",
     "An article on black holes. They're not so black after all, it says. Same with people: forty years in a school proved that to me."),
    ("Моя любимая «Кунсткамера»: рыба, которая ходит по дну на плавниках, как на ножках. Нарисую её детям.",
     "My favourite page of curiosities: a fish that walks along the bottom on its fins, like little legs. I'll draw it for the children."),
    ("Задачи на смекалку на последней странице. Решу за вечер. Одну оставлю на завтра — для удовольствия.",
     "Brain-teasers on the back page. I'll do them tonight. I'll save one for tomorrow, for the pleasure of it."),
    ("Пишут, Луна каждый год отходит от нас на четыре сантиметра. Обиделась, видно. Надо чаще на неё смотреть.",
     "The Moon moves four centimetres further from us every year, it says. Offended, I expect. We should look at it more often."),
    ("Выписываю с шестьдесят какого-то года. Подшивки на чердаке весь потолок держат. Уберу — дом рухнет.",
     "I've taken it since nineteen-sixty-something. The back issues in the attic hold up the ceiling. Move them and the house falls down."),
    ("Тут статья про пчёл — отнесу Михалычу. Скажет «всё враньё», а потом попросит оставить почитать.",
     "There's a piece on bees; I'll take it to Mikhalych. He'll say “it's all lies” and then ask to keep it a few days."),
    ("Пишут про новую комету. Видно будет лет через двадцать. Ничего, подождём, бинокль у меня хороший.",
     "A new comet, they write. It'll be visible in twenty years or so. Never mind, we'll wait; I've good binoculars."),
    ("Шахматный этюд: «Белые начинают и выигрывают». Сорок лет начинаю — пока не выигрывают.",
     "A chess study: “White to play and win.” Forty years I've been playing white. They haven't won yet."),
    ("Статья про сон: человеку нужно восемь часов. Восемь! Кто ж столько спит в деревне? Разве что кот.",
     "An article on sleep: a person needs eight hours. Eight! Who sleeps that long in a village? The cat, maybe."),
    ("Про древний механизм со дна моря, две тысячи лет. Сравнить бы его с ходиками на почте — кто точнее.",
     "About an ancient mechanism found on the seabed, two thousand years old. I'd like to race it against the post-office clock."),
    ("Почему небо синее — три страницы формул. Детям я это объяснял фонариком и стаканом молока. Мой способ лучше.",
     "Why the sky is blue: three pages of formulas. I used to explain it to children with a torch and a glass of milk. My way's better."),
    ("Рубрика «Маленькие хитрости»: как починить ручку чайника проволокой. Я это придумал в семьдесят девятом. Не признали.",
     "Little Tricks: how to mend a kettle handle with wire. I invented that in seventy-nine. Nobody gave me credit."),
    ("На обложке северное сияние. Ерофей Кузьмич говорит, на полярке видел такое, что ни на какую обложку не влезет.",
     "There's an aurora on the cover. Yerofei Kuzmich says he saw ones in the Arctic that no cover could hold."),
    ("Пишут, в капле росы можно увидеть весь сад вверх ногами. Завтра с утра проверю. С лупой.",
     "In a dewdrop, it says, you can see the whole garden upside down. I'll check tomorrow morning. With a magnifying glass."),
])

T("mag_bees", "monthly", "12", "", "mikhalych", "newspaper", ("Журнал «Пчеловодство»", "Beekeeping magazine"),
  ("Михалыч получил «Пчеловодство» и теперь до вечера спорит с журналом.", "Mikhalych got his Beekeeping and will argue with it till evening."),
  "f_bees", [
    ("Пишут: пчела за всю жизнь собирает двенадцатую часть ложки мёда. Двенадцатую! А мы его ложками. Ешьте с уважением.",
     "A bee collects a twelfth of a teaspoon of honey in her whole life, it says. A twelfth! And we eat it by the spoonful. Eat it with respect."),
    ("Статья про итальянских пчёл. Итальянки, конечно, красивые. Но наши, среднерусские, злые да работящие. Как наша зима.",
     "An article on Italian bees. Pretty, the Italians, I grant you. But ours, the dark northern ones, are fierce and hardworking. Like our winters."),
    ("Опять советуют ставить ульи летком на юго-восток. А мои на липы смотрят. Пчеле виднее, куда смотреть.",
     "They advise facing the hive entrances south-east again. Mine face the lime trees. A bee knows best where to look."),
    ("Читатель пишет: пчёлы роем улетели к соседу, а сосед не отдаёт. Ну, это уже не пчеловодство, это сельсовет.",
     "A reader writes that his bees swarmed off to the neighbour's and the neighbour won't give them back. That's not beekeeping, that's the village council."),
    ("Новый дымарь продают, с термометром. С термометром! Мой без всяких термометров, а пчёлы его уважают.",
     "They're selling a new smoker, with a thermometer. A thermometer! Mine hasn't got one, and the bees respect it all the same."),
    ("Рецепт канди на зиму — сахар с мёдом. Это ещё мой дед делал. А теперь вот в журнале, с цветной фотографией.",
     "A recipe for winter candy: sugar and honey. My grandfather made it. Now it's in a magazine, in colour."),
    ("Пишут, пчёлы узнают человека в лицо. Я и не сомневался. Мои меня за версту узнают — и встречают. Строго.",
     "Bees recognise human faces, it says. I never doubted it. Mine know me a mile off, and they greet me. Sternly."),
    ("Реклама медогонки, нержавейка, с мотором. Моя ручная, скрипит, как ходики. Но я ей верен.",
     "An advert for an extractor, stainless steel, with a motor. Mine's hand-cranked and creaks like a wall clock. But I'm loyal to it."),
    ("Пчеловодный костюм «с полной защитой». Полной защиты, скажу я вам, не бывает. Бывают спокойные руки.",
     "A bee suit “with full protection”. There's no such thing as full protection, I'll tell you. There are calm hands."),
    ("Статья «Пчела перед грозой». Что перед грозой пчела злая, я и без статьи знаю — меня в июле три раза за нос учили.",
     "An article: Bees Before a Storm. That bees are cross before thunder I know without reading it. They taught me on the nose three times in July."),
    ("Объявление: меняют пасеку на Кубани на дом с пасекой в средней полосе. Жара, видно, допекла. Пусть едут — лип хватит.",
     "An ad: an apiary in the Kuban to swap for one up here in the middle of Russia. The heat got to them. Let them come, there are limes enough."),
    ("Кроссворд пчеловодный: «Хозяйка улья, пять букв». Матка. Это даже Варя знает.",
     "A beekeeping crossword: “mistress of the hive, five letters”. Queen. Even Varya knows that."),
    ("Письмо пчеловода из Башкирии — мёд у него с липы, как у нас. Написать ему, что ли? Поспорим, чей слаще.",
     "A letter from a beekeeper in Bashkiria: lime honey, like ours. Maybe I'll write to him. We can argue whose is sweeter."),
])

T("mag_radio", "monthly", "15", "", "kolya", "newspaper", ("Журнал «Радио»", "Radio magazine"),
  ("Коля получил журнал «Радио». На кухне опять запахнет канифолью.", "Kolya got his Radio magazine. The kitchen will smell of solder again."),
  "f_radio", [
    ("Схема приёмника на одной лампе! Соберу к зиме. Бабушка говорит: «Паять — не на кухне». Значит, на крыльце.",
     "A one-valve receiver circuit! I'll build it by winter. Gran says, “No soldering in the kitchen.” The porch, then."),
    ("Тут антенна «волновой канал» из алюминиевых трубок. Где взять трубки… Раскладушка! Шучу. Почти.",
     "There's a Yagi antenna made of aluminium tubes. Where do I get tubes… the camp bed! Joking. Mostly."),
    ("Пишут про связь через Луну: сигнал отражается и возвращается. Через Луну! Как письмо, которое само к тебе вернулось.",
     "An article on moonbounce: the signal bounces off the Moon and comes back. Off the Moon! Like a letter that comes back to you on its own."),
    ("Таблица позывных стран. Тут и Тувалу есть! Вот бы связаться — там людей, как у нас в районе.",
     "A table of country prefixes. Tuvalu's in it! I'd love a contact — there are about as many people there as in our district."),
    ("Пишут, морзянка отмирает. А у нас Тамара Ивановна на разъезде до сих пор стучит. Значит, не отмирает.",
     "It says Morse is dying out. But Tamara Ivanovna at the halt still taps away. So it isn't."),
    ("Почему ночью лучше слышно дальние станции? Ионосфера. Бабушке объяснял — она сказала: «Ночью все добрее». Тоже верно.",
     "Why do far stations come in better at night? The ionosphere. I told Gran; she said, “Everyone's kinder at night.” Also true."),
    ("Реклама новых раций. Красивые. Но с самодельной интереснее: каждый раз не знаешь, заработает или нет.",
     "Adverts for new transceivers. Nice. But a homemade one's more fun: you never know if it'll work this time."),
    ("Интервью с радистом полярной станции. Отнесу Ерофею Кузьмичу — пусть скажет, правду пишут или нет.",
     "An interview with a polar-station radio operator. I'll take it to Yerofei Kuzmich and he can tell me if it's true."),
    ("QSL-карточки читателей на развороте. Одна — с пингвином! Будет и у меня такая. Буду ловить.",
     "Readers' QSL cards across two pages. One has a penguin on it! I'll get one like that. I'll keep listening."),
    ("Детектор без батареек — конкурс для начинающих. Я такой в седьмом классе собирал. Ловил «Маяк» и сверчка.",
     "A crystal set with no batteries, a contest for beginners. I built one in year seven. It picked up Radio Mayak and a cricket."),
    ("Чертёж паяльной станции из старого утюга. Бабушке, пожалуй, пока не скажу, куда делся утюг. Шучу! Утюг на месте.",
     "Plans for a soldering station made from an old iron. I won't tell Gran where the iron went. Joking! The iron's fine."),
    ("Рассказ про мальчишку, который поймал голос с дрейфующей льдины. Сам, на самоделку. Вот это я понимаю.",
     "A story about a boy who caught a voice from a drifting ice station. On a homemade set. That's the stuff."),
])

T("mag_sewing", "monthly", "8", "", "anna", "newspaper", ("Журнал «Шьём сами»", "Sew It Yourself magazine"),
  ("Анне пришёл журнал «Шьём сами» — с выкройками на вкладке.", "Anna's sewing magazine came, with patterns on the pull-out."),
  "f_sewing", [
    ("Выкройка платья с запахом. Сошью к лету — из ситца в васильки, что лежит у меня второй год и ждёт.",
     "A wrap-dress pattern. I'll make it by summer, from the cornflower chintz that's been waiting in my drawer for two years."),
    ("Пишут, снова в моде пышные рукава, как у бабушек. Бабушкины платья из сундука сейчас бы в Москве продавать.",
     "Puffed sleeves are back, like our grannies wore. The dresses in Gran's trunk would sell in Moscow now."),
    ("Урок: как вшить потайную молнию. Потайную! У меня все молнии и так прячутся — в нужный момент не найдёшь.",
     "A lesson on sewing in an invisible zip. Invisible! All my zips hide anyway, never there when you need one."),
    ("Конкурс читательниц — лоскутное одеяло. Вот где пригодятся мои обрезки. Их у меня на три одеяла и коврик.",
     "A readers' contest: a patchwork quilt. There's a use for my scraps at last. I've enough for three quilts and a rug."),
    ("Детская выкройка, комбинезончик. Ну… пусть полежит. Когда-нибудь пригодится.",
     "A child's pattern, little overalls. Well… I'll keep it. It'll come in handy some day."),
    ("Советуют гладить шерсть через влажную марлю. Это и мама знала. А вот капля уксуса в воду — это новое. Попробую.",
     "They say to iron wool through damp muslin. Mum knew that. But a drop of vinegar in the water, that's new. I'll try it."),
    ("Фартук с карманом для прищепок. Сошью себе и Агафье Петровне — она прищепки во рту держит, как гвозди.",
     "An apron with a peg pocket. I'll make one for me and one for Agafya Petrovna; she holds her pegs in her mouth like nails."),
    ("Старые вологодские узоры для вышивки. Вот этот, с птицами, вышью на занавеску. Будут птицы на окне.",
     "Old Vologda embroidery patterns. This one with the birds I'll stitch on a curtain. Birds in the window."),
    ("«Начинающим лучше шить из хлопка, он прощает ошибки». Хлопок прощает. А моя машинка — нет.",
     "“Beginners should sew cotton, it forgives mistakes.” Cotton forgives. My sewing machine doesn't."),
    ("Выкройка мужской рубашки, косоворотки. Сошью к празднику. Есть кому.",
     "A pattern for a man's shirt, the old side-buttoned kind. I'll make it for the holiday. I know who for."),
    ("На обложке пальто цвета брусники. Цвета брусники! Где ж такой драп найти — разве ягодой выкрасить.",
     "A coat on the cover the colour of lingonberries. Where would I find cloth like that? I'd have to dye it with berries."),
    ("Читательница из Твери сшила свадебное платье за неделю. За неделю! Я неделю только фату примериваю… в мыслях.",
     "A reader from Tver made a wedding dress in a week. A week! I spend a week just trying on veils… in my head."),
])

T("mag_knit", "monthly", "18", "", "agafya", "newspaper", ("Журнал «Вяжем дома»", "Knit at Home magazine"),
  ("Агафье Петровне пришёл журнал по вязанию. Спицы уже стучат.", "Agafya Petrovna's knitting magazine came. The needles are already clicking."),
  "f_knit", [
    ("Узор «косы с шишечками». Свяжу кому-нибудь свитер. В деревне всегда найдётся, кому холодно.",
     "A cable-and-bobble pattern. I'll knit someone a jumper. There's always somebody cold in a village."),
    ("Как вязать пятку «бумерангом». Пятьдесят лет вяжу пятки по-своему — и ни одна пятка не жаловалась.",
     "How to knit a boomerang heel. Fifty years I've knitted heels my own way, and not one heel has complained."),
    ("Носочки для новорождённых — вяжутся за вечер. Свяжу три пары. В деревне всегда кто-нибудь да родится.",
     "Socks for newborns, done in an evening. I'll knit three pairs. Somebody's always being born in a village."),
    ("Пряжа с люрексом теперь в моде, блестит. Варежки с блеском… А что, на Новый год — пусть блестят.",
     "Sparkly yarn is in fashion now. Glittering mittens… Well, why not, for New Year let them glitter."),
    ("Читательница прислала фото: кот в свитере. Кот, судя по морде, против.",
     "A reader sent a photo of a cat in a jumper. Judging by its face, the cat objects."),
    ("Олени на свитере, жаккард. Оленей вязать не буду — у меня олени всегда выходят коровами.",
     "Reindeer on a jumper, Fair Isle. I won't knit reindeer; mine always come out as cows."),
    ("Пишут, вязание успокаивает нервы. Это смотря что вязать. Ажур — не успокаивает.",
     "Knitting calms the nerves, it says. Depends what you knit. Lace doesn't."),
    ("Конкурс «Тёплые руки»: варежки для сельских школ. Свяжу пять пар. Нет, десять. Десять — число красивее.",
     "A Warm Hands appeal: mittens for village schools. I'll knit five pairs. No, ten. Ten's a nicer number."),
    ("Шарф в двенадцать цветов. Двенадцать! У меня клубочков-обрывков как раз двенадцать цветов. Будет радуга.",
     "A scarf in twelve colours. Twelve! I've got odds and ends in exactly twelve colours. It'll be a rainbow."),
    ("Советуют хранить шерсть с лавандой от моли. А я — с полынью. Моль журнал не читает, полынь ей понятнее.",
     "They say to keep wool with lavender against moths. I use wormwood. The moths don't read magazines; wormwood they understand."),
    ("Носки с узором «сова». Свяжу Варе. Пусть ходит совой.",
     "Socks with an owl pattern. I'll knit them for Varya. Let her go about as an owl."),
    ("Спицы бамбуковые рекламируют, лёгкие. А мне мои алюминиевые дороже: шестьдесят лет вместе, они как пальцы.",
     "They're advertising bamboo needles, very light. I prefer my aluminium ones: sixty years together, they're like my fingers."),
])

T("mag_kids", "monthly", "20", "", "varya", "newspaper", ("Журнал «Мурзилка»", "Murzilka magazine"),
  ("Варе пришёл «Мурзилка». Пол-улицы уже знает про новые загадки.", "Varya got her Murzilka. Half the street has heard the new riddles already."),
  "f_kids", [
    ("Ура, «Мурзилка»! Тут загадка: «Зимой и летом одним цветом». Ёлка! Я давно знаю. Но всё равно приятно.",
     "Hooray, Murzilka! There's a riddle: “Same colour summer and winter.” A fir tree! I've known that for ages. But it's still nice."),
    ("Тут нарисован котик-почтальон с сумкой! Совсем как вы. Только у вас хвоста нет.",
     "There's a picture of a cat postman with a bag! Just like you. Only you haven't got a tail."),
    ("Конкурс рисунков «Мой питомец». Нарисую Сургуча. Он не мой, но спит на ваших письмах — значит, немножко общий.",
     "A drawing contest, My Pet. I'll draw Surguch. He's not mine, but he sleeps on your letters, so he's a bit everybody's."),
    ("Лабиринт: надо довести ёжика до яблока. Я довела! Только два раза через стенку.",
     "A maze: get the hedgehog to the apple. I did it! Only through the wall twice."),
    ("Мама говорит, она тоже «Мурзилку» читала. Значит, он очень старый. А выглядит молодым — весь жёлтый.",
     "Mum says she read Murzilka too. So he must be really old. But he looks young, all yellow."),
    ("Тут рассказ про девочку, которая писала письма Луне. Я тоже напишу. Только куда — «Луна, до востребования»?",
     "There's a story about a girl who wrote letters to the Moon. I'll write one too. But where to? “The Moon, poste restante”?"),
    ("Самоделка: кормушка из пакета из-под молока. Папа поможет. Он так поможет, что будет целый дом.",
     "A make: a bird feeder from a milk carton. Dad will help. He'll help so much it'll be a whole house."),
    ("Найди десять отличий. Я нашла девять. Десятое, наверное, спряталось.",
     "Spot ten differences. I found nine. The tenth must be hiding."),
    ("Вырезалка — маски зверей. Я буду лиса, а вам дам зайца. Вы же быстро ходите.",
     "Cut-out animal masks. I'll be the fox, and you can be the hare. You walk fast."),
    ("Тут письмо от мальчика с Камчатки! Не моего, другого. Сколько же там мальчиков письма пишет…",
     "There's a letter from a boy in Kamchatka! Not mine, another one. How many boys out there write letters…"),
    ("Стишок про дождик. Я его выучу и расскажу вам в следующий раз. Ну… когда выучу.",
     "A poem about the rain. I'll learn it and say it to you next time. Well… when I've learned it."),
    ("Ребус: «КО», потом картинка с совой, потом… Мам! Мама, иди сюда!",
     "A rebus: a picture of a key, then an owl, then… Mum! Mum, come here!"),
])

T("mag_world", "monthly", "6", "", "gleb", "newspaper", ("Журнал «Вокруг света»", "Around the World magazine"),
  ("На кордон пришёл «Вокруг света». У Глеба Андреевича сегодня кругосветка.", "Around the World reached the cordon. Gleb Andreyevich is travelling tonight."),
  "f_world", [
    ("Фарерские острова: ветер такой, что овцы ходят боком. У меня на кордоне ветер не хуже, только овец нет. Хожу боком сам.",
     "The Faroes: winds so strong the sheep walk sideways. The cordon has winds as good, only no sheep. So I walk sideways myself."),
    ("Статья про станцию в Антарктиде: сорок человек, одна кухня. У меня — один человек, одна кухня. Тоже свои плюсы.",
     "An article on an Antarctic base: forty people, one kitchen. Here it's one person, one kitchen. That has its upsides too."),
    ("Самое дождливое место на Земле — в Индии, двенадцать метров осадков в год. Вот бы там померить. Утонул бы с дождемером.",
     "The wettest place on Earth is in India, twelve metres of rain a year. I'd love to measure that. I'd drown along with the rain gauge."),
    ("Про японских почтальонов на велосипедах. Велосипед — мысль. Хотя по нашим корням вы и пешком быстрее.",
     "About Japanese postmen on bicycles. A bicycle's an idea. Though over our tree roots you're faster on foot."),
    ("Путешественник прошёл Сибирь на лыжах — три тысячи километров. Вы столько за пару лет нашагаете. Почти.",
     "A traveller crossed Siberia on skis, three thousand kilometres. You'll walk that in a couple of years. Nearly."),
    ("Карта облаков на развороте. Повешу на стену. Там раньше календарь висел, но облака интереснее.",
     "A cloud atlas across two pages. I'll pin it on the wall. There used to be a calendar there, but clouds are more interesting."),
    ("Пишут, в Исландии двери на ночь не запирают. У нас на кордоне тоже. Только у нас ещё и стучать некому.",
     "In Iceland, it says, nobody locks the door at night. Same here at the cordon. Only here there's nobody to knock either."),
    ("Кулик с маячком летел без посадки одиннадцать дней. Одиннадцать! Я так долго письмо пишу.",
     "A tagged godwit flew eleven days without landing. Eleven! That's how long it takes me to write a letter."),
    ("В Монголии пьют чай с маслом и солью. Попробую. Масло есть, соль есть. Отвагу найдём.",
     "In Mongolia they drink tea with butter and salt. I'll try it. Butter, yes. Salt, yes. Courage we'll find."),
    ("Кроссворд про реки мира. Липки нет. Безобразие. Надо им написать.",
     "A crossword about the rivers of the world. No Lipka. Outrageous. I'll have to write to them."),
    ("Статья про смотрителей маяков. Сидит человек один, светит другим. Похоже на мою работу, только у меня свет — прогноз.",
     "An article on lighthouse keepers. One man alone, shining for others. Rather like my job, only my light's the forecast."),
    ("Фото туманов над Байкалом. Красиво. Но наши, сосновые, не хуже. Утром у меня такой же — только в нём ещё дятел.",
     "Photos of mist over Baikal. Lovely. But our pine-forest mists are no worse. Mine this morning had a woodpecker in it."),
])

T("mag_garden", "monthly", "14", "", "nina,marina", "newspaper", ("Журнал «Сад и огород»", "Garden and Plot magazine"),
  ("Пришёл «Сад и огород» — где-то уже пересаживают рассаду.", "Garden and Plot has come: somewhere seedlings are being pricked out."),
  "f_garden", [
    ("Пишут, огурцы любят музыку. Буду им петь. Соседи тоже услышат — ничего, пусть и соседи растут.",
     "Cucumbers like music, it says. I'll sing to them. The neighbours will hear too; never mind, let the neighbours grow."),
    ("Советуют сажать бархатцы между капустой, от вредителей. Будет капуста в оранжевых бусах. Красота.",
     "They advise planting marigolds among the cabbages against pests. Cabbages in orange beads. Lovely."),
    ("Статья «Огород для ленивых». Вот! Наконец-то про меня написали.",
     "An article: The Lazy Gardener's Plot. At last, they've written about me."),
    ("Удобрение из банановой кожуры. Где ж столько бананов взять… Придётся есть. Ради огорода чего не сделаешь.",
     "Fertiliser from banana skins. Where would we get so many bananas… We'll have to eat them. Anything for the garden."),
    ("Читательница вырастила тыкву на крыше сарая. Тыква свисает и пугает почтальона. Надеюсь, не вас.",
     "A reader grew a pumpkin on her shed roof. It hangs down and frightens the postman. Not you, I hope."),
    ("Как отличить рассаду томатов от рассады перца. А если перепутаешь — будет сюрприз. Я люблю сюрпризы.",
     "How to tell tomato seedlings from pepper seedlings. And if you mix them up, you get a surprise. I like surprises."),
    ("Поливать вечером, тёплой водой из бочки. Бочка есть, вечер есть. Теперь бы ещё спину.",
     "Water in the evening, with warm water from a butt. I've the butt, I've the evening. Now for a back to go with them."),
    ("Обмен семенами по почте! Напишу. Пошлю свою фасоль — пусть путешествует, раз сама я никуда.",
     "Seed swapping by post! I'll write in. I'll send my beans; let them travel, since I don't."),
    ("Слово-то какое — «сидераты». А это, оказывается, горчица. Её у нас и так сеют, просто без слова.",
     "What a word, “green manure”. It turns out it's just mustard. People here sow it anyway, without the word."),
    ("Фото огорода-мандалы, круглого. Круглый огород! Пойду с колышками. А то всё квадратное да квадратное.",
     "A photo of a mandala garden, round. A round vegetable plot! I'll go out with pegs. Everything's so square otherwise."),
    ("Клубника «Царица». Не знаю, царица или нет, а усы пускает, как гусар.",
     "A strawberry called Tsaritsa. Don't know about a queen, but she sends out runners like a hussar's moustache."),
    ("Календарь посадок по луне. По луне так по луне. Луна, по крайней мере, не спорит.",
     "A planting calendar by the moon. By the moon it is. At least the moon doesn't argue."),
])

T("mag_rail", "monthly", "9", "", "viktor,lyosha", "newspaper", ("Журнал «Железнодорожник»", "The Railwayman magazine"),
  ("На разъезд пришёл «Железнодорожник». На перроне читают вслух.", "The Railwayman reached the halt. They're reading it aloud on the platform."),
  "f_rail", [
    ("Новый скоростной — триста пятьдесят в час. Наша «Кукушка» — сорок. Зато у нас видно, как зайцы в поле сидят.",
     "The new high-speed train does three hundred and fifty an hour. Our Cuckoo does forty. But from ours you can see the hares sitting in the field."),
    ("Пишут, за старые фонари обходчиков коллекционеры деньги платят. Деньги! За фонарь! А его надо в руке держать и светить.",
     "Collectors pay money for old track-walkers' lanterns, it says. Money! For a lantern! A lantern's for holding up and shining."),
    ("Раньше станционные часы сверяли по телеграфу каждый полдень. Вот это порядок. У нас часы сверяют по «Кукушке».",
     "Station clocks used to be set by telegraph every noon. That was order. Here we set the clocks by the Cuckoo."),
    ("В Африке поезд идёт, а по путям — жирафы. У нас — коровы. Тоже, знаете, не уступают.",
     "In Africa the train runs and there are giraffes on the line. Here it's cows. They don't give way either, you know."),
    ("Детская страничка, раскраска «Паровоз». Раскрашу. Никто не видит — значит, можно.",
     "A children's page, a colouring-in steam engine. I'll colour it. No one's looking, so it's allowed."),
    ("Самый короткий перегон в стране — меньше километра. У нас восемнадцать вёрст, и каждую можно узнать по берёзе.",
     "The shortest stretch in the country is under a kilometre. Ours is eighteen versts, and you can tell each one by its birch."),
    ("Машинист на пенсии пишет: «Тридцать лет водил поезда — ни разу не опоздал на свидание». Хороший человек.",
     "A retired driver writes: “Thirty years at the controls and never once late for a date.” A good man, you can tell."),
    ("Фото новой формы. Фуражка с золотым околышем. Наша старая тоже ничего. Только на ней кот спал.",
     "Photos of the new uniform. A cap with a gold band. Ours is fine too. The cat just slept on it, that's all."),
    ("Светофор новый, светодиодный. А прежний, керосиновый, был теплее. И на вид, и вообще.",
     "A new LED signal. The old paraffin one was warmer. To look at, and generally."),
    ("Рубрика «Как это было»: на маленьких станциях держали кур. По шпалам у нас до сих пор ходит одна — правнучка тех.",
     "How It Was: small stations used to keep hens. One still walks our sleepers, a great-granddaughter of those."),
    ("Кроссворд: «Стрелочный перевод, восемь букв». Тут думать нечего… а всё равно сижу, думаю. Хорошо.",
     "The crossword: “points on a railway, eight letters”. Nothing to think about… and still I sit and think. Pleasant."),
    ("Статья про снегоочиститель с ротором. Красавец. А у нас Сергей с отвалом на тракторе — и тоже красавец.",
     "An article on a rotary snowplough. A beauty. And we've got Sergey with a blade on his tractor. Also a beauty."),
])

T("mag_art", "monthly", "22", "", "irina,marina", "newspaper", ("Журнал «Художник»", "The Artist magazine"),
  ("Пришёл журнал «Художник» — кто-то сегодня рисует допоздна.", "The Artist magazine came: someone will be painting late tonight."),
  "f_art", [
    ("Левитан, «Март»: лошадь у крыльца, снег синий. Всю зиму ждала март — вот он, в журнале.",
     "Levitan's March: a horse by the porch, blue snow. I've waited all winter for March, and here it is, in a magazine."),
    ("Урок: как рисовать воду. «Вода — это отражение неба». А если вода — это Липка в апреле? Тогда отражение огородов.",
     "A lesson on painting water: “Water is the reflection of the sky.” And if the water is the Lipka in April? Then it reflects vegetable plots."),
    ("Берлинскую лазурь, пишут, открыли случайно, когда хотели получить красный. У меня так каждый день.",
     "Prussian blue, it says, was discovered by accident while someone was trying to make red. That happens to me every day."),
    ("Мастер-класс по линогравюре. Нужен линолеум. Вот и пригодится кусок с кухни — тот, что вздулся.",
     "A linocut workshop. You need lino. That's what the bulging bit of kitchen floor was for."),
    ("«На этюды берите складной стул, зонт и терпение». Терпение есть, стула нет.",
     "“Take a folding stool, an umbrella and patience on your sketching trips.” I've the patience. Not the stool."),
    ("Как Шишкин писал сосны: «Сосна — это не дерево, это характер». Вот это правда.",
     "How Shishkin painted pines: “A pine is not a tree, it's a character.” That's true."),
    ("Палитра месяца «Ноябрь»: охра, серый, сажа. Кто придумал? Ноябрь — он ещё и с брусникой.",
     "This month's palette, November: ochre, grey, soot black. Who chose that? November has lingonberries too."),
    ("Спорят, какие кисти лучше, беличьи или колонковые. Я готова спорить до хрипоты, как в институте.",
     "They're arguing whether squirrel or sable brushes are better. I'm ready to argue till I'm hoarse, like back in art school."),
    ("Айвазовский писал море по памяти. Я по памяти могу только кошку. И то сзади.",
     "Aivazovsky painted the sea from memory. From memory I can only do a cat. From behind."),
    ("Акварель по мокрому — как туман по утрам. Только туман быстрее сохнет.",
     "Wet-on-wet watercolour is like morning mist. Except the mist dries faster."),
    ("Фото мастерской художника в Плёсе: окно во всю стену, на окне кот. Окно хочу. Кот, допустим, найдётся.",
     "A photo of an artist's studio in Plyos: a window the size of a wall, a cat on the sill. I want the window. A cat can be found."),
    ("Про охру: её, оказывается, копали прямо в оврагах. Пойду в наш овраг. Вдруг тоже охра, а мы не знаем.",
     "About ochre: they used to dig it straight out of ravines. I'll go to our ravine. Maybe it's ochre and nobody knows."),
])

T("mag_tech", "monthly", "16", "", "dima,sergey", "newspaper", ("«Техника — молодёжи»", "Tech for the Young magazine"),
  ("Пришла «Техника — молодёжи». В каком-то сарае скоро что-то загудит.", "Tech for the Young has come. Soon something will hum in somebody's shed."),
  "f_tech", [
    ("Статья про летающие автомобили. Нам бы сначала дорогу до Городка. По ней и так машина летает — на ухабах.",
     "An article about flying cars. We'd settle for a road to Gorodok first. Cars already fly on it, over the potholes."),
    ("Схема самодельного ветряка. Поставлю на сарай. Если сорвёт — значит, ветер хороший.",
     "Plans for a homemade wind turbine. I'll put it on the shed. If it blows off, the wind's good."),
    ("Фантастический рассказ про робота, который пасёт коз. Козы его, конечно, перехитрили. Это правдоподобно.",
     "A science-fiction story about a robot goatherd. The goats outwitted it, of course. That part's realistic."),
    ("Пишут, двигатель можно заправлять подсолнечным маслом. Масло есть. Двигатель есть. Жена против.",
     "You can run an engine on sunflower oil, it says. I've the oil. I've the engine. My wife's against it."),
    ("«Сделай сам»: коптильня из старого холодильника. Холодильник старый как раз есть. Вот и не зря не выбросили.",
     "Make It Yourself: a smokehouse from an old fridge. We happen to have an old fridge. Good thing we never threw it out."),
    ("Задача: перевезти волка, козу и капусту, но у лодки мотор. С мотором всё просто — и интерес пропадает.",
     "A puzzle: get the wolf, the goat and the cabbage across, but the boat has a motor. With a motor it's easy, and the fun's gone."),
    ("Кроссворд: «Деталь, без которой трактор не заведётся». Тут вариантов штук двадцать. Любая!",
     "The crossword: “part a tractor won't start without”. There are about twenty answers. Any of them!"),
    ("Изобретатель из Тулы сделал самовар с блютусом. Зачем?.. А хочу.",
     "An inventor in Tula made a samovar with Bluetooth. Why?… I still want one."),
    ("Чертёж снегохода из мотоблока. Этой зимой соберу. Каждую зиму так говорю — но в этот раз чертёж хороший.",
     "Plans for a snowmobile made from a walk-behind tractor. I'll build it this winter. I say that every winter, but this time the plans are good."),
    ("Обложка: космический лифт до орбиты. Лифт! В универмаге Городка и тот третий год не ходит.",
     "The cover: a space elevator to orbit. An elevator! The one in the Gorodok department store hasn't worked in three years."),
    ("Города будущего: башни с садами на крышах. А у нас и так сад. Только без башни, зато с баней.",
     "Cities of the future: towers with gardens on the roofs. We've got a garden already. No tower, but there's a bathhouse."),
    ("Колонка «Вопрос инженеру»: почему скрипит дверь. Отвечают три страницы. Я бы ответил одним словом: смазать.",
     "Ask an Engineer: why does a door creak? Three pages of answer. I'd answer in one word: oil."),
])

T("mag_fish", "monthly", "25", "", "matvei,andrei", "newspaper", ("Журнал «Рыболов»", "The Angler magazine"),
  ("Пришёл «Рыболов». Где-то у печки уже перебирают блёсны.", "The Angler has come. Somewhere by a stove, lures are being sorted."),
  "f_fish", [
    ("Новая блесна, «как живая». Рыба, видно, не знает, как выглядит живая блесна. Посмотрим.",
     "A new lure, “just like the real thing”. The fish don't know what a real lure looks like, I suppose. We'll see."),
    ("Как ловить леща на горох. Горох есть. Лещ где-то есть. Осталось их познакомить.",
     "How to catch bream on peas. I've the peas. The bream's somewhere. Just need to introduce them."),
    ("В Карелии поймали щуку в рост внука рыбака. Внук на фото держится за папу. Правильно делает.",
     "In Karelia someone caught a pike as long as his grandson is tall. On the photo the grandson's holding on to his dad. Wise boy."),
    ("Советуют на рыбалке молчать. А с рыбой разговаривать? Не сказано. Я разговариваю. Она отвечает поклёвкой.",
     "They advise silence when fishing. And talking to the fish? Doesn't say. I talk. They answer with a bite."),
    ("Узел «паломар». Сколько лет вяжу узлы — этого не знал. Научусь. Рыба тоже не знает, а то бы развязывала.",
     "The Palomar knot. All these years tying knots and I didn't know it. I'll learn. The fish don't know it either, or they'd untie it."),
    ("«Клёв зависит от давления». И от погоды, и от луны, и от настроения рыбы. А от рыбака, выходит, ничего.",
     "“Bites depend on the pressure.” And the weather, and the moon, and the mood of the fish. Nothing depends on the angler, then."),
    ("Рецепт ухи по-фински, со сливками. Уха! Со сливками! Попробую. Но никому не скажу.",
     "A recipe for Finnish fish soup, with cream. Fish soup! With cream! I'll try it. But I won't tell a soul."),
    ("Эхолот, «видит каждую рыбу». А рыба, значит, его тоже видит. Пусть меряются.",
     "An echo sounder that “sees every fish”. And the fish see it too, then. Let them stare each other out."),
    ("Опять рассказ про сома, который утащил лодку. Каждый год про этого сома пишут. Знаменитый, видно, сом.",
     "Another story about the catfish that dragged a boat away. They write about that catfish every year. A famous fish."),
    ("Рыбак поймал свою же блесну, потерянную год назад. Вместе с окунем. Окунь, видно, хранил.",
     "An angler caught the lure he'd lost a year before. Along with a perch. The perch must have been keeping it safe."),
    ("Как сплести садок. Сплету. Вечером у печки самое то: руки заняты, голова отдыхает.",
     "How to weave a keep net. I will. Just the job for evenings by the stove: hands busy, head resting."),
    ("Календарь клёва: «среда — отлично». Значит, в среду. Дела подождут, рыба ждать не станет.",
     "The bite calendar: “Wednesday: excellent.” Wednesday it is, then. Work can wait. The fish won't."),
])

T("mag_history", "monthly", "26", "", "sofia,lidia", "newspaper", ("Журнал «Родина»", "Rodina history magazine"),
  ("Пришёл исторический журнал «Родина» — с картами и старыми фотографиями.", "Rodina, the history magazine, came, full of maps and old photographs."),
  "f_history", [
    ("Про земских почтальонов: ходили по сорок вёрст в день, с колокольчиком. С колокольчиком! Вам бы тоже колокольчик.",
     "About rural postmen of old: forty versts a day, with a little bell. A bell! You should have a bell too."),
    ("Про письма с сургучными печатями. Вот откуда у кота на почте имя — Сургуч! Красиво придумано.",
     "About letters sealed with sealing wax. So that's why the post-office cat is called Surguch! Nicely thought of."),
    ("«Находка»: в стене старого дома нашли записку плотника столетней давности — «Строили на совесть». И правда, стоит.",
     "The Find: a carpenter's note in the wall of an old house, a century old: “Built with a conscience.” And it's still standing."),
    ("Про первые сельские библиотеки: двадцать книг на всю волость, читали в очередь. В очередь! За книгой!",
     "About the first village libraries: twenty books for a whole district, read in turn. A queue! For books!"),
    ("Старые вывески: «Чайная», «Керосин», «Почта-телеграф». «Почта-телеграф» — вернуть бы. Звучит.",
     "Old shop signs: Tea Room, Paraffin, Post and Telegraph. Post and Telegraph, I'd bring that back. It sounds right."),
    ("На старинных ярмарках продавали живых медведей. И покупали! Что с ними потом делали, история умалчивает.",
     "At the old fairs they sold live bears. And people bought them! What they did with them next, history doesn't say."),
    ("Про старинные открытки: подписывали так нежно, что и сейчас читать неловко.",
     "About old postcards: they were signed so tenderly it still feels awkward to read them."),
    ("Как делали чернила из дубовых орешков. Попробую. Хоть одно письмо напишу по-старинному.",
     "How ink was made from oak galls. I'll try it. Just one letter written the old way."),
    ("Фото сельского хора, тысяча девятьсот десятый год. Все серьёзные, только мальчишка с краю смеётся. Вот его бы найти.",
     "A photo of a village choir, 1910. All serious, except a little boy at the end, laughing. I'd like to find out who he was."),
    ("Про самовары: в каждой губернии свой. Тульский пузатый, уральский строгий. Прямо как люди.",
     "About samovars: each province had its own. Tula ones are round-bellied, Urals ones are stern. Just like people."),
    ("Карта старых трактов. Наш тракт отмечен пунктиром. Пунктиром мы, значит, в истории.",
     "A map of the old post roads. Ours is a dotted line. So that's how we are in history: dotted."),
    ("Письма ямщиков домой: «Жив, сыт, лошади в порядке». Коротко и всё сказано. Учиться бы так писать.",
     "Coachmen's letters home: “Well, fed, horses in order.” Short and everything said. We should learn to write like that."),
])


# --------------------------------------------------------------------------- templates: shop, library, seeds, bills, clinic
T("shop_invoice", "monthly", "2", "", "zina", "registered", ("Райпо, оптовая база", "District co-op warehouse"),
  ("Зинаиде Павловне пришла накладная с базы — в магазине переучёт.", "Zinaida Pavlovna got the warehouse invoice: stocktaking at the shop."),
  "f_shop", [
    ("Заказывала двадцать кило пряников, а пришлют, пишут, двадцать ящиков. Ну, будет у деревни пряничный месяц.",
     "I ordered twenty kilos of gingerbread and they write they're sending twenty crates. Well, the village is in for a gingerbread month."),
    ("В накладной: «гвозди 100 мм — 0 шт.». Ноль гвоздей! Зато написано аккуратно, с печатью.",
     "On the invoice: “nails, 100 mm — 0 pcs.” Zero nails! Very neatly written, though, and stamped."),
    ("Новинка: чай «Бергамот с чабрецом». Возьму коробку. Наши всё равно купят чёрный со слоном, но пусть стоит для красоты.",
     "Something new: bergamot-and-thyme tea. I'll take a box. Everyone will still buy the black one with the elephant, but it'll look nice on the shelf."),
    ("По отчёту за месяц конфет «Коровка» ушло, как на свадьбу. В деревне кто-то влюблён, точно вам говорю.",
     "According to last month's figures, the toffees went like it was a wedding. Someone in the village is in love, I'm telling you."),
    ("В каталоге мыло в виде клубники. Варя же его съест. Не возьму. Возьму два.",
     "In the catalogue: soap shaped like strawberries. Varya will eat it. I won't order it. I'll order two."),
    ("Пишут, сахар подорожает. Каждый месяц пишут, а варенье всё равно варят. И правильно.",
     "Sugar's going up, they write. They write that every month, and people make jam anyway. Quite right too."),
    ("База просит вернуть ящики из-под лимонада. А в этих ящиках полдеревни рассаду держит. Весной верну.",
     "The warehouse wants its lemonade crates back. Half the village has seedlings in those crates. I'll return them in spring."),
    ("Прислали календарь с котятами, «постоянным клиентам». Повешу над кассой. Сургуч ревновать будет.",
     "They sent a kitten calendar “for regular customers”. I'll hang it over the till. Surguch will be jealous."),
    ("Ошибка: вместо «мука — 50 кг» написали «5 кг». Пять кило муки на всю деревню — это бабе Нине на одно утро.",
     "A mistake: “flour, 5 kg” instead of fifty. Five kilos of flour for the whole village, that's one morning's baking for Granny Nina."),
    ("Новый товар — семечки в шоколаде. Клуб, считай, обеспечен: кино без семечек — не кино.",
     "New stock: chocolate-coated sunflower seeds. The club's sorted, then: a film without seeds isn't a film."),
    ("Пишут: «Доставка во вторник». Вторник у базы — понятие растяжимое. Бывает, до пятницы тянется.",
     "They write, “Delivery on Tuesday.” Tuesday at the warehouse is a flexible idea. Sometimes it stretches to Friday."),
    ("Расписание завоза поменяли: молоко теперь по средам. Напишу на двери. Три раза напишу — всё равно спросят.",
     "The delivery schedule's changed: milk on Wednesdays now. I'll write it on the door. I'll write it three times and they'll still ask."),
])

T("library_books", "monthly", "24", "", "lidia", "parcel", ("Районный библиотечный коллектор", "District library supply"),
  ("В клуб пришла коробка новых книг — Лидия Аркадьевна уже ставит штампы.", "A box of new books reached the club: Lidia Arkadyevna is already stamping them."),
  "f_library", [
    ("Новые книги! Детективов четыре, а очередь на них — семь человек. Будем читать по графику, как воду в засуху давали.",
     "New books! Four detective novels and seven people already queuing. We'll read by rota, like water in a drought."),
    ("Опять прислали Чехова. Пятый раз. Чехова у меня уже больше, чем читателей. Ничего, Чехов не портится.",
     "Chekhov again. The fifth time. I've more Chekhov than readers now. Never mind, Chekhov doesn't go off."),
    ("«Справочник садовода» — на него запись с прошлой осени. Отдам бабе Нине первой, она пирогом обещала.",
     "The Gardener's Handbook: there's been a waiting list since last autumn. Granny Nina gets it first, she promised a pie."),
    ("Пишут: «Верните задолженные книги до конца квартала». А должник у нас один — тот, кто в восемьдесят шестом унёс «Трёх мушкетёров». Ждём.",
     "They write, “Return all overdue books by the end of the quarter.” We've one debtor: whoever took The Three Musketeers in 1986. We're waiting."),
    ("Плакаты «Читайте с детьми». Повешу у входа. У нас дети и так читают — им бы плакат «Ложитесь спать».",
     "Posters saying Read with Your Children. I'll put one by the door. Our children read anyway; what they need is a poster saying Go to Bed."),
    ("Сборник стихов поэта из Городка. Про нашу Липку! Правда, рифма «Липка — скрипка» уже была у двоих.",
     "A collection by a poet from Gorodok. Poems about our Lipka! Though “Lipka” has been rhymed with “fiddle” twice before."),
    ("Учебник по астрономии — Николай Семёнович будет счастлив. Он по нему проверяет, всё ли на небе правильно.",
     "An astronomy textbook: Nikolai Semyonovich will be delighted. He uses it to check the sky is in order."),
    ("Коробка пришла мокрая, дождь. Сушу книги на печке, страницу за страницей. Пахнет на весь клуб, как у бабушки в детстве.",
     "The box came wet, it rained. I'm drying the books on the stove page by page. The whole club smells like Gran's house when I was little."),
    ("Три романа, все про любовь. Ну, у нас зима длинная. Любви много не бывает.",
     "Three novels, all about love. Well, our winters are long. You can't have too much love."),
    ("Детские книжки-раскладушки: раскроешь — и вылезает изба с печкой. Себе бы такую.",
     "Pop-up children's books: open one and up comes a cottage with a stove. I'd like one for myself."),
    ("Сборник пьес для любительского театра. Очень кстати. Кто будет Бабой-Ягой — опять будем тянуть жребий.",
     "A collection of plays for amateur theatre. Just in time. We'll draw lots again for who plays Baba Yaga."),
    ("Подшивка журналов за год. Будет что читать вслух на зимних посиделках. Вслух — оно вкуснее.",
     "A year's run of magazines, bound. Something to read aloud at the winter gatherings. Read aloud, it tastes better."),
])

T("seeds_w", "yearly", "02-10", "", "nina,vera,nadya,agafya,marina,darya,tanya", "parcel", ("Каталог «Семена — почтой»", "Seeds by Post catalogue"),
  ("Пришли каталоги семян. Февраль, а в деревне уже говорят о рассаде.", "Seed catalogues are here. February, and the village talks seedlings."),
  "f_seeds", [
    ("Каталог! Это лучше всякого журнала мод. Томаты «Бычье сердце», «Де Барао», «Сахарный бизон». Бизон! Беру бизона.",
     "The catalogue! Better than any fashion magazine. Tomatoes: Oxheart, De Barao, Sugar Bison. Bison! I'll have the bison."),
    ("Огурец «Кураж», огурец «Изумрудный поток». А «Нежинский» есть? Есть. «Нежинский» — он как старый друг.",
     "Cucumber Courage, cucumber Emerald Stream. And is Nezhinsky there? It is. Nezhinsky's like an old friend."),
    ("Морковь на картинке ровная, как карандаши. У меня такой сроду не вырастало. Но закажу. Вдруг.",
     "The carrots in the picture are as straight as pencils. I've never grown anything like that. But I'll order them. You never know."),
    ("До весны буду листать. Отмечу галочками полкаталога, закажу пять пакетиков. Это у меня такой февраль.",
     "I'll leaf through it till spring. Tick half the catalogue and order five packets. That's my February."),
    ("Космея! Название-то какое, будто из космоса. Ей и место — у самого забора, пусть все видят.",
     "Cosmos! What a name, as if it came from space. It goes right by the fence, where everyone can see."),
    ("Тыква «Россиянка», тыква «Улыбка». Беру «Улыбку». Пусть хоть тыква улыбается, если огурцы подведут.",
     "Pumpkin Rossiyanka, pumpkin Smile. I'll take Smile. At least the pumpkin can smile if the cucumbers let me down."),
    ("Горох «Сахарный». Посажу у калитки, пусть ребятишки щиплют. Всё равно щиплют — так хоть сладкий.",
     "Sugar peas. I'll plant them by the gate for the children to pick. They pick them anyway, so at least they'll be sweet."),
    ("«Новинка — арбуз для средней полосы». Каждый год пишут, каждый год заказываю, каждый год арбуз с яблоко. Но мой!",
     "“New: a watermelon for central Russia.” They write it every year, I order it every year, and every year it's the size of an apple. But it's mine!"),
    ("Подсолнух «Тедди», пушистый, как медвежонок. Посажу у окна — будет заглядывать.",
     "A sunflower called Teddy, fluffy as a bear cub. I'll plant it by the window and it'll peep in."),
    ("Скидка, если заказать до первого марта. Все торопятся. А семена — они не торопятся. Они в пакетике спят.",
     "A discount if you order before the first of March. Everyone's in a hurry. Seeds aren't. They're asleep in the packet."),
])

T("seeds_m", "yearly", "02-20", "", "fedor,mikhalych,sergey,dima,timofei,matvei,andrei", "parcel", ("Каталог «Семена — почтой»", "Seeds by Post catalogue"),
  ("Мужикам пришли каталоги семян. В сараях проверяют лопаты.", "The men got their seed catalogues. Spades are being inspected in sheds."),
  "f_seeds", [
    ("Ну вот и весна началась — с бумажки. Сначала бумажка, потом рассада, потом грядки, потом спина.",
     "There, spring's begun, with a bit of paper. First the paper, then seedlings, then beds, then your back."),
    ("Картошка семенная, сорт «Удача». Возьму «Удачу». Удачи много не бывает.",
     "Seed potatoes, variety Luck. I'll take Luck. You can't have too much."),
    ("Лук-севок по почте. Это его что, в конверте пошлют? Вы уж его поаккуратнее, когда понесёте.",
     "Onion sets by post. Will they send them in an envelope? Do carry them carefully when they come."),
    ("Медоносы — фацелия, донник. Посею у забора. Пусть соседские пчёлы ко мне в гости летают.",
     "Bee plants: phacelia, sweet clover. I'll sow them by the fence. Let the neighbour's bees come visiting."),
    ("Хрен «Валковский». Хрен заказывать — это ж надо додуматься. У меня за баней хрен сам растёт. Как хрен.",
     "Horseradish, Valkovsky variety. Who orders horseradish? Mine grows behind the bathhouse on its own. Like a weed. Like horseradish."),
    ("Перец «Богатырь», редис «Жара», капуста «Слава». Прямо оркестр, а не огород.",
     "Pepper Bogatyr, radish Heat, cabbage Glory. It's a brass band, not a vegetable plot."),
    ("Газонная трава. Газон! В деревне! Нет уж, картошку. Газон пусть в Городке растят.",
     "Lawn seed. A lawn! In a village! No, potatoes. Let Gorodok grow lawns."),
    ("Чеснок озимый, «Любаша». Мужики засмеют. Ничего, посажу и «Любашу».",
     "Winter garlic, a variety called Lyubasha. The men will laugh. Never mind, Lyubasha's going in."),
    ("Отмечу карандашом, что заказать, а потом половину вычеркну. Каталог — как совесть: показывает, сколько хочется и сколько можно.",
     "I'll mark what to order in pencil and then cross out half. A catalogue's like a conscience: it shows how much you want and how much you can."),
    ("Кукуруза «Сахарная». Посажу, а вороны спасибо скажут. Хоть кто-то спасибо скажет.",
     "Sweetcorn. I'll plant it and the crows will say thank you. At least somebody will."),
])

T("bill_power", "monthly", "20", "", "agafya,fedor,teacher,nina,erofey,zina,olga,marina,vera,tamara,gleb,darya", "notice",
  ("Энергосбыт", "The power company"),
  ("Разнесли квитанции за свет. Деревня считает киловатты.", "Electricity bills went round. The village is counting kilowatts."),
  "f_bill", [
    ("Квитанция за свет. Насчитали, будто тут ночью кузница работает. Ну и пусть. Свет у нас хороший, тёплый.",
     "The electricity bill. They've charged as if there's a forge running here at night. Oh well. It's good light, warm light."),
    ("Как прочитаешь счёт — так сразу и выключаешь лишнюю лампочку. Действует лучше всяких уговоров.",
     "Read the bill and you go straight off and switch off a bulb. Works better than any amount of nagging."),
    ("Пишут: «Переходите на электронные квитанции». Ага. А почтальон тогда с пустой сумкой ходить будет? Нет уж.",
     "They write, “Switch to e-bills.” Oh yes? And then the postman walks about with an empty bag? No thank you."),
    ("Счётчику, говорят, «истёк срок поверки». У счётчика срок, а мы тут крутимся без всякой поверки.",
     "The meter's “verification period has expired”, they say. The meter's got an expiry date, and we just keep going, unverified."),
    ("Реклама на обороте — энергосберегающие лампы. Мы и так экономим: днём читаем у окна, вечером — у печки.",
     "An advert on the back: energy-saving bulbs. We save already: by day we read by the window, by night by the stove."),
    ("Долг, оказывается, двенадцать копеек с прошлого месяца. Двенадцать копеек! Пойду отдам, а то спать не буду.",
     "It turns out there's twelve kopecks owing from last month. Twelve kopecks! I'll go and pay, or I won't sleep."),
    ("Квитанция теперь цветная, с картинкой: лампочка улыбается. Ей-то что — не ей платить.",
     "The bill's in colour now, with a picture of a smiling light bulb. Easy for it to smile. It isn't paying."),
    ("Квитанцию — сразу на гвоздик, к остальным. На этом гвоздике вся жизнь по месяцам висит. Как календарь.",
     "The bill goes straight on the nail with the others. That nail holds a whole life month by month. Like a calendar."),
    ("Прислали благодарность за своевременную оплату. Благодарность! Повесим рядом с грамотой.",
     "They've sent a thank-you for paying on time. A thank-you! It'll go up next to the certificate."),
    ("Опять квитанция? Ну и пусть. Хоть бумажка, а почта. Без почты день пустой.",
     "Another bill? Fine. It's only paper, but it's post. A day without post is an empty day."),
    ("Посчитали «по нормативу», а показания-то были отправлены. Ладно, напишем им письмо. Длинное. С выражением.",
     "They've estimated it “by the standard rate”, though the readings were sent. Fine, we'll write them a letter. A long one. With feeling."),
    ("Фамилию опять переврали, одна буква лишняя. А так даже красивее. Может, оставить?",
     "They've got the surname wrong again, one letter too many. It's prettier, actually. Maybe keep it?"),
    ("Счёт пришёл, а свет вчера три часа отключали. За эти три часа вычтут? Не вычтут. Зато звёзды были видны — как в детстве.",
     "The bill's here, and yesterday the power was off for three hours. Will they deduct those? They won't. But you could see the stars, like when we were small."),
    ("Зимой счёт вырос. Зато по вечерам полдеревни у нас чай пьёт. Не жалко: свет общий, разговор общий.",
     "The bill went up over winter. But half the village drinks tea here in the evenings. No regrets: shared light, shared talk."),
])

T("clinic", "yearly", "03-15", "", "agafya,fedor,teacher,mikhalych,nina,erofey,vera,nadya,matvei", "notice",
  ("Районная поликлиника", "District polyclinic"),
  ("Поликлиника зовёт на осмотр. Старики едут в Городок, как на ярмарку.", "Check-up letters: the old folk are off to Gorodok as if to a fair."),
  "", [
    ("Зовут на диспансеризацию. «При себе иметь паспорт и хорошее настроение». Настроение есть. Паспорт бы найти.",
     "They're calling us in for a check-up. “Bring your passport and a good mood.” I've the mood. Now to find the passport."),
    ("Опять поликлиника приглашает. Поеду. Там в очереди все наши — как на ярмарке. Новостей на месяц наберу.",
     "The polyclinic's inviting me again. I'll go. Everyone we know is in that queue; it's like a fair. A month's worth of news."),
    ("Пишут: «Не откладывайте заботу о себе». Раз пишут — поеду. Заодно у вокзала пирожков с капустой куплю.",
     "They write, “Don't put off looking after yourself.” Well, if they say so. And I'll get cabbage pies by the station while I'm there."),
    ("Доктор там новый, молоденький, говорят. Будем его жизни учить, а он нас — давлению.",
     "There's a new doctor, very young, they say. We'll teach him about life and he'll teach us about blood pressure."),
    ("Напоминают: «Мерить давление каждый день». Меряю. Каждый день хорошее. Аппарат, видно, вежливый.",
     "A reminder: “Check your blood pressure daily.” I do. It's good every day. The gadget must be polite."),
    ("Талончик к окулисту. Прочитать бы ещё, на какое число, — буквы мелкие. Вот и повод съездить.",
     "An appointment with the eye doctor. If only I could read which day, the print's so small. There's the reason to go."),
    ("Пишут: «Больше ходите пешком». Это не нам писать надо, это вам. Хотя вам уже больше некуда.",
     "They write, “Walk more.” They should be writing that to you. Though you can't walk any more than you do."),
    ("Флюорография. Автобус в семь, обратно в два. Возьму термос и бутерброды — будет целая экскурсия.",
     "A chest X-ray. The bus at seven, back at two. I'll take a flask and sandwiches; it'll be a proper outing."),
    ("«Вы давно не были у врача». Давно. Потому что всё хорошо. Но съезжу, пусть порадуются.",
     "“You have not seen a doctor for some time.” True. Because all's well. But I'll go and let them be pleased."),
    ("Прививку предлагают. Ладно. Укол — дело минутное, а разговоров потом на неделю.",
     "They're offering a jab. All right. A jab takes a minute, and you get a week of talking out of it."),
])


# --------------------------------------------------------------------------- templates: birthdays
BDAY_FROM = ("Поздравительная открытка", "A birthday card")

T("bday_old_w", "birthday", "", "", "agafya,nina,sofia", "postcard", BDAY_FROM,
  ("Именины: в одном доме сегодня пекут пирог и ждут гостей.", "A birthday: in one house there's a pie in the oven and guests expected."),
  "f_bday", [
    ("Внучка прислала открытку с котёнком в шляпе: «Бабуля, не скучай!» Скучать некогда — к вечеру полон дом, а пирог ещё в печи.",
     "My granddaughter sent a card with a kitten in a hat: “Granny, don't be lonely!” No time for that: the house will be full by evening and the pie's still in the oven."),
    ("Подруга пишет: «Сколько тебе — не скажу, но ты всё такая же». Какая — такая же? Она, видно, меня с косой до пояса помнит.",
     "My friend writes, “I won't say how old you are, but you're just the same.” The same as what? She must remember me with a plait down to my waist."),
    ("Дети пишут: «Мама, приедем в субботу, ничего не готовь». Ничего не готовь! Я уже третий день готовлю.",
     "The children write, “Mum, we're coming on Saturday, don't cook anything.” Don't cook! I've been cooking for three days."),
    ("Открытка с розами, а в ней засушенный кленовый лист. Это внук. Он с детства всё засушивает: листья, жуков, слова в тетрадке.",
     "A card with roses and a pressed maple leaf inside. That's my grandson. He's pressed everything since he was little: leaves, beetles, words in his exercise book."),
    ("Племянница стихами: «С днём рожденья поздравляем, счастья, радости желаем». Стихи не её конёк. Зато от сердца.",
     "My niece wrote a poem: “Happy birthday, joy and cheer, all the best this coming year.” Poetry isn't her strength. But it's from the heart."),
    ("Платок прислали, оренбургский, пуховый. Такой тонкий, что в кольцо пролезает. Сейчас при вас проверю — вот! Пролез!",
     "They've sent a shawl, an Orenburg down shawl. So fine it goes through a ring. I'll test it in front of you. There! Straight through!"),
    ("На конверте: «{name}, с днём рождения!» — а внутри фотография правнука. Два зуба, щёки на весь снимок. Лучший подарок.",
     "On the envelope: “{name}, happy birthday!” And inside, a photo of my great-grandson. Two teeth and cheeks that fill the picture. The best present."),
    ("«Желаем здоровья, счастья, долгих лет». Всё правильно, всё пригодится. А внизу приписка: «И вареньица пришли». Это внук. Почерк его.",
     "“Wishing you health, happiness and many years.” All very proper, all useful. And a P.S.: “And send some jam.” That's my grandson. His handwriting."),
    ("Открытка, а в ней сто рублей, «на конфетки». Как маленькой. А я и рада, как маленькая.",
     "A card with a hundred roubles in it “for sweets”. As if I were little. And I'm as pleased as if I were."),
    ("Двоюродная сестра пишет: «Помнишь, как мы на твой день рождения вброд за черёмухой ходили?» Помню. Мама мне ту юбку неделю не прощала.",
     "My cousin writes, “Remember wading the river for bird cherry on your birthday?” I do. Mum didn't forgive me for that skirt for a week."),
    ("Из клуба поздравляют: «Уважаемая {name}!» С печатью. Повешу у зеркала — буду каждое утро уважаемой.",
     "Greetings from the club: “Dear {name}!” With a stamp. I'll hang it by the mirror and be dear every morning."),
])

T("bday_old_m", "birthday", "", "", "fedor,teacher,mikhalych,erofey,matvei", "postcard", BDAY_FROM,
  ("Именины у старика: к вечеру поставят самовар.", "An old man's birthday: the samovar goes on by evening."),
  "f_bday", [
    ("Внук прислал рисунок: я ростом с дом, а рядом кот ростом с меня. Пропорции, видно, по важности.",
     "My grandson sent a drawing: me as tall as the house and the cat as tall as me. Drawn to scale by importance, I suppose."),
    ("Однокашник пишет: «Тебе сколько, старый? Мне на год больше, так что не задавайся». Шестьдесят лет так пишет.",
     "An old schoolmate writes, “How old are you, old man? I'm a year older, so don't get above yourself.” He's written that for sixty years."),
    ("Дочь пишет: «Папа, купи себе что-нибудь, а не гвозди». Знает меня. Ладно, куплю. Гвозди, но хорошие.",
     "My daughter writes, “Dad, buy yourself something, and not nails.” She knows me. All right, I'll buy something. Nails, but good ones."),
    ("Шарф прислали, в клетку. Я в клетку сроду не ходил. Значит, теперь буду — раз дочь связала.",
     "They sent a scarf. Checked. I've never worn checks in my life. Well, I will now, since my daughter knitted it."),
    ("«Желаем долгих лет и крепкого здоровья». Долгих лет — это пожалуйста. А здоровье у меня как пень. И голова тоже, говорят.",
     "“Wishing you long life and good health.” Long life, by all means. My health is as sturdy as a stump. So's my head, they say."),
    ("Внуки приписали: «Деда, пирог мы тебе не пошлём — почта не довезёт. Мы его съели за тебя». Правильно сделали.",
     "The grandchildren added: “Grandad, we won't post you the cake, it wouldn't survive. We ate it for you.” Quite right."),
    ("Открытка с паровозом. Мне давно не семь, а мне всё паровозы шлют. И правильно. Паровоз — он на всю жизнь.",
     "A card with a steam engine. I haven't been seven for a long time, but they still send me engines. Quite right. A steam engine's for life."),
    ("Сын пишет: «Батя, в субботу приедем всем табором, ставь самовар». Самовар ставить я с пятницы начну.",
     "My son writes, “Dad, we're all coming on Saturday, the whole tribe, put the samovar on.” I'll start putting it on on Friday."),
    ("В конверте фотографии, где мы все вместе, лет тридцать назад. Это я? С чубом? Был чуб.",
     "Photos in the envelope of all of us together, thirty-odd years ago. Is that me? With a forelock? There was a forelock."),
    ("Всего три слова: «Поздравляем, гордимся, целуем». А я, видите, стою тут и улыбаюсь как дурак.",
     "Just three words: “Congratulations, proud, love.” And look at me standing here grinning like a fool."),
    ("Подарок — тапочки. С помпонами. При вас не надену. Но вечером…",
     "The present is slippers. With pompoms. I won't put them on in front of you. But tonight…"),
    ("На конверте: «{name}, с днём рождения!» — почерк старого товарища. Сорок лет не виделись, а почерк тот же, с закорючкой.",
     "On the envelope: “{name}, happy birthday!” in an old friend's hand. Forty years since we met, and his writing's the same, with that little curl."),
])

T("bday_twins", "birthday", "", "", "vera,nadya", "postcard", BDAY_FROM,
  ("У сестёр Ласточкиных день рождения — один на двоих, как всегда.", "The Lastochkin sisters' birthday: one between the two of them, as always."),
  "f_twins", [
    ("Опять открытки одинаковые, мне и сестре. Племянница на фантазии экономит. Ну ничего, моя всё равно красивее.",
     "Identical cards again, for me and my sister. Our niece saves on imagination. Never mind, mine's prettier anyway."),
    ("Каждый год спорим, кто старше. Мама говорила — на двадцать минут. А кто — не говорила. Хитрая была.",
     "Every year we argue about who's older. Mum said by twenty minutes. She never said who. She was a clever one."),
    ("Прислали два платка, голубой и зелёный. До вечера будем спорить, кому какой. А потом поменяемся. Как всегда.",
     "They sent two headscarves, a blue and a green. We'll argue till evening about who gets which. Then we'll swap. As always."),
    ("«Дорогие наши Ласточки!» Хоть бы раз кто-нибудь поздравил по отдельности — а то и поругаться не из-за чего.",
     "“Our dear Swallows!” If only someone would congratulate us separately for once, then we'd have something to quarrel about."),
    ("Внучатый племянник нарисовал нас: две старушки и три козы. Коз нарисовал лучше. Ну, козы и правда лучше.",
     "Our great-nephew drew us: two old women and three goats. He drew the goats better. Well, the goats are better."),
    ("Сестра подарила мне то же, что и я ей: носки. Из одной пряжи. Пятый год подряд. Это традиция, а не жадность.",
     "My sister gave me the same as I gave her: socks. From the same wool. Fifth year running. It's tradition, not stinginess."),
    ("Подруга пишет: «Девчонки, а мне всё кажется — вы с косичками у колодца». Косички-то у нас и сейчас есть.",
     "Our friend writes, “Girls, I still see you with your plaits by the well.” We've still got the plaits."),
    ("День рождения на Восьмое марта — нам всю жизнь дарят вдвое меньше подарков. Мы посчитали.",
     "A birthday on the Eighth of March: all our lives we've got half as many presents. We've counted."),
    ("Пишут нам: «Желаем не ссориться». Это зря. Если не ссориться — о чём тогда разговаривать?",
     "They write, “We wish you'd stop quarrelling.” A waste of a wish. If we didn't quarrel, what would we talk about?"),
    ("Родня прислала сыр, швейцарский. Попробуем, сравним с нашим, козьим. Наш лучше. Ещё не пробовали, но уже знаем.",
     "The family sent cheese, Swiss. We'll try it against our goat's cheese. Ours is better. We haven't tasted it yet, but we know."),
])

T("bday_w", "birthday", "", "", "anna,olga,zina,lidia,marina,tanya,tamara,irina,darya", "postcard", BDAY_FROM,
  ("День рождения: открытки, звонки с горки у водокачки и пирог.", "A birthday: cards, phone calls from the hill by the water tower, and a cake."),
  "f_bday", [
    ("Мама прислала открытку и пирог. Пирог по почте! Немножко помялся в дороге, зато пахнет домом на всю калитку.",
     "Mum sent a card and a pie. A pie by post! A bit squashed on the way, but it smells of home right out to the gate."),
    ("Подруга пишет: «Помнишь, как мы на твой день рождения жарили блины на утюге?» До сих пор не знаю, как мы до этого додумались.",
     "My friend writes, “Remember frying pancakes on an iron for your birthday?” I still don't know how we thought of it."),
    ("Открытка с ёжиком и подписью: «Не колись!» Это брат. Он меня с детства ёжиком зовёт.",
     "A card with a hedgehog: “Don't be prickly!” That's my brother. He's called me Hedgehog since we were small."),
    ("В открытке засушенные васильки. Кто-то помнит, что я люблю васильки. Кто — не подписано. Ох, загадка.",
     "There are pressed cornflowers in the card. Someone remembers I love cornflowers. Who, it doesn't say. Oh, a mystery."),
    ("Тётя пишет: «Желаю счастья, здоровья, успехов в труде и в личной жизни». Всё по списку. Тётя у нас бухгалтер, ничего не пропустит.",
     "My aunt writes, “Wishing you happiness, health, success at work and in your personal life.” All in order. She's an accountant; she never misses an item."),
    ("Серёжки прислали, маленькие, с бирюзой. Надену прямо сейчас. Ну как? Вот и я думаю — хорошо.",
     "Earrings, little turquoise ones. I'll put them on right now. Well? That's what I think too. Lovely."),
    ("Племяшка нарисовала меня в короне. С короной, правда, перестаралась — получился чайник.",
     "My little niece drew me in a crown. She overdid the crown a bit. It came out as a teapot."),
    ("Носки шерстяные и записка: «Чтоб ноги в тепле, а голова в облаках». Это мамино пожелание, она его нам с детства пишет.",
     "Woollen socks and a note: “Warm feet and your head in the clouds.” Mum's wish; she's written it to us since we were small."),
    ("Открытка с музыкой! Откроешь — играет «Каравай». Закроешь — играет дальше. Теперь не знаю, как её остановить.",
     "A musical card! Open it and it plays the birthday song. Close it and it keeps playing. Now I don't know how to stop it."),
    ("Сестра прислала альбом с нашими детскими фотографиями. Тут я с бантом больше головы. Мама любила большие банты.",
     "My sister sent an album of our childhood photos. Here I am with a bow bigger than my head. Mum loved big bows."),
    ("Одноклассница опять написала первой. Каждый год успевает первой! В этом году я её обгоню. В следующем.",
     "My old classmate wrote first again. Every year she's first! This year I'll beat her. Next year, I mean."),
    ("На конверте: «{name}, с днём рождения!» — и нарисовано солнце с ресницами. Так рисуют только в нашей семье.",
     "On the envelope: “{name}, happy birthday!” and a sun with eyelashes. Only our family draws suns like that."),
])

T("bday_m", "birthday", "", "", "sergey,dima,andrei,grisha,lyosha,viktor,gleb,timofei,pavel", "postcard", BDAY_FROM,
  ("День рождения: сегодня кто-то принимает поздравления и делает вид, что не рад.", "A birthday: someone's getting greetings today and pretending not to be pleased."),
  "f_bday", [
    ("Брат прислал открытку с трактором: «Чтоб пахал и не ломался». Это он мне или трактору?",
     "My brother sent a card with a tractor: “Keep ploughing and don't break down.” Is that to me or the tractor?"),
    ("Мама пишет: «Сынок, носи шапку». Мне сколько лет-то? Ну, ношу, ношу.",
     "Mum writes, “Son, wear your hat.” How old am I? All right, all right, I wear it."),
    ("Друг по армии пишет: «А я всё помню, как ты кашу на всю роту пересолил». Двадцать лет помнит! Пересолил-то один раз.",
     "A friend from my army days writes, “I still remember you oversalting the porridge for the whole company.” Twenty years he's remembered! It was only once."),
    ("Открытка со щенком. Я не щенок. Но приятно.",
     "A card with a puppy. I'm not a puppy. But it's nice."),
    ("Тётка прислала свитер с оленями. С оленями! Ну куда я в нём… А, на Новый год. Вот на Новый год и надену.",
     "My aunt sent a jumper with reindeer. Reindeer! Where would I wear that… Ah, New Year. New Year it is."),
    ("Однокурсники скинулись на открытку — тридцать подписей. Половину почерков не узнаю. Остальные узнаю — и смеюсь.",
     "My old college friends all signed one card, thirty signatures. Half the handwriting I don't recognise. The other half I do, and I'm laughing."),
    ("Отец прислал свой старый перочинный нож, с которым сорок лет на рыбалку ходил. Пишет: «Теперь твой». Вот это подарок.",
     "Dad sent his old penknife, the one he took fishing for forty years. He writes, “It's yours now.” Now that's a present."),
    ("В конверте лотерейный билет и записка: «Если выиграешь — половина моя». Это сестра. Деловая.",
     "A lottery ticket in the envelope and a note: “If you win, half's mine.” That's my sister. Businesslike."),
    ("Открытка с часами: «Время — лучший подарок». Подарю себе время: полчаса на крыльце с чаем, ничего не делая.",
     "A card with a clock: “Time is the best present.” I'll give myself some: half an hour on the porch with tea, doing nothing."),
    ("Мама прислала пирожков. Полкоробки, наверное, на почте съели? Шучу! Все целы. Пересчитал.",
     "Mum sent pies. Half the box eaten at the post office, I suppose? Joking! All present. I counted."),
    ("Поздравляют стихами: «Ты сильный, смелый и умелый…» Дальше рифма на «белый». При чём тут белый — не знаю. Но приятно.",
     "They've sent a poem: “You're strong and brave and good with tools…” Then a rhyme with “fools”. Not sure about the fools. Still nice."),
    ("Племянник прислал фотографию: стоит в моей старой куртке. Куртка ему велика. Пока.",
     "My nephew sent a photo of himself in my old jacket. It's too big for him. For now."),
])

T("bday_varya", "birthday", "", "", "varya", "postcard", BDAY_FROM,
  ("У Вари день рождения! Кузнецовы пекут пирог с вишней.", "It's Varya's birthday! The Kuznetsovs are baking a cherry pie."),
  "f_bday_kid", [
    ("Бабушка прислала открытку-раскладушку! Открываешь — и выпрыгивает торт! Ненастоящий, но всё равно.",
     "Gran sent a pop-up card! You open it and a cake jumps out! Not a real one, but still."),
    ("Мне прислали наклейки! Сто штук! Можно я одну наклею на вашу сумку? Ну одну, маленькую.",
     "I got stickers! A hundred! Can I put one on your bag? Just one, a little one."),
    ("Тётя прислала заколку с бабочкой. Бабочка блестит. Я теперь как будто летаю.",
     "My aunt sent a hair clip with a butterfly. The butterfly sparkles. Now it's like I'm flying."),
    ("Открытка от мальчика с Камчатки! Он нарисовал вулкан и меня. Я у него больше вулкана.",
     "A card from the boy in Kamchatka! He drew a volcano and me. I'm bigger than the volcano."),
    ("Мне пишут: «Расти большая». Я и так расту! Мама на двери отметки делает, вот, смотрите.",
     "They wrote “Grow up big.” I am growing! Mum marks it on the door, look."),
    ("Мне настоящее письмо, как взрослой, в конверте с маркой! Марку я себе возьму, а письмо дам маме почитать.",
     "A real letter for me, like a grown-up, in an envelope with a stamp! I'll keep the stamp and let Mum read the letter."),
    ("Дедушка прислал свисток. Мама сказала, что дедушка пошутил. Я свищу, а мама говорит: «Вот дедушка!»",
     "Grandad sent a whistle. Mum said Grandad was joking. I'm whistling, and Mum keeps saying, “Oh, Grandad!”"),
    ("Двоюродная сестра прислала книжку про лошадок. Я её уже прочитала. Пока вы шли.",
     "My cousin sent a book about horses. I've read it already. While you were walking up."),
    ("Вечером пирог с вишней, и все придут! И вы приходите. И Сургуча зовите. Он не пойдёт, но вы позовите.",
     "There's cherry pie tonight and everyone's coming! You come too. And invite Surguch. He won't come, but invite him."),
])

T("bday_kolya", "birthday", "", "", "kolya", "postcard", BDAY_FROM,
  ("У Коли день рождения. Баба Нина с утра у печи.", "It's Kolya's birthday. Granny Nina has been at the stove since dawn."),
  "f_bday_kid", [
    ("Мама прислала открытку и паяльник. Паяльник! Лучший человек на свете. Только бабушке не говорите.",
     "Mum sent a card and a soldering iron. A soldering iron! Best person in the world. Just don't tell Gran."),
    ("Радиолюбитель из Новосибирска прислал QSL-карточку с тортом и антенной. Нарочно нарисовал. Свои понимают.",
     "A radio ham in Novosibirsk sent a QSL card with a cake and an antenna. He drew it specially. Our lot understand."),
    ("Отец пишет: «Расти, сын, и не спали весь дом». Это он про прошлый Новый год. Подумаешь, одна гирлянда.",
     "Dad writes, “Grow up well, son, and don't burn the house down.” That's about last New Year. One fairy-light string, that's all."),
    ("Друг прислал флешку со старыми радиоэфирами. Вечером буду слушать в наушниках. Бабушка решит, что я заболел, — так тихо будет.",
     "A friend sent a flash drive of old radio broadcasts. I'll listen in headphones tonight. Gran will think I'm ill, it'll be that quiet."),
    ("«Занимательная физика», старое издание, с картинками. Я её читал, но эту буду перечитывать.",
     "Physics for Entertainment, an old edition with pictures. I've read it, but I'll read this one again."),
    ("Открытка от одноклассницы. Просто открытка, ничего такого. Ну и что, что с сердечком. Ручка у неё такая.",
     "A card from a girl in my class. Just a card, nothing special. So what if there's a heart on it. That's just her pen."),
    ("Дядя прислал налобный фонарик. Буду теперь паять ночью, как шахтёр.",
     "My uncle sent a head torch. Now I can solder at night, like a miner."),
    ("Бабушке тоже открытка пришла: «С внуком поздравляем». Её с моим днём рождения поздравили. Правильно — она старалась.",
     "Gran got a card too: “Congratulations on your grandson.” They congratulated her on my birthday. Fair enough, she did the work."),
])

# --------------------------------------------------------------------------- templates: New Year cards
NY_FROM = ("Новогодняя открытка", "A New Year card")

T("ny_a", "yearly", "12-27", "", "agafya,fedor,teacher,mikhalych,nina,zina", "postcard", NY_FROM,
  ("Пошли новогодние открытки — сумка пахнет мандаринами.", "The New Year cards have started: the bag smells of tangerines."),
  "f_ny_fir", [
    ("Открытка с Дедом Морозом на тройке. Дед Мороз румяный, как после бани. Поставлю на окно — пусть на улицу смотрит.",
     "A card with Ded Moroz on a troika. He's as rosy as if he'd just left the bathhouse. I'll stand it in the window to watch the street."),
    ("Из Новосибирска: «У нас минус сорок, а у вас?» А у нас минус двенадцать и пироги. Так и напишем.",
     "From Novosibirsk: “It's minus forty here, how about you?” Here it's minus twelve and pies. That's what we'll write back."),
    ("Открытка с блёстками. Блёстки теперь везде — на столе, на руках, на вас. До весны не отмоемся. С Новым годом!",
     "A glittery card. Now there's glitter everywhere: on the table, on my hands, on you. We'll be sparkling till spring. Happy New Year!"),
    ("Пишут: «Пусть в новом году всё будет как в старом, только лучше». Хорошее пожелание. Без лишнего.",
     "They write, “May the new year be like the old one, only better.” A good wish. Nothing extra."),
    ("Старые друзья каждый год шлют одну и ту же открытку — заяц на лыжах. Тридцать лет одного зайца. Зайцы стареют, а друзья нет.",
     "Old friends send the same card every year: a hare on skis. Thirty years of the same hare. The hares get older; the friends don't."),
    ("В открытке снежинка из бумаги, вырезана детской рукой. Немножко кривая. Самая лучшая на свете.",
     "A paper snowflake in the card, cut out by a child. A bit lopsided. The best in the world."),
    ("Открытка с часами: без пяти двенадцать. Каждый год такую присылают — и каждый год сердце ёкает: успеем ли?",
     "A card with a clock at five to midnight. They send one every year, and every year my heart skips: will we make it?"),
    ("Из Сочи: «У нас пальмы в гирляндах». Пальмы в гирляндах! Нет уж, ёлка лучше. Она хоть пахнет.",
     "From Sochi: “Our palm trees have fairy lights on.” Palm trees with lights! No, a fir is better. At least it smells."),
    ("На обороте рецепт салата: «Попробуй, всем нравится». Майонез, майонез и ещё раз майонез. Попробуем!",
     "A salad recipe on the back: “Try it, everybody loves it.” Mayonnaise, mayonnaise and more mayonnaise. We'll try it!"),
    ("Коротко: «С Новым годом. Скучаем. Летом приедем». Шесть слов, а читать можно весь вечер.",
     "Short: “Happy New Year. Miss you. Coming in summer.” Seven words, and you can read them all evening."),
])

T("ny_b", "yearly", "12-28", "", "anna,olga,sergey,lidia,marina,dima,kolya", "postcard", NY_FROM,
  ("Новогодние открытки идут пачками. Сургуч спит на самой блестящей.", "New Year cards are coming in bundles. Surguch is asleep on the shiniest."),
  "f_ny_snow", [
    ("Друзья из Питера: «Приезжайте на каникулы». Каждый год зовут. А мы им: «Приезжайте вы — у нас снег настоящий».",
     "Friends in Petersburg: “Come for the holidays.” They ask every year. And we say, “You come here, our snow is real.”"),
    ("Открытка с ёлкой, а ёлка — из пуговиц, пришитых нитками. Кто-то полвечера сидел. Вот это открытка.",
     "A card with a fir tree made of buttons, sewn on with thread. Somebody spent half an evening on that. Now that's a card."),
    ("Из Мурманска: «У нас полярная ночь, а у вас?» А у нас к четырём уже темно. Почти полярная. Ёлка светит — и ладно.",
     "From Murmansk: “It's polar night here, and you?” Here it's dark by four. Nearly polar. The tree's lit, that'll do."),
    ("«Желаем счастья, здоровья, успехов» — печатными буквами, сразу на двадцать адресов, видно. Ничего, наш — самый главный.",
     "“Wishing you happiness, health and success”, in block capitals, clearly sent to twenty addresses at once. Never mind, ours is the main one."),
    ("Открытка с мандарином. И пахнет мандарином! Пропитали, что ли? Понюхайте сами.",
     "A card with a tangerine. And it smells of tangerine! Did they soak it? Here, smell it."),
    ("Друг детства пишет: «Помнишь, как мы с горки на картонке до самой речки?» Помню. Картонку до сих пор жалко.",
     "A childhood friend writes, “Remember sliding on cardboard all the way down to the river?” I do. I still miss that bit of cardboard."),
    ("В конверте гирлянда из флажков, на каждом буква. Повешу — выйдет «С НОВЫМ ГОДОМ». Если правильно повешу.",
     "A string of paper flags in the envelope, a letter on each. Hang them up and it says HAPPY NEW YEAR. If I hang them right."),
    ("От старых соседей по прежнему дому. Двенадцать лет не писали — а тут вдруг. Новый год всех находит.",
     "From old neighbours where we used to live. Twelve years without a word, and now this. New Year finds everyone."),
    ("Открытка с медведем, который пьёт чай. Это про нас. Будем как медведь: чай, печка и никуда.",
     "A card with a bear drinking tea. That's us. We'll be like the bear: tea, the stove and going nowhere."),
    ("Открытка с совой в шапке: «Чтоб в новом году всё знать и ничему не удивляться». Нет уж. Удивляться — самое лучшее.",
     "A card with an owl in a hat: “May you know everything this year and be surprised by nothing.” No thanks. Being surprised is the best bit."),
])

T("ny_c", "yearly", "12-29", "", "erofey,andrei,tanya,grisha,vera,nadya,matvei,irina", "postcard", NY_FROM,
  ("За реку и на Озёрки несут новогодние открытки.", "New Year cards are going across the river and out to Ozyorki."),
  "f_ny_sled", [
    ("Открытка с санями и бубенцами. Бубенцы нарисованы, а кажется — слышно.",
     "A card with a sleigh and bells. The bells are only drawn, but you'd think you could hear them."),
    ("«Кланяемся всем вашим — и кошке, если есть, и собаке, если есть». Аккуратные люди, всех учли.",
     "“Our regards to all your household, and to the cat if there is one, and the dog if there is one.” Careful people, they've counted everyone."),
    ("Ёлка из ниток, наклеенных на картон. Ниток не пожалели — мохнатая, как настоящая.",
     "A fir tree made of thread glued on card. They didn't skimp; it's as shaggy as a real one."),
    ("Пишут: «Пусть в новом году дорогу не заметает и мост стоит». Кто-то из наших, уехавших. Знает, чего желать.",
     "They write, “May the road stay clear and the bridge stand this year.” One of our people who moved away. Knows what to wish for."),
    ("С Байкала: лёд прозрачный, как стекло, а под ним камни. Вот бы наш лёд такой — до дна видно.",
     "From Baikal: ice as clear as glass with stones beneath. If only our ice were like that, you'd see right to the bottom."),
    ("В конверте пакетик чая, «новогодний», с корицей. Заварим вечером. Корица — для праздника, в будни не положено.",
     "A sachet of “New Year” tea with cinnamon in the envelope. We'll brew it tonight. Cinnamon's for holidays, not weekdays."),
    ("Щенок в шапке Деда Мороза. Это год собаки, что ли? Или кошки? Путаюсь я в этих годах. Пусть будет год щенка.",
     "A puppy in a Ded Moroz hat. Is it the year of the dog? Or the cat? I muddle those years up. Let's call it the year of the puppy."),
    ("«Сколько лет, сколько зим!» — а под этим снеговики, по одному на каждую зиму. Целая толпа снеговиков.",
     "“Long time no see!” And underneath, snowmen, one for every winter. A whole crowd of snowmen."),
    ("Открытка с опозданием на год — прошлогодняя! Где-то путешествовала. Ну, поздравление не портится.",
     "A card a year late: last year's! It's been travelling somewhere. Well, good wishes don't go off."),
    ("Племянники пишут: «Приедем на каникулы кататься с горки». Горку надо залить. Вот и дело на неделю.",
     "The nephews write, “We're coming for the holidays to go sledging.” The slope needs icing. That's the week's job."),
])

T("ny_d", "yearly", "12-30", "", "tamara,lyosha,viktor,gleb,darya,timofei,pavel,sofia", "postcard", NY_FROM,
  ("Последние новогодние открытки — на разъезд, на кордон и в Городок.", "The last New Year cards: to the halt, the cordon and Gorodok."),
  "f_ny_fireworks", [
    ("Открытка с паровозом в снегу. Дым из трубы — из ваты, настоящей, приклеенной. Потрогайте!",
     "A card with a steam engine in the snow. The smoke is cotton wool, real, glued on. Feel it!"),
    ("С юга пишут: «У нас плюс восемь и дождь, завидуем вашему снегу». Пусть завидуют. Снега у нас на всех хватит.",
     "From the south: “Plus eight and raining, we envy your snow.” Let them. We've snow enough for everyone."),
    ("«Желаем, чтобы в новом году было много писем». Это и вам пожелание выходит. Будем стараться — писать.",
     "“Wishing you lots of letters in the new year.” That's a wish for you too, then. We'll do our best, and write."),
    ("Мышка тащит сыр больше себя. Мышка — это я в декабре. Сыр — все дела.",
     "A mouse dragging a cheese bigger than itself. The mouse is me in December. The cheese is everything I've got to do."),
    ("Конверт заклеен наклейками-снежинками со всех сторон. Открывали, как подарок. Внутри открытка и леденец.",
     "An envelope sealed all over with snowflake stickers. Opened it like a present. A card and a boiled sweet inside."),
    ("Знакомые каждый год шлют один и тот же вид своего города. Мы его уже наизусть знаем. Будто сами там бывали.",
     "Friends send the same view of their town every year. We know it by heart now. As if we'd been there."),
    ("Коротко: «С Новым годом! Твой Л.» Кто такой Л.? Перебираю всех знакомых. Загадка на все праздники.",
     "Short: “Happy New Year! Yours, L.” Who's L.? I'm going through everyone I know. A puzzle for the whole holiday."),
    ("А в открытке колокольчик, маленький, на ленточке. Повешу на ёлку. Динь!",
     "And in the card there's a tiny bell on a ribbon. It's going on the tree. Ding!"),
    ("«Пусть Новый год придёт вовремя, как ваша почта». Вот и вас похвалили.",
     "“May the New Year arrive on time, like your post.” There, you've been praised."),
    ("Приписка: «Пришлите рецепт ваших солёных груздей». Рецепт — секрет. Пошлю груздей, пусть сами угадывают.",
     "A P.S.: “Send us your salted mushroom recipe.” The recipe's a secret. I'll send the mushrooms and let them guess."),
])

# --------------------------------------------------------------------------- templates: holidays
T("march8", "yearly", "03-07", "", "anna,agafya,olga,zina,nina,lidia,marina,tanya,vera,nadya,tamara,irina,darya,sofia", "postcard",
  ("Открытка к 8 Марта", "An Eighth of March card"),
  ("Открытки к Восьмому марта: мимоза в каждом втором конверте.", "Cards for the Eighth of March: mimosa in every other envelope."),
  "f_mar8", [
    ("В открытке веточка мимозы, засушенная. Пахнет ещё. Чуть-чуть, но пахнет.",
     "A sprig of mimosa pressed in the card. It still smells. Only a little, but it does."),
    ("Племянник пишет: «Поздравляю с Международным женским днём!» Официально, как на собрании. Стесняется.",
     "My nephew writes, “Congratulations on International Women's Day!” As formal as a meeting. He's shy."),
    ("Брат прислал тюльпаны на открытке: «Тюльпаны — по почте, остальное — при встрече». Ловлю на слове.",
     "My brother sent tulips on a card: “Tulips by post, the rest in person.” I'll hold him to that."),
    ("Подруга из Ташкента пишет: у них абрикосы цветут. А у нас сосульки. Тоже цветут, по-своему.",
     "A friend in Tashkent writes that the apricots are in blossom there. Here it's icicles. They blossom too, in their way."),
    ("Стихами: «Восьмое марта — день чудесный, ты вся такая интересная». Интересная! Ну спасибо.",
     "In verse: “The Eighth of March, a day so fine, you're interesting all the time.” Interesting! Well, thank you."),
    ("Открытка и шоколадка. Шоколадка подтаяла — видно, у печки на почте лежала. Ничего, вкус тот же.",
     "A card and a bar of chocolate. It's melted a bit; it must have sat by the stove at the post office. Never mind, tastes the same."),
    ("Мальчишка-племянник нарисовал меня с букетом больше меня. Подписал: «Это ты, а это цветы». Чтоб не перепутала.",
     "My little nephew drew me with a bouquet bigger than me. He labelled it: “This is you and these are flowers.” So I don't mix them up."),
    ("Подруга пишет: «Девочки, с праздником!» Нам на двоих уже немало, а всё «девочки». И правильно.",
     "My friend writes, “Happy holiday, girls!” Between us we're no spring chickens, but still “girls”. Quite right."),
    ("Открытка с котом, у которого в зубах тюльпан. Кот, по-моему, сам удивлён.",
     "A card with a cat holding a tulip in its mouth. The cat looks surprised, if you ask me."),
    ("Из района: «Уважаемая {name}! С праздником весны!» С печатью. Повешу рядом с грамотой.",
     "From the district: “Dear {name}! Happy Spring Holiday!” With a stamp. It'll go up next to my certificate."),
    ("Пакетик семян астр и подпись: «Цветы, которые ты вырастишь сама». Хитро. Но мило.",
     "A packet of aster seeds and a note: “Flowers you'll grow yourself.” Crafty. But sweet."),
    ("А мне варежки прислали. На Восьмое марта! Ну, март у нас ещё февраль, так что в самый раз.",
     "And I got mittens. For the Eighth of March! Well, our March is still February, so they're just right."),
])

T("sept1", "yearly", "09-01", "", "varya,kolya", "postcard", ("Открытка к 1 сентября", "A First of September card"),
  ("Первое сентября: школьникам пришли открытки от родни.", "The First of September: the schoolchildren got cards from their families."),
  "f_bell", [
    ("Бабушка прислала открытку с портфелем и ручку на двенадцать цветов. Двенадцать цветов в одной ручке! Будет чем подчёркивать.",
     "Gran sent a card with a satchel on it and a twelve-colour pen. Twelve colours in one pen! Plenty to underline with."),
    ("Пишут: «Учись на пятёрки». А на четвёрки можно? Иногда?",
     "They write, “Get top marks.” What about second-best marks? Sometimes?"),
    ("Прислали пенал с секретным отделением. Что я туда положу — секрет.",
     "They sent a pencil case with a secret compartment. What goes in it is a secret."),
    ("Сова в очках: «Сова желает мудрости». Сова сама не очень мудрая — очки вверх ногами.",
     "An owl in glasses: “The owl wishes you wisdom.” The owl's not very wise itself. The glasses are upside down."),
    ("Тётя прислала атлас! Весь мир! Буду искать, где живут все, кто нам пишет.",
     "My aunt sent an atlas! The whole world! I'll find where everyone who writes to us lives."),
    ("«Первое сентября — праздник». Праздник, а портфель тяжёлый. Странный праздник.",
     "“The First of September is a holiday.” A holiday, but the satchel's heavy. A funny sort of holiday."),
    ("Закладка с лисой. Лиса будет сторожить нужную страницу.",
     "A bookmark with a fox. The fox will guard the right page."),
    ("Двоюродный брат пишет: «В школе весело, если повезёт с соседом по парте». Надо, чтобы повезло.",
     "My cousin writes, “School's fun if you get a good desk-mate.” Got to get lucky, then."),
    ("На открытке колокольчик блестящей краской. Звенит, если потрясти? Не звенит. А похоже.",
     "The card has a bell in shiny paint. Does it ring if you shake it? No. But it looks like it would."),
])

T("teachers_day", "yearly", "10-05", "", "teacher", "postcard", ("Открытки от выпускников", "Cards from former pupils"),
  ("День учителя: Николаю Семёновичу пишут ученики со всей страны.", "Teachers' Day: pupils from all over the country write to Nikolai Semyonovich."),
  "f_teacher", [
    ("От выпускника восемьдесят второго: «Я теперь сам учитель физики. Простите за всё, что я делал с вашим маятником». Прощаю. Маятник выжил.",
     "From a boy of the class of '82: “I'm a physics teacher myself now. Forgive me for everything I did to your pendulum.” Forgiven. The pendulum survived."),
    ("От Тани Мироновой, троечницы. Теперь она строит мосты. Держатся, пишет, по моим формулам. Ну, по Ньютону. Но объяснял-то я.",
     "From Tanya Mironova, a C-grade girl. She builds bridges now. They stand up, she writes, by my formulas. Well, Newton's. But I explained them."),
    ("«Помним, как вы вывели нас вечером на школьное крыльцо и показали Сатурн». Тридцать человек у одной трубы, куртки поверх пижам. Помню.",
     "“We remember you taking us out on the school steps one night to see Saturn.” Thirty children at one telescope, coats over pyjamas. I remember."),
    ("Три открытки от одного класса. Договорились, видно, и забыли, кто пишет. Тройное поздравление.",
     "Three cards from the same class. They agreed someone would write and forgot who. A triple greeting."),
    ("Из Мурманска: «Я капитан, и звёзды знаю по-прежнему — по вашей карте». Карту я ему в седьмом классе от руки нарисовал. Вот ведь.",
     "From Murmansk: “I'm a captain now and still know the stars by your chart.” I drew him that chart by hand when he was thirteen. Well, well."),
    ("Рисунок: я у доски, на доске E=mc². Подпись: «Это вы. Узнали?» Узнал. По пиджаку.",
     "A drawing: me at the blackboard, E=mc² on the board. Caption: “This is you. Recognise yourself?” I do. By the jacket."),
    ("«Спасибо за задачу про поезд, который вышел из пункта А. Я его до сих пор жду». Остряк. Это Петров, точно.",
     "“Thank you for the problem about the train leaving station A. I'm still waiting for it.” A comedian. That'll be Petrov."),
    ("От девочки, которая боялась физики: «Я теперь врач, и в рентгене всё понимаю — вы объясняли про свет». Свет — он для всех.",
     "From a girl who was scared of physics: “I'm a doctor now and I understand X-rays because you explained light.” Light's for everybody."),
    ("Конверт фотографий: выпуск девяносто пятого, тридцать лет спустя. Лица взрослые, а глаза те же — с последней парты.",
     "An envelope of photos: the class of '95, thirty years on. Grown-up faces, but the same eyes, from the back row."),
    ("«Ваш прибор для опытов стоит у меня в лаборатории как талисман». Это они про банку с проволокой. Талисман!",
     "“Your experiment apparatus stands in my lab as a mascot.” That's the jar with the wire in it. A mascot!"),
    ("Открытка от Ильи с обсерватории: «Учителю, который показал мне небо». Коротко. Больше и не надо.",
     "A card from Ilya at the observatory: “To the teacher who showed me the sky.” Short. Nothing more needed."),
    ("Внучка выпускницы пишет: «Бабушка рассказывала, как вы рассказывали про кометы. Расскажите и мне». Третье поколение. Сяду писать про кометы.",
     "A former pupil's granddaughter writes, “Gran told me how you told her about comets. Tell me too.” The third generation. I'll sit down and write about comets."),
])

T("old_new_year", "yearly", "01-14", "", "agafya,fedor,nina,erofey,mikhalych,matvei,vera,nadya", "postcard",
  ("Открытка к Старому Новому году", "An Old New Year card"),
  ("Старый Новый год: старикам опять пришли открытки — «на всякий случай».", "Old New Year: the old folk got cards again, “just in case”."),
  "f_oldny", [
    ("Пишут: «Отмечайте, как раньше: с варениками и песнями». Вареники будут. Песни — как получится.",
     "They write, “Celebrate the old way, with dumplings and songs.” Dumplings, yes. Songs, we'll see."),
    ("«Старый Новый год — наш праздник, стариковский». Старики! Скажут тоже. Нам до стариков ещё жить и жить.",
     "“Old New Year is our holiday, the old folks' one.” Old folks! The cheek. We've a long way to go before that."),
    ("«Ещё раз с Новым годом — на всякий случай». Правильно. Лишний раз не помешает.",
     "“Happy New Year once more, just in case.” Quite right. Once more never hurt."),
    ("На Старый Новый год у нас вареники с сюрпризом: в одном монетка, в одном нитка, в одном перец. Что попадётся — такой и год. Приходите!",
     "On Old New Year we make dumplings with surprises: a coin in one, a thread in one, a pepper in one. What you get is your year. Come and try!"),
    ("Снегирь на рябине. Снегирей нынче много — к морозам. И в открытке, и за окном.",
     "A bullfinch on a rowan. Lots of bullfinches this year, that means frost. On the card and outside the window."),
    ("Родня пишет: «Ёлку не разбирайте до Старого Нового года». А мы и до Масленицы не разбираем. Лень — тоже традиция.",
     "The family writes, “Don't take the tree down before Old New Year.” We don't take it down till Maslenitsa. Laziness is a tradition too."),
    ("«С наступающим старым Новым годом, с прошедшим новым». Голову сломаешь, а всё правильно.",
     "“Happy coming Old New Year, and belated happy new New Year.” It'll twist your head, but it's all correct."),
    ("В открытке вырезанная из бумаги звезда. Повесим на окно, пусть до весны светит.",
     "A paper star cut out and tucked in the card. We'll hang it in the window to shine till spring."),
])

T("spring_day", "yearly", "03-01", "", "teacher,anna,marina,irina,gleb,tamara,lidia,dima", "postcard",
  ("Открытка «С первым днём весны»", "A First Day of Spring card"),
  ("Первое марта: открытки с подснежниками — при сугробах по пояс.", "The first of March: snowdrop cards, with snowdrifts up to the waist."),
  "f_spring", [
    ("«С первым днём весны!» — а за окном метель. Ну, весна по календарю. Календарю виднее.",
     "“Happy first day of spring!” And there's a blizzard outside. Well, it's spring by the calendar. The calendar knows best."),
    ("На открытке подснежник. Настоящие вылезут к апрелю, а этот уже тут. Торопыга.",
     "A snowdrop on the card. The real ones won't be up till April, but this one's here already. Impatient thing."),
    ("Пишут: «Весна пришла!» Куда пришла? Где? Пойду поищу. Может, она у вас в сумке.",
     "They write, “Spring is here!” Where? Here where? I'll go and look. Maybe it's in your bag."),
    ("С юга прислали фото: миндаль цветёт. Миндаль! А мы тут сосульки считаем. Ничего, догоним.",
     "A photo from the south: almond trees in blossom. Almonds! And we're counting icicles. Never mind, we'll catch up."),
    ("В конверте семена и записка: «Посади первого марта на подоконник — будет весна в горшке». Посажу.",
     "Seeds in the envelope and a note: “Plant them on the windowsill on the first of March and you'll have spring in a pot.” I will."),
    ("Открытка с грачами. В школе такая картина висела — «Грачи прилетели». Там грачи грустные, а на открытке весёлые.",
     "A card with rooks. There was a painting like it at school, The Rooks Have Come Back. Sad rooks in that one; these are cheerful."),
    ("«Первый день весны — открывайте форточку!» Открою. На минутку. Пусть весна зайдёт, погреется.",
     "“First day of spring: open the window!” I will. For a minute. Let spring come in and warm up."),
    ("Жаворонок из теста на картинке, а на обороте рецепт. Испечём жаворонков, как в детстве, с изюминками вместо глаз.",
     "A dough lark on the front and the recipe on the back. We'll bake larks like when we were small, with raisins for eyes."),
])

T("elders_day", "yearly", "10-01", "", "agafya,fedor,teacher,mikhalych,nina,erofey,vera,nadya,matvei,sofia", "postcard",
  ("Районный Дом культуры", "District House of Culture"),
  ("Первое октября: старшим — открытки и приглашения на концерт.", "The first of October: cards and concert invitations for the older folk."),
  "f_elders", [
    ("Приглашают на концерт ко Дню пожилого человека. Пожилого! Ладно, пойду. Но сидеть буду в первом ряду, как молодёжь.",
     "An invitation to a concert for the Day of Older People. Older! All right, I'll go. But I'll sit in the front row like the young ones."),
    ("«Спасибо вам за всё, что вы сделали». Прямо так — за всё. Это ж сколько всего сделано… Приятно.",
     "“Thank you for everything you've done.” Just like that, everything. That's a lot of doing… Nice, though."),
    ("Чаепитие будет с самоваром и баянистом. Тот самый баянист, что всё время в другую песню уходит. Пойдём слушать, куда уйдёт.",
     "There'll be tea with a samovar and a button-accordion player. The very one who always wanders off into another song. We'll go and see where he wanders."),
    ("Подарок от района — плед, клетчатый. Будем теперь с котом спорить, чей.",
     "A present from the district: a checked blanket. Now we'll argue with the cat over whose it is."),
    ("Школьники пишут: «Уважаемые бабушки и дедушки!» Всех сразу, оптом. Ну, нас много, правильно.",
     "The schoolchildren write, “Dear grannies and grandads!” All of us at once, wholesale. Well, there are a lot of us."),
    ("Зовут на конкурс частушек. Частушек я знаю сто. Тех, что можно петь со сцены, — три.",
     "They're inviting us to a ditty contest. I know a hundred ditties. Ones you can sing on stage: three."),
    ("«Желаем бодрости духа». Дух бодрый. А у спины своё мнение, она с духом не советуется.",
     "“Wishing you good spirits.” The spirits are fine. The back has its own opinion and doesn't consult them."),
    ("Выставка «Руки мастера» — просят принести что-нибудь своё. Принесу варенья банку. Тоже руки, тоже мастер.",
     "An exhibition, Master's Hands: bring something you've made. I'll bring a jar of jam. Hands too, mastery too."),
])

T("radio_day", "yearly", "05-07", "", "kolya,erofey", "postcard", ("Радиоклуб «Эфир», Городок", "Ether Radio Club, Gorodok"),
  ("День радио: радистам пришли открытки с позывными.", "Radio Day: the radio operators got cards with call signs."),
  "f_radioday", [
    ("Открытка с антенной и подписью «73!». По-нашему, по-радийному, — наилучшие пожелания.",
     "A card with an antenna, signed “73!” That's radio talk for best wishes."),
    ("«Слушайте эфир вечером — праздничные позывные». Будем слушать. Чай заварим — и в наушники.",
     "“Listen tonight for the holiday call signs.” We will. Make a pot of tea and on with the headphones."),
    ("Открытка — Попов у приёмника. Сто с лишним лет, а усы как вчера.",
     "A card of Popov at his receiver. More than a hundred years ago, and his moustache looks like yesterday."),
    ("Зовут на слёт радиолюбителей в Городок. Возьму ключ. Вдруг кто захочет посостязаться на скорость.",
     "An invitation to the radio hams' gathering in Gorodok. I'll take my key. Someone might fancy a speed contest."),
    ("Значок радиоклуба прислали, маленький, с молнией. Приколю на шапку.",
     "They sent a radio club badge, a little one with a lightning bolt. It's going on my hat."),
    ("В открытке строчка морзянкой. Сейчас прочитаю… «С праздником, друг». Ну вот. Расстрогали, а ещё радисты.",
     "A line of Morse in the card. Let me read it… “Happy holiday, friend.” There. Gone all soft, and they call themselves radio men."),
    ("«Радио живо, пока его кто-то слушает». Слушаем. Каждый вечер слушаем.",
     "“Radio is alive as long as someone's listening.” We are. Every evening."),
    ("Конкурс: кто больше стран поймает за праздничную ночь. Спать, значит, не будем.",
     "A contest: who can catch the most countries in the holiday night. So no sleep, then."),
])


# --------------------------------------------------------------------------- events (every year)
E("capel", "03-20", "03-26", 0, "none", ("Капель", "Drip-time"),
  ("Объявление на почте: «Граждане! С крыш капает и падает. Под сосульками не стоять, рты не раскрывать, кота Сургуча с крыльца не сгонять — он греется». Подпись: «Почта».",
   "A notice at the post office: “Citizens! Things are dripping and dropping off roofs. Do not stand under icicles, do not stand gaping, and do not shoo Surguch off the steps: he is warming up.” Signed: “The Post.”"),
  ("Капель: с крыш звенит, на дорогах первые лужи.", "Drip-time: the roofs are ringing and the first puddles are out."), "")

E("maslenitsa", "easter-55", "easter-49", 0, "maslenitsa", ("Масленица", "Maslenitsa"),
  ("Клуб зовёт на Масленицу! Блины у каждого двора, катание с горы на чём придётся, взятие снежной крепости, столб с сапогами (сапоги новые, столб старый). В воскресенье — проводы зимы на лугу у мельницы. Чучело шьём всей деревней, солома от Кузнецовых.",
   "The club invites you to Maslenitsa! Pancakes at every gate, sledging down the hill on anything that slides, storming the snow fort, the greasy pole with boots on top (new boots, old pole). On Sunday, seeing off winter in the meadow by the mill. The whole village is making the straw winter-doll; the straw is from the Kuznetsovs."),
  ("Масленица! Над деревней пахнет блинами и дымом.", "Maslenitsa! The village smells of pancakes and smoke."), "f_maslenitsa")

E("icebreak", "04-08", "04-15", 0, "icebreak", ("Ледоход", "The ice goes out"),
  ("От сельсовета и рыбаков: «Лёд на Липке тронулся. На лёд не выходить, лодки от берега убрать, детей на мост за руку. Кто хочет смотреть — смотрите с высокого берега у мельницы, там видно лучше и не страшно».",
   "From the village council and the fishermen: “The ice on the Lipka is moving. Keep off it, pull the boats up, hold children's hands on the bridge. Those who want to watch, watch from the high bank by the mill; you see more and it's safe.”"),
  ("Ледоход! Вся деревня на берегу, льдины ломаются с грохотом.", "The ice is going out! The whole village is on the bank as the floes boom."), "f_icebreak")

E("subbotnik", "04-22", "04-26", 0, "none", ("Субботник", "Spring clean-up"),
  ("Субботник! В субботу с девяти: убираем прошлогодние листья у клуба и школы, красим скамейки, белим липы. Грабли — свои, краска — от магазина, чай с баранками — от Зинаиды Павловны. Гармошка будет.",
   "Clean-up day! Saturday from nine: raking last year's leaves by the club and the school, painting the benches, whitewashing the limes. Bring your own rake; paint from the shop, tea and bagels from Zinaida Pavlovna. There'll be an accordion."),
  ("Субботник: вся деревня с граблями, пахнет краской и костром.", "Clean-up day: everyone out with rakes; smells of paint and bonfires."), "")

E("swallows", "05-02", "05-07", 0, "swallows", ("Прилетели ласточки", "The swallows are back"),
  ("Юннаты школы просят: «Если ласточка села под вашей крышей — не сбивайте гнездо и напишите нам, сколько их. Прошлой весной насчитали сорок две пары. Под почтовой крышей — четыре!»",
   "The school's young naturalists ask: “If a swallow has settled under your roof, leave the nest be and tell us how many. Last spring we counted forty-two pairs. Four under the post-office roof!”"),
  ("Прилетели ласточки — чертят небо над почтой.", "The swallows are back, scribbling across the sky over the post office."), "f_swallows")

E("potato_planting", "05-10", "05-15", 0, "none", ("Сажаем картошку", "Potato planting"),
  ("Объявление Сергея Кузнецова: «Пашу огороды трактором, очередь по записи на двери магазина. Бабушкам — в первую очередь и бесплатно. Остальным — за пирог». Ниже чужой рукой: «Пирог — с чем угодно?»",
   "A notice from Sergey Kuznetsov: “Ploughing vegetable plots by tractor, sign up on the shop door. Grannies first and free. Everyone else, one pie.” And underneath in another hand: “A pie with any filling?”"),
  ("Сажают картошку: на огородах согнутые спины и разговоры через забор.", "Potato planting: bent backs in every plot and talk across the fences."), "")

E("nightingales", "05-17", "05-23", 0, "none", ("Соловьиные ночи", "Nightingale nights"),
  ("В клубе на двери: «Вечера отменяются. Все равно все сидят у реки и слушают соловьёв. Библиотека открыта до восьми». И приписка: «Соловей у мельницы — самый громкий. Проверено».",
   "On the club door: “Evening events are cancelled. Everyone's down by the river listening to nightingales anyway. Library open till eight.” And a P.S.: “The nightingale by the mill is the loudest. Tested.”"),
  ("Соловьиные ночи: у реки поют так, что не уснуть.", "Nightingale nights: they sing so loud by the river that no one can sleep."), "")

E("last_bell", "05-24", "05-25", 0, "school", ("Последний звонок", "The last bell"),
  ("Школа приглашает на последний звонок. Выпускников в этом году трое, и звонить будет первоклассница — колокольчиком, которому семьдесят лет. Приходите все, кто здесь учился. Это значит — вся деревня.",
   "The school invites you to the last bell. There are three school-leavers this year, and a first-grader will ring the seventy-year-old handbell. Everyone who studied here, come. That means the whole village."),
  ("Последний звонок: банты, сирень и колокольчик на всю улицу.", "The last bell: hair bows, lilac and a handbell heard down the whole street."), "f_lastbell")

E("lilac", "05-26", "06-05", 0, "lilac", ("Сирень цветёт", "Lilac time"),
  ("Объявление на почте: «Сирень у почты не ломать! Кому нужна ветка — спросите, срежем аккуратно. Ищете пятилистник на счастье — ищите, это можно».",
   "A notice at the post office: “Do not break the lilac by the post office! If you'd like a sprig, ask and we'll cut one neatly. Looking for a five-petalled flower for luck? Go ahead, that's allowed.”"),
  ("Цветёт сирень — деревня пахнет так, что голова кругом.", "The lilac's out: the whole village smells so sweet it makes your head spin."), "f_lilac")

E("cheese_day", "06-10", "06-11", 1, "fair", ("Сырный день в Заречье", "Cheese Day in Zarechye"),
  ("Ласточкины зовут на Сырный день: дегустация молодого козьего сыра, конкурс «Чья коза голосистее», мастер-класс «Как не поссориться из-за рецепта» (ведущие — Вера и Надя, ссорятся с утра). Мост открыт, сыр бесплатный, козы — нет.",
   "The Lastochkin sisters invite you to Cheese Day: tasting the young goat's cheese, a Loudest Goat contest, and a workshop on How Not to Quarrel over a Recipe (hosted by Vera and Nadya, who have been quarrelling since morning). The bridge is open, the cheese is free, the goats are not."),
  ("В Заречье Сырный день: козы голосят, сыр раздают с ножа.", "Cheese Day in Zarechye: goats bleating, cheese handed out off the knife."), "f_cheese")

E("kupala", "07-06", "07-07", 0, "kupala", ("Купальская ночь", "Kupala Night"),
  ("Клуб зовёт на Купальскую ночь на луг у реки: костёр, венки на воду, хоровод, прыжки через огонь (только через маленький!). Кто найдёт цветок папоротника — покажите Лидии Аркадьевне, она запишет в летопись. Пока не нашёл никто.",
   "The club invites you to Kupala Night on the river meadow: a bonfire, wreaths floated on the water, ring dances, jumping the fire (the small one only!). Whoever finds the fern flower, show it to Lidia Arkadyevna and she'll put it in the village chronicle. Nobody has yet."),
  ("Купальская ночь: по Липке плывут венки, на лугу костёр.", "Kupala Night: wreaths drifting down the Lipka and a bonfire on the meadow."), "f_kupala")

E("haymaking", "07-08", "07-20", 0, "haymaking", ("Сенокос", "Haymaking"),
  ("Сенокос! Косим заливной луг у мельницы, начинаем с росой, в пять утра. Косы отбить с вечера. Обед — на лугу, квас — от бабы Нины, огурцы — свои. Кто не косит, тот ворошит. Кто не ворошит, тот поёт.",
   "Haymaking! We mow the water meadow by the mill, starting with the dew at five. Sharpen your scythes the night before. Lunch in the meadow, kvass from Granny Nina, bring your own cucumbers. Whoever doesn't mow, turns hay. Whoever doesn't turn, sings."),
  ("Сенокос: на лугу звенят косы, пахнет сеном до самой почты.", "Haymaking: scythes ringing, and the smell of hay right up to the post office."), "f_hay")

E("fishermen_day", "07-11", "07-13", 3, "fishing", ("День рыбака на Озёрках", "Fishermen's Day at Ozyorki"),
  ("День рыбака на Озёрках! Конкурс на самую большую рыбу (мерить при свидетелях), гонки на лодках-плоскодонках, уха на сто человек из общего котла. Рыбацкие байки — после третьей тарелки. Правду не говорить.",
   "Fishermen's Day at Ozyorki! A biggest-fish contest (measured before witnesses), flat-bottomed boat races, fish soup for a hundred from one big cauldron. Fishing tales after the third bowl. No telling the truth."),
  ("На Озёрках День рыбака: уха в котле, лодки наперегонки.", "Fishermen's Day at Ozyorki: soup in the cauldron, boats racing on the lake."), "f_fishday")

E("berries", "07-21", "08-04", 0, "berries", ("Пора ягод", "Berry season"),
  ("Лесник Андрей Громов просит: «Ягодники! В лесу не шуметь, костры не жечь, на болото за Сосновкой одним не ходить. Корзинки берите, медведя не берите — он свои ягоды сам соберёт».",
   "Andrei Gromov the forester asks: “Berry pickers! No noise in the woods, no fires, and nobody goes to the bog beyond Sosnovka alone. Take your baskets, leave the bear: he picks his own berries.”"),
  ("Пошла ягода: у всех руки синие от черники.", "The berries are in: everyone's hands are blue with bilberries."), "f_berries")

E("railway_day", "08-02", "08-08", 2, "railway", ("День железнодорожника", "Railway Day"),
  ("День железнодорожника на разъезде 118 км! «Кукушка» вся в флажках, Виктор Павлович даёт три гудка в честь праздника, выставка старых фонарей на перроне. Тамара Ивановна принимает праздничные телеграммы бесплатно — по одному слову с человека.",
   "Railway Day at Halt 118 km! The Cuckoo hung with flags, three blasts on the whistle from Viktor Pavlovich, a show of old lanterns on the platform. Tamara Ivanovna sends holiday telegrams for free: one word per person."),
  ("На разъезде День железнодорожника: «Кукушка» в флажках и гудит.", "Railway Day at the halt: the Cuckoo is decked in flags and whistling."), "f_railday")

E("honey", "08-05", "08-10", 0, "harvest", ("Качают мёд", "Honey extracting"),
  ("Михалыч объявляет: «Качаю мёд. Кто хочет посмотреть — приходите, но в светлом и без духов. Дети — пробуют с ложки. Взрослые — тоже, но потом помогают крутить медогонку. Пчёл не махать!»",
   "Mikhalych announces: “Extracting honey. Come and watch, but wear light colours and no scent. Children may taste off the spoon. Grown-ups too, but then you turn the extractor. Don't wave at the bees!”"),
  ("На пасеке качают мёд — к почте летят любопытные пчёлы.", "Honey extracting at the apiary: curious bees drift over to the post office."), "f_bees")

E("starfall", "08-11", "08-14", 0, "none", ("Звездопад", "Falling stars"),
  ("Николай Семёнович приглашает: «Персеиды! Смотреть с луга за школой после одиннадцати. Брать одеяло, чай и терпение. Желания загадывать коротко, а то звезда не успеет».",
   "Nikolai Semyonovich invites you: “The Perseids! Watch from the meadow behind the school after eleven. Bring a blanket, tea and patience. Keep your wishes short or the star won't have time.”"),
  ("Звездопад: полдеревни лежит на лугу и считает падающие звёзды.", "Falling stars: half the village is lying in the meadow counting shooting stars."), "f_starfall")

E("apple_day", "08-19", "08-20", 0, "apples", ("Яблочный Спас", "Apple Day"),
  ("Яблочный Спас — праздник урожая! Несите яблоки в клуб: конкурс на самое большое, самое красное и самое кривое. Пироги, пастила, моченые яблоки. Кто принесёт больше всех — уносит обратно меньше всех: угощаем всю деревню.",
   "Apple Day, the harvest feast! Bring apples to the club: prizes for the biggest, the reddest and the most crooked. Pies, pastila, pickled apples. Whoever brings the most takes home the least: we're feeding the whole village."),
  ("Яблочный Спас: в каждом доме пахнет яблоками и корицей.", "Apple Day: every house smells of apples and cinnamon."), "f_apples")

E("mushrooms", "08-21", "08-31", 0, "mushrooms", ("Пошли грибы", "Mushroom season"),
  ("От фельдшерского пункта: «Грибники! Незнакомые грибы — не есть, показывать Ольге Кузнецовой, она отличит. В лес — с компасом или с бабой Ниной. Бабу Нину на всех не хватает».",
   "From the medical post: “Mushroom hunters! Don't eat mushrooms you don't know; show them to Olga Kuznetsova and she'll tell you. Go into the woods with a compass or with Granny Nina. There isn't enough Granny Nina for everyone.”"),
  ("Пошли грибы: с утра по дороге в лес тянутся корзинки.", "The mushrooms are up: a line of baskets heads for the woods at dawn."), "f_mushrooms")

E("knowledge_day", "09-01", "09-01", 0, "school", ("День знаний", "Day of Knowledge"),
  ("Школа приглашает на линейку! Первоклассники, родители, бабушки, учителя бывшие и нынешние. Букеты — астры и гладиолусы со своих огородов. Первый звонок даст выпускник. После линейки — чай и арбуз.",
   "The school invites you to the opening assembly! First-graders, parents, grannies, teachers old and new. Bouquets: asters and gladioli from your own gardens. A school-leaver will ring the first bell. Tea and watermelon afterwards."),
  ("День знаний: по деревне идут букеты на ножках.", "The Day of Knowledge: bouquets on legs are walking through the village."), "f_bell")

E("town_day", "09-05", "09-06", 5, "fair", ("День Городка", "Gorodok Day"),
  ("День Городка! На площади ярмарка мастеров, духовой оркестр, музей открыт бесплатно, редакция «Сельской нови» печатает праздничный листок прямо на улице. Вечером — салют над рекой.",
   "Gorodok Day! A craft fair on the square, a brass band, the museum free all day, and the Village News printing a holiday sheet right in the street. Fireworks over the river in the evening."),
  ("В Городке праздник: оркестр слышно даже на дальних улицах.", "Gorodok's holiday: you can hear the band from the furthest streets."), "f_townday")

E("potato_digging", "09-07", "09-13", 0, "harvest", ("Копаем картошку", "Potato digging"),
  ("Объявление в магазине: «Мешки есть. Перчатки есть. Спины — у кого какие. Картошку копаем всем миром: в субботу — у Агафьи Петровны, в воскресенье — у Фёдора Ильича. Печёная картошка в костре — каждому, кто копал».",
   "A notice at the shop: “Sacks in stock. Gloves in stock. Backs, whatever you've got. We dig together: Saturday at Agafya Petrovna's, Sunday at Fyodor Ilyich's. A potato baked in the bonfire for everyone who dug.”"),
  ("Копают картошку: над огородами дым от ботвы и звон вёдер.", "Potato digging: smoke from burning haulms and the clank of buckets."), "f_potato")

E("cranes", "09-14", "09-21", 0, "cranes", ("Журавли улетают", "The cranes leave"),
  ("Юннаты просят: «Кто увидит журавлиный клин — запишите число, час и сколько птиц, и опустите записку в ящик на почте. В прошлом году насчитали триста двенадцать. Варя уверена, что одного журавля посчитали дважды».",
   "The young naturalists ask: “If you see a skein of cranes, note the date, the hour and how many birds, and drop the note in the post-office box. Last year we counted three hundred and twelve. Varya is sure one crane was counted twice.”"),
  ("Над Липкой тянутся журавли. Курлычут так, что все задирают головы.", "Cranes are passing over the Lipka, calling so that everyone looks up."), "f_cranes")

E("forest_day", "09-18", "09-20", 4, "none", ("День леса на кордоне", "Forest Day at the Cordon"),
  ("День леса на Сосновом кордоне: сажаем молодые сосны на старой просеке, Глеб Андреевич показывает метеостанцию, Белкины угощают пирогами с брусникой. Лопата — с собой, пироги — на месте.",
   "Forest Day at Pine Cordon: planting young pines on the old cutting, a tour of the weather station with Gleb Andreyevich, lingonberry pies from the Belkins. Bring a spade; the pies will be there."),
  ("На кордоне День леса: сажают сосны, а над просекой пахнет пирогами.", "Forest Day at the cordon: pines going in, pies smelling over the cutting."), "f_forestday")

E("indian_summer", "09-23", "09-30", 0, "none", ("Бабье лето", "Indian summer"),
  ("Клуб объявляет «последний тёплый вечер»: чай на крыльце клуба, патефон, кто хочет — танцует. Если пойдёт дождь — значит, вечер не последний, переносим.",
   "The club announces “the last warm evening”: tea on the club porch, a gramophone, dancing for those who want it. If it rains, it wasn't the last warm evening after all and we'll move it."),
  ("Бабье лето: паутинки летят над огородами, солнце низкое и тёплое.", "Indian summer: gossamer drifting over the gardens and a low, warm sun."), "f_indian")

E("leaf_fall", "10-01", "10-10", 0, "none", ("Листопад", "Leaf fall"),
  ("Объявление на почте: «Листья у крыльца почты не сметать до пятницы. Варя и её друзья строят из них дом. Почтальон проходит по тропинке справа».",
   "A notice at the post office: “Do not sweep the leaves by the post-office steps until Friday. Varya and her friends are building a house out of them. The postman uses the path on the right.”"),
  ("Листопад: липы у клуба осыпаются золотом, под ногами шуршит.", "Leaf fall: the club limes are dropping gold; everything rustles underfoot."), "")

E("pokrov_fair", "10-13", "10-15", 0, "fair", ("Покровская ярмарка", "The Pokrov Fair"),
  ("Покровская ярмарка у клуба! Мёд Михалыча, сыры из Заречья, игрушки Гриши Резникова, варенье всех сортов. Калач в два метра (несём вчетвером), карусель на руках, перетягивание каната Липовка против Заречья. Кто проиграет — моет котлы.",
   "The Pokrov Fair by the club! Mikhalych's honey, cheeses from Zarechye, Grisha Reznikov's toys, jam of every kind. A two-metre kalach (four to carry it), a hand-pushed merry-go-round, tug of war Lipovka against Zarechye. The losers wash the pots."),
  ("Покровская ярмарка: гармонь, калачи и весь район у клуба.", "The Pokrov Fair: an accordion, kalachi and the whole district at the club."), "f_fair")

E("first_snow", "11-03", "11-08", 0, "firstsnow", ("Первый снег", "First snow"),
  ("Объявление на почте: «Выпал первый снег. Почта работает как обычно. Следы почтальона просьба не затаптывать — по ним видно, кому сегодня письма».",
   "A notice at the post office: “The first snow has fallen. The post office is open as usual. Please don't trample the postman's footprints: they show who's had letters today.”"),
  ("Выпал первый снег. Деревня проснулась белой и тихой.", "The first snow has fallen. The village woke up white and quiet."), "f_firstsnow")

E("river_freeze", "11-20", "11-27", 0, "frost", ("Ледостав", "The river freezes"),
  ("От рыбаков и сельсовета: «Липка встала. Лёд тонкий! Ходить по нему — только когда Матвей Савельич скажет, а он скажет не раньше декабря. Мальчишкам — особенно».",
   "From the fishermen and the village council: “The Lipka has frozen. The ice is thin! Nobody walks on it until Matvei Savelyich says so, and he won't say so before December. That means you, boys.”"),
  ("Липка встала: по ночам лёд поёт и потрескивает.", "The Lipka has frozen: at night the ice sings and crackles."), "f_freeze")

E("solstice", "12-21", "12-22", 0, "frost", ("Самый короткий день", "The shortest day"),
  ("Николай Семёнович напоминает: «Сегодня самый короткий день в году. Завтра день прибавится на минуту. Считайте: к Новому году — на целых десять! Есть ради чего жить до весны».",
   "Nikolai Semyonovich reminds you: “Today is the shortest day of the year. Tomorrow it'll be a minute longer. Do the sums: ten whole minutes by New Year! Something to live for till spring.”"),
  ("Самый короткий день: темнеет к четырём, в окнах рано зажигают свет.", "The shortest day: dark by four, and the windows light up early."), "f_frost")

E("club_tree", "12-25", "12-31", 0, "newyear", ("Ёлка в клубе", "The club's New Year tree"),
  ("Клуб приглашает на ёлку! Ёлку принёс лесник, игрушки — со всей деревни, звезду склеила Варя. Утренник для детей, вечер для взрослых, Дед Мороз — по секрету. Мешок подарков собираем вскладчину: несите конфеты в библиотеку.",
   "The club invites you to the New Year tree! The forester brought the tree, the decorations come from the whole village, Varya glued the star. A children's party in the morning, grown-ups in the evening, Ded Moroz played by — that's a secret. We're filling the present sack together: bring sweets to the library."),
  ("В клубе нарядили ёлку. Пахнет хвоей и мандаринами.", "The tree's up at the club. It smells of pine needles and tangerines."), "f_clubtree")

E("carols", "01-06", "01-10", 0, "newyear", ("Колядки", "Carolling"),
  ("Объявление: «Ряженые пойдут по дворам с песнями. Козу будет изображать Дима Соколов, медведя — по жребию. Готовьте пироги и конфеты. Кто не откроет — тому споют под окном ещё громче».",
   "A notice: “The mummers will go from house to house singing. Dima Sokolov will play the goat, the bear will be chosen by lot. Have pies and sweets ready. Anyone who doesn't open the door gets sung to under the window even louder.”"),
  ("По деревне ходят ряженые с песнями — коза, медведь и полкласса.", "Mummers are going round singing: a goat, a bear and half the school."), "f_carols")

E("old_new_year", "01-13", "01-14", 0, "newyear", ("Старый Новый год", "Old New Year"),
  ("Клуб зовёт на Старый Новый год: вареники с сюрпризами, лото на конфеты, частушки. Ёлку разбираем все вместе — кто снимет последнюю игрушку, тот и вешает её на следующий год первым.",
   "The club invites you to Old New Year: dumplings with surprises, lotto for sweets, ditties. We'll take the tree down together: whoever takes off the last bauble hangs the first one next year."),
  ("Старый Новый год: в клубе лото и вареники с сюрпризами.", "Old New Year: lotto at the club and dumplings with surprises."), "f_oldny")

E("frosts", "01-17", "01-23", 0, "frost", ("Январские морозы", "January frosts"),
  ("От фельдшерского пункта: «Морозы до минус тридцати! Старикам — дров не жалеть, детям — носы под шарф, почтальону — горячий чай в каждом доме. Проверим!»",
   "From the medical post: “Frosts down to minus thirty! Old folk, don't spare the firewood. Children, noses under your scarves. And a hot cup of tea in every house for the postman. We'll be checking!”"),
  ("Трескучие морозы: дым из труб стоит столбом, снег скрипит.", "A crackling frost: chimney smoke stands up in columns and the snow squeaks."), "f_frost")

E("ice_fishing", "02-12", "02-18", 3, "fishing", ("Подлёдный лов на Озёрках", "Ice fishing at Ozyorki"),
  ("Матвей Савельич объявляет: «Лёд на озере — сорок сантиметров. Подлёдный лов открыт. Лунки сверлить подальше друг от друга, чай носить поближе. Кто поймает налима — с того уха на всех».",
   "Matvei Savelyich announces: “The lake ice is forty centimetres. Ice fishing is open. Drill your holes well apart, keep the tea close. Whoever catches a burbot makes fish soup for everyone.”"),
  ("На Озёрках подлёдный лов: на льду точки рыбаков и дымок от чайников.", "Ice fishing at Ozyorki: anglers dotted on the ice and steam rising from kettles."), "f_icefish")


# --------------------------------------------------------------------------- fillers: old
F("old", ("Двоюродная сестра, Кострома", "A cousin in Kostroma"),
  ("Из Костромы прислали фотографии со свадьбы.", "Wedding photos came from Kostroma."),
  ("Внучатая племянница вышла замуж в Костроме, прислали карточки. Невеста в фате, а за спиной Волга вся в солнце. А это кто с гармошкой? Это ж наш Колька! Сорок лет не виделись, а улыбка та же, щербатая.",
   "My great-niece got married in Kostroma and they've sent the photos. The bride in her veil, the Volga behind her full of sun. And who's that with the accordion? It's our Kolka! Forty years since we saw him, and the same gap-toothed grin."))
F("old", ("Бывшая соседка, Тверь", "A former neighbour, Tver"),
  ("Бывшая соседка прислала семена из Твери.", "A former neighbour sent seeds from Tver."),
  ("Жила тут раньше соседка, весь проулок бархатцами засадила. Переехала к дочке в Тверь — и вот, семена: «Те самые, с нашего проулка, я их с собой увезла. Посади обратно». Посадим. Пусть возвращаются.",
   "There used to be a neighbour here who planted the whole lane with marigolds. She moved to her daughter's in Tver, and now look, seeds: “The very ones from our lane, I took them with me. Plant them back.” We will. Let them come home."))
F("old", ("Племянник, Сочи", "A nephew in Sochi"),
  ("Открытка из Сочи: море, пальмы и привет от племянника.", "A postcard from Sochi: sea, palms and greetings from a nephew."),
  ("Племянник пишет: «Тут жара, море, а я всё равно скучаю по вашей бане». На открытке пальма, а море синее, как чернила. Повешу над столом. Зимой буду смотреть и греться.",
   "My nephew writes, “It's hot here, there's the sea, and I still miss your bathhouse.” A palm tree on the card and the sea as blue as ink. I'll pin it over the table. In winter I'll look at it and warm up."))
F("old", ("«Товары — почтой»", "Goods by Post"),
  ("Пришёл каталог «Товары — почтой», с грелками и кофтами.", "A Goods by Post catalogue came, full of hot-water bottles and cardigans."),
  ("Каталог! Тут и грелка, и кофта, и лупа с подсветкой, и машинка для катышков. Машинка для катышков! Всю жизнь руками снимали. Отмечу, что хочется, закажу, что нужно. Это два разных списка.",
   "A catalogue! Hot-water bottles, cardigans, a magnifying glass with a light, and a machine for removing bobbles. A bobble machine! We did that by hand all our lives. I'll tick what I want and order what I need. Those are two different lists."))
F("old", ("Однокурсники по техникуму", "Old college classmates"),
  ("Пришло круговое письмо от однокурсников — ходит по стране двадцать лет.", "A round-robin letter from old classmates, travelling for twenty years."),
  ("Круговое письмо! Его по очереди дописывают и шлют дальше, уже двадцать лет. Тут пять почерков, один кривее другого. Теперь моя очередь дописать и отправить в Пермь. Вот и работа на вечер.",
   "A round-robin letter! Each of us adds a page and posts it on; it's been going twenty years. Five different hands in it, each wobblier than the last. Now it's my turn to add mine and send it to Perm. That's my evening sorted."))
F("old", ("Двоюродная сестра, Вологда", "A cousin in Vologda"),
  ("Из Вологды прислали рецепт пирога с черёмуховой мукой.", "A recipe for bird-cherry-flour pie came from Vologda."),
  ("Сестра двоюродная прислала рецепт: пирог с черёмуховой мукой. Пишет: «Пеки, только помни — тесто любит, когда с ним разговаривают». Буду разговаривать. О чём только с тестом говорить? О погоде, наверное.",
   "My cousin sent a recipe: pie made with bird-cherry flour. She writes, “Bake it, but remember, dough likes to be talked to.” I'll talk to it. What do you talk to dough about? The weather, I suppose."))
F("old", ("Родня из Вологды", "Family in Vologda"),
  ("Прислали схему носков «с косичкой» и строгие указания.", "A cable-sock pattern came, with strict instructions."),
  ("Схема носков «с косичкой», из журнала вырезана. А внизу приписка: «Пятку вяжи по-нашему, по-вологодски, а не как в журнале». Вот она, родня: и пришлют, и сразу поправят.",
   "A pattern for cable socks, cut out of a magazine. And a note at the bottom: “Do the heel our way, the Vologda way, not like the magazine.” That's family for you: they send it and correct it in the same breath."))
F("old", ("Старый знакомый, Мурманск", "An old acquaintance in Murmansk"),
  ("Из Мурманска пришла старая фотография: «Угадай, где ты».", "An old photograph came from Murmansk: “Guess which one is you.”"),
  ("Прислали старую фотографию: все на крыльце, году в семьдесят каком-то. На обороте: «Угадай, где ты». Вот, с краю, в кепке. Кепку помню. А себя — не очень.",
   "They've sent an old photo: everyone on a porch, nineteen-seventy-something. On the back: “Guess which one is you.” There, at the end, in the cap. I remember the cap. Myself, not so much."))
F("old", ("Липовка Тамбовская", "Lipovka, Tambov region"),
  ("Письмо пришло не в ту Липовку — из Тамбовской области.", "A letter came to the wrong Lipovka, meant for the Tambov one."),
  ("Это не нам! Липовка, да не та — Тамбовская. «Дорогому Ване от тёти Шуры». Вы уж отправьте обратно, пусть Ваня получит. Он, поди, ждёт. Тётя Шура пишет крупно — видно, торопилась.",
   "This isn't ours! Lipovka, but the wrong one, in the Tambov region. “To dear Vanya from Aunt Shura.” Please send it back so Vanya gets it. He'll be waiting. Aunt Shura writes in big letters; she must have been in a hurry."))
F("old", ("Подруга по переписке, Пловдив", "A pen-friend in Plovdiv"),
  ("Из Болгарии пришёл пузырёк розового масла.", "A tiny bottle of rose oil came from Bulgaria."),
  ("С шестьдесят девятого года переписываемся. Она по-русски, а я по-болгарски — ну, пытаюсь. Прислала розового масла, пузырёк с напёрсток. Понюхайте! Вот так у них пахнет целая долина.",
   "We've been writing since 1969. She writes in Russian and I write in Bulgarian, or try to. She's sent rose oil, a bottle the size of a thimble. Smell it! That's what a whole valley smells like over there."))
F("old", ("Семена — почтой", "Seeds by Post"),
  ("Пришли заказанные семена — и лишний пакетик в подарок.", "The seeds ordered in winter came, plus a free packet."),
  ("Семена пришли, что зимой заказывали, — а в посылке лишний пакетик, «в подарок»: тыква «Ажурная». Ажурная тыква! Посажу и буду ждать, в чём там ажур.",
   "The seeds I ordered in winter are here, and there's an extra packet “as a gift”: a pumpkin called Lacework. A lace pumpkin! I'll plant it and wait to see where the lace comes in."))
F("old", ("Одноклассник, Ярославль", "A schoolmate in Yaroslavl"),
  ("Одноклассники собирают встречу выпускников.", "Old schoolmates are organising a class reunion."),
  ("Одноклассник пишет: собирают встречу, столько лет выпуску, что и считать боязно. Пишет: «Узнаем ли друг друга?» Узнаем. Кто громче всех смеётся — тот он и есть.",
   "A schoolmate writes that they're organising a reunion; it's been so many years since we left school I'm afraid to count. He writes, “Will we recognise each other?” We will. Whoever laughs loudest, that's him."))
F("old", ("Знакомая травница, Алтай", "A herbalist friend in the Altai"),
  ("С Алтая прислали травяной чай с «секретной» травой.", "Herbal tea with a “secret” herb came from the Altai."),
  ("Знакомая с Алтая прислала сбор: чабрец, душица, мята и ещё что-то, «секретное». Заварю вечером. Если запою — значит, секретное подействовало.",
   "A friend in the Altai sent a herb mix: thyme, oregano, mint and something else, “secret”. I'll brew it tonight. If I start singing, the secret ingredient's working."))
F("old", ("Календарь от родни", "A calendar from family"),
  ("Прислали отрывной календарь с советом на каждый день.", "A tear-off calendar came, with advice for every day."),
  ("Отрывной календарь на следующий год, с советами. Открываю наугад: «Сегодня хорошо сеять редис и мириться с соседями». Редис потом. А с соседями — сейчас пойду.",
   "A tear-off calendar for next year, with tips. I open it at random: “A good day for sowing radishes and making up with the neighbours.” Radishes later. The neighbours I'll go and see now."))
F("old", ("Родня, Череповец", "Family in Cherepovets"),
  ("Родня прислала посылку с вещами, среди них — ярко-жёлтая куртка.", "Family sent a parcel of clothes, including a bright yellow jacket."),
  ("Посылка с вещами: свитер, шарф и куртка с капюшоном. Куртка ярко-жёлтая. В такой меня из Городка видно будет. Ну и хорошо — не потеряюсь.",
   "A parcel of clothes: a jumper, a scarf and a hooded jacket. The jacket is bright yellow. You'll be able to see me from Gorodok in it. Good, then. I won't get lost."))
F("old", ("Бывшая сослуживица, Анапа", "A former colleague in Anapa"),
  ("Бывшая сослуживица пишет из Анапы — считает чаек.", "A former colleague writes from Anapa, where she counts seagulls."),
  ("Бывшая сослуживица на пенсии теперь, в Анапе. «Хожу каждое утро к морю, считаю чаек». А сколько насчитала — не пишет. Спрошу. Интересно же.",
   "A former colleague, retired now, in Anapa. “I go down to the sea every morning and count the seagulls.” She doesn't say how many. I'll ask. I want to know."))
F("old", ("Букинист, Ленинград", "A second-hand bookseller"),
  ("Букинист прислал старую книгу о травах, с пометками на полях.", "A bookseller sent an old book on herbs, with notes in the margins."),
  ("Пришла книга, что заказывали у букиниста: «Травы средней полосы», пятьдесят седьмого года. На полях карандашом: «проверено», «проверено», «не проверять!». Кем проверено — неизвестно. Но раз проверено…",
   "The book from the second-hand dealer: Herbs of Central Russia, 1957. Pencilled in the margins: “tested”, “tested”, “do not test!” Who tested them, nobody knows. But if they're tested…"))
F("old", ("Знакомые из-под Вологды", "Friends near Vologda"),
  ("Знакомые прислали фото нового дома под Вологдой.", "Friends sent a photo of their new house near Vologda."),
  ("Знакомые построили дом под Вологдой, прислали фото: дом жёлтый, ставни синие, на крыше петух-флюгер. Пишут: «Приезжайте, покажем, где у нас солнце встаёт». Солнце там, видно, тоже жёлтое.",
   "Friends built a house near Vologda and sent a photo: yellow walls, blue shutters, a cockerel weathervane on the roof. They write, “Come and we'll show you where the sun rises here.” I expect the sun there is yellow too."))
F("old", ("Друзья, Петербург", "Friends in St Petersburg"),
  ("Открытка из Петербурга: разведённые мосты и привет.", "A postcard from St Petersburg: raised bridges and greetings."),
  ("Нева, мосты разведены. На обороте: «Сидим на набережной, ждём, когда сведут. Как ты там без нас?» А без них тихо. Только тишина какая-то скучная.",
   "The Neva with the bridges raised. On the back: “Sitting on the embankment waiting for them to come down. How are you without us?” It's quiet without them. A dull sort of quiet."))
F("old", ("Старый друг, Киров", "An old friend in Kirov"),
  ("В конверте вырезка: девяностолетняя бабушка прыгнула с парашютом.", "A cutting in the envelope: a woman of ninety did a parachute jump."),
  ("Газетная вырезка: в Кирове бабушка девяноста лет прыгнула с парашютом. Приписка: «Тебе ещё рано, но имей в виду». Имею. Буду иметь в виду.",
   "A newspaper cutting: in Kirov a woman of ninety did a parachute jump. A note: “You're too young yet, but bear it in mind.” I am. I'll bear it in mind."))
F("old", ("Друзья, Карелия", "Friends in Karelia"),
  ("Из Карелии прислали веточку багульника в письме.", "A sprig of wild rosemary came in a letter from Karelia."),
  ("Друзья из Карелии пишут, а в письме — веточка багульника. Пахнет, как лес после дождя. Положу в книгу. Через год открою — и вспомню.",
   "Friends in Karelia write, and there's a sprig of wild rosemary in the letter. It smells like the forest after rain. I'll put it in a book. Open it in a year and remember."))
F("old", ("Знакомые, Рязань", "Friends in Ryazan"),
  ("Прислали рецепт варенья из одуванчиков.", "A recipe for dandelion jam came."),
  ("Рецепт варенья из одуванчиков! Из одуванчиков! Пишут: «На вкус как мёд». Пчеловоды, если узнают, обидятся. Не будем им говорить.",
   "A recipe for dandelion jam! Dandelions! They write, “Tastes just like honey.” If the beekeepers hear, they'll be offended. We won't tell them."))
F("old", ("Друзья с теплохода", "Friends on a river cruise"),
  ("Друзья плывут до Астрахани и шлют открытки с каждой пристани.", "Friends cruising to Astrakhan send a card from every landing."),
  ("Друзья поплыли на теплоходе до Астрахани и шлют открытку с каждой пристани. Это уже пятая, из Самары. «Арбузы ещё не начались, но мы держимся».",
   "Friends are cruising down to Astrakhan on a river boat and sending a card from every landing. This is the fifth, from Samara. “No watermelons yet, but we're bearing up.”"))
F("old", ("Племянник, Северный флот", "A nephew in the Northern Fleet"),
  ("Племянник со службы пишет: снятся домашние блины.", "A nephew in the navy writes that he dreams of home-made pancakes."),
  ("Племянник служит на флоте: «Кормят хорошо, но не как у вас. Приснились ваши блины — проснулся голодный». Соберём посылку. Блины по почте не дойдут, а варенье дойдёт.",
   "My nephew's in the navy: “The food's good, but not like yours. I dreamt of your pancakes and woke up starving.” We'll make up a parcel. Pancakes won't survive the post, but jam will."))
F("old", ("Школьники, Городок", "Schoolchildren in Gorodok"),
  ("Школьники из Городка просят рассказать, как жили без телевизора.", "Gorodok schoolchildren ask what life was like without television."),
  ("Школьники пишут — у них проект «Живая история». Спрашивают: «Как вы жили, когда не было телевизора?» Как жили… Хорошо жили. Разговаривали. Сяду отвечу — длинно, с картинками.",
   "Schoolchildren write; they're doing a Living History project. They ask, “How did you live before there was television?” How… We lived well. We talked. I'll sit down and answer: at length, with pictures."))
F("old", ("Старый друг, Тула", "An old friend in Tula"),
  ("В конверте — старинная двухкопеечная монета.", "An old two-kopeck coin came in an envelope."),
  ("В конверте монетка — две копейки, пятьдесят второго года. Пишет: «Нашёл в кармане старого пальто. Помнишь, что на неё было можно?» Помню. Позвонить из автомата. Или коробок спичек. Или счастье — смотря кому звонить.",
   "A coin in the envelope: two kopecks, 1952. He writes, “Found it in an old coat pocket. Remember what it bought?” I do. A call from a phone box. Or a box of matches. Or happiness, depending on who you rang."))
F("old", ("Двоюродный брат, Курган", "A cousin in Kurgan"),
  ("Двоюродный брат купил козу и написал о ней три страницы.", "A cousin bought a goat and wrote three pages about it."),
  ("Двоюродный брат купил козу. Про козу — три страницы: что ест, как смотрит, кого бодает. Про себя — две строчки: «Жив-здоров». Ну что ж, значит, всё у него хорошо.",
   "My cousin's bought a goat. Three pages about the goat: what she eats, how she looks at you, who she butts. Two lines about himself: “Alive and well.” Well, that means all's fine with him."))
F("old", ("Знакомые, вернувшиеся из Индии", "Friends back from India"),
  ("Прислали индийский чай — сумка почтальона пахнет пряностями.", "Indian tea arrived: the postbag smells of spices."),
  ("Знакомые вернулись из Индии, прислали чай. Пачка пахнет так, что вся ваша сумка, наверное, пропахла. Понюхайте рукав! Вот. Индия.",
   "Friends back from India sent tea. The packet smells so strong your whole bag must smell of it. Sniff your sleeve! There. That's India."))
F("old", ("Издательство «Досуг»", "Leisure Press"),
  ("Пришёл сборник кроссвордов «крупным шрифтом».", "A book of crosswords “in large print” arrived."),
  ("Сборник кроссвордов, «для старшего возраста, крупным шрифтом». Крупным шрифтом! Обидно. А читается легко. Обидно, но удобно.",
   "A crossword book, “for older readers, in large print”. Large print! How insulting. But it's easy to read. Insulting, but handy."))
F("old", ("Племянник, Ижевск", "A nephew in Izhevsk"),
  ("Пришёл пустой конверт. Второй, с запиской, будет через неделю.", "An empty envelope came. The second one, with the letter, will follow in a week."),
  ("Конверт пустой! Марка, адрес — и ничего. Это племянник, он такой. Через неделю придёт второй, с запиской «Забыл вложить». Каждый раз так. Но конверт-то надписан с любовью.",
   "The envelope's empty! Stamp, address, nothing else. That's my nephew for you. In a week a second one will come with a note: “Forgot to put it in.” Every time. But he addressed it lovingly."))
F("old", ("Племянница с фермы", "A niece on a farm"),
  ("Племянница прислала фото телёнка по имени Пятница.", "A niece sent a photo of a calf called Friday."),
  ("Племянница с фермы прислала фото: телёнок, родился в пятницу, назвали Пятницей. Глаза как сливы. Вот кому позавидуешь: ни забот, ни квитанций.",
   "My niece on the farm sent a photo: a calf born on a Friday and named Friday. Eyes like plums. There's one to envy: no worries and no bills."))
F("old", ("Друг юности, Пенза", "A friend from youth, Penza"),
  ("Друг юности прислал слова старой песни — с забытым куплетом.", "A friend from youth sent the words of an old song, forgotten verse included."),
  ("Прислали слова песни, что пели когда-то у костра. Второй куплет из наших никто не помнил, а он помнит. Вечером спою. Тихонько, а то соседи решат, что праздник.",
   "He's sent the words of the song we used to sing round the campfire. None of us remembered the second verse, but he does. I'll sing it tonight. Quietly, or the neighbours will think it's a party."))
F("old", ("Родня, Архангельск", "Family in Arkhangelsk"),
  ("Из Архангельска прислали варежки с северным узором.", "Mittens with a northern pattern came from Arkhangelsk."),
  ("Варежки из Архангельска, с северным узором: ёлочки, олени, звёздочки — всё в одной паре. Надену — и руки будто в гостях.",
   "Mittens from Arkhangelsk with a northern pattern: fir trees, reindeer, stars, all in one pair. Put them on and your hands feel like they're visiting."))
F("old", ("Бывшая студентка, Москва", "A former student, Moscow"),
  ("Пишет москвичка, которая студенткой была здесь на картошке.", "A Muscovite writes who came here as a student to dig potatoes."),
  ("Пишет женщина из Москвы: студенткой была у нас на картошке, давным-давно. «Помню, как пахла ваша печь и как пел петух — в три часа ночи». Петухи у нас и сейчас в три поют. Традиция.",
   "A woman from Moscow writes; she came here as a student to help with the potato harvest, ages ago. “I remember how your stove smelt and the cockerel crowing at three in the morning.” Our cockerels still crow at three. It's tradition."))
F("old", ("Друзья, Калуга", "Friends in Kaluga"),
  ("В письме прислали засушенный четырёхлистный клевер.", "A pressed four-leaf clover came in a letter."),
  ("В письме четырёхлистный клевер, засушенный. «Нашли на лугу, отдаём тебе — тебе нужнее». Это почему мне нужнее? А, ладно. Удача не помешает.",
   "A pressed four-leaf clover in the letter. “Found it in a meadow, it's yours, you need it more.” Why do I need it more? Oh, all right. A bit of luck never hurts."))
F("old", ("Знакомые, Уфа", "Friends in Ufa"),
  ("Из Уфы прислали банку тёмного гречишного мёда.", "A jar of dark buckwheat honey came from Ufa."),
  ("Мёд башкирский прислали, гречишный, тёмный, как крепкий чай. Наш, конечно, лучше. Но и этот ничего. Ложечку попробуйте — для сравнения.",
   "They sent Bashkir honey, buckwheat, as dark as strong tea. Ours is better, of course. But this one's not bad. Have a spoonful, for comparison."))
F("old", ("Старый друг-стихотворец", "An old friend who writes verse"),
  ("Старый друг прислал письмо в стихах — про протекающую крышу.", "An old friend sent a letter in verse, about his leaking roof."),
  ("Всю жизнь пишет стихами, даже про то, что крыша течёт: «Течёт моя крыша, как слёзы весной…» Рифма хромает, а крыша, видно, правда течёт. Надо ему совет послать. Тоже стихами.",
   "All his life he's written in verse, even about his leaking roof: “My roof is weeping like spring's own tears…” The rhyme limps, but the roof really is leaking. I'll send him some advice. In verse."))
F("old", ("Знакомые, Владимир", "Friends in Vladimir"),
  ("Прислали вырезку из областной газеты — про нашу мельницу.", "A cutting from the regional paper came, about our mill."),
  ("В областной газете написали про нашу мельницу! Знакомые вырезали, прислали. Фото, правда, перевёрнуто — колесо крутится не в ту сторону. Ну, зато все узнают.",
   "The regional paper wrote about our mill! Friends cut it out and sent it. The photo's printed back to front, so the wheel turns the wrong way. Still, everyone will recognise it."))
F("old", ("Друзья, Иркутск", "Friends in Irkutsk"),
  ("С Байкала пришла открытка с нерпой.", "A postcard of a Baikal seal arrived."),
  ("Открытка с Байкала: нерпа на камне. Пишут: «Нерпа смотрит, как ты, когда тебе пересолили суп». Похоже. Очень похоже.",
   "A card from Baikal: a seal on a rock. They write, “The seal is looking at you the way you look at oversalted soup.” It's a likeness. A real likeness."))
F("old", ("Часовая мастерская, Городок", "The watch repairer, Gorodok"),
  ("Из мастерской в Городке вернулись починенные часы.", "Mended watches came back from the repair shop in Gorodok."),
  ("Часы починили, вернули! Тикают. Сорок лет на руке, полгода в ящике — и снова на руке. Мы с ними оба отдохнули.",
   "They've mended my watch and sent it back! It's ticking. Forty years on my wrist, six months in a drawer, and back on my wrist. We've both had a rest."))
F("old", ("«Оптика — почтой»", "Spectacles by Post"),
  ("Пришли новые очки, заказанные почтой.", "New glasses ordered by post have arrived."),
  ("Очки пришли! Примерю при вас. Ну как? Вот теперь вас хорошо видно. А то всё — сумка, шапка и голос.",
   "My glasses have come! I'll try them on right here. Well? Now I can see you properly. Until now you were just a bag, a hat and a voice."))
F("old", ("Радиостанция «Ностальгия»", "Nostalgia Radio"),
  ("Радио обещает поставить песню «для жителя Липовки».", "The radio station promises to play a song “for a Lipovka listener”."),
  ("Ответ с радио: заявку приняли, в субботу в десять поставят песню «для жителя Липовки». Будем слушать. Всей улицей. Пусть знают, что Липовка слушает.",
   "A reply from the radio: they've taken the request, and on Saturday at ten they'll play a song “for a listener in Lipovka”. We'll listen. The whole street. Let them know Lipovka's listening."))
F("old", ("Знакомые, Тула", "Friends in Tula"),
  ("Из Тулы прислали печатный пряник.", "A stamped gingerbread came from Tula."),
  ("Пряник тульский прислали, печатный, с повидлом, и надпись на нём — «Тула». Его есть жалко — красивый. Пусть лежит до праздника. Если дотерпим.",
   "They've sent a Tula gingerbread, the stamped kind with jam inside and “Tula” on top. Too pretty to eat. It can wait for a holiday. If we last that long."))
F("old", ("Старый друг, Саратов", "An old friend in Saratov"),
  ("Старый друг в семьдесят лет начал рисовать и прислал картинку.", "An old friend took up painting at seventy and sent a picture."),
  ("Пишет: в семьдесят лет пошёл учиться рисовать. Прислал картинку: берёза и лодка. Лодка кривая, а берёза — как живая. Пишет: «Начни и ты что-нибудь». А что… Может, на гармони?",
   "He writes that at seventy he's started painting lessons. Sent a picture: a birch and a boat. The boat's crooked, but the birch is alive. He writes, “You start something too.” Well… maybe the accordion?"))
F("old", ("Друзья, Казань", "Friends in Kazan"),
  ("Из Казани прислали коробку чак-чака.", "A box of chak-chak came from Kazan."),
  ("Из Казани — чак-чак, в коробке, медовый, рассыпчатый. Пишут: «Ешь, пока свежий». Вот и съедим. Вместе! Берите, берите, не стесняйтесь.",
   "Chak-chak from Kazan, in a box, honeyed and crumbly. They write, “Eat it while it's fresh.” So we shall. Together! Go on, help yourself."))
F("old", ("Дальняя родня, Пермь", "Distant family in Perm"),
  ("Родня из Перми составляет родословную и просит помочь.", "Family in Perm are making a family tree and want help."),
  ("Родня из Перми составляет родословную. Спрашивают, как звали прадеда и где он жил. Прадеда звали… сейчас… Захар! Точно, Захар. Жил у самой реки, держал лодку. Вот и напишем.",
   "Relatives in Perm are making a family tree. They ask what our great-grandfather was called and where he lived. He was called… hang on… Zakhar! Yes, Zakhar. Lived right by the river and kept a boat. That's what we'll write."))
F("old", ("Старый друг, Курск", "An old friend in Kursk"),
  ("Друг прислал анекдот «про нас с тобой».", "A friend sent a joke “about you and me”."),
  ("Друг прислал анекдот из журнала и приписал: «Это про нас с тобой». Анекдот про двух стариков, которые спорят, кто из них моложе. Ну, про нас, допустим. Только я — моложе.",
   "A friend sent a joke from a magazine with a note: “This is about you and me.” It's about two old people arguing over which of them is younger. All right, it's about us. Only I'm younger."))
F("old", ("Двоюродная сестра, Брянск", "A cousin in Bryansk"),
  ("Двоюродная сестра взяла второе место за огурцы на районной выставке.", "A cousin won second prize for cucumbers at a district show."),
  ("Сестра двоюродная пишет: на выставке взяла второе место за огурцы. Первое дали за кабачок. «Кабачок, конечно, больше. Но огурцы — честнее». С этим не поспоришь.",
   "My cousin writes she took second prize for cucumbers at the show. First went to a marrow. “The marrow's bigger, of course. But cucumbers are more honest.” You can't argue with that."))
F("old", ("Друг детства, Москва", "A childhood friend in Moscow"),
  ("Друг детства просит прислать фотографию Липки.", "A childhood friend asks for a photo of the Lipka."),
  ("Друг детства, сто лет как в городе, просит: «Пришли фотографию Липки. Хочу посмотреть, всё ли там так». Всё так. Только ива у моста стала толще. Вы не сфотографируете? У вас ноги быстрее.",
   "A childhood friend, in the city for a hundred years, asks, “Send me a photo of the Lipka. I want to see if it's all still the same.” It is. Only the willow by the bridge is fatter. Could you take a picture? Your legs are quicker."))
F("old", ("Родня, Кострома", "Family in Kostroma"),
  ("Прислали вязаные тапочки с помпонами.", "Knitted slippers with pompoms arrived."),
  ("Тапочки вязаные прислали, с помпонами. «Чтоб по полу не мёрзло». Надену — буду ходить, как кот, неслышно. Помпоны только кот будет ловить.",
   "Knitted slippers with pompoms. “So the floor doesn't chill you.” Put them on and I'll walk as quiet as a cat. Only the cat will chase the pompoms."))
F("old", ("Землячество Сосновки", "The Sosnovka homecoming society"),
  ("Зовут на праздник родной деревни, от которой осталось семь домов.", "An invitation to a home-village festival: the village has seven houses left."),
  ("Зовут на праздник Сосновки, что за Городком. Домов там осталось семь, а гостей, пишут, будет триста — все, кто там родился или гостил. Поеду. Хоть посмотрю на тот колодец.",
   "An invitation to the Sosnovka festival, out past Gorodok. Only seven houses left there, but they say three hundred guests are coming: everyone born there or who ever stayed. I'll go. Just to see that well again."))
F("old", ("Армейский друг брата", "A brother's army friend"),
  ("Старый армейский друг брата пишет по старому адресу.", "A brother's old army friend is still writing to the old address."),
  ("Это брату. Его армейский друг шлёт по старому адресу, тридцать лет подряд. «Помнишь, как мы с тобой на учениях заблудились и вышли к пасеке?» Перешлю. Пусть брат вспомнит, а то он забывать начал, где мёд.",
   "This is for my brother. His army friend keeps sending to the old address, thirty years running. “Remember getting lost on manoeuvres and coming out at an apiary?” I'll forward it. Let my brother remember; he's starting to forget where the honey is."))
F("old", ("Товарищ по стройотряду", "A friend from student building brigade"),
  ("Друг по студенческому стройотряду прислал фото коровника.", "A friend from a student building brigade sent a photo of a cowshed."),
  ("Друг по стройотряду прислал фото: коровник, что мы строили в семидесятых. Стоит! Покрашен, крыша новая. Пишет: «Наша работа, сто лет простоит». Сто лет — это он загнул. Но пятьдесят уже простоял.",
   "A friend from our student building brigade sent a photo of the cowshed we built in the seventies. Still standing! Painted, new roof. He writes, “Our work, it'll last a hundred years.” A hundred's pushing it. But it's done fifty already."))
F("old", ("Бывшие соседи по общежитию", "Old hostel neighbours"),
  ("Бывшие соседи по общежитию прислали банку огурцов — проверить рецепт.", "Old hostel neighbours sent a jar of pickles to check a recipe."),
  ("Соседи по старому общежитию прислали огурцов банку — по моему же рецепту. Пишут: «Проверь, так ли». Проверим. Так. Только чеснока пожалели. Город — он и есть город.",
   "Neighbours from the old hostel sent a jar of pickled cucumbers made from my own recipe. They write, “Check we got it right.” Let's see. Right. Just stingy on the garlic. Townsfolk, what can you do."))
F("old", ("«Сад и огород», редакция", "Garden and Plot, the editors"),
  ("Журнал напечатал письмо читателя из Липовки — прислали гонорар.", "A magazine printed a letter from Lipovka and sent a fee."),
  ("Из журнала пишут: моё письмо про картошку в соломе напечатали! И гонорар — триста рублей. Первый гонорар в жизни. Не потрачу. Положу в рамку. Ну, или потрачу, но на рамку.",
   "The magazine writes that they printed my letter about growing potatoes under straw! And a fee: three hundred roubles. My first ever fee. I won't spend it. I'll frame it. Or spend it, but on the frame."))
F("old", ("Друг по переписке, Минск", "A pen-friend in Minsk"),
  ("Друг по переписке из Минска прислал драников рецепт — с поправками.", "A pen-friend in Minsk sent a potato-pancake recipe, with corrections."),
  ("Рецепт драников из Минска. Первая строчка: «Забудь всё, что ты знаешь о драниках». Забуду. Хотя я много чего знаю. Ладно, попробуем по-белорусски.",
   "A potato-pancake recipe from Minsk. First line: “Forget everything you know about potato pancakes.” I'll forget. Though I know a lot. All right, we'll try it the Belarusian way."))
F("old", ("Санаторий «Сосны»", "Pines Sanatorium"),
  ("Санаторий прислал рекламу: «Отдых для души и тела».", "A sanatorium sent an advert: “Rest for body and soul.”"),
  ("Реклама санатория: «Отдых для души и тела, сосновый бор, танцы по вечерам». Сосновый бор у нас и тут есть. Танцы — в клубе по субботам. Выходит, мы и так в санатории живём. Бесплатно.",
   "An advert for a sanatorium: “Rest for body and soul, a pine forest, dancing in the evenings.” We've got pine forest here. Dancing at the club on Saturdays. So we live in a sanatorium already. For free."))
F("old", ("Племянница, Новгород", "A niece in Novgorod"),
  ("Племянница прислала фотографию — первая пятёрка её сына.", "A niece sent a photo of her son's first top mark."),
  ("Племянница прислала фотографию тетрадки. Тетрадки! А в тетрадке — пятёрка, первая, у её сынишки. Красной ручкой, на полстраницы. Вот это новость. Вот это я понимаю — фотография.",
   "My niece sent a photo of an exercise book. An exercise book! And in it, a top mark, her little boy's first. In red, half a page tall. Now that's news. Now that's a photo worth sending."))
F("old", ("Подруга, Липецк", "A friend in Lipetsk"),
  ("Из Липецка прислали выкройку фартука и лоскуток ситца «на пробу».", "A friend in Lipetsk sent an apron pattern and a scrap of chintz “to try”."),
  ("Выкройка фартука и лоскут ситца в горошек, «на пробу — подойдёт ли цвет». Горошек! Синий! Подойдёт. Ко всему подойдёт: к кухне, к забору, к настроению.",
   "An apron pattern and a scrap of polka-dot chintz, “to see if the colour suits”. Polka dots! Blue! It suits. It suits everything: the kitchen, the fence, my mood."))
F("old", ("Старый друг, Омск", "An old friend in Omsk"),
  ("Из Омска пришло письмо, написанное перьевой ручкой.", "A letter written with a fountain pen came from Omsk."),
  ("Письмо перьевой ручкой, с нажимом, с завитушками — как в школе учили. Сейчас так никто не пишет. Он пишет. Пятнадцать минут читать, а приятно — будто музыку слушаешь.",
   "A letter in fountain pen, with proper thick and thin strokes and flourishes, the way they taught us at school. Nobody writes like that now. He does. It takes fifteen minutes to read, and it's lovely, like listening to music."))
F("old", ("Родня, Ростов", "Family in Rostov"),
  ("Из Ростова прислали посылку сушёной рыбы — чехони.", "A parcel of dried fish came from Rostov."),
  ("Из Ростова — рыбка сушёная, чехонь. Пахнет так, что Сургуч на почте, наверное, неделю будет этот угол нюхать. Возьмите одну, не отказывайтесь. Ну, тогда коту.",
   "Dried fish from Rostov. It smells so strong that Surguch will be sniffing that corner of the post office for a week. Take one, don't refuse. Well then, take one for the cat."))
F("old", ("Клуб читателей журнала", "A magazine readers' club"),
  ("Клуб читателей просит прислать рецепт пирога «из детства».", "A readers' club asks for a pie recipe “from childhood”."),
  ("Клуб читателей журнала собирает книжку «Пироги нашего детства». Просят рецепт. Рецепт… Его ж не записать. Там «на глаз», «сколько возьмёт» и «пока не запахнет». Так и напишем.",
   "A magazine readers' club is putting together a book, Pies of Our Childhood, and wants a recipe. A recipe… You can't write it down. It's “by eye”, “as much as it takes” and “until it smells right”. That's what we'll write."))
F("old", ("Знакомые, Псков", "Friends in Pskov"),
  ("Из Пскова прислали фото: у знакомых аист свил гнездо на столбе.", "Friends in Pskov sent a photo: storks nesting on a pole."),
  ("Знакомые из-под Пскова прислали фото: на столбе у них аист свил гнездо, огромное, как шапка великана. Пишут: «Теперь весь год к счастью». А у нас ласточки. Тоже к счастью, только помельче.",
   "Friends near Pskov sent a photo: storks have nested on a pole by their house, a nest like a giant's hat. They write, “Luck all year now.” We have swallows. Luck too, just smaller."))
F("old", ("Племянник, Новосибирск", "A nephew in Novosibirsk"),
  ("Племянник прислал фото: научился печь хлеб.", "A nephew sent a photo: he's learnt to bake bread."),
  ("Племянник научился печь хлеб, прислал фото. Буханка кривенькая, но румяная, а он рядом гордый, как будто дом построил. Ну, хлеб — это тоже дом. Маленький.",
   "My nephew's learnt to bake bread and sent a photo. The loaf's a bit lopsided but golden, and he's standing next to it as proud as if he'd built a house. Well, a loaf is a house too. A little one."))
F("old", ("Подруга, Ессентуки", "A friend in Yessentuki"),
  ("Подруга на водах прислала открытку: «Пью воду, скучаю».", "A friend at the spa sent a card: “Drinking the waters, missing you.”"),
  ("Открытка с курорта: «Пью воду три раза в день, гуляю по терренкуру, скучаю по вашим огурцам». По огурцам! Воду пьёт — а скучает по огурцам. Наш человек.",
   "A card from the spa: “Drinking the waters three times a day, walking the trails, missing your pickles.” Pickles! She drinks the waters and misses pickles. One of us."))
F("old", ("Друг, Великий Новгород", "A friend in Veliky Novgorod"),
  ("Друг прислал берестяную грамоту — сувенирную.", "A friend sent a souvenir birch-bark letter."),
  ("Друг прислал берестяную грамоту — сувенирную, из музея. Там по-старинному: «Поклон от Онфима». Онфим был мальчишка, рисовал на бересте. Восемьсот лет назад. А письмо дошло. Вот это почта.",
   "A friend sent a birch-bark letter, a museum souvenir. It says in the old tongue: “Greetings from Onfim.” Onfim was a boy who drew on birch bark eight hundred years ago. And the letter still got here. Now that's a postal service."))
F("old", ("Бывший сосед, Мурманск", "A former neighbour in Murmansk"),
  ("Бывший сосед прислал морошки в банке.", "A former neighbour sent a jar of cloudberries."),
  ("Морошка из Мурманска! Бывший сосед помнит, что я её люблю. Двадцать лет помнит. Банка маленькая, а радости — на всю зиму.",
   "Cloudberries from Murmansk! An old neighbour remembers I love them. Twenty years he's remembered. A little jar, but enough joy for the whole winter."))
F("old", ("Родня, Вятка", "Family in Vyatka"),
  ("Прислали дымковскую игрушку — барыню с коромыслом.", "A painted Dymkovo clay lady with yoke and buckets arrived."),
  ("Из Вятки прислали дымковскую игрушку: барыня с коромыслом, в юбке колоколом, вся в кружочках. Поставлю на подоконник. Пусть воду носит, раз уж приехала.",
   "A Dymkovo clay toy from Vyatka: a lady with a yoke and two buckets, bell-shaped skirt covered in painted circles. I'll put her on the windowsill. She can fetch the water, since she's here."))
F("old", ("Друг, Ялта", "A friend in Yalta"),
  ("Из Ялты пришла открытка с кипарисами и запахом лаванды.", "A card with cypresses came from Yalta, smelling of lavender."),
  ("Открытка с кипарисами, а пахнет лавандой — друг в конверт мешочек вложил. «Чтобы и у тебя было лето». Вот и есть. Посреди всего — лето.",
   "A card with cypresses, smelling of lavender: my friend tucked a little bag of it in the envelope. “So you can have summer too.” And I have. Summer, right in the middle of everything."))
F("old", ("«Новый урожай», агрофирма", "New Harvest seed company"),
  ("Агрофирма прислала поздравление «с успешным садовым сезоном».", "A seed company sent congratulations “on a successful gardening season”."),
  ("Агрофирма поздравляет «с успешным садовым сезоном». Это у кого он успешный? У слизней он успешный. Но открытка красивая, с подсолнухом. Подсолнух у них тоже успешный.",
   "A seed company congratulates me “on a successful gardening season”. Successful for whom? For the slugs, yes. But it's a pretty card with a sunflower. Their sunflower's had a good season too."))
F("old", ("Старый друг, Тверь", "An old friend in Tver"),
  ("Старый друг прислал письмо и фото своего кота — «познакомиться».", "An old friend sent a letter and a photo of his cat, “to introduce him”."),
  ("Прислал фото кота, «чтоб познакомились». Кот серый, щекастый, лежит на газете. Пишет: «Он тоже газеты читает — лёжа». Кошки, видно, везде одинаковые. Наш Сургуч тоже лёжа читает. Письма.",
   "He sent a photo of his cat “so you can be introduced”. A grey, chubby-cheeked cat lying on a newspaper. He writes, “He reads the papers too, lying down.” Cats are the same everywhere. Our Surguch reads lying down too. Letters."))
F("old", ("Землячка, Ленинградская область", "A woman from the old village"),
  ("Землячка пишет: нашла в старом сундуке тетрадь песен.", "A woman from the old village found a notebook of songs in a chest."),
  ("Землячка нашла в сундуке тетрадь песен, ещё её бабушки. Переписала мне три — про реку, про гармониста и про рябину. Петь будем на посиделках. Только мотив кто-нибудь пусть вспомнит.",
   "A woman from my old village found her grandmother's songbook in a chest. She's copied three for me: about the river, the accordion player and the rowan tree. We'll sing them at the gatherings. If someone can remember the tunes."))
F("old", ("Подписка «Здоровье»", "Health magazine subscription"),
  ("Журнал «Здоровье» предлагает продлить подписку — со скидкой.", "A health magazine offers a renewal, with a discount."),
  ("Предлагают продлить подписку на журнал «Здоровье». В прошлом номере советовали больше ходить и меньше волноваться. Ходить — ладно. А не волноваться за подписку — не получается.",
   "They want me to renew my subscription to a health magazine. Last issue advised walking more and worrying less. Walking, fine. But not worrying about the subscription, that I can't manage."))
F("old", ("Друзья, Вологда", "Friends in Vologda"),
  ("Из Вологды прислали вологодского масла — в фольге, с печатью.", "Vologda butter came in foil, with the stamp."),
  ("Масло вологодское прислали! В фольге, с печатью. Почта, правда, тёплая была — оно немного загрустило. Ничего. Блины с ним грустить не будут.",
   "They sent Vologda butter! In foil, with the official stamp. The post was a bit warm and it's gone a little sad. Never mind. The pancakes won't be sad with it."))
F("old", ("Подруга по курорту", "A friend from the spa"),
  ("Знакомые по санаторию прислали групповое фото — «все в панамах».", "Spa friends sent a group photo: “everyone in sun hats”."),
  ("Фото из санатория, двенадцать человек, все в панамах. Подписано: «Узнай себя». Ну это нечестно — в панамах все одинаковые. Вот эта, третья слева, вроде… нет. Вот эта.",
   "A photo from the sanatorium, twelve people, all in sun hats. Written on it: “Find yourself.” That's not fair, everyone looks the same in a sun hat. That one, third from the left… no. That one."))
F("old", ("Дальний родственник, Канада", "A distant relative in Canada"),
  ("Письмо из Канады — от родни, о которой давно не слышали.", "A letter from Canada, from relatives not heard from in years."),
  ("Из Канады! Дальняя родня, внук троюродного деда. Пишет по-русски, с ошибками: «Дорогие родные, я хочу узнать, где моя деревня». Ну, где… Вот же она. Напишем, позовём. Пусть приезжает смотреть.",
   "From Canada! Distant family, the grandson of a second cousin of my grandfather. He writes in Russian with mistakes: “Dear relatives, I want to know where my village is.” Where? Right here. We'll write and invite him. Let him come and see."))


# --------------------------------------------------------------------------- fillers: young
F("young", ("Друзья, Москва", "Friends in Moscow"),
  ("Друзья зовут в Москву на концерт — в субботу.", "Friends invite someone to a concert in Moscow on Saturday."),
  ("Друзья из Москвы зовут на концерт в субботу. В Москву! В субботу! А у меня в субботу баня. Нет, баня важнее. Москва подождёт, она большая.",
   "Friends in Moscow are inviting me to a concert on Saturday. Moscow! Saturday! But Saturday's bathhouse day. No, the bathhouse wins. Moscow can wait; it's big."))
F("young", ("Интернет-магазин", "An online shop"),
  ("Пришла посылка из интернет-магазина — лампа «как в скандинавском доме».", "A parcel from an online shop: a lamp “like in a Scandinavian home”."),
  ("Заказывали лампу «как в скандинавском доме». Пришла лампа как в нашем доме. Ну, тоже хорошо. Даже лучше — родная.",
   "We ordered a lamp “like in a Scandinavian home”. What came is a lamp like in our home. Fine. Better, even: it's one of ours."))
F("young", ("Друг по переписке, Япония", "A pen-friend in Japan"),
  ("Из Японии прислали бумажного журавлика и схему.", "A paper crane and instructions came from Japan."),
  ("Друг из Японии прислал журавлика из бумаги — и схему, как сложить самому. Сорок шагов! Попробую. Выйдет, наверное, утка. Тоже птица.",
   "A friend in Japan sent a paper crane and instructions to fold one myself. Forty steps! I'll try. It'll probably come out a duck. Still a bird."))
F("young", ("Однокурсники, Ярославль", "College friends in Yaroslavl"),
  ("Пришло приглашение на свадьбу в Ярославль, дресс-код — «всё синее».", "A wedding invitation from Yaroslavl, dress code: “everything blue”."),
  ("Однокурсники женятся! В августе, в Ярославле. Дресс-код: «всё синее». Синего у меня только валенки. Надо думать.",
   "College friends are getting married! August, in Yaroslavl. Dress code: “everything blue”. The only blue thing I own is felt boots. Need to think."))
F("young", ("Старая подруга, Самара", "An old friend in Samara"),
  ("Старая подруга прислала настоящее бумажное письмо.", "An old friend sent a real letter on paper."),
  ("Письмо от подруги — настоящее, на бумаге! «Решила попробовать, как в старину». Почерк у неё совсем детский, круглый. Сто лет его не было видно. Отвечу тоже от руки. Где-то тут была ручка…",
   "A letter from a friend, a real one on paper! “I thought I'd try the old-fashioned way.” Her handwriting is round, like a child's. Haven't seen it in a hundred years. I'll answer by hand too. There was a pen somewhere…"))
F("young", ("Брат, Стамбул", "A brother in Istanbul"),
  ("Из Стамбула пришла открытка: чайки и чай в стаканчиках.", "A card from Istanbul: seagulls and tea in tulip glasses."),
  ("Брат прислал открытку из Стамбула: чайки над проливом и чай в стаканчиках-тюльпанах. Пишет: «Чай тут сладкий, а скучаю по-нашему, по крепкому, из самовара».",
   "My brother sent a card from Istanbul: seagulls over the strait and tea in little tulip glasses. He writes, “The tea's sweet here, but I miss ours, strong, from the samovar.”"))
F("young", ("Онлайн-школа гитары", "An online guitar school"),
  ("Онлайн-школа гитары напоминает о пропущенных уроках.", "An online guitar school sends a reminder about missed lessons."),
  ("Пишут: «Вы пропустили семь уроков». Семь! Кто-то, выходит, считал. Гитара лежит на шкафу. Ей тоже отдохнуть надо. Завтра. Честно, завтра.",
   "They write, “You have missed seven lessons.” Seven! Somebody's been counting. The guitar's on top of the wardrobe. It needs a rest too. Tomorrow. Honestly, tomorrow."))
F("young", ("Друг-фотограф, Тверь", "A photographer friend, Tver"),
  ("Друг прислал плёночные фотографии с прошлого лета.", "A friend sent film photos from last summer."),
  ("Плёночные фото с прошлого лета. На половине — чей-то палец. Но на одной — закат над рекой, такой, что палец прощаем.",
   "Film photos from last summer. Half of them have somebody's finger in. But one is a sunset over the river so lovely we forgive the finger."))
F("young", ("Подруга, Москва", "A friend in Moscow"),
  ("Подруга с балконным огородом прислала семена помидоров.", "A friend with a balcony garden sent tomato seeds."),
  ("Подруга в Москве завела огород на балконе. Прислала семена «балконных» помидоров: «Вырастут маленькие, зато гордые». Посадим. Пусть посмотрят, как в деревне растут гордые.",
   "A friend in Moscow has started a balcony garden and sent seeds of “balcony” tomatoes: “They grow small but proud.” We'll plant them. Let them see how proud grows in a village."))
F("young", ("Друзья, Нижний Новгород", "Friends in Nizhny Novgorod"),
  ("Друзья прислали настольную игру про железную дорогу.", "Friends sent a board game about building railways."),
  ("Настольная игра! Про строительство железной дороги. Правила на шести страницах. Вечер будет длинный. И с чаем.",
   "A board game! About building railways. Six pages of rules. It's going to be a long evening. With tea."))
F("young", ("Журнал «Юность»", "Youth magazine"),
  ("Журнал ответил на присланные стихи.", "A magazine replied about some poems."),
  ("Из журнала ответ: стихи не возьмут, но «в них есть искренность». Искренность есть. Рифмы нет. Ничего, есть с чего начать.",
   "A reply from the magazine: they won't print the poems, but “there is sincerity in them”. Sincerity, yes. Rhymes, no. Well, it's somewhere to start."))
F("young", ("Сестра, Казань", "A sister in Kazan"),
  ("Сестра прислала программку концерта, где она поёт в хоре.", "A sister sent the programme of a concert where she sings in a choir."),
  ("Сестра поёт в хоре, прислала программку. Её фамилия во втором столбце, мелко. Обвела ручкой: «Найдёшь?» Нашли! Вот она, между двух Ивановых.",
   "My sister sings in a choir and sent the programme. Her name's in the second column, tiny. She's circled it: “Can you find me?” Found! There, between two Ivanovs."))
F("young", ("Книжный магазин, Ярославль", "A bookshop in Yaroslavl"),
  ("Книжный прислал купон на скидку.", "A bookshop sent a discount voucher."),
  ("Купон из книжного: «Скидка двадцать процентов на любую книгу». На любую! Значит, на самую толстую. Чтобы на всю зиму.",
   "A bookshop voucher: “Twenty per cent off any book.” Any book! The fattest one, then. To last all winter."))
F("young", ("Друг-путешественник, Чита", "A travelling friend, Chita"),
  ("Друг едет автостопом до Владивостока — открытка из Читы.", "A friend hitchhiking to Vladivostok sent a card from Chita."),
  ("Друг едет автостопом до Владивостока. Открытка из Читы: «Половину проехал. Вторая половина длиннее». Это как с письмами: начать легко, а закончить…",
   "A friend is hitchhiking to Vladivostok. A card from Chita: “Halfway. The second half is longer.” Like writing letters: easy to start, but finishing…"))
F("young", ("Однокурсник, Кавказ", "A college friend in the Caucasus"),
  ("Однокурсник прислал засушенный эдельвейс с гор.", "A college friend sent a pressed edelweiss from the mountains."),
  ("Однокурсник был в горах, прислал эдельвейс. «Лез за ним три часа». Цветок с ноготок. Три часа! Вот это любовь — к ботанике.",
   "A college friend went to the mountains and sent an edelweiss. “Climbed three hours for it.” A flower the size of a fingernail. Three hours! Now that's love. Of botany."))
F("young", ("Школьный друг, Вологда", "A school friend in Vologda"),
  ("Школьный друг прислал кассету с песнями, «как в школе».", "A school friend sent a cassette of songs, “like at school”."),
  ("Кассета! Настоящая, с лентой. «Записал тебе песни, как в школе». А магнитофон? Есть! У соседей на чердаке. Сейчас добудем.",
   "A cassette! A real one, with tape. “Recorded you some songs, like at school.” And something to play it on? There is! In the neighbours' attic. We'll get it down."))
F("young", ("Вестник выпускников", "The alumni bulletin"),
  ("Институт прислал вестник выпускников с фото группы.", "The institute sent its alumni bulletin with a class photo."),
  ("Вестник выпускников, а на последней странице — наша группа, двенадцать лет назад. Все такие серьёзные. С чего бы? Стипендию, что ли, задержали.",
   "The alumni bulletin, and on the back page, our group twelve years ago. All so serious. Why? Was the grant late, or something?"))
F("young", ("Подруга, Тула", "A friend in Tula"),
  ("Подруга родила — прислала первую фотографию малыша.", "A friend has had a baby and sent the first photo."),
  ("Подруга родила! Фото: свёрток, нос пуговкой и шапка с ушками. «Приезжай знакомиться». Поеду. Надо только связать что-нибудь. Или купить — быстрее.",
   "My friend's had her baby! A photo: a bundle, a button nose and a hat with ears. “Come and meet him.” I'll go. I need to knit something first. Or buy something, it's quicker."))
F("young", ("Бывший коллега, Москва", "A former colleague in Moscow"),
  ("Бывший коллега спрашивает, не скучно ли в деревне без офиса.", "A former colleague asks if village life is dull without the office."),
  ("Бывший коллега пишет: «Скучаешь по офису?» По офису… По кофемашине, может быть. По офису — нет. Тут вон какие облака.",
   "A former colleague writes, “Do you miss the office?” The office… The coffee machine, maybe. The office, no. Look at the clouds here."))
F("young", ("Радио «Городок FM»", "Gorodok FM"),
  ("Радио прислало футболку за победу в викторине.", "The radio station sent a T-shirt for winning a quiz."),
  ("Выиграли викторину на радио — прислали футболку с надписью «Я слушаю». Буду носить. Пусть все знают: я слушаю.",
   "Won a radio quiz and they sent a T-shirt saying I'M LISTENING. I'll wear it. Let everyone know: I'm listening."))
F("young", ("Автошкола, Городок", "Driving school, Gorodok"),
  ("Из автошколы: экзамен по вождению назначен на среду.", "The driving school has set the test for Wednesday."),
  ("Экзамен по вождению — в среду. В среду! Надо ещё раз объехать все столбы у клуба. Столбы у нас знакомые, они не подведут.",
   "The driving test is on Wednesday. Wednesday! I'll go round all the posts by the club once more. Our posts are friendly; they won't let me down."))
F("young", ("Друг по переписке, Германия", "A pen-friend in Germany"),
  ("Друг из Германии пишет по-русски — с милыми ошибками.", "A German pen-friend writes in Russian, with sweet mistakes."),
  ("Друг из Германии учит русский: «Я очень скучаю по вашей бане и по вашей пирожки». По вашей пирожки! Поправлю. Но нежно.",
   "A friend in Germany is learning Russian: “I very much miss your bathhouse and your pie-s.” Your pie-s! I'll correct it. Gently."))
F("young", ("Друзья, Петербург", "Friends in St Petersburg"),
  ("Друзья прислали план новой квартиры — с местом для гостя.", "Friends sent a plan of their new flat, with a spot for a guest."),
  ("Друзья переехали, нарисовали план квартиры. На плане: «Здесь будешь спать ты». Это раскладушка у балкона. Место хорошее, с видом.",
   "Friends have moved and drew a plan of the flat. On it: “This is where you'll sleep.” A camp bed by the balcony. Good spot, with a view."))
F("young", ("Сестрёнка, Калуга", "A little sister in Kaluga"),
  ("Младшая сестра сдала физику на пятёрку.", "A little sister got top marks in physics."),
  ("Сестрёнка пишет: «Физику на пять! Картинки к задачам помогли!» Помогли! Всю зиму ей по почте задачи рисовали. Вот она, почта, — и физику сдаёт.",
   "My little sister writes, “Top marks in physics! Drawing the problems helped!” It did! All winter we drew her problems by post. That's the post for you: it passes physics exams."))
F("young", ("Друзья с фестиваля", "Friends from a festival"),
  ("Друзья прислали фото с фестиваля: все в грязи и счастливые.", "Friends sent festival photos: everyone muddy and happy."),
  ("Фото с фестиваля под открытым небом: грязь по колено, все счастливые. «В следующий раз — с тобой». В грязь по колено? Ладно. С ними можно.",
   "Photos from an open-air festival: mud up to the knees and everyone happy. “Next time, with you.” Knee-deep in mud? All right. With them, yes."))
F("young", ("Подруга, Петербург", "A friend in St Petersburg"),
  ("Подруга прислала самодельный журнал про старые дворы.", "A friend sent her home-made zine about old courtyards."),
  ("Подруга сама делает журнал, на ксероксе, про старые питерские дворы. Прислала третий номер. Там её двор, где кошки сидят на трубе. Сургуч бы оценил.",
   "A friend makes her own zine on a photocopier, about old Petersburg courtyards. She sent issue three. Her courtyard's in it, with cats sitting on a drainpipe. Surguch would approve."))
F("young", ("Брат, Краснодар", "A brother in Krasnodar"),
  ("Брат прислал семена самого острого перца в мире.", "A brother sent seeds of the hottest pepper in the world."),
  ("Семена перца «Каролинский жнец», самого острого на свете. Подписано: «Не ешь. Просто посади и бойся». Посажу. И буду бояться.",
   "Seeds of the Carolina Reaper, the hottest pepper in the world. The label says, “Don't eat it. Just plant it and be afraid.” I'll plant it. And be afraid."))
F("young", ("Друзья, Воронеж", "Friends in Voronezh"),
  ("Прислали пазл на тысячу кусочков — «Ночь в Венеции».", "A thousand-piece jigsaw arrived: Night in Venice."),
  ("Пазл на тысячу кусочков, «Ночь в Венеции». Половина кусочков — чёрная ночь. Ничего, зима длинная. Справимся.",
   "A thousand-piece jigsaw, Night in Venice. Half the pieces are black night. Never mind, winter's long. We'll manage."))
F("young", ("Подруга-вегетарианка", "A vegetarian friend"),
  ("Подруга прислала рецепт котлет из свёклы.", "A friend sent a recipe for beetroot burgers."),
  ("Подруга стала вегетарианкой, прислала рецепт «котлет из свёклы». Котлеты из свёклы! Ну, попробовать можно. Свёкла своя, не жалко.",
   "A friend has gone vegetarian and sent a recipe for “beetroot burgers”. Beetroot burgers! Well, we can try. It's our own beetroot, no loss."))
F("young", ("Друг из похода, Карелия", "A friend hiking in Karelia"),
  ("Из похода пришло письмо на промокшей бумаге — и перо сойки.", "A letter from a hike, on rain-wrinkled paper, with a jay feather."),
  ("Письмо из похода по Карелии — бумага промокла и высохла, волнами. И перо сойки в конверте. «Нашёл у костра, подумал о тебе». Приятно, что у костра думают о нас.",
   "A letter from a hike in Karelia, the paper soaked and dried in waves. And a jay feather in the envelope. “Found it by the campfire and thought of you.” Nice to be thought of by a campfire."))
F("young", ("Друзья с барахолки", "Friends at a flea market"),
  ("Прислали пачку старых открыток с барахолки — все подписанные.", "A bundle of old written postcards from a flea market."),
  ("Двадцать старых открыток с барахолки, все подписаны кем-то когда-то. «Маруся, жду», «Вася, приезжай». Чужие письма, а читать хочется. Надеюсь, все Маруси дождались.",
   "Twenty old postcards from a flea market, all written by someone, sometime. “Marusya, I'm waiting.” “Vasya, do come.” Strangers' letters, but you want to read them. I hope all the Marusyas got their visit."))
F("young", ("Онлайн-курсы фотографии", "An online photography course"),
  ("Пришёл сертификат об окончании курса фотографии.", "A certificate arrived for finishing a photography course."),
  ("Сертификат: «Курс фотографии окончен». Восемь недель, а главное, чему научили: свет надо ждать. Вот и ждём. Утром у реки — самый лучший.",
   "A certificate: “Photography course completed.” Eight weeks, and the main lesson: you have to wait for the light. So we wait. Mornings by the river are best."))
F("young", ("Магазин пластинок", "A record shop"),
  ("Пришла заказанная виниловая пластинка — а проигрывателя нет.", "An ordered vinyl record arrived, with nothing to play it on."),
  ("Пластинка пришла! Чёрная, тяжёлая, в конверте с картинкой. Проигрывателя, правда, нет. Ничего. Пока будем на неё смотреть.",
   "The record's here! Black, heavy, in a sleeve with a picture. There's no record player, mind you. Never mind. For now we'll look at it."))
F("young", ("Подруга, Португалия", "A friend in Portugal"),
  ("Подруга из Португалии просит прислать ей снега.", "A friend in Portugal asks to be sent some snow."),
  ("Подруга уехала в Португалию: «Тут океан, но нет снега. Пришли мне снега». Снег по почте… Пришлю фото сугроба. И варежку. Пусть представит.",
   "A friend moved to Portugal: “There's the ocean, but no snow. Send me some snow.” Snow by post… I'll send a photo of a snowdrift. And a mitten. She can imagine."))
F("young", ("Друг-обжарщик, Тверь", "A coffee-roaster friend, Tver"),
  ("Друг открыл кофейню и прислал зёрна своей обжарки.", "A friend opened a café and sent his own roasted beans."),
  ("Друг открыл кофейню в Твери — прислал зёрна. Пахнет так, что на почте, наверное, все проснулись. Сварю в турке, по-деревенски. Пусть удивляется.",
   "A friend has opened a café in Tver and sent beans. The smell must have woken the whole post office. I'll brew it in a Turkish pot, village style. Let him be surprised."))
F("young", ("Двоюродный брат, 16 лет", "A cousin, sixteen"),
  ("Шестнадцатилетний кузен просит совета в сердечных делах.", "A sixteen-year-old cousin asks for advice on matters of the heart."),
  ("Двоюродный брат, шестнадцать лет, спрашивает: «Как понять, что она тоже?» Ох. Сяду отвечать. Длинно. С примерами. Без имён.",
   "My cousin, sixteen, asks, “How do you know if she feels the same?” Oh dear. I'll sit down and answer. At length. With examples. No names."))
F("young", ("Друзья, Екатеринбург", "Friends in Yekaterinburg"),
  ("Друзья прислали открытку-гармошку с видами Урала.", "Friends sent a fold-out postcard of the Urals."),
  ("Открытка-гармошка, двенадцать видов Урала. Развернёшь — через всю комнату. Камни, озёра, сосны. А в конце — их кот на подоконнике. Тоже, видимо, достопримечательность.",
   "A fold-out card, twelve views of the Urals. Unfold it and it stretches across the room. Rocks, lakes, pines. And at the end, their cat on the windowsill. A local landmark, I suppose."))
F("young", ("Друг-барабанщик", "A drummer friend"),
  ("Друг прислал диск своей группы — «громко, но с душой».", "A friend sent his band's CD: “loud, but with soul”."),
  ("Друг прислал диск своей группы: «Слушать громко». Громко у нас нельзя — коровы пугаются. Будем слушать тихо, но с душой. Он поймёт.",
   "A friend sent his band's CD: “Play it loud.” We can't play loud here, it frightens the cows. We'll listen quietly but with feeling. He'll understand."))
F("young", ("Подруга по общежитию", "An old hostel room-mate"),
  ("Соседка по общежитию прислала фото их старой комнаты.", "An old hostel room-mate sent a photo of their old room."),
  ("Соседка по общежитию была в институте и сфотографировала нашу старую комнату. Кровати те же, обои те же, а на подоконнике — чужой кактус. Наш был лучше. Наш цвёл.",
   "My old hostel room-mate visited the institute and photographed our old room. Same beds, same wallpaper, and a stranger's cactus on the windowsill. Ours was better. Ours flowered."))
F("young", ("Клуб «Что? Где? Когда?»", "A quiz club"),
  ("Клуб знатоков в Городке зовёт в свою команду.", "A Gorodok quiz club invites someone to join the team."),
  ("Клуб знатоков в Городке ищет игроков: «Нужен человек, который знает, как называется деталь от трактора и кто написал „Муму“». Ну это ж просто. Пойду.",
   "A quiz club in Gorodok needs players: “Wanted: someone who knows what that tractor part's called and who wrote Mumu.” That's easy. I'll go."))
F("young", ("Друзья, Сочи", "Friends in Sochi"),
  ("Друзья с юга прислали мандарины — прямо в посылке, с листьями.", "Friends in the south sent tangerines with their leaves on."),
  ("Мандарины из Сочи, прямо с листьями! Пахнет так, что можно не есть — просто нюхать. Но съедим. Берите, берите, их много.",
   "Tangerines from Sochi, leaves and all! The smell's so good you needn't eat them, just sniff. But we'll eat them. Go on, take some, there are plenty."))
F("young", ("Друг, Новосибирск", "A friend in Novosibirsk"),
  ("Друг прислал свою первую научную статью — на английском.", "A friend sent his first scientific paper, in English."),
  ("Друг прислал свою первую научную статью — на английском, про какие-то частицы. Ничего не понятно, кроме благодарности в конце. А там — наша фамилия! «За терпение». Вот это вклад в науку.",
   "A friend sent his first scientific paper, in English, about some particles or other. Couldn't understand a word except the thanks at the end. And there's our name! “For their patience.” Now that's a contribution to science."))

# --------------------------------------------------------------------------- fillers: family
F("family", ("Сваты, Курск", "The in-laws in Kursk"),
  ("Сваты прислали посылку: сало, яблоки и безразмерную кофту.", "The in-laws sent a parcel: salo, apples and a one-size-fits-all cardigan."),
  ("Сваты из Курска прислали посылку: сало, яблоки и кофту — безразмерную, на всех сразу. Кто первый замёрзнет, того и кофта.",
   "The in-laws in Kursk sent a parcel: salo, apples and a cardigan, one size fits all, for everybody at once. Whoever gets cold first gets the cardigan."))
F("family", ("Родители, Рязань", "Parents in Ryazan"),
  ("Родители пишут вдвоём: мама ровно, папа поперёк.", "Parents write together: Mum along the lines, Dad across them."),
  ("Мама с папой пишут вдвоём на одном листе: мама ровно, по строчкам, папа — поперёк, на полях. Мама про огород, папа про рыбалку. Читаешь — как будто дома за столом.",
   "Mum and Dad write on one sheet: Mum neatly along the lines, Dad sideways in the margins. Mum about the garden, Dad about fishing. Reading it is like sitting at the table at home."))
F("family", ("Брат, Липецк", "A brother in Lipetsk"),
  ("Брат прислал фото семьи на фоне новой машины.", "A brother sent a family photo in front of a new car."),
  ("Брат прислал фото всей семьи на фоне новой машины. Машину видно хорошо. Брата — хуже. Ну, видно, так он и хотел.",
   "My brother sent a photo of the whole family in front of their new car. You can see the car very well. My brother, less so. That was the idea, I expect."))
F("family", ("Мама", "Mum"),
  ("Мама прислала бабушкину скатерть — с вышивкой и старым пятнышком.", "Mum sent Gran's tablecloth, embroidered, with an old stain."),
  ("Мама прислала бабушкину скатерть — с вышивкой и с пятнышком от варенья, которое тридцать лет никто не смог отстирать. Пятнышко — тоже память. Самое вкусное место.",
   "Mum sent Gran's tablecloth: embroidered, with a jam stain nobody's managed to wash out in thirty years. The stain's a memory too. The tastiest bit."))
F("family", ("Мама", "Mum"),
  ("Мама прислала рецепт щей на трёх страницах, с рисунками.", "Mum sent a three-page cabbage-soup recipe, illustrated."),
  ("Мамин рецепт щей, на трёх страницах, с рисунками. На рисунке капуста похожа на солнце. Мама у нас художник. По капусте.",
   "Mum's cabbage soup recipe, three pages, illustrated. The cabbage in the drawing looks like the sun. Mum's an artist. A cabbage artist."))
F("family", ("Родня, Ярославль", "Family in Yaroslavl"),
  ("Родня прислала коробку игрушек «от наших выросших вашим растущим».", "Family sent a box of toys “from our grown-ups to your growing-ups”."),
  ("Коробка игрушек, «от наших выросших вашим растущим». Машинки, кубики, медведь без уха. Медведь без уха — самый любимый будет, увидите.",
   "A box of toys “from our grown-ups to your growing-ups”. Toy cars, blocks, a bear with one ear. The one-eared bear will be the favourite, you'll see."))
F("family", ("Сестра, Иваново", "A sister in Ivanovo"),
  ("Сестра просит взять племянников на лето.", "A sister asks if the nephews can come for the summer."),
  ("Сестра просит взять на лето племянников. Двоих! «Они тихие». Тихие — это она про чужих детей пишет. Ладно. Будет у нас лагерь.",
   "My sister asks if we'll take the nephews for the summer. Both! “They're quiet.” Quiet: she must be thinking of someone else's children. All right. We'll run a summer camp."))
F("family", ("Родня, Тамбов", "Family in Tambov"),
  ("Зовут на золотую свадьбу: пятьдесят лет вместе.", "An invitation to a golden wedding: fifty years together."),
  ("Золотая свадьба у родни — пятьдесят лет вместе! «Приезжайте, будем танцевать». В приглашении фото: им по двадцать, оба в кепках. Танцевать будем обязательно.",
   "A golden wedding in the family, fifty years together! “Come, we'll dance.” A photo in the invitation: both twenty, both in caps. We'll dance, all right."))
F("family", ("Семейная газета", "The family newspaper"),
  ("Пришёл свежий выпуск рукописной семейной газеты.", "A new issue of the handwritten family newspaper arrived."),
  ("Родня выпускает семейную газету — раз в полгода, от руки, на четырёх листах. Рубрики: «Кто родился», «Кто женился», «Кто наловил». В «Кто наловил» опять дядя Гена. Монополист.",
   "The family puts out a newspaper twice a year, handwritten, four pages. Sections: Who Was Born, Who Got Married, Who Caught What. Uncle Gena's in Who Caught What again. A monopoly."))
F("family", ("Родня, Москва", "Family in Moscow"),
  ("Из Москвы прислали детский велосипед в разобранном виде.", "A flat-packed child's bicycle arrived from Moscow."),
  ("Детский велосипед, разобранный, в коробке. Инструкция по-китайски. Соберём! А лишние детали — в хозяйстве пригодятся. Лишние детали всегда бывают.",
   "A child's bicycle, flat-packed in a box. Instructions in Chinese. We'll build it! And the spare parts will come in handy. There are always spare parts."))
F("family", ("Родители", "Parents"),
  ("Родители продали старый дом и прислали последнюю фотографию.", "Parents sold the old house and sent one last photo."),
  ("Родители продали старый дом, прислали последнюю фотографию: крыльцо, сирень, качели. Грустно. Зато качели забрали — пишут, привезут нам. Качели будут жить тут.",
   "My parents sold the old house and sent a last photo: the porch, the lilac, the swing. Sad. But they took the swing, and they're bringing it here. The swing will live with us now."))
F("family", ("Дядя-часовщик", "An uncle who mends clocks"),
  ("Дядя-часовщик предлагает посмотреть домашние ходики.", "An uncle who mends clocks offers to look at the wall clock."),
  ("Дядя пишет: «Привезите ваши ходики, посмотрю». Ходики у нас идут. Отстают на полчаса, но идут. Мы к ним привыкли — живём на полчаса медленнее. Это даже хорошо.",
   "My uncle writes, “Bring me your wall clock and I'll look at it.” Our clock works. It's half an hour slow, but it works. We're used to it: we live half an hour slower. Not a bad thing."))
F("family", ("Брат, Мурманск", "A brother in Murmansk"),
  ("Брат из Мурманска прислал печень трески — «чтоб все были крепкие».", "A brother in Murmansk sent cod liver, “to keep everyone strong”."),
  ("Брат прислал три банки печени трески и записку: «Чтоб все были крепкие». Будем крепкие. На бутерброде.",
   "My brother sent three tins of cod liver and a note: “To keep you all strong.” We'll be strong. On toast."))
F("family", ("Сестра, Вологда", "A sister in Vologda"),
  ("Племянник сделал первые шаги — прислали фото.", "A nephew took his first steps; a photo came."),
  ("Племянник пошёл! Фото: стоит, руки в стороны, лицо такое, будто сам удивился. Восемь шагов, пишут. Вы вон тысячи в день, а у него восемь — и все главные.",
   "My nephew's walking! A photo: standing, arms out, looking surprised at himself. Eight steps, they write. You do thousands a day, and he's done eight, every one of them important."))
F("family", ("Родня, Калуга", "Family in Kaluga"),
  ("Родня собирается в гости и прислала список «что привезти».", "Family are coming to stay and sent a list of what to bring."),
  ("Родня едет в гости. Прислали список: «Что вам привезти?» — и сами же ответили: «Привезём всё». Значит, в сарае место освобождать.",
   "Family are coming to stay. They sent a list: “What shall we bring?” And answered it themselves: “We'll bring everything.” Time to clear space in the shed."))
F("family", ("Сваты, Геленджик", "The in-laws, Gelendzhik"),
  ("Сваты зовут всех на море — «палатка большая».", "The in-laws invite everyone to the seaside: “the tent is big”."),
  ("Сваты зовут на море, в Геленджик: «Места хватит всем, палатка большая». Палатка! Всем! Это сколько ж нас в палатке будет… Весело будет.",
   "The in-laws invite us to the sea at Gelendzhik: “Room for everyone, the tent's big.” A tent! For everyone! How many of us would that be in a tent… It'll be fun."))
F("family", ("Родня, Нижний Новгород", "Family in Nizhny Novgorod"),
  ("Родня подарила мультиварку — «чтоб меньше у печки стоять».", "Family sent a slow cooker, “so you spend less time at the stove”."),
  ("Мультиварка! Подарок от родни: «Чтоб меньше у печки стоять». Поставим рядом с печкой. Пусть знакомятся. Подружатся — посмотрим.",
   "A slow cooker! A present from the family: “So you spend less time at the stove.” We'll put it next to the stove. Let them get acquainted. We'll see if they make friends."))
F("family", ("Племянница, Тверь", "A niece in Tver"),
  ("Племянница нарисовала всю семью — кот в короне.", "A niece drew the whole family, with the cat in a crown."),
  ("Племянница нарисовала всю нашу семью. Все с улыбками до ушей, а кот — в короне. Сразу видно, кто тут главный.",
   "My niece drew our whole family. Everyone grinning ear to ear, and the cat wearing a crown. Clear who's in charge."))
F("family", ("Мама", "Mum"),
  ("Мама прислала шесть банок вишни, каждая подписана.", "Mum sent six jars of cherries, each one labelled."),
  ("Мама прислала варенье, шесть банок, и каждая подписана: «Вишня, на каждый день», «Вишня, для пирогов», «Вишня, если гости». Есть, значит, особая вишня для гостей. Вам — её.",
   "Mum sent jam, six jars, each labelled: “Cherry, everyday”, “Cherry, for pies”, “Cherry, if guests come”. So there's a special cherry for guests. That one's yours."))
F("family", ("Брат, Пермь", "A brother in Perm"),
  ("Брат завёл огромную собаку, которая ест тапки.", "A brother got a huge dog that eats slippers."),
  ("Брат завёл собаку: «Огромная, добрая, ест всё, включая мой тапок». Фото: собака лежит на диване, брат — на табуретке. Расстановка сил понятна.",
   "My brother got a dog: “Huge, kind, eats everything including my slipper.” Photo: the dog on the sofa, my brother on a stool. The balance of power is clear."))
F("family", ("Двоюродная сестра, Владимир", "A cousin in Vladimir"),
  ("Двоюродная сестра защитила диплом и прислала фото в мантии.", "A cousin graduated and sent a photo in her gown."),
  ("Двоюродная сестра защитила диплом! Фото в мантии и квадратной шапке. Шапку она, видно, впервые держит — как торт.",
   "My cousin has graduated! A photo in a gown and a square cap. She's obviously never held one before; she's holding it like a cake."))
F("family", ("Родители, Подмосковье", "Parents outside Moscow"),
  ("Родители записались на бальные танцы и прислали фото.", "Parents have taken up ballroom dancing and sent a photo."),
  ("Родители записались на бальные танцы! Фото: папа в бабочке, мама в блёстках. Папа сосредоточен — считает такты. Мама смеётся — видно, он опять сбился.",
   "My parents have taken up ballroom dancing! Photo: Dad in a bow tie, Mum in sequins. Dad's concentrating, counting the beats. Mum's laughing; he's lost count again."))
F("family", ("Мама", "Mum"),
  ("Мама разобрала антресоли и прислала коробку детских фотографий.", "Mum cleared the top shelves and sent a box of childhood photos."),
  ("Мама разбирала антресоли и прислала коробку старых фотографий. Тут кто-то в три года в ванночке — зачем это слать по почте?! Вы ведь не смотрели? Ну и хорошо.",
   "Mum cleared out the top cupboards and sent a box of old photos. Someone aged three in a baby bath, why post that?! You didn't look, did you? Good."))
F("family", ("Тётя, Курск", "An aunt in Kursk"),
  ("Тётя прислала посылку, где каждая вещь завёрнута с яблоком.", "An aunt sent a parcel with an apple wrapped in every item."),
  ("Посылка от тёти: в каждую вещь завёрнуто по яблоку. Свитер — с яблоком, носки — с яблоком. «Чтоб не помялось». Теперь всё пахнет садом.",
   "A parcel from my aunt: an apple wrapped inside every item. An apple in the jumper, an apple in the socks. “So nothing gets crushed.” Now everything smells of an orchard."))
F("family", ("Мама и тётя", "Mum and an aunt"),
  ("Мама и тётя прислали два рецепта одного пирога — и спорят.", "Mum and an aunt each sent a recipe for the same pie, and disagree."),
  ("Мама и тётя прислали два рецепта одного пирога, и каждая пишет: «Тот рецепт не слушай». Будем печь оба. А они пусть спорят дальше.",
   "Mum and my aunt each sent a recipe for the same pie, and each one writes, “Don't listen to the other one.” We'll bake both. Let them keep arguing."))
F("family", ("Родня, Тамбов", "Family in Tambov"),
  ("Зовут на семейный сбор — «привозите табуретки».", "An invitation to a family reunion: “bring your own stools”."),
  ("Семейный сбор летом, у деда под Тамбовом. «Будет сорок человек, привозите табуретки». Свои табуретки! Видно, учли прошлый раз.",
   "A family reunion this summer at Grandad's near Tambov. “Forty people coming, bring stools.” Bring your own stools! They've learnt from last time."))
F("family", ("Племянник, Курган", "A nephew in Kurgan"),
  ("Племянник просит помочь с сочинением «Как я провёл лето».", "A nephew asks for help with an essay, How I Spent My Summer."),
  ("Племянник просит помочь с сочинением «Как я провёл лето»: «Своё не помню, расскажите ваше». Расскажем! Только он потом пятёрку получит за наше лето.",
   "My nephew wants help with an essay, How I Spent My Summer: “I don't remember mine, tell me yours.” We will! Only then he'll get top marks for our summer."))
F("family", ("Сестра", "A sister"),
  ("Сестра прислала первую прядку волос своего малыша.", "A sister sent her baby's first lock of hair."),
  ("Сестра прислала прядку волос малыша — первую, в конвертике с ленточкой. Мягкие, как пух одуванчика. Пусть лежит в шкатулке, к остальным сокровищам.",
   "My sister sent her baby's first lock of hair, in a tiny envelope with a ribbon. Soft as dandelion fluff. It'll go in the little box with the other treasures."))
F("family", ("Сваты, Брянск", "The in-laws in Bryansk"),
  ("Сваты прислали почтой мешок картошки.", "The in-laws sent a sack of potatoes by post."),
  ("Сваты прислали картошки мешок. Почтой! Как будто у нас своей нет. Ну, своя — своя, а сватова — сватова. Будем сравнивать.",
   "The in-laws sent a sack of potatoes. By post! As if we had none. Well, ours are ours and theirs are theirs. We'll compare."))
F("family", ("Родня, Иваново", "Family in Ivanovo"),
  ("Родня делает ремонт и просит выбрать обои.", "Family are redecorating and want help choosing wallpaper."),
  ("Родня делает ремонт, прислали образцы обоев: «Выберите вы, у вас вкус». Вкус! Ну всё. Выбираем вон те, с птицами.",
   "Family are redecorating and sent wallpaper samples: “You choose, you have taste.” Taste! Right. We choose the one with birds."))
F("family", ("Родня, Барнаул", "Family in Barnaul"),
  ("Родня прислала фото с Алтая — все в одинаковых панамках.", "Family sent Altai photos, everyone in identical sun hats."),
  ("Родня была на Алтае: горы, река бирюзовая, а они все в одинаковых панамках. Панамки, видно, на месте купили. Уж очень одинаковые. Не перепутались бы.",
   "Family went to the Altai: mountains, a turquoise river, and all of them in identical sun hats. Bought on the spot, I expect. Very identical. Hope they didn't mix each other up."))
F("family", ("Сваты, Смоленск", "The in-laws in Smolensk"),
  ("Сваты прислали льняную скатерть и рушник.", "The in-laws sent a linen tablecloth and an embroidered towel."),
  ("Сваты прислали лён: скатерть и рушник с петухами. Петухи красные, гордые, смотрят друг на друга, как наши соседские. Повесим у печки — пусть там спорят.",
   "The in-laws sent linen: a tablecloth and a towel embroidered with cockerels. Red, proud cockerels glaring at each other like our neighbours'. It'll hang by the stove; they can argue there."))
F("family", ("Родители", "Parents"),
  ("Родители прислали старый фотоаппарат «Зенит».", "Parents sent an old Zenit camera."),
  ("Папа прислал свой «Зенит» и плёнку: «Снимай своих, пока маленькие». Снимать будем всех — и маленьких, и больших, и кота. Кот самый фотогеничный.",
   "Dad sent his old Zenit camera and a roll of film: “Take pictures of your lot while they're little.” We'll photograph everyone, little and big, and the cat. The cat's the most photogenic."))
F("family", ("Брат, Мурманск", "A brother in Murmansk"),
  ("Брат обещает приехать летом — «если отпустят».", "A brother promises to come in summer, “if they let me go”."),
  ("Брат пишет: «Летом приеду, если отпустят». Каждый год пишет «если отпустят». Кто его держит — непонятно. Кажется, рыба.",
   "My brother writes, “I'll come in summer if they let me go.” He writes “if they let me go” every year. Who's holding him, nobody knows. The fish, I think."))
F("family", ("Тётя, Пенза", "An aunt in Penza"),
  ("Тётя прислала деньги «на мороженое детям» — сто рублей.", "An aunt sent a hundred roubles “for the children's ice cream”."),
  ("Тётя прислала сто рублей, «на мороженое детям». Мороженое нынче дороже, но тётя считает по-старому. Ничего. Добавим — и купим всем, и себе тоже.",
   "My aunt sent a hundred roubles “for the children's ice cream”. Ice cream costs more these days, but she counts the old way. Never mind. We'll add a bit and buy some for everyone, ourselves included."))
F("family", ("Родня, Орёл", "Family in Oryol"),
  ("Родня прислала семейную реликвию — бабушкину швейную машинку.", "Family sent an heirloom: Gran's sewing machine."),
  ("Бабушкину швейную машинку прислали, «Зингер», с ножным приводом. Тяжёлая — вы-то как донесли? Вот это работа. Машинка ещё шьёт. Сто лет, а шьёт.",
   "They sent Gran's sewing machine, a Singer with a treadle. It's heavy, how did you carry it? Now that's work. The machine still sews. A hundred years old and it sews."))
F("family", ("Двоюродный брат, Сургут", "A cousin in Surgut"),
  ("Двоюродный брат прислал фото: его сын поймал первую рыбу.", "A cousin sent a photo: his son caught his first fish."),
  ("Двоюродный брат прислал фото: сынишка поймал первую рыбу. Рыба с ладошку, а гордости — на кита. Рыбу, пишут, отпустили. Сын говорит: «Пусть растёт, потом ещё поймаю».",
   "My cousin sent a photo: his little boy caught his first fish. A fish the size of a palm and pride the size of a whale. They let it go, he writes. The boy said, “Let it grow, I'll catch it again later.”"))
F("family", ("Родители", "Parents"),
  ("Родители прислали посылку с банками — и с подушкой.", "Parents sent a parcel of jars, padded with a pillow."),
  ("Родители прислали банки с соленьями, а чтобы не побились — обложили подушкой. Подушкой! Теперь у нас огурцы и ещё одна подушка. Мама всё продумала.",
   "My parents sent jars of pickles and padded them with a pillow so they wouldn't break. A pillow! Now we have pickles and an extra pillow. Mum thought of everything."))
F("family", ("Родня, Саратов", "Family in Saratov"),
  ("Родня решила раз в месяц писать бумажные письма — «вместо чата».", "The family decided to write paper letters once a month, “instead of the chat”."),
  ("Родня решила: раз в месяц все пишут бумажные письма — «вместо чата». Первое письмо — от самой младшей, три строчки и рисунок. Лучше любого чата. Ответим длинно.",
   "The family's decided everyone writes a paper letter once a month “instead of the group chat”. The first is from the youngest: three lines and a drawing. Better than any chat. We'll write back at length."))
F("family", ("Сестра, Тула", "A sister in Tula"),
  ("Сестра прислала детские вещи племянников — «вашим пригодится».", "A sister sent the nephews' outgrown clothes, “for yours”."),
  ("Сестра прислала мешок детских вещей: «Нашим мало, вашим пригодится». Комбинезон, валенки, шапка с помпоном. На помпоне — следы чьих-то зубов. Семейная традиция.",
   "My sister sent a bag of children's clothes: “Ours have outgrown them, yours will use them.” A snowsuit, felt boots, a bobble hat. There are tooth marks on the bobble. A family tradition."))
F("family", ("Дедушка, Кострома", "Grandad in Kostroma"),
  ("Дедушка прислал письмо в три строчки — зато каких.", "Grandad sent a three-line letter, but what a letter."),
  ("Дед пишет раз в год, три строчки: «Жив. Здоров. Скучаю». Каждый год одно и то же. А читаешь — и будто обнял.",
   "Grandad writes once a year, three lines: “Alive. Well. Missing you.” The same every year. And reading it feels like a hug."))
F("family", ("Родня, Владимир", "Family in Vladimir"),
  ("Родня прислала календарь с семейными фотографиями на каждый месяц.", "Family sent a calendar with a family photo for every month."),
  ("Календарь с семейными фотографиями, на каждый месяц своя. Январь — все на санках, июль — все в реке, а ноябрь — один кот. Видно, в ноябре больше никто не позировал.",
   "A calendar with a family photo for each month. January: everyone on sledges. July: everyone in the river. November: just the cat. Nobody else would pose in November, I suppose."))
F("family", ("Сваты, Тверь", "The in-laws in Tver"),
  ("Сваты прислали рассаду клубники в коробке из-под обуви.", "The in-laws sent strawberry plants in a shoebox."),
  ("Клубничные усы в коробке из-под ботинок, с мокрой газеткой. «Наш сорт, без названия, очень сладкий». Без названия — значит, назовём сами. Будет «Сватовская».",
   "Strawberry runners in a shoebox with wet newspaper. “Our own variety, no name, very sweet.” No name, so we'll name it. It'll be the In-Law Strawberry."))


# --------------------------------------------------------------------------- fillers: children
F("child", ("Друг по переписке, Калининград", "A pen-pal in Kaliningrad"),
  ("Из Калининграда ребёнку прислали кусочек янтаря.", "A child got a piece of amber from Kaliningrad."),
  ("Мне пишут из Калининграда! Прислали янтарик, маленький, а внутри — пузырик воздуха. Ему, наверное, сто миллионов лет. Пузырику! А он как новенький.",
   "Someone wrote to me from Kaliningrad! They sent a little piece of amber with an air bubble inside. It's probably a hundred million years old. The bubble! And it looks brand new."))
F("child", ("Двоюродный брат", "A cousin"),
  ("Двоюродный брат прислал рисунок: динозавр ест мороженое.", "A cousin sent a drawing of a dinosaur eating ice cream."),
  ("Брат двоюродный прислал рисунок: динозавр ест мороженое. Подписал: «Это я». Ну, похож. Особенно мороженое.",
   "My cousin sent a drawing: a dinosaur eating ice cream. He wrote “This is me” on it. Well, it looks like him. Especially the ice cream."))
F("child", ("Конкурс «Весёлая каша»", "The Happy Porridge contest"),
  ("Ребёнку пришёл приз за конкурс с коробки каши — наклейки с планетами.", "A child won a cereal-box contest: planet stickers."),
  ("Приз за конкурс с коробки каши! Наклейки с планетами! Сатурн наклею на кровать. А Землю — на окно, чтобы было видно, где мы.",
   "A prize from the porridge-box contest! Planet stickers! Saturn's going on my bed. And Earth on the window, so you can see where we are."))
F("child", ("Зоопарк, Ярославль", "Yaroslavl Zoo"),
  ("Зоопарк ответил на детский рисунок жирафа.", "A zoo replied to a child's drawing of a giraffe."),
  ("Зоопарк ответил на мой рисунок жирафа! Пишут: «Жирафу понравилось». Они ему показывали! Жираф видел мой рисунок! Он, наверное, наклонился.",
   "The zoo answered about my giraffe drawing! They wrote, “The giraffe liked it.” They showed it to him! The giraffe saw my drawing! He must have bent down."))
F("child", ("Бабушка", "Gran"),
  ("Бабушка прислала семечки подсолнуха — кто вырастет выше.", "Gran sent sunflower seeds: who'll grow taller?"),
  ("Бабушка прислала семечки и пишет: «Посади, посмотрим, кто вырастет выше — ты или подсолнух». Подсолнух, наверное. Он быстрее растёт. Но я дольше.",
   "Gran sent sunflower seeds and wrote, “Plant them and we'll see who grows taller, you or the sunflower.” The sunflower, probably. It grows faster. But I grow longer."))
F("child", ("Тётя", "An aunt"),
  ("Тётя прислала книжку загадок.", "An aunt sent a riddle book."),
  ("Книжка загадок! Вот: «Сидит дед, во сто шуб одет, кто его раздевает, тот слёзы проливает». Это лук! Я знаю. А вы знали? Знали. Все знают. Но всё равно смешно.",
   "A riddle book! Here: “An old man in a hundred coats; whoever undresses him sheds tears.” It's an onion! I know it. Did you know? You did. Everyone does. It's still funny."))
F("child", ("Друг из Москвы", "A friend in Moscow"),
  ("Из Москвы пришла открытка с пандой.", "A postcard with a panda came from Moscow."),
  ("Открытка с пандой! Панда ест бамбук и смотрит так, будто её застукали. Я так же смотрю, когда меня с вареньем застукают.",
   "A card with a panda! The panda's eating bamboo and looking as if it's been caught. That's how I look when I'm caught with the jam."))
F("child", ("Двоюродный брат", "A cousin"),
  ("Двоюродному брату за выпавший зуб дали монетку. Здесь — нет.", "A cousin got a coin for a lost tooth. Not here."),
  ("Брат пишет: у него выпал зуб, он положил его под подушку, а утром там — монетка! А у меня два выпали, и ничего… Надо было под подушку. Теперь буду знать.",
   "My cousin writes that his tooth fell out, he put it under his pillow and in the morning there was a coin! Two of mine fell out and nothing… Should have used the pillow. I know now."))
F("child", ("Магазин «Юный химик»", "Young Chemist shop"),
  ("Пришла посылка — набор «Юный химик».", "A parcel came: a Young Chemist set."),
  ("Пришла моя посылка! «Юный химик»! Мама сказала — только с папой. Папа сказал — только с мамой. Будем, наверное, втроём. Так даже интереснее.",
   "My parcel came! A Young Chemist set! Mum said only with Dad. Dad said only with Mum. So all three of us, I suppose. That's even better."))
F("child", ("Детский журнал, редакция", "A children's magazine"),
  ("Детский журнал напечатает загадку из Липовки.", "A children's magazine will print a riddle from Lipovka."),
  ("Мне ответили из журнала! Мою загадку напечатают! Вот она: «Спит на письмах, ест сметану, ловит всё, кроме мышей». Догадались, про кого?",
   "The magazine wrote back! They're printing my riddle! Here it is: “Sleeps on letters, eats sour cream, catches everything except mice.” Guess who?"))
F("child", ("Друг по переписке", "A pen-pal"),
  ("Прислали схему, как сложить бумажного журавлика.", "Instructions came for folding a paper crane."),
  ("Прислали схему, как сложить журавлика. Вот, смотрите, журавлик! Ну, почти. Одно крыло больше. Он так поворачивает.",
   "They sent instructions for folding a crane. Look, a crane! Well, nearly. One wing's bigger. That's how he turns."))
F("child", ("Бабушка", "Gran"),
  ("Бабушка связала шапку с кошачьими ушками.", "Gran knitted a hat with cat ears."),
  ("Бабушка связала шапку с ушками, как у кота! Теперь я кот. Мяу! Это значит — спасибо, что принесли.",
   "Gran knitted a hat with ears like a cat's! Now I'm a cat. Miaow! That means thank you for bringing it."))
F("child", ("Друг из лагеря", "A friend from summer camp"),
  ("Пишет друг из летнего лагеря — вспоминает ночного ежа.", "A friend from summer camp writes, remembering the night-time hedgehog."),
  ("Друг из летнего лагеря пишет! Помнит, как мы ночью ходили смотреть на ежа. Ёж тоже, наверное, помнит. Он так пыхтел!",
   "A friend from summer camp wrote! He remembers when we sneaked out at night to see the hedgehog. The hedgehog probably remembers too. He huffed so much!"))
F("child", ("Дядя", "An uncle"),
  ("Дядя прислал настоящую лупу.", "An uncle sent a real magnifying glass."),
  ("Настоящая лупа! Теперь всё видно: у муравья ноги, у листика жилки, у вас на сумке — ниточка. Хотите, отрежу? Нет? Ладно.",
   "A real magnifying glass! Now I can see everything: an ant's legs, a leaf's veins, a thread on your bag. Shall I cut it off? No? All right."))
F("child", ("Друг по переписке, Казахстан", "A pen-pal in Kazakhstan"),
  ("Мальчик из Казахстана прислал рисунок верблюда.", "A boy in Kazakhstan sent a drawing of a camel."),
  ("Мальчик из Казахстана нарисовал верблюда. У верблюда два горба. Я ему нарисую нашу козу. У козы ни одного. Пусть удивится.",
   "A boy in Kazakhstan drew me a camel. The camel has two humps. I'll draw him our goat. The goat has none. That'll surprise him."))
F("child", ("Тётя", "An aunt"),
  ("Тётя прислала календарь со щенками.", "An aunt sent a calendar with puppies."),
  ("Календарь со щенками! На каждый месяц — новый щенок. Больше всех майский нравится. Он с бантиком. Жалко, что май один раз в году.",
   "A puppy calendar! A new puppy every month. I like May's best. He's got a bow. Shame May only comes once a year."))
F("child", ("Дедушка", "Grandad"),
  ("Дедушка прислал книжку про космос.", "Grandad sent a book about space."),
  ("Книжка про космос! Тут написано, что на Венере день длиннее года. Значит, там день рождения бывает раньше, чем вечер. Здорово же!",
   "A book about space! It says a day on Venus is longer than a year. So your birthday comes round before it's even evening. Brilliant!"))
F("child", ("Школа, Архангельск", "A school in Arkhangelsk"),
  ("Целый класс из Архангельска спрашивает, есть ли тут медведи.", "A whole class in Arkhangelsk asks if there are bears here."),
  ("Нам пишет целый класс из Архангельска! Спрашивают, есть ли у нас медведи. Есть! В лесу. И у меня — плюшевый. Напишу про обоих.",
   "A whole class in Arkhangelsk wrote to us! They ask if we have bears. We do! In the forest. And I've got a teddy one. I'll write about both."))
F("child", ("Тётя", "An aunt"),
  ("Тётя прислала калейдоскоп.", "An aunt sent a kaleidoscope."),
  ("Калейдоскоп! Поворачиваешь — и каждый раз новый узор, и такого больше никогда не будет. Жалко. Но и хорошо. Вот, посмотрите, пока он есть!",
   "A kaleidoscope! Every turn there's a new pattern, and that one will never come again. A shame. But nice too. Here, look quick while it's there!"))
F("child", ("Друг", "A friend"),
  ("Пришла открытка с Котом в сапогах.", "A postcard of Puss in Boots arrived."),
  ("Открытка с Котом в сапогах! Сапоги красные. Если бы у Сургуча были сапоги, он бы в них спал.",
   "A Puss in Boots card! Red boots. If Surguch had boots he'd sleep in them."))
F("child", ("Дедушка", "Grandad"),
  ("Дедушка прислал карту клада, зарытого в детстве.", "Grandad sent a map of treasure he buried as a boy."),
  ("Дедушка прислал карту — где он в детстве закопал клад! Под старой яблоней, три шага от забора. Яблоня у нас есть! Мама говорит — сначала уроки. Уроки — это не клад.",
   "Grandad sent a map of where he buried treasure when he was little! Under the old apple tree, three steps from the fence. We've got an apple tree! Mum says homework first. Homework isn't treasure."))
F("child", ("Тётя", "An aunt"),
  ("Тётя прислала набор печатей — «своя почта».", "An aunt sent a set of rubber stamps, “your own post office”."),
  ("Набор печаток! Теперь у меня своя почта. Буду ставить штампы на все письма. Можно и вам на руку? Маленький, кошечку.",
   "A set of rubber stamps! Now I've got my own post office. I'll stamp all my letters. Can I stamp your hand? A little one, a kitty."))
F("child", ("Двоюродная сестра", "A cousin"),
  ("Прислали инструкцию, как сделать телефон из баночек.", "Instructions came for a tin-can telephone."),
  ("Двоюродная сестра прислала, как сделать телефон из двух баночек и нитки. Будем звонить с крыльца на крыльцо! Алло! Почта? Вы меня слышите?",
   "My cousin sent instructions for a telephone made of two tins and a string. We'll ring from porch to porch! Hello! Post office? Can you hear me?"))
F("child", ("Друзья из Крыма", "Friends in Crimea"),
  ("Ребёнку прислали ракушку, в которой шумит море.", "A child was sent a shell that holds the sound of the sea."),
  ("Ракушка! Если приложить к уху, шумит море. Послушайте! Ну что? Шумит? Шумит! Значит, море теперь у нас.",
   "A shell! Hold it to your ear and you can hear the sea. Listen! Well? Can you hear it? You can! So now the sea is ours."))
F("child", ("Брат, Москва", "A cousin in Moscow"),
  ("Брат из Москвы спрашивает, что делать в деревне без торгового центра.", "A cousin in Moscow asks what anyone does in a village without a shopping centre."),
  ("Брат из Москвы спрашивает: «Чем вы там занимаетесь без торгового центра?» Мы на плоту катаемся, в шалаше живём, козу пасём и лягушек ловим. Ему завидно будет.",
   "My cousin in Moscow asks, “What do you even do without a shopping centre?” We ride on a raft, live in a den, mind the goat and catch frogs. He'll be jealous."))
F("child", ("Бабушка", "Gran"),
  ("Бабушка прислала носки с динозаврами.", "Gran sent socks with dinosaurs on."),
  ("Носки с динозаврами! Левый динозавр рычит, а правый — нет. Правый, наверное, добрый. Или спит.",
   "Dinosaur socks! The left dinosaur's roaring and the right one isn't. The right one must be friendly. Or asleep."))
F("child", ("Маленький кузен", "A little cousin"),
  ("Малыш, который ещё не умеет писать, прислал письмо-рисунок.", "A toddler who can't write yet sent a letter in pictures."),
  ("Письмо от малыша, двоюродного. Писать он ещё не умеет, поэтому нарисовал. Тут солнце, тут я, а тут — не знаю что. Надо спросить. Он, наверное, тоже не знает.",
   "A letter from my little cousin. He can't write yet, so he drew it. Here's the sun, here's me, and here's — I don't know what. I'll ask. He probably doesn't know either."))
F("child", ("Тётя, Москва", "An aunt in Moscow"),
  ("Тётя прислала коробку из сорока восьми карандашей.", "An aunt sent a box of forty-eight pencils."),
  ("Сорок восемь карандашей! Тут даже «серебряный» и «золотой». Золотым нарисую Сургуча. Он рыжий, почти золотой.",
   "Forty-eight pencils! There's even silver and gold. I'll draw Surguch in gold. He's ginger, nearly gold."))
F("child", ("Планетарий, Москва", "The Moscow Planetarium"),
  ("Планетарий ответил на детский вопрос о жизни на Луне.", "The planetarium answered a child's question about living on the Moon."),
  ("Мне ответили из планетария! Вопрос был: можно ли жить на Луне. Ответ: «Пока нельзя, но готовься». Готовлюсь! Уже ем кашу.",
   "The planetarium wrote back! The question was: can you live on the Moon? The answer: “Not yet, but get ready.” I'm getting ready! I'm already eating my porridge."))
F("child", ("Двоюродная сестра", "A cousin"),
  ("Прислали фото с линейки: у двоюродной сестры огромные банты.", "A photo from school assembly: a cousin with enormous bows."),
  ("Фото с линейки: двоюродная сестра с бантами. Банты такие, что её саму почти не видно. Мама говорит, в первом классе у меня были такие же. Не помню. Наверное, тоже не было видно.",
   "A photo from the school assembly: my cousin with bows. The bows are so big you can hardly see her. Mum says I had bows like that in first grade. I don't remember. Probably couldn't see out."))
F("child", ("Двоюродный брат", "A cousin"),
  ("Двоюродный брат прислал письмо шифром.", "A cousin sent a letter in code."),
  ("Письмо шифром! Тут цифры вместо букв. Сейчас… три, один… Ой, это долго. Вы идите, я потом расскажу!",
   "A letter in code! Numbers instead of letters. Wait… three, one… Oh, this'll take ages. You go on, I'll tell you later!"))
F("child", ("Бабушка", "Gran"),
  ("Бабушка прислала семена гороха — для окна.", "Gran sent pea seeds to grow on the windowsill."),
  ("Бабушка прислала горох — посадить в стаканчик на окне. Пишет: «Будет у тебя свой огород, маленький». Маленький огород! На подоконнике! Козы не достанут.",
   "Gran sent peas to plant in a cup on the windowsill. She writes, “You'll have your own garden, a little one.” A little garden! On the windowsill! The goats can't get it."))
F("child", ("Друг по переписке, Мурманск", "A pen-pal in Murmansk"),
  ("Мальчик из Мурманска пишет про полярную ночь.", "A boy in Murmansk writes about the polar night."),
  ("Мальчик из Мурманска пишет, что у них зимой солнца совсем нет, целый месяц! Ходят в школу ночью. Ночью в школу! А у нас солнце каждый день. Пошлю ему рисунок солнца, пусть повесит.",
   "A boy in Murmansk writes that in winter they get no sun at all for a whole month! They go to school in the dark. School at night! And we have sun every day. I'll send him a drawing of the sun to put on his wall."))
F("child", ("Тётя", "An aunt"),
  ("Тётя прислала скакалку со счётчиком прыжков.", "An aunt sent a skipping rope that counts the jumps."),
  ("Скакалка со счётчиком! Сама считает прыжки. Вот: раз, два, три… сорок! А у вас тоже счётчик, только на шаги. Давайте соревноваться! Ой, у вас же больше.",
   "A skipping rope with a counter! It counts your jumps by itself. Look: one, two, three… forty! You've got a counter too, for steps. Let's have a race! Oh. You've got more."))
F("child", ("Детская библиотека, Городок", "Gorodok children's library"),
  ("Детская библиотека прислала грамоту «Самому читающему».", "The children's library sent a certificate “To Our Keenest Reader”."),
  ("Грамота из библиотеки! «Самому читающему читателю». Это за двадцать две книжки за лето. Двадцать третью я дочитаю сегодня. Пусть дописывают!",
   "A certificate from the library! “To Our Keenest Reader.” That's for twenty-two books over the summer. I'll finish the twenty-third today. They'll have to change the number!"))
F("child", ("Друг по переписке, Сочи", "A pen-pal in Sochi"),
  ("Друг из Сочи прислал фото медузы — «не трогай».", "A pen-pal in Sochi sent a photo of a jellyfish: “don't touch”."),
  ("Из Сочи фото медузы. Прозрачная, как кисель! Подпись: «Не трогай, щиплется». Я и не трогаю. Она же на фотографии. Но всё равно не трогаю — на всякий случай.",
   "A jellyfish photo from Sochi. See-through, like jelly! Caption: “Don't touch, it stings.” I'm not touching. It's a photo. But I'm still not touching, just in case."))


# --------------------------------------------------------------------------- fillers: anyone
F("any", ("Без подписи", "No signature"),
  ("Пришла открытка без подписи: кот и луна.", "A card with no signature: a cat and the moon."),
  ("Открытка без подписи. Только рисунок: кот сидит на крыше и смотрит на луну. Кто бы это? Ох, будем гадать всю неделю. Это даже лучше, чем знать.",
   "A card with no signature. Just a drawing: a cat on a roof looking at the moon. Who could it be? We'll be guessing all week. That's better than knowing."))
F("any", ("Дом культуры, Городок", "House of Culture, Gorodok"),
  ("Листовка: в Городке концерт духового оркестра.", "A leaflet: a brass band concert in Gorodok."),
  ("Концерт духового оркестра в Городке! Трубы, барабан, медные тарелки, как блины. Надо ехать. Духовой оркестр — это как праздник, который сам к тебе идёт.",
   "A brass band concert in Gorodok! Trumpets, a big drum, brass cymbals like pancakes. Must go. A brass band is a holiday that marches right up to you."))
F("any", ("«Окна навсегда»", "Windows Forever Ltd"),
  ("Реклама пластиковых окон — в печку.", "An advert for plastic windows went into the stove."),
  ("Реклама пластиковых окон. А у нас деревянные, с наличниками, их никакой пластик не переглядит. Листовку — на растопку. Хоть какая-то от неё польза.",
   "An advert for plastic windows. Ours are wooden with carved frames; no plastic can outstare them. The leaflet's for kindling. At least it'll be some use."))
F("any", ("Магазин «Хозтовары»", "The hardware shop"),
  ("Бесплатный лотерейный билет от магазина: главный приз — чайник.", "A free lottery ticket from a shop: first prize is a kettle."),
  ("Лотерейный билет, «бесплатный, от магазина». Главный приз — чайник. Чайник у нас есть. Но второй не помешает: один для чая, другой — для компании.",
   "A lottery ticket, “free from the shop”. First prize: a kettle. We've got a kettle. But a second wouldn't hurt: one for tea, one for company."))
F("any", ("Бюро находок, автостанция Городка", "Lost property, Gorodok bus station"),
  ("Бюро находок нашло перчатку, потерянную год назад.", "Lost property found a glove lost a year ago."),
  ("Из бюро находок пишут: нашлась перчатка, с вышитой буквой на манжете. Наша! Потеряли в автобусе в прошлом году. Год путешествовала — и вернулась. Вторая её ждёт.",
   "Lost property writes that they've found a glove with a letter stitched on the cuff. Ours! Lost on the bus last year. A year of travelling and it's coming home. Its twin has been waiting."))
F("any", ("Краеведческий музей, Городок", "Local history museum, Gorodok"),
  ("Музей собирает старые открытки для выставки.", "The museum is collecting old postcards for an exhibition."),
  ("Музей собирает старые открытки для выставки. Есть у нас такие? Есть! Целая коробка. Пусть посмотрят, как раньше поздравляли — с ангелочками и с ошибками.",
   "The museum's collecting old postcards for an exhibition. Have we got any? We have! A whole box. Let them see how people used to send greetings: with cherubs and spelling mistakes."))
F("any", ("Велосипедист, Иркутск", "A cyclist, Irkutsk"),
  ("Велосипедист, ночевавший тут на сеновале, доехал до Байкала.", "A cyclist who slept in a hayloft here made it to Baikal."),
  ("Открытка от велосипедиста, что прошлым летом ночевал на нашем сеновале. Доехал до Байкала! Пишет: «Ваш сеновал — лучшая гостиница на всём пути».",
   "A card from the cyclist who slept in our hayloft last summer. He made it to Baikal! He writes, “Your hayloft was the best hotel of the whole trip.”"))
F("any", ("Чайная компания", "A tea company"),
  ("Прислали бесплатный пробник чая — «оцените».", "A free tea sample came: “please rate it”."),
  ("Пробник чая, «бесплатно, оцените». Оценим! Одной заварки как раз на двоих. Садитесь — вместе и оценим.",
   "A free tea sample: “please give us your rating.” We will! One sachet is just enough for two. Sit down and we'll rate it together."))
F("any", ("Без обратного адреса", "No return address"),
  ("В конверте без единой строчки — пёстрое перо.", "An envelope with not a word in it, only a speckled feather."),
  ("В конверте перо. Длинное, пёстрое, сойкино, кажется. И ни строчки. Видно, кто-то знает, что слова тут лишние.",
   "A feather in the envelope. Long, speckled, a jay's, I think. Not a single line. Someone knows words aren't needed here."))
F("any", ("Районная библиотека", "District library"),
  ("Районная библиотека зовёт на «летнее чтение».", "The district library invites everyone to “summer reading”."),
  ("Библиотека напоминает: «Запишитесь на летнее чтение!» Летнее чтение — это в гамаке, с яблоком, пока не уснёшь. Записываемся.",
   "The library reminds us: “Sign up for summer reading!” Summer reading means a hammock, an apple and reading until you nod off. Count us in."))
F("any", ("Аптека «Здоровье», Городок", "Health Pharmacy, Gorodok"),
  ("Прислали карманный календарик с котёнком.", "A pocket calendar with a kitten arrived."),
  ("Карманный календарик с котёнком. Котёнок в корзинке, глаза — как пуговицы. Буду носить в кармане. Смотреть, какое число и какой котёнок.",
   "A pocket calendar with a kitten. A kitten in a basket with button eyes. I'll carry it in my pocket. To check the date and the kitten."))
F("any", ("Родные, с ошибкой", "Family, with a mistake"),
  ("Письмо пришло с перепутанной фамилией.", "A letter came with the surname muddled."),
  ("Письмо нам, а фамилия перепутана: вместо одной буквы — другая. Новая фамилия смешная, на «-ушкин». Но письмо наше, и почерк родной. Вы правильно принесли.",
   "The letter's for us, but the surname's muddled: one letter swapped for another. The new name's a funny one ending in “-ushkin”. But it's ours, and the handwriting is family. You brought it to the right place."))
F("any", ("Отправлено пять лет назад", "Posted five years ago"),
  ("Пришла открытка, отправленная пять лет назад.", "A card arrived that was posted five years ago."),
  ("Открытка пришла — штемпель пятилетней давности! Где ж она гуляла пять лет? Поздравляют с весной. Ну, весна-то опять будет. Вовремя пришла, выходит.",
   "A card's come with a postmark from five years ago! Where has it been wandering all this time? It wishes us a happy spring. Well, spring's coming round again. Right on time, then."))
F("any", ("Радиовикторина «Знаток»", "The Know-It radio quiz"),
  ("Радиовикторина прислала значок «Знатоку из Липовки».", "A radio quiz sent a badge “To the Know-It of Lipovka”."),
  ("Ответили правильно в радиовикторине — прислали значок и открытку: «Знатоку из Липовки». Знатоку! Повесим на видное место. Пусть все знают.",
   "We answered the radio quiz right and they sent a badge and a card: “To the Know-It of Lipovka.” Know-It! It's going somewhere everyone can see."))
F("any", ("Цирк-шапито", "The travelling circus"),
  ("Цирк приезжает в Городок — на афише слон.", "The circus is coming to Gorodok, with an elephant on the poster."),
  ("Цирк приезжает в Городок! На афише слон. Настоящий слон! В Городке! Как он там по мосту пройдёт? Надо ехать — хоть посмотреть, как пройдёт.",
   "The circus is coming to Gorodok! There's an elephant on the poster. A real elephant! In Gorodok! How will it get over the bridge? We'll have to go, if only to see that."))
F("any", ("«Сельская новь», редакция", "The Village News, the editors"),
  ("Газета благодарит за фото на конкурс «Моя Липовка».", "The newspaper thanks someone for their My Lipovka photo."),
  ("Газета благодарит за участие в фотоконкурсе «Моя Липовка». Фото — то, где туман над рекой и корова в тумане. Корова, пишут, больше всех понравилась жюри.",
   "The paper thanks us for entering the My Lipovka photo contest. It was the one with mist over the river and a cow in the mist. The jury liked the cow best, they say."))
F("any", ("Друзья, Чукотка", "Friends in Chukotka"),
  ("С Чукотки пришла открытка с моржом.", "A postcard with a walrus came from Chukotka."),
  ("С Чукотки открытка: морж на льдине, усы как у Деда Мороза. Подпись: «У нас всё спокойно, моржи передают привет». Передаём моржам ответный.",
   "A card from Chukotka: a walrus on an ice floe with a moustache like Ded Moroz. Caption: “All quiet here, the walruses send their regards.” We send ours back to the walruses."))
F("any", ("«Сад-огород», реклама", "Garden Supplies advert"),
  ("В рекламном конверте — пакетик семян васильков.", "A packet of cornflower seeds came in an advertising envelope."),
  ("В рекламном конверте — пакетик семян васильков. Реклама уйдёт в печку, а васильки — в землю. Вот это правильная реклама.",
   "A packet of cornflower seeds in an advertising envelope. The advert goes in the stove and the cornflowers go in the ground. Now that's proper advertising."))
F("any", ("Приют «Верный друг», Городок", "Faithful Friend dog shelter, Gorodok"),
  ("Приют для собак благодарит за старые одеяла.", "The dog shelter says thank you for old blankets."),
  ("Приют для собак благодарит за посылку с одеялами. Прислали фото: щенок спит на нашем старом пледе. Плед, выходит, счастливый. Он всегда такой был.",
   "The dog shelter thanks us for the parcel of blankets. They sent a photo: a puppy asleep on our old rug. It's a lucky rug, then. It always was."))
F("any", ("Без подписи", "No signature"),
  ("Открытка с сердечком и печатными буквами — без подписи.", "A card with a heart, in block capitals, unsigned."),
  ("Открытка с сердечком. Подписи нет, а написано печатными буквами — чтобы не узнали. Ну, узнаем. Не сразу, но узнаем.",
   "A card with a heart on it. No name, and written in block capitals so we won't know. Oh, we'll find out. Not straight away, but we will."))
F("any", ("Фольклорная экспедиция", "A folklore expedition"),
  ("Фольклористы приедут летом записывать частушки.", "Folklorists are coming in summer to record ditties."),
  ("Пишут фольклористы из университета: собирают частушки, летом приедут с магнитофоном. Частушки будут. Главное, чтобы магнитофон выдержал.",
   "Folklorists from the university write that they're collecting ditties and coming in summer with a recorder. We'll give them ditties. As long as the recorder can take it."))
F("any", ("Газета, отдел кроссвордов", "The newspaper's crossword desk"),
  ("За разгаданный кроссворд прислали набор открыток «Птицы России».", "A crossword prize: a set of Birds of Russia postcards."),
  ("Приз за кроссворд — открытки «Птицы России». Тут и снегирь, и иволга, и удод с хохолком. Можно всем родным разослать — по птице на каждого.",
   "A crossword prize: Birds of Russia postcards. A bullfinch, an oriole, a hoopoe with its crest. We can send them to all the family: a bird each."))
F("any", ("Картографическая фабрика", "The map factory"),
  ("Прислали новую карту района — Липовка на ней крошечная точка.", "A new district map came: Lipovka is a tiny dot."),
  ("Новая карта района. Липовка на ней есть — крошечная точка у реки. Точка, а сколько всего в этой точке. Ни одна карта не вместит.",
   "A new map of the district. Lipovka's on it, a tiny dot by the river. Just a dot, and look how much is in it. No map could hold it all."))
F("any", ("Туристы, Ярославль", "Hikers from Yaroslavl"),
  ("Туристы прислали фото двойной радуги над деревней.", "Hikers sent a photo of a double rainbow over the village."),
  ("Туристы, что летом шли через деревню, прислали фото: двойная радуга над нашей улицей. А мы и не видели — от дождя дома сидели. А она, оказывается, была.",
   "Hikers who came through the village last summer sent a photo: a double rainbow over our street. We never saw it, we were indoors hiding from the rain. And there it was all along."))
F("any", ("Клуб, Липовка", "The club, Lipovka"),
  ("Клуб зовёт на концерт самодеятельности с фокусником.", "The club invites everyone to an amateur concert, with a magician."),
  ("Концерт самодеятельности в клубе: песни, стихи и фокусник из Городка — тот, что в прошлый раз потерял кролика. Кролик, говорят, нашёлся. Интересно, найдётся ли снова.",
   "An amateur concert at the club: songs, poems, and the magician from Gorodok, the one who lost his rabbit last time. The rabbit turned up, they say. Wonder if it'll turn up again."))
F("any", ("Орнитологическая станция", "A bird-ringing station"),
  ("Орнитологи просят искать птиц с колечками.", "Ornithologists ask people to look out for ringed birds."),
  ("Орнитологи пишут: найдёте птицу с колечком на лапке — перепишите номер и пришлите. Будем смотреть на лапки. У всех птиц. Даже у кур, на всякий случай.",
   "Ornithologists write: if you find a bird with a ring on its leg, copy the number and send it in. We'll be checking legs. On every bird. Even the hens, just in case."))
F("any", ("Кинопередвижка", "The travelling cinema"),
  ("Кинопередвижка привезёт в клуб «Морозко».", "The travelling cinema is bringing Morozko to the club."),
  ("Кинопередвижка приедет в клуб! В пятницу — «Морозко». Сто раз видели. В сто первый тоже пойдём. «Тепло ли тебе, девица?» — тепло, если в клубе печку затопят.",
   "The travelling cinema is coming to the club! Morozko on Friday. We've seen it a hundred times. We'll go a hundred and first. “Are you warm, maiden?” Warm enough, if they light the club stove."))
F("any", ("Знакомые знакомых, Канада", "Friends of friends in Canada"),
  ("Из Канады прислали красный кленовый лист.", "A red maple leaf came from Canada."),
  ("Из Канады кленовый лист! Красный, как у них на флаге. Знакомые знакомых прислали. Положим в книгу, к нашим кленовым. Пусть познакомятся.",
   "A maple leaf from Canada! Red, like on their flag. Friends of friends sent it. We'll press it in a book with our own maple leaves. Let them get acquainted."))
F("any", ("Астрахань, нашедшие бутылку", "The finders of a bottle, Astrakhan"),
  ("В Волге нашли бутылку с запиской и адресом из Липовки.", "A bottle with a note giving a Lipovka address was found in the Volga."),
  ("Письмо из Астрахани! Нашли в Волге бутылку, а в записке — наш адрес. Кто-то из наших бросал, лет десять назад, в Липку. Дошла! Без марки, зато по воде.",
   "A letter from Astrakhan! They found a bottle in the Volga, and the note inside had our address. One of us threw it in the Lipka ten years ago. It got there! No stamp, but by water."))
F("any", ("Газета «Наш край»", "Our Region newspaper"),
  ("Пришёл пробный номер новой газеты «Наш край».", "A free trial issue of a new paper, Our Region, came."),
  ("Пробный номер газеты «Наш край». Пишут про наш район так, будто впервые увидели: «удивительный уголок». А мы и не знали, что удивительный. Приятно.",
   "A trial issue of a paper called Our Region. They write about our district as if they'd just discovered it: “a remarkable corner of the land.” We never knew we were remarkable. Nice."))
F("any", ("Районный узел связи", "District Post Office"),
  ("Районная почта благодарит получателей за то, что пишут письма.", "The district post office thanks people for writing letters."),
  ("Районный узел связи прислал открытку: «Спасибо, что пишете письма». Получателям — спасибо! Не ожидали. Ну, раз так — будем писать больше. Вам работы прибавится.",
   "The district post office sent a card: “Thank you for writing letters.” Thanking the customers! Didn't expect that. Well then, we'll write more. More work for you."))
F("any", ("Эрмитаж, музейный магазин", "The Hermitage museum shop"),
  ("Открытка из Эрмитажа с музейным котом.", "A card from the Hermitage with a museum cat."),
  ("Открытка из Эрмитажа: кот на подоконнике, музейный. Подпись: «Тоже служит при музее». Как наш Сургуч — при почте. Служба у них одинаковая: лежать с важным видом.",
   "A card from the Hermitage: a museum cat on a windowsill. Caption: “Also on the museum staff.” Like our Surguch at the post office. Same job: lying about looking important."))
F("any", ("Точильщик", "The knife grinder"),
  ("Точильщик будет в Липовке в среду.", "The knife grinder is coming to Lipovka on Wednesday."),
  ("Объявление: «Точу ножи, ножницы, косы. Буду в Липовке в среду». Ножи тупые у всех. Будет у точильщика праздник, а у нас — искры.",
   "A notice: “Knives, scissors and scythes sharpened. In Lipovka on Wednesday.” Everyone's knives are blunt. A holiday for the grinder, and sparks for us."))
F("any", ("Детская художественная школа", "The children's art school"),
  ("Зовут на выставку детских рисунков «Почта».", "An invitation to a children's art show called The Post."),
  ("Приглашение на выставку детских рисунков в Городке. Тема — «Почта». Будет сорок почтальонов с огромными сумками. Сходите. На себя посмотрите.",
   "An invitation to a children's art show in Gorodok. The theme: The Post. Forty postmen with enormous bags. Do go. You'll see yourself."))
F("any", ("Биологи университета", "University biologists"),
  ("Учёные просят записывать, когда весной запоют лягушки.", "Scientists ask people to note when the frogs start singing in spring."),
  ("Учёные из университета просят: записывайте весной, когда начнут квакать лягушки. Будем записывать. Лягушки у нас голосистые, им понравится, что их слушают.",
   "University scientists ask us to note down when the frogs start croaking in spring. We will. Our frogs have good voices; they'll like being listened to."))
F("any", ("Музей Городка", "Gorodok museum"),
  ("Музей благодарит за чугунный утюг для витрины.", "The museum says thank you for a cast-iron iron for its display."),
  ("Музей благодарит за подаренный утюг — чугунный, на углях. Поставят в витрину с табличкой. Утюг — в музее! Он такого не ожидал. Всю жизнь гладил — и вот, прославился.",
   "The museum thanks us for the cast-iron charcoal iron. It'll go in a display case with a label. An iron in a museum! It never expected that. A lifetime of ironing, and now it's famous."))
F("any", ("Издательство «Сказка»", "Fairy Tale Press"),
  ("Прислали рекламную закладку с котом-читателем.", "An advertising bookmark with a reading cat arrived."),
  ("Закладка пришла, рекламная, с котом в очках. Реклама забудется, а кот останется — в книге, на нужной странице.",
   "An advertising bookmark with a cat in glasses. The advert will be forgotten; the cat will stay, in a book, on the right page."))
F("any", ("Филателист, Польша", "A stamp collector in Poland"),
  ("Филателист из Польши просит марки с липовской почты.", "A Polish stamp collector asks for stamps from the Lipovka post office."),
  ("Филателист из Польши просит прислать марки с нашей почты. С нашей! Значит, и у Липовки будет место в чьём-то альбоме. Выберем самые красивые.",
   "A stamp collector in Poland asks for stamps from our post office. Ours! So Lipovka will have a place in somebody's album. We'll choose the prettiest."))
F("any", ("Промокший конверт", "A rain-soaked envelope"),
  ("Конверт промок в дороге, буквы поплыли.", "An envelope got soaked on the way and the ink ran."),
  ("Конверт подмок — видно, в дождь шёл. Буквы поплыли, а слова остались. Хорошие слова не размываются.",
   "The envelope's soaked; it must have come through the rain. The letters have run, but the words are still there. Good words don't wash away."))
F("any", ("Неизвестный отправитель", "An unknown sender"),
  ("Письмо адресовано «самому доброму человеку в Липовке».", "A letter addressed “to the kindest person in Lipovka”."),
  ("Письмо адресовано: «Липовка, самому доброму человеку». Почему нам — непонятно. Но приятно. Может, вам отдать? Вы почтальон, вы всех знаете.",
   "The letter's addressed “Lipovka, to the kindest person”. Why us, no idea. But it's nice. Maybe it should go to you? You're the postman, you know everyone."))
F("any", ("Метеостанция-любитель", "An amateur weather watcher"),
  ("Любитель погоды из Твери просит записывать первый снег.", "A weather enthusiast in Tver asks people to record the first snow."),
  ("Любитель погоды из Твери собирает по всей области, когда выпал первый снег. Просит записать. Запишем: и число, и час, и кто первый увидел. Первым обычно видит кот.",
   "A weather enthusiast in Tver is collecting the date of the first snow from all over the region. He asks us to note it. We will: the date, the hour, and who saw it first. It's usually the cat."))
F("any", ("Подписка на журнал «Огонёк»", "A magazine subscription offer"),
  ("Предлагают подписку на журнал с подарком — ручкой.", "A magazine offers a subscription with a free pen."),
  ("Предлагают подписку на журнал, а в подарок — ручка. Ручку уже прислали, вот она, в конверте. Подписка ещё под вопросом, а ручка уже пишет. Хитрые.",
   "They're offering a magazine subscription with a free pen. They've sent the pen already, here it is. The subscription's still undecided, but the pen already writes. Crafty."))
F("any", ("Школьники, Вологда", "Schoolchildren in Vologda"),
  ("Школьники просят прислать рецепт любимого пирога для книги.", "Schoolchildren ask for a favourite pie recipe for their book."),
  ("Школьники из Вологды собирают «Книгу пирогов России», просят рецепт. Какой пирог главный? С капустой. Нет, с яблоками. Нет… Пошлём оба. Пусть разбираются.",
   "Schoolchildren in Vologda are making a Book of Russian Pies and ask for a recipe. Which pie is the main one? Cabbage. No, apple. No… We'll send both. They can sort it out."))
F("any", ("Добровольцы «Чистая река»", "Clean River volunteers"),
  ("Добровольцы зовут чистить берега Липки.", "Volunteers invite people to clean up the Lipka's banks."),
  ("Добровольцы «Чистая река» зовут в субботу чистить берег Липки. Перчатки дадут, мешки дадут, бутерброды — с собой. Пойдём. Река у нас одна, хорошая.",
   "Clean River volunteers are inviting everyone to clear the Lipka's banks on Saturday. Gloves provided, sacks provided, bring your own sandwiches. We'll go. We've only got the one river, and it's a good one."))
F("any", ("Компания «Электросвет»", "The lighting company"),
  ("Прислали бесплатную лампочку — «попробуйте экономить».", "A free light bulb came: “try saving energy”."),
  ("Лампочку бесплатную прислали: «Попробуйте экономить». Вкрутим на крыльцо. Пусть экономит — и светит тем, кто в темноте идёт. Вам, например.",
   "They've sent a free light bulb: “Try saving energy.” It's going over the porch. Let it save energy, and light the way for anyone walking in the dark. You, for instance."))
F("any", ("Открытка с вокзала", "A card from a station"),
  ("Кто-то прислал открытку прямо с вокзала, наспех.", "Someone sent a card in a hurry, straight from a station."),
  ("Открытка с вокзала, наспех: «Еду мимо, поезд стоит две минуты, машу вам!» Две минуты! Мы, наверное, в это время чай пили. Ну, помашем в ответ. Задним числом.",
   "A hurried card from a railway station: “Passing through, the train stops for two minutes, waving to you!” Two minutes! We were probably having tea. Well, we'll wave back. Belatedly."))
F("any", ("Общество садоводов-любителей", "Amateur Gardeners' Society"),
  ("Общество садоводов зовёт на обмен рассадой.", "The gardeners' society invites everyone to a seedling swap."),
  ("Садоводы зовут на обмен рассадой у клуба: «Приносите лишнее, забирайте нужное». Лишнего у нас — полподоконника помидоров. Нужного — терпения. Его на обмене не дают.",
   "The gardeners invite everyone to a seedling swap at the club: “Bring what you've too much of, take what you need.” We've half a windowsill of spare tomatoes. What we need is patience. You can't swap for that."))
F("any", ("Пенфренд, Аргентина", "A pen-friend in Argentina"),
  ("Открытка из Аргентины: там сейчас лето наоборот.", "A card from Argentina, where the seasons are upside down."),
  ("Открытка из Аргентины! Там всё наоборот: у нас зима — у них лето, у нас лето — у них зима. Пишут: «Пришлите немного вашего лета, у нас тут июль и холодно». Пришлём.",
   "A card from Argentina! Everything's upside down there: our winter's their summer and our summer's their winter. They write, “Send us a little of your summer, it's July here and cold.” We will."))
F("any", ("Клуб любителей кошек", "The Cat Lovers' Club"),
  ("Клуб любителей кошек прислал приглашение на выставку.", "The Cat Lovers' Club sent an invitation to its show."),
  ("Зовут на выставку кошек в Городок. Записать ли Сургуча? Он, конечно, победит. Только его до Городка не донести — он на письмах спит. Выставка подождёт, письма — нет.",
   "An invitation to the cat show in Gorodok. Shall we enter Surguch? He'd win, of course. Only you'd never carry him that far; he's asleep on the letters. The show can wait. The letters can't."))
F("any", ("Открытка «Привет из Липовки»", "A Greetings from Lipovka card"),
  ("Кто-то из уехавших прислал открытку с видом Липовки.", "Someone who moved away sent a card with a view of Lipovka."),
  ("Открытка «Привет из Липовки» — с нашей мельницей и клубом. Кто-то из уехавших купил её в Городке и прислал нам. Привет из Липовки — в Липовку. Дошёл.",
   "A Greetings from Lipovka card, with our mill and our club. Somebody who moved away bought it in Gorodok and posted it to us. Greetings from Lipovka, to Lipovka. Delivered."))
F("any", ("Издательство календарей", "A calendar publisher"),
  ("Прислали календарь с репродукциями картин про деревню.", "A calendar of paintings of village life arrived."),
  ("Календарь с картинами про деревню: баня, сенокос, гуси, девочка с ведром. Каждый месяц как в окно смотришь. А в окно посмотришь — тоже картина, и без календаря.",
   "A calendar of paintings of village life: a bathhouse, haymaking, geese, a girl with a bucket. Each month is like looking out of a window. And when you look out of the real window, there's a painting there too, no calendar needed."))
F("any", ("Поисковый клуб «Корни»", "The Roots genealogy club"),
  ("Клуб генеалогов ищет потомков тех, кто строил мельницу.", "A genealogy club is looking for descendants of the mill's builders."),
  ("Клуб «Корни» ищет потомков тех, кто сто лет назад строил нашу мельницу. Список фамилий прислали. Половина деревни в этом списке! Значит, мы все немножко мельники.",
   "The Roots club is looking for descendants of the men who built our mill a hundred years ago. They sent a list of surnames. Half the village is on it! So we're all a little bit millers."))
F("any", ("Открытка-головоломка", "A puzzle postcard"),
  ("Пришла открытка-пазл: собери, тогда прочитаешь.", "A jigsaw postcard came: put it together to read it."),
  ("Открытка-пазл! Двадцать кусочков, собери — тогда прочитаешь. Хитро. Пол-утра собирать. Ну, что ещё делать в такую погоду? Вы идите, вам письма носить.",
   "A jigsaw postcard! Twenty pieces, assemble it to read it. Clever. That's half the morning. Well, what else is there to do in this weather? You go on, you've letters to carry."))

# --------------------------------------------------------------------------- fillers: mixed tags
F("old,family", ("Родня, Самара", "Family in Samara"),
  ("Из Самары прислали фото ведра раков.", "A photo of a bucket of crayfish came from Samara."),
  ("Из Самары пишут: наловили раков, ведро. Прислали фото: раки красные, родня довольная. «Жаль, по почте нельзя». Жаль. Зато фото не убежит.",
   "From Samara: they've caught a bucket of crayfish. A photo came: red crayfish, pleased relatives. “Shame we can't post them.” A shame. But at least the photo won't crawl off."))
F("young,family", ("Друзья, Петрозаводск", "Friends in Petrozavodsk"),
  ("Друзья зовут в поход на байдарках по Карелии.", "Friends invite someone kayaking in Karelia."),
  ("Друзья зовут летом на байдарках по Карелии. «Две недели, комары, уха, без связи». Без связи! Это у нас и так. Комары тоже. А вот уха с ними — это заманчиво.",
   "Friends are inviting us kayaking in Karelia this summer. “Two weeks, mosquitoes, fish soup, no phone signal.” No signal: we have that already. Mosquitoes too. But fish soup with them, that's tempting."))
F("old,family", ("Знакомые, Тула", "Friends in Tula"),
  ("Прислали самоварную трубу — старую, но целую.", "Someone sent an old but sound samovar chimney."),
  ("Жаловались как-то знакомым, что у самовара труба прогорела. Прислали трубу! Старую, медную, целую. Вот это друзья. Вечером — самовар. Приходите на пробу.",
   "We once complained to friends that our samovar chimney had burnt through. They've sent one! Old, copper, sound. Now those are friends. Samovar tonight. Come and try it."))
F("young,family", ("Сестра, Москва", "A sister in Moscow"),
  ("Сестра прислала посылку с книгами, которые «надо прочитать».", "A sister sent a parcel of books one “simply must read”."),
  ("Сестра прислала пять книг: «Обязательно прочитай». Пять! Обязательно! Положу у кровати стопкой. Стопка — это уже полдела.",
   "My sister sent five books: “You simply must read these.” Five! Must! I'll stack them by the bed. A stack is half the battle."))
F("any", ("Опечатка в адресе", "A misaddressed letter"),
  ("Письмо дошло, хотя на конверте написано «Лиловка».", "A letter arrived despite a misspelt village name."),
  ("На конверте вместо «Липовка» написано «Лиловка». Лиловка! А дошло. Почта — она умная, она понимает, что Лиловка — это мы. Вы понимаете.",
   "The envelope says “Lilacovka” instead of Lipovka. Lilacovka! And it still got here. The post is clever; it knows Lilacovka is us. You knew."))
F("old,young,family", ("Знакомые с Байкала", "Friends at Baikal"),
  ("С Байкала прислали кедровых орехов в мешочке.", "A little bag of cedar nuts came from Baikal."),
  ("Кедровые орешки с Байкала, в льняном мешочке. Щёлкать их — дело долгое, вечернее, под разговор. Вот и разговор будет. Садитесь, пощёлкаем.",
   "Cedar nuts from Baikal in a linen bag. Cracking them is a long evening job, done over a chat. So there'll be a chat. Sit down, let's crack some."))
F("old,family", ("Бывшие соседи, Вологда", "Former neighbours in Vologda"),
  ("Бывшие соседи прислали фото: их внук вырос и уехал учиться.", "Former neighbours sent a photo: their grandson's grown and gone to study."),
  ("Бывшие соседи пишут: внук вырос, уехал учиться на моряка. Фото: стоит в форме, а уши — те же, что в три года, когда он у нас яблоки воровал. По ушам и узнали.",
   "Former neighbours write: their grandson's grown up and gone to naval college. A photo: standing in uniform, and the same ears as at three, when he used to pinch our apples. We knew him by the ears."))
F("young,family", ("Друг детства, Ярославль", "A childhood friend in Yaroslavl"),
  ("Друг детства нашёлся спустя двадцать лет.", "A childhood friend got in touch after twenty years."),
  ("Друг детства нашёлся! Двадцать лет ни слуху. Пишет: «Помнишь шалаш у реки?» Помню. Шалаша давно нет, а место есть. Сфотографирую и пошлю.",
   "A childhood friend has turned up! Twenty years without a word. He writes, “Remember our den by the river?” I do. The den's long gone, but the spot's still there. I'll photograph it and send it."))
F("old", ("Знакомые, Мичуринск", "Friends in Michurinsk"),
  ("Из Мичуринска прислали черенки яблони старинного сорта.", "Cuttings of an old apple variety came from Michurinsk."),
  ("Черенки яблони прислали, старинный сорт, «Бабушкино». Завёрнуты во мох, как дети в одеяло. Привьём весной. Лет через пять будет «Бабушкино» и у нас.",
   "Apple cuttings, an old variety called Granny's. Wrapped in moss like babies in a blanket. We'll graft them in spring. In five years we'll have Granny's too."))
F("old", ("Друг, Таганрог", "A friend in Taganrog"),
  ("Друг с юга прислал старую пластинку — «нашу».", "A friend in the south sent an old record, “our song”."),
  ("Друг прислал пластинку, старую, с той самой песней, под которую танцевали на выпускном. Проигрыватель есть? Есть! На шкафу, под чехлом. Вечером поставим. Осторожно, иголочкой.",
   "A friend sent a record, an old one, with the very song we danced to at our school-leaving dance. Got a player? We have! On top of the cupboard under a cover. We'll put it on tonight. Gently, with the needle."))
F("old", ("Землячество", "The home-town society"),
  ("Прислали книгу воспоминаний о родной деревне — и там знакомое имя.", "A book of memories of a home village arrived, with a familiar name in it."),
  ("Прислали книгу воспоминаний — про деревню, где когда-то учились в школе. И на сто двенадцатой странице — про нас! Что мы на уроке выпустили из коробка лягушку. Всё правда. Лягушку звали Жанна.",
   "They've sent a book of memories about the village where we went to school. And on page one hundred and twelve, there's us! Letting a frog out of a matchbox in a lesson. It's all true. The frog was called Zhanna."))
F("any", ("Внук соседей", "The neighbours' grandson"),
  ("Соседский внук прислал рисунок «Липовка будущего».", "The neighbours' grandson drew The Lipovka of the Future."),
  ("Рисунок от соседского внука: «Липовка будущего». На рисунке ракета у клуба, мост из радуги и почтальон на крыльях. На крыльях! Вот бы вам такие.",
   "A drawing from the neighbours' grandson: The Lipovka of the Future. A rocket by the club, a rainbow bridge and a postman with wings. Wings! Wish you had some."))

# --------------------------------------------------------------------------- fillers with {name}
F("any", ("Районная библиотека", "District library"),
  ("Районная библиотека поздравляет своего тысячного читателя.", "The district library congratulates its thousandth reader."),
  ("Пишут: «{name}, поздравляем! Вы — тысячный читатель года». Тысячный! Приз — книжка и шоколадка. Книжку прочитаем, а шоколадку разделим. Берите половину.",
   "They write, “{name}, congratulations! You are our thousandth reader of the year.” The thousandth! The prize is a book and a bar of chocolate. We'll read the book and share the chocolate. Have half."))
F("young", ("Подруга, Тверь", "A friend in Tver"),
  ("Подруга спрашивает, куда пропали.", "A friend asks where someone has disappeared to."),
  ("Подруга пишет: «{name}, ты где пропадаешь? Напиши хоть строчку!» Строчку? Напишу три страницы. Пусть знает: тут, в Липовке, и пропадаю. Хорошо пропадаю.",
   "A friend writes, “{name}, where have you vanished to? Write me one line at least!” One line? I'll write three pages. Let her know: right here in Lipovka, that's where. And vanishing very nicely."))
F("old", ("Без обратного адреса", "No return address"),
  ("Конверт «лично в руки», а внутри — старая школа и одно слово.", "An envelope “to be handed in person”, with an old school photo and one word."),
  ("Крупно на конверте: «{name} — лично в руки». Вот, в руках. Внутри фотография нашей старой школы и одна строчка: «Помнишь?» Помню. Ещё бы не помнить.",
   "In big letters on the envelope: “{name}, to be handed over in person.” There, in my hands. Inside, a photo of our old school and one line: “Remember?” I do. How could I not."))
F("child", ("Тётя (или заяц)", "An aunt (or a hare)"),
  ("Ребёнку пришло письмо «от зайца».", "A child got a letter “from a hare”."),
  ("На конверте: «{name}, тебе письмо от зайца!» А внутри рисунок зайца и морковка из бумаги. Это, конечно, тётя. Но вдруг заяц?",
   "On the envelope: “{name}, a letter for you from a hare!” And inside, a drawing of a hare and a paper carrot. It's my aunt, of course. But what if it's a hare?"))
F("family", ("Брат, Воронеж", "A brother in Voronezh"),
  ("Брат едет в гости летом «всей оравой».", "A brother is coming in summer “with the whole gang”."),
  ("Брат пишет: «{name}, встречайте в июле, едем всей оравой». Оравой! Значит, раскладушки доставать с чердака. И пироги — с запасом.",
   "My brother writes, “{name}, expect us in July, we're coming with the whole gang.” The whole gang! So the camp beds come down from the attic. And pies, plenty of them."))


# --------------------------------------------------------------------------- output
def cell(s):
    s = s.strip()
    assert "\t" not in s and "\n" not in s and "\r" not in s, s
    return s


def write(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["\t".join(header)] + ["\t".join(cell(c) for c in r) for r in rows]
    path.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


def write_all():
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    warn = []
    rows = []
    keys = set()
    for t in TEMPLATES:
        assert t["key"] not in keys, t["key"]
        keys.add(t["key"])
        vs = t["variants"]
        for ru, en in vs:
            if "|" in ru or "|" in en:
                warn.append(f"{t['key']}: pipe inside a variant")
        for lang in (0, 1):
            if len(t["brief"][lang]) > 80 or len(t["frm"][lang]) > 40:
                warn.append(f"{t['key']}: brief/from too long")
        if not 8 <= len(vs) <= 20:
            warn.append(f"{t['key']}: {len(vs)} variants")
        ru = " | ".join(cell(v[0]) for v in vs)
        en = " | ".join(cell(v[1]) for v in vs)
        for lang, s in (("ru", ru), ("en", en)):
            if len(s) > 2400:
                warn.append(f"{t['key']}: news_{lang} {len(s)} chars (over by {len(s) - 2400})")
        rows.append([t["key"], t["every"], t["day"], t["months"], t["to"], t["kind"], t["frm"][0], t["frm"][1],
                     t["brief"][0], t["brief"][1], ru, en, t["stamp"]])
    write(C / "templates.tsv", ["key", "every", "day", "months", "to", "kind", "from_ru", "from_en", "brief_ru",
                                "brief_en", "news_ru", "news_en", "stamp"], rows)

    rows = []
    for tags, frm, brief, news in FILLERS:
        for lang in (0, 1):
            if len(news[lang]) > 340:
                warn.append(f"filler {news[0][:40]}: news {len(news[lang])} chars")
            if len(brief[lang]) > 80:
                warn.append(f"filler {brief[0][:40]}: brief {len(brief[lang])} chars")
            if len(frm[lang]) > 40:
                warn.append(f"filler {frm[0]}: from {len(frm[lang])} chars")
        rows.append([tags, frm[0], frm[1], brief[0], brief[1], news[0], news[1]])
    write(C / "fillers.tsv", ["tags", "from_ru", "from_en", "brief_ru", "brief_en", "news_ru", "news_en"], rows)

    rows = []
    for key, start, end, d, look, name, notice, brief, stamp in EVENTS:
        for lang in (0, 1):
            for what, v, lim in (("name", name, 40), ("notice", notice, 340), ("brief", brief, 80)):
                if len(v[lang]) > lim:
                    warn.append(f"event {key}: {what}_{'ru' if lang == 0 else 'en'} {len(v[lang])} chars (max {lim})")
        rows.append([key, start, end, d, look, name[0], name[1], notice[0], notice[1], brief[0], brief[1], stamp])
    write(C / "events.tsv", ["key", "start", "end", "district", "look", "name_ru", "name_en", "notice_ru", "notice_en",
                             "brief_ru", "brief_en", "stamp"], rows)

    write(C / "stamps/f.tsv", ["key", "family", "bg", "value", "name_ru", "name_en", "series"], STAMPS)

    nv = sum(len(t["variants"]) for t in TEMPLATES)
    print(f"{len(TEMPLATES)} templates ({nv} variants), {len(FILLERS)} fillers, {len(EVENTS)} events, {len(STAMPS)} stamps")
    tags = {}
    for f in FILLERS:
        for t in f[0].split(","):
            tags[t] = tags.get(t, 0) + 1
    print("filler tags:", tags)
    for w in warn:
        print("WARN", w)


write_all()
