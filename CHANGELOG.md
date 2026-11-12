# Changelog

<!--
Telegram: end each version's section with a hidden block for the StillCraft chat. Start it with a
line "<!-- tg", then 2-4 short lines in Russian for users (what is new, what is fixed), no markdown,
then close it like any HTML comment. The release notes carry it, and the chat bot posts those lines.
-->

## [1.0.25] - 2026-11-12

### Fixed
- On the "going to" card, "walked N, M of them today" no longer runs into "N steps to go": there is a gap between them, and when the line wraps the steps to go sit level with its last line. The number stays with "today" when it wraps.

<!-- tg
Исправлено: на карточке «иду:» строка «пройдено…, из них сегодня…» больше не налезает на «ещё … шагов».
-->

## [1.0.24] - 2026-11-11

### Added
- Post office sounds, on unless turned off in Settings → Sounds, while the app is open: the wall clock ticks in step with its pendulum, and the hour and weather bring rain, a thunderstorm, the wind, birds on a summer day, crickets on a warm evening, the stove crackling on a cold one. Upstairs in the room the clock isn't heard. The rain, storm, wind, birds and crickets are real recordings (credits in About).
- A notification when Bublik the dog starts walking with the postman, and when a district opens, with a word about what is there.

### Fixed
- The newest thing on the room's shelf no longer stands on the desk lamp's shade.

<!-- tg
Новое: звуки почты. Тикают ходики в такт маятнику, за стеной дождь, гроза, ветер, летом птицы и сверчки, зимой трещит печка. Выключаются в настройках.
Новое: уведомления, когда к почтальону прибивается Бублик и когда открывается новый район.
Исправлено: новая вещь на полке больше не стоит на абажуре лампы.
-->

## [1.0.23] - 2026-11-11

### Fixed
- The morning bag could come empty after a few evenings of "Take more" in Lipovka alone: every neighbour had had a letter lately, so no everyday letter went out. Now those who have waited longest get them.

<!-- tg
Исправлено: после нескольких вечеров со «Взять ещё» утренняя сумка могла прийти пустой. Теперь утром письма есть всегда.
-->

## [1.0.22] - 2026-11-10

### Fixed
- After taking many letters with "Take more", the next morning no longer adds more on top: the long roads of the letters still in the bag count towards the usual day, and the bag is only topped up to it.
- "Take more" no longer brings a letter to the house that has just had one, or to one already in the bag, so the same person doesn't get two letters in a row.

<!-- tg
Исправлено: если вечером взять много писем через «Взять ещё», утром игра больше не накидывает новые сверху, а только добирает до обычной нормы.
«Взять ещё» больше не даёт одному и тому же человеку два письма подряд.
-->

## [1.0.21] - 2026-11-09

### Changed
- "Take more" puts one letter into the bag per press, and the button is there whenever the bag isn't full, also in the middle of a round. The shelf goes first; then an everyday letter for a neighbour who had no post today.
- Each press makes the walk longer by a growing stretch: 1 500 steps the first time in a day, then 2 250, 3 000 and so on. When the house is nearer than that, the road to it goes the long way round.
- The round card shows the whole bag's road under the steps to the next gate, so a letter taken is a walk you can see.

<!-- tg
Новое: «Взять ещё» добавляет по одному письму за нажатие, и кнопка видна, пока сумка не полная.
Каждое нажатие удлиняет прогулку всё больше: 1 500 шагов, потом 2 250, 3 000 и дальше.
Под «ещё N шагов» теперь видно, сколько шагов во всей сумке.
-->

## [1.0.20] - 2026-11-09

### Fixed
- "Take more" always finds letters, however far you walk: after a few rounds the bag no longer comes back empty. The neighbours who had no post today go first, then the others, a second letter the same day only when everyone has had one.

<!-- tg
Исправлено: «Взять ещё» больше не возвращается с пустой сумкой — сколько бы вы ни прошли, письма найдутся.
Сначала письма получают те, кому сегодня ещё ничего не приносили, а уже потом — по второму разу.
-->

## [1.0.19] - 2026-11-09

### Added
- The diary is a month calendar: each day tinted by how far it was walked, marked if something was written, with the month's kilometres, letters and notes underneath. A tap on a day opens it: its line, and a log of what was handed to whom.
- A line can be written or added to on any past day, not only tonight.
- A tapped stamp opens over the album with a little story of how it came: who it was addressed to, how they handed it over, who the letter was from.
- The post screen labels its tiles "today": steps, kilometres and letters for today, with yesterday's and the day before's steps under them; the total distance and letters are in the line under the bag.
- After the last letter the postman walks back to the post office instead of spending the night at a gate.
- "Take more" is there even when the shelf is empty: there's always an everyday letter for a neighbour, up to a full bag.
- An optional note for every letter handed over at a gate, with the next stop (Settings → Notifications, off by default).
- Letters to the postman in the diary fold to the last three.

### Fixed
- The app could close while typing in the evening diary.
- After midnight the evening is called the night ("The night before 8 November"), and the line written then goes to the day just walked; a dark winter morning no longer shows the evening.
- The newspaper's news no longer says "Thursday" when it is delivered on another day.
- The weather town is shown in the search field when settings are opened again.
- The morning post notification waits until you're up: the first steps, an alarm clock that has rung, or ten o'clock.
- A long diary line no longer goes under the keyboard and buttons.
- Steps a watch hands over late for an earlier day count for that day, not for today's round; a road begun on an earlier day says how much of it was walked today.
- "Letters" and "days" agree with their numbers; the stat tiles stand level.

<!-- tg
Новое: дневник стал календарём — нажмите на день, чтобы увидеть запись и кому что разнесли. Писать можно и задним числом.
У марки теперь своя история: кто её отдал и откуда пришло письмо. Почтальон после разноса возвращается на почту.
Исправлено: вылет при записи в дневник, «вечер» после полуночи, четверг в новостях, ранние утренние уведомления и шкала шагов.
-->

## [1.0.18] - 2026-11-07

### Added
- Settings -> Community has a "Support Lipovka" line: it opens the StillCraft support page, for new letters and warm evenings.

<!-- tg
Новое: в Настройках, в разделе «Сообщество», появилась строчка «Поддержать Липовку» — на новые письма и тёплые вечера.
-->

## [1.0.17] - 2026-11-07

### Added
- A tear-off calendar hangs on the post office wall. Each morning it still shows yesterday, its corner stirring now and then; a tap tears the sheet off, it flutters down to the desk, and today's sheet is held up to read: the day and the weekday, what's on in the village, sunrise, sunset and the length of the day, the moon, the name days (in Russian), a folk sign or the month's saying, and a hint or a recipe on the back. A new or restored post office starts on today's sheet.

<!-- tg
Новое: на почте висит отрывной календарь. Утром на нём ещё вчерашний день — оторвите листок.
На листке восход и закат, луна, именины, народная примета и совет или рецепт на обороте.
-->

## [1.0.16] - 2026-11-06

### Fixed
- Steps from Health Connect reach the widget even after the app is swiped away from recents. On Xiaomi and some other phones that stops the app and its 15-minute step check; the widget now wakes the app every half hour to fetch the steps and start the check again.

<!-- tg
Исправлено: шаги из Health Connect доходят до виджета, даже если смахнуть приложение из недавних.
На Xiaomi это останавливало фоновую проверку шагов; теперь виджет сам раз в полчаса подтягивает шаги и запускает её снова.
Совет для Xiaomi: в настройках приложения включите «Автозапуск» и «Контроль активности: нет ограничений» — тогда виджет обновляется раз в 15 минут.
-->

## [1.0.15] - 2026-11-06

### Added
- The widget has a picture of the hour: by day the post office with the cat asleep on the letters, from dusk the evening table with the kerosene lamp (out on the widget too if it was put out tonight), in the real weather and season. Under the words a road runs to the next gate, trodden as far as the postman has come.

### Changed
- Long diary entries rest folded to a few lines, on the evening card and in the Diary tab; a tap opens them.
- The diary entry saves itself as you write, so closing the app without putting out the lamp no longer loses it.

### Fixed
- The line being typed in the diary stays above the keyboard instead of going on behind it.
- The widget keeps up with the steps while you walk with the app minimized, not only when the app is opened again.

<!-- tg
Виджет стал уютнее: днём на нём почта с котом на письмах, вечером — стол с керосиновой лампой, а под текстом дорожка до следующей калитки.
Дневник: строка больше не прячется за клавиатурой, длинные записи сворачиваются, а запись сохраняется сама, даже если не гасить лампу.
Исправлено: виджет обновляет шаги на ходу, пока приложение свёрнуто.
-->

## [1.0.14] - 2026-11-06

### Added
- Backup: Settings -> Backup saves the whole post office to a file, and "Restore from a file" brings it back on another phone: letters, stories, things, stamps, the steps of every day and the diary. The first page of the introduction offers the restore too, so a new phone goes straight back to the village.
- The school answers a tap. The house above the Sokolovs' has its name on the map and its own card: what's going on there right now, its pupils and the old teacher (a tap opens their house), and the school year with its dates.

### Changed
- A day's line in the diary can be up to 2000 characters, not 240.

### Fixed
- Steps agree with their numbers: "1 шаг", "2 шага", "5 шагов" (and "1 step"), on the post screen, in the bag, on the widget and in the diary.
- The evening lamp stays out once it's put out, after switching tabs or reopening the app, until the next day.

<!-- tg
Новое: резервная копия. Настройки → «Резервная копия» сохраняют всю почту в файл, а на новом телефоне её можно восстановить прямо с первого экрана.
Школа над домом Соколовых теперь открывается: что там сегодня, ученики и школьный год.
Исправлено: шаги склоняются по числу («2 шага», «5 шагов»), погашенная лампа больше не загорается сама, а запись в дневнике может быть до 2000 знаков.
-->

## [1.0.13] - 2026-11-05

### Fixed
- "Take more" halfway to a house no longer breaks the round. The steps already walked could count towards a different house, even one behind: its letters were delivered at once, and the house that was almost reached moved to the end of the round. Now the postman walks on to the house they were heading for, and the letters taken on the way come after it.

<!-- tg
Исправлено: «Взять ещё» посреди дня больше не ломает маршрут.
Раньше письма могли разом доставиться в дома позади, а дом, до которого оставалось чуть-чуть, уезжал в конец маршрута.
Теперь почтальон доходит до дома, к которому шёл, а новые письма встают в маршрут после него. Спасибо за находку!
-->

## [1.0.12] - 2026-11-05

### Added
- The kettle comes to the boil when tapped, at the post office, in the room and on the evening table: a thick jet of steam shoots from the spout and it whistles (a real kettle, by Work With Sounds / Konrad Gutkowski, CC BY 4.0).
- The cat-faced clock at the post office strikes the hour when tapped, as many times as the hour on its face. The pendulum swings wide, the clock cat's eyes dart, and a note floats up for every strike.

### Removed
- The groundwork for reading steps straight from Huawei Health. It would need the app registered with Huawei; Huawei Health's steps still reach the village through the Health Sync app and Health Connect.

<!-- tg
Чайник и часы на почте теперь тоже отзываются на нажатие.
Чайник закипает и свистит, а часы с кошачьей мордой бьют столько раз, сколько сейчас часов.
-->

## [1.0.11] - 2026-11-05

### Added
- Stroke the cat: a tap on the sleeping cat at the post office, in the room or on the evening windowsill wakes it for a few seconds. It lifts its head, squints happily, and purrs (a real cat, "Misha purrs" by AstronautDown, CC0), hearts rise from it, and the phone buzzes softly in time.

### Changed
- Groundwork for taking steps straight from Huawei Health through Huawei Health Kit. The choice doesn't show yet: it waits for the app's registration with Huawei.

<!-- tg
Кота теперь можно погладить: нажмите на спящего кота на почте, в комнате или на вечернем подоконнике.
Он поднимет мордочку, замурлычет, и телефон мягко завибрирует в такт.
-->

## [1.0.10] - 2026-11-03

### Fixed
- The app no longer closes when it is left for just a moment, such as for a permission dialog or the notification shade (for example, right after allowing Health Connect). The background step counting was being stopped before it had finished starting, and Android closed the app for that.

<!-- tg
Приложение больше не закрывается само, если ненадолго из него выйти: в окно разрешений или шторку уведомлений.
Например, сразу после того, как дали доступ к Health Connect.
-->

## [1.0.9] - 2026-11-03

### Added
- Steps can come from Health Connect instead of the phone's own counter (Settings → Steps). Samsung Health, Mi Fitness, Zepp Life, Google Fit, watches and bands put their steps there, so the village walks as far as they say, and a day's steps a watch hands over late still arrive. Huawei Health doesn't share with Health Connect; the Health Sync app can carry its steps over.

<!-- tg
Шаги теперь можно брать из Health Connect: Настройки → Шаги.
Туда пишут Samsung Health, Mi Fitness, Zepp Life, Google Fit, часы и браслеты, и в Липовке будет столько же шагов.
Huawei Health с Health Connect не делится, но его шаги может переносить приложение Health Sync.
-->

## [1.0.8] - 2026-11-01

### Fixed
- The step count no longer jumps by tens of thousands. A step counter reading lower than the last one, without the phone having restarted, used to be taken for a restart, and the whole count since the phone was turned on landed as new steps, sometimes delivering the whole day's post at once. Such readings now bring no steps, and no reading can bring more steps than can be walked in the time since the last one.

<!-- tg
Шаги больше не скачут на десятки тысяч сразу, и письма не разносятся сами, пока вы не ходили.
Приложение теперь не засчитывает больше шагов, чем можно пройти за прошедшее время.
-->

## [1.0.7] - 2026-11-01

### Fixed
- The text stays dark ink on paper on phones with a forced dark mode, instead of turning white a moment after the screen opens.
- When the lamp is put out at the end of the day, the cat on the windowsill and the curtains go dark with the room, instead of staying lit.

<!-- tg
Текст больше не белеет через секунду после открытия экрана на телефонах с принудительной тёмной темой.
Липовка всегда в своих цветах: чернила на бумаге.
Когда гасишь лампу в конце дня, кот на подоконнике и занавески темнеют вместе с комнатой.
-->

## [1.0.6] - 2026-10-29

### Fixed
- Clouds and stars stay in the sky: they pass behind the roofs at the gate, and behind the window frames and curtains at the post office, in the room and at the evening table, instead of drifting over them.

<!-- tg
Облака и звёзды больше не залезают на крыши и в дома: у калитки они проходят за крышей.
В окнах почты, комнаты и вечерней сцены облака плывут за рамой и занавесками.
-->

## [1.0.5] - 2026-10-29

### Fixed
- Everything at the gate stands on the ground: the goats, the boat, the woodpile, the tractor, the telescope, the weather box, the swing, the posts and the easel, each with its shadow. The cheese and the books lie on a bench, the carvings and the nets hang on the fence, the owl sits on a fence post.

<!-- tg
У калитки больше ничего не висит в воздухе: козы, лодка, поленница, трактор, телескоп и качели стоят на земле.
Сыр и книги лежат на скамейке, резьба и сети висят на заборе, сова сидит на столбике.
-->

## [1.0.4] - 2026-10-28

### Fixed
- Steps keep counting while the app is minimized, not only while the screen is locked, with the same quiet notification meanwhile.

<!-- tg
Шаги теперь считаются и когда приложение свёрнуто, а не только при заблокированном экране.
Пока оно в фоне, в шторке висит тихое уведомление «Почтальон на маршруте».
-->

## [1.0.3] - 2026-10-26

### Added
- Every house at the gate is its own: logs new, old or dark, or painted boards; the gable or the eaves to the street; lookouts, verandas, porches and sheds; tin, shingle, slate or thatch roofs; carved or plain window frames and shutters; the mill's water wheel, the club's columns, the shop's window.
- Residents have faces and their own things: glasses, beards, braids, buns, caps, a beret, aprons, shawls, beads, headphones; in winter, hats, fur collars and felt boots.

### Fixed
- Steps keep counting while the screen is locked with the app open, with a quiet notification meanwhile.
- The bedroom window is round, with no square corners past the frame.
- The well and the hives stand on the ground instead of hanging in the air.

<!-- tg
У каждого дома теперь своё лицо: брёвна, крашеные доски, светёлки, веранды, ставни, колесо у мельницы.
Жители стали подробнее: очки, бороды, косы, платки, кепки, зимой шапки и валенки.
Шаги считаются, пока экран заблокирован с открытым приложением.
Исправлены окно в спальне и висящий в воздухе колодец.
-->

## [1.0.2] - 2026-10-25

### Added
- Community links in settings: report a bug, suggest an idea or follow updates through the StillCraft bot on Telegram, and the StillCraft chat.

<!-- tg skip -->

## [1.0.1] — 2026-10-23

More fixes from running it on a phone.

- The keyboard no longer hides what you type: the screen moves up with it (town search, the diary), and the tab bar steps aside meanwhile.
- The town search box answers a tap anywhere on it, not only on the word in it.
- Putting out the lamp shows: the room goes dark but for the window, the keyboard closes, and the button offers to light it again.
- Steps show up while the app is open, without the old ten-second wait, and phones that hold the counter back are asked for it on every step.
- The widget starts the new day at midnight and redraws whenever you leave the app.
- The map's hint has its own strip and no longer covers house names.

## [1.0.0] — 2026-10-22

The first round of the Lipovka post.

- Your real steps carry the bag: the phone's step counter, counted even with the app closed, and a bag sorted each morning for about a usual day's walk.
- The post office, the map of the countryside, every house at its gate, the room above the post office, the evening table: pixel art drawn in code, in every season, weather and hour.
- 30 residents, 55 story arcs, 669 letters for years of play; recurring mail (the newspaper, pensions, magazines, birthdays, holidays), 267 everyday letters and 35 yearly events keep the bag full after that.
- Districts open as you walk: Zarechye at 50 km, then the railway halt, Ozyorki, the Pine Cordon and Gorodok.
- Gifts for your room, 264 stamps for the album, the postman's diary.
- The real weather and daylight of your town (optional, from Open-Meteo), or Lipovka's own.
- A home-screen widget and two quiet notifications.
- English and Russian.
