
# Steam-ML

Проект собирает и анализирует данные пользователей и игр Steam для последующего машинного обучения.

## Структура проекта

```
Steam-ML/
├── data/                          # все собранные датасеты (будут выложены в будущем)
│   ├── steamUsersDataset.json     # профили пользователей + их игры
│   ├── steamGamesDataset.json     # информация об играх (отзывы, owners, tags и т.д.)
│   ├── steamCrawlQueue.json       # очередь для краулинга SteamID
│   └── simpleStatistics.txt       # простая статистика после краулинга
├── notebooks/
│   ├── dataAnalysis.ipynb
│   └── clustering.ipynb
├── .env                           # нудно создать
├── requirements.txt
└── README.md
```

## Создание файла среды (`.env`)

1. Создайте файл среды в корне проекта: `.env`

2. Откройте `.env` и укажите свой Steam Web API ключ и Steam ID:
   ```env
   STEAM_API_KEY=ваш_ключ_здесь
   STEAM_ID=ваш_id_здесь
   ```

Ключ можно получить бесплатно на [Steam Web API](https://steamcommunity.com/dev/apikey).  
ID можно получить поссылке профиля на [SteamID I/O](https://steamid.io/), нужен `steamID64`.

## Собираемые данные

- **steamUsersDataset.json** — информация о пользователях (steamId, personaname, ownedGames, playtimeForever, loccountrycode, timecreated и др.).
- **steamGamesDataset.json** — информация об играх (название, отзывы, owners, жанр, tags, languages, averageForever и т.д.).
- **steamCrawlQueue.json** — очередь SteamID для дальнейшего краулинга.
- **simpleStatistics.txt** — общая статистика по собранным данным.
