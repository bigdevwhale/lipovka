# Lipovka Post — Privacy Policy

*Last updated: 30 October 2026*

Lipovka Post is a pedometer for Android in which your real steps carry the post around a small village.
It is published as open source at <https://github.com/bigdevwhale/lipovka>.

## What we collect

**Nothing.** Lipovka Post has no accounts, no analytics, no advertising and no crash reporting.
We run no server, so nothing you do in the app ever reaches us.

## What stays on your device

The app keeps the following only in its private storage on your phone:

- your steps: the readings of the phone's own step counter and the totals per day;
- the post: the letters delivered and waiting, the stories, the gifts in your room and the stamps in the album;
- the postman's diary and the lines you write in it;
- your settings (language, the chosen town, notifications).

Steps are read from the phone's built-in step counter sensor. The app does not use Google Fit or
Health Connect and never sends your steps anywhere.

## The weather

The weather is optional. Only if you pick a town in settings:

- the name you type into the town search is sent to the Open-Meteo geocoding service to find matching towns;
- the chosen town's coordinates (rounded to about 100 metres) are sent to Open-Meteo
  (<https://open-meteo.com>), or to MET Norway (<https://api.met.no>) when Open-Meteo can't be reached,
  to get the current weather.

Nothing else is sent with these requests: no account, no device identifier, no steps. Your phone's
GPS location is never used; the town is the one you choose. Without a town the app makes no network
requests at all and the village keeps its own seasonal weather. These services' own privacy policies
apply to the requests they receive.

## Sharing

- **Community links** in settings open Telegram or your browser, only when you tap them; what you do
  there is governed by those services' own policies.
- **Backups.** Android may include the app's data in your own device backup to your Google account, if
  you have that turned on in system settings.

## Permissions

- **Physical activity** — to read the phone's step counter.
- **Notifications** — for the morning post, an evening "almost there", and the quiet notification shown
  while steps are counted with the app in the background.
- **Foreground service (health)** — to keep counting steps while the app is minimized or the screen is locked.
- **Internet** — only for the weather, and only if a town is chosen.

## Children

Lipovka Post is not directed at children under 13.

## Changes

Any change to this policy will be published on this page with a new date.

## Contact

Questions: open an issue at <https://github.com/bigdevwhale/lipovka/issues>.

---

# Почта в Липовке — Политика конфиденциальности

*Обновлено: 30 октября 2026*

«Почта в Липовке» — шагомер под Android, в котором ваши настоящие шаги разносят почту по маленькой деревне.
Код открыт: <https://github.com/bigdevwhale/lipovka>.

## Что мы собираем

**Ничего.** В приложении нет аккаунтов, аналитики, рекламы и отчётов о сбоях.
У нас нет сервера, поэтому ничего из того, что вы делаете в приложении, к нам не попадает.

## Что хранится на устройстве

Только в собственном хранилище приложения на телефоне:

- шаги: показания встроенного счётчика шагов телефона и итоги по дням;
- почта: доставленные и ожидающие письма, истории, подарки в комнате и марки в альбоме;
- дневник почтальона и ваши строчки в нём;
- настройки (язык, выбранный город, уведомления).

Шаги берутся со встроенного датчика шагов телефона. Приложение не использует Google Fit и Health Connect
и никуда не отправляет ваши шаги.

## Погода

Погода необязательна. Только если вы выбрали город в настройках:

- название, которое вы вводите в поиск города, уходит в сервис геокодинга Open-Meteo, чтобы найти подходящие города;
- координаты выбранного города (округлённые примерно до 100 метров) уходят в Open-Meteo
  (<https://open-meteo.com>), а если он недоступен — в MET Norway (<https://api.met.no>), чтобы узнать текущую погоду.

Больше в этих запросах ничего нет: ни аккаунта, ни идентификатора устройства, ни шагов. GPS телефона
не используется: город вы выбираете сами. Без города приложение вообще не выходит в сеть, а в деревне
своя погода по сезону. К запросам, которые получают эти сервисы, применяются их собственные политики.

## Ссылки

- **Ссылки на сообщество** в настройках открывают Telegram или браузер, только когда вы на них нажимаете;
  там действуют правила этих сервисов.
- **Резервная копия.** Android может включить данные приложения в резервную копию устройства в вашем
  аккаунте Google, если она включена в настройках.

## Разрешения

- **Физическая активность** — чтобы читать счётчик шагов телефона.
- **Уведомления** — утренняя почта, вечернее «осталось чуть-чуть» и тихое уведомление, пока шаги
  считаются со свёрнутым приложением.
- **Фоновая служба (здоровье)** — чтобы шаги считались, когда приложение свёрнуто или экран заблокирован.
- **Интернет** — только для погоды и только если выбран город.

## Дети

Приложение не предназначено для детей младше 13 лет.

## Изменения

Изменения этой политики публикуются на этой странице с новой датой.

## Контакты

Вопросы — через issue: <https://github.com/bigdevwhale/lipovka/issues>.
