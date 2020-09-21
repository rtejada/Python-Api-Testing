import requests
import os
from dotenv import load_dotenv

load_dotenv(os.getcwd() + "/../../.env.OpenData")
api_Key = os.getenv('OPEN_WEATHER_KEY')
api_url = os.getenv('URL_BASE_WEATHER')

city = input('Dime el nombre de una ciudad: ')

parameters = {"q": city, "mode": "json", "units": "metric", "APPID": api_Key}
response = requests.get(api_url, params=parameters)

if response.status_code == 200:
    data = response.json()
    print('La temperatura actual en', city, 'es:', data["main"]["temp"])

else:
    print('No tengo datos de esa ciudad')
