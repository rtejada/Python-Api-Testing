import requests
import os
from dotenv import load_dotenv

load_dotenv(os.getcwd() + "/../../.env.OpenData")
api_key = os.getenv("OPEN_API_MOVIES")
api_url = os.getenv('URL_BASE_MOVIES')

parameters = {"language": "es-ES", "page": "1", "region": "ES", "api_key": api_key}
r = requests.get(api_url + "tv/1416/season/1/episode/1", params=parameters)

if r.status_code == 200:
    data = r.json()
    cont = 1
    ids = []
    session_id = ''

    for movie in data["guest_stars"]:
        print(cont, movie["name"], "->", movie["order"])

        ids.append(movie["id"])
        cont += 1

    print(data["overview"])
