
# Steam-ML

Проект собирает и анализирует данные пользователей и игр Steam для машинного обучения: кластеризация пользователей, рекомендательная система, графа друзей и предсказание дружбы.

## Структура проекта

```
Steam-ML/
├── data/                              # собранные датасеты
│   ├── steamUsersDataset.json         # профили пользователей + их игры
│   ├── steamGamesDataset.json         # информация об играх (отзывы, owners, tags)
│   ├── friendsGraph.json              # граф дружбы между пользователями
│   ├── linkPredictionDataset.csv      # обучающая выборка для Link Prediction
│   ├── steamCrawlQueue.json           # очередь для краулинга SteamID
│   └── simpleStatistics.txt           # статистика после краулинга
├── notebooks/
│   ├── steamDataCollector.ipynb       # сбор данных пользователей и игр
│   ├── dataAnalysis.ipynb             # анализ и визуализация данных
│   ├── clustering.ipynb               # кластеризация пользователей
│   ├── recommendationSystem.ipynb     # рекомендательная система игр
│   ├── friendsGraphAnalysis.ipynb     # сбор графа друзей + Community Detection + 3D-визуализация
│   ├── linkPrediction.ipynb           # Link Prediction: предсказание дружбы
│   └── main.ipynb                     # общий пайплайн
├── .env                               # API ключи (нужно создать)
├── requirements.txt
└── README.md
```

## Установка

```bash
pip install -r requirements.txt
```

## Создание файла среды (`.env`)

Создайте файл `.env` в корне проекта:

```env
STEAM_API_KEY=ваш_ключ_здесь
STEAM_ID=ваш_steamid64_здесь
```

- Ключ можно получить на [Steam Web API](https://steamcommunity.com/dev/apikey)
- SteamID64 можно узнать на [SteamID I/O](https://steamid.io/)

## Собираемые данные

- **steamUsersDataset.json** — информация о пользователях (steamId, personaname, ownedGames, playtimeForever, loccountrycode, timecreated и др.).
- **steamGamesDataset.json** — информация об играх (название, отзывы, owners, жанр, tags, languages, averageForever и т.д.).
- **steamCrawlQueue.json** — очередь SteamID для дальнейшего краулинга.
- **simpleStatistics.txt** — общая статистика по собранным данным.
- **friendsGraph.json** — граф дружбы: {steamId: [список друзей в датасете]}
- **linkPredictionDataset.csv** — 110 000 примеров с 11 признаками для Link Prediction