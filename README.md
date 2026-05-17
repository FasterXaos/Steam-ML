
# Steam-ML

Проект собирает и анализирует данные пользователей и игр Steam для машинного обучения: кластеризация пользователей, рекомендательная система, граф друзей и предсказание дружбы.

## Структура проекта

```
Steam-ML/
├── data/                              # собранные данные
│   ├── steamUsersDataset.json         # профили пользователей + их игры
│   ├── steamGamesDataset.json         # информация об играх (отзывы, owners, tags и т.д.)
│   ├── friendsGraph.json              # граф дружбы между пользователями
│   ├── steamCrawlQueue.json           # очередь для краулинга SteamID
│   └── simpleStatistics.txt           # базовая статистика после краулинга
├── notebooks/
│   ├── clustering.ipynb               # кластеризация пользователей
│   ├── dataAnalysis.ipynb             # анализ и визуализация данных
│   ├── friendsGraphAnalysis.ipynb     # сбор графа друзей + Community Detection + 3D-визуализация
│   ├── linkPrediction.ipynb           # предсказание дружбы
│   ├── recommendationSystem.ipynb     # рекомендательная система игр
│   └── steamDataCollector.ipynb       # сбор данных пользователей и игр
├── .env                               # (нужно создать)
├── README.md
└── requirements.txt
```

## Установка

```bash
pip install -r requirements.txt
```

## Создание файла среды (`.env`)

1. Создайте файл среды в корне проекта: `.env`

2. Откройте `.env` и укажите свой Steam Web API ключ и Steam ID:
   ```env
   STEAM_API_KEY=ваш_ключ_здесь
   STEAM_ID=ваш_id_здесь
   ```

Ключ можно получить бесплатно на [Steam Web API](https://steamcommunity.com/dev/apikey).  
ID можно получить по ссылке профиля на [SteamID I/O](https://steamid.io/), нужен `steamID64`.

## Собираемые данные

- **friendsGraph.json** — граф дружбы: {steamId: [список друзей в датасете]}
- **simpleStatistics.txt** — общая статистика по собранным данным.
- **steamCrawlQueue.json** — очередь SteamID для дальнейшего краулинга.
- **steamGamesDataset.json** — информация об играх (название, отзывы, owners, жанр, tags, languages, averageForever и т.д.).
- **steamUsersDataset.json** — информация о пользователях (steamId, personaname, ownedGames, playtimeForever, loccountrycode, timecreated и др.).
