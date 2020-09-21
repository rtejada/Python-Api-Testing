import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv(os.getcwd() + "/../../.env.OpenData")
api_Key = os.getenv('OPEN_WEATHER_KEY')
api_url = os.getenv('URL_BASE_WEATHER')

parameters = {"q": "Madrid", "mode": "json", "units": "metric", "APPID": api_Key}
response = requests.get(api_url, params=parameters)
print(response.url)

print(response.status_code)
data = response.json()
print(data["main"]["temp"])

date = str(datetime.date.today().strftime("%Y-%m-%d"))
print(date)

