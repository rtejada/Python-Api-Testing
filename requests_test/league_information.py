import requests
import os
from dotenv import load_dotenv

load_dotenv(os.getcwd() + "/../../.env.OpenData")
api_Key = os.getenv('OPEN_SOCCER_KEY')
api_url = os.getenv('URL_BASE_SOCCER')

num_league = input('Que liga de futbol deseas consultar: ')
num_league = int(num_league)

parameters = {"league": num_league, "req": "tables", "format": "json", "key": api_Key}
response = requests.get(api_url, params=parameters)

print(response.url)
if response.status_code == 200:
    data = response.json()
    for eq in data["table"]:
        print(eq["pos"], eq["team"], eq["points"])
else:
    print('Error en la consulta')
