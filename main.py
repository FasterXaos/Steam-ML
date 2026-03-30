import os

import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("STEAM_API_KEY")
STEAM_ID =  os.getenv("STEAM_ID")

if not API_KEY:
    print("API ключ не найден")
    exit()
elif not STEAM_ID:
    print("STEAM_ID не найден")
    exit()

url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"

params = {
    "key": API_KEY,
    "steamid": STEAM_ID,
    "include_appinfo": True,
    "format": "json"
}

response = requests.get(url, params=params)
data = response.json()

if "games" not in data["response"]:
    print("Нет доступа к играм (возможно, профиль приватный)")
    exit()

games = data["response"]["games"]

# Сортируем по времени игры (в минутах)
gamesSorted = sorted(games, key=lambda x: x["playtime_forever"], reverse=True)

top20Games = gamesSorted[:20]

names = [game["name"] for game in top20Games]
playtime = [game["playtime_forever"] / 60 for game in top20Games]

plt.figure()
plt.barh(names[::-1], playtime[::-1])
plt.xlabel("Часы")
plt.title("Топ 10 игр по времени в Steam")
plt.tight_layout()

plt.show()
