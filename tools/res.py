"""Writes the string resources (English and Russian) from one table, so the two never drift apart.

python tools/res.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "app/src/main/res"

S = [
    ("app_name", "Lipovka Post", "Почта в Липовке"),
    ("channel_post", "The post", "Почта"),
    ("channel_walk", "On the round", "На маршруте"),
    ("walk_title", "The postman is on the round", "Почтальон на маршруте"),
    ("walk_text", "Steps are counted while the app is in the background.", "Шаги считаются, пока приложение свёрнуто."),
    ("n_morning_title", "The morning post", "Утренняя почта"),
    ("n_telegram", "There's a telegram in the bag for %1$s.", "В сумке телеграмма. Адресат: %1$s."),
    ("n_desk", "There's a letter for you on the desk.", "На столе письмо для вас."),
    ("n_evening_title", "Almost there", "Совсем рядом"),
    ("n_evening", "%1$s is %2$d steps away.", "%1$s: осталось всего %2$d шагов."),
    ("tab_post", "Post", "Почта"),
    ("tab_village", "Village", "Деревня"),
    ("tab_room", "Room", "Комната"),
    ("tab_album", "Stamps", "Марки"),
    ("tab_diary", "Diary", "Дневник"),
    ("bag_title", "Today's bag", "Сумка на сегодня"),
    ("bag_empty", "The bag is empty. Everything is delivered.", "Сумка пуста. Всё разнесено."),
    ("bag_more", "Take more", "Взять ещё"),
    ("steps_today", "steps today", "шагов сегодня"),
    ("going_to", "on the way to %1$s", "иду: %1$s"),
    ("steps_left", "%1$s steps to go", "ещё %1$s шагов"),
    ("steps_n", "%1$s steps", "%1$s шагов"),
    ("steps_walked", "walked %1$s", "пройдено %1$s"),
    ("letter_for_you", "A letter for you", "Письмо вам"),
    ("visit_go", "Go to the gate", "К калитке"),
    ("km_total", "%1$s km walked in all", "всего пройдено %1$s км"),
    ("next_district", "%1$s opens in %2$s km", "%1$s откроется через %2$s км"),
    ("all_open", "Every road is open.", "Все дороги открыты."),
    ("add_steps", "+1000 steps", "+1000 шагов"),
    ("steps_permission", "Let the app count your steps, or the bag won't move.", "Разрешите считать шаги, иначе сумка не сдвинется."),
    ("allow", "Allow", "Разрешить"),
    ("no_sensor", "This phone has no step counter, so the post will wait.", "В этом телефоне нет шагомера. Почта подождёт."),
    ("evening_title", "Evening, %1$s", "Вечер, %1$s"),
    ("evening_news", "today's news", "новости дня"),
    ("evening_none", "A quiet day. The letters will wait. Never mind, tomorrow.", "Тихий день. Письма подождут. Ничего, завтра."),
    ("diary_title", "the postman's diary", "дневник почтальона"),
    ("diary_hint", "One line about today…", "Одна строчка о сегодняшнем дне…"),
    ("lamp_off", "Put out the lamp", "Погасить лампу"),
    ("lamp_on", "Light the lamp", "Зажечь лампу"),
    ("s_steps", "steps", "шагов"),
    ("s_letters", "letters", "писем"),
    ("s_km", "km", "км"),
    ("k_letter", "letter", "письмо"),
    ("k_postcard", "postcard", "открытка"),
    ("k_parcel", "parcel", "посылка"),
    ("k_telegram", "telegram", "телеграмма"),
    ("k_registered", "registered", "заказное"),
    ("k_newspaper", "newspaper", "газета"),
    ("k_notice", "notice", "афиша"),
    ("urgent", "urgent", "срочно"),
    ("at_gate", "at the gate · %1$s", "у калитки · %1$s"),
    ("thanks", "Thank you", "Спасибо"),
    ("take_reply", "Take the reply", "Взять ответ"),
    ("reply_out", "The reply goes with the morning post.", "Ответ уйдёт с утренней почтой."),
    ("reply_local", "A reply for %1$s: it goes in tomorrow's bag.", "Ответ для: %1$s. Ляжет в завтрашнюю сумку."),
    ("gift_to_room", "for the room above the post office", "в комнату над почтой"),
    ("stamp_to_album", "a stamp for the album", "марка в альбом"),
    ("reply_1", "%1$s reads the note from %2$s and smiles.", "%1$s читает записку. Это от: %2$s. Улыбается."),
    ("reply_2", "A note from %2$s. %1$s reads it twice and tucks it into a pocket.", "Записка, от кого: %2$s. Прочитано дважды и спрятано в карман."),
    ("reply_3", "From %2$s? %1$s laughs: \"Couldn't walk two houses, so wrote instead.\"", "От кого, от кого? %2$s? Смеются: «Через два дома не дойти, так написать!»"),
    ("from_reply", "note from %1$s", "записка: %1$s"),
    ("letter_put", "Put it in the box", "Положить в шкатулку"),
    ("letter_date", "on the desk since %1$s", "на столе с %1$s"),
    ("village_hint", "Tap a house to meet the people.", "Нажмите на дом, чтобы узнать жителей."),
    ("story", "their story", "история"),
    ("nothing_yet", "No letters yet.", "Писем ещё не было."),
    ("gifts_from", "gifts", "гостинцы"),
    ("locked", "Mist. Opens in %1$s km", "Туман. Откроется через %1$s км"),
    ("room_title", "The room above the post office", "Комната над почтой"),
    ("room_empty", "Empty for now. The village doesn't know you yet.", "Пока пусто. Деревня ещё не знает вас."),
    ("from_whom", "from %1$s · %2$s", "от: %1$s · %2$s"),
    ("album_title", "Stamp album", "Альбом марок"),
    ("album_hint", "Stamps come with the letters. The rarest ones come from the far roads.", "Марки приходят с письмами. Самые редкие идут дальними дорогами."),
    ("stamp_got", "received %1$s", "получена %1$s"),
    ("diary_tab", "The postman's diary", "Дневник почтальона"),
    ("served", "year %1$d of service", "%1$d-й год службы"),
    ("day_line", "%1$s steps · %2$d letters", "%1$s шагов · %2$d писем"),
    ("no_days", "The diary begins with your first walk.", "Дневник начнётся с первой прогулки."),
    ("settings", "Settings", "Настройки"),
    ("weather", "Weather", "Погода"),
    ("weather_hint", "Find your town and Lipovka will have the same weather. Only its coordinates go to the weather service.",
     "Найдите свой город, и в Липовке будет та же погода. В сервис погоды уходят только его координаты."),
    ("weather_search", "Town", "Город"),
    ("weather_find", "Find", "Найти"),
    ("weather_none", "Lipovka's own weather", "Своя погода Липовки"),
    ("weather_off", "No town: Lipovka keeps its own weather, by the season.", "Без города: в Липовке своя погода, по сезону."),
    ("weather_now", "%1$s now: %2$s, %3$s°", "%1$s сейчас: %2$s, %3$s°"),
    ("weather_fail", "Couldn't reach the weather service.", "Не удалось связаться с сервисом погоды."),
    ("notifications", "Notifications", "Уведомления"),
    ("notify_text", "The morning post and an evening \"almost there\"", "Утренняя почта и вечернее «совсем рядом»"),
    ("on", "On", "Вкл."),
    ("off", "Off", "Выкл."),
    ("language", "Language", "Язык"),
    ("lang_system", "As the phone", "Как в телефоне"),
    ("about", "About", "О приложении"),
    ("credits", "Font m6x11 by Daniel Linssen, Cyrillic by Natto Games. Weather by Open-Meteo.com and MET Norway (CC BY 4.0). No ads, no accounts: everything stays on the phone.",
     "Шрифт m6x11: Daniel Linssen, кириллица: Natto Games. Погода: Open-Meteo.com и MET Norway (CC BY 4.0). Без рекламы и аккаунтов, всё остаётся в телефоне."),
    ("steps_ok", "Step counter: on", "Шагомер: работает"),
    ("steps_off", "Step counter: not allowed", "Шагомер: нет разрешения"),
    ("next", "Next", "Дальше"),
    ("skip", "Skip", "Пропустить"),
    ("ob_title", "Lipovka Post", "Почта в Липовке"),
    ("ob_text", "You have been appointed postman of Lipovka, a small village by the river Lipka. The kettle is on, the cat is asleep on the letters. Your real steps carry the bag from house to house.",
     "Вас назначили почтальоном в Липовку, маленькую деревню на реке Липке. Чайник уже на плитке, кот спит на письмах. Ваши настоящие шаги понесут сумку от дома к дому."),
    ("ob_steps_title", "Your steps are the bag", "Ваши шаги — это сумка"),
    ("ob_steps_text", "The phone counts steps by itself, even when the app is closed. Every morning the post is sorted for about a usual day's walk. Walk, and the letters arrive.",
     "Телефон сам считает шаги, даже когда приложение закрыто. Каждое утро почта собирается примерно на обычный день ходьбы. Гуляйте, и письма дойдут."),
    ("ob_weather_title", "The weather outside", "Погода за окном"),
    ("ob_weather_text", "The village can have your weather and your sunrise. Find your town, or skip: Lipovka has its own weather too.",
     "В деревне может быть ваша погода и ваш рассвет. Найдите свой город или пропустите: у Липовки есть и своя погода."),
    ("ob_notify_title", "Two quiet notifications", "Два тихих уведомления"),
    ("ob_notify_text", "In the morning: the post has come. In the evening, only if a door is close: almost there.",
     "Утром: почта пришла. Вечером, и только если дом совсем близко: осталось чуть-чуть."),
    ("ob_start", "Take the keys", "Принять ключи"),
    ("today", "today", "сегодня"),
    ("yesterday", "yesterday", "вчера"),
    ("tap_close", "Close", "Закрыть"),
    ("shelf_hint", "On the shelf: %1$d more. They'll go on a lighter day.", "На полке ещё %1$d. Пойдут в более лёгкий день."),
    ("at_post", "at the post office", "на почте"),
    ("unknown_sender", "a neighbour", "сосед"),
    ("visit_none", "Nobody is waiting at the gates.", "У калиток никто не ждёт."),
]

PL = [
    ("n_bag", {"one": "%d letter in the bag.", "other": "%d letters in the bag."},
     {"one": "В сумке %d письмо.", "few": "В сумке %d письма.", "many": "В сумке %d писем.", "other": "В сумке %d письма."}),
    ("visits", {"one": "%d waiting at the gate", "other": "%d waiting at the gates"},
     {"one": "У калитки ждут: %d", "few": "У калиток ждут: %d", "many": "У калиток ждут: %d", "other": "У калиток ждут: %d"}),
    ("things", {"one": "%d thing", "other": "%d things"}, {"one": "%d вещь", "few": "%d вещи", "many": "%d вещей", "other": "%d вещи"}),
    ("letters_n", {"one": "%d letter", "other": "%d letters"}, {"one": "%d письмо", "few": "%d письма", "many": "%d писем", "other": "%d письма"}),
    ("days_ago", {"one": "%d day ago", "other": "%d days ago"}, {"one": "%d день назад", "few": "%d дня назад", "many": "%d дней назад", "other": "%d дня назад"}),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace("'", "\\'").replace('"', '\\"')


def write(path, idx):
    out = ['<?xml version="1.0" encoding="utf-8"?>', "<resources>"]
    for k, en, ru in S:
        out.append(f'    <string name="{k}">{esc((en, ru)[idx])}</string>')
    for k, en, ru in PL:
        out.append(f'    <plurals name="{k}">')
        for q, v in (en, ru)[idx].items():
            out.append(f'        <item quantity="{q}">{esc(v)}</item>')
        out.append("    </plurals>")
    out.append("</resources>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    write(RES / "values/strings.xml", 0)
    write(RES / "values-ru/strings.xml", 1)
