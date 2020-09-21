import requests
import datetime
import json

Format = "%Y-%m-%d"
BackDay = datetime.date.today() - datetime.timedelta(days=0)
Day = BackDay.strftime(Format)


api_key = 'KX6EScQN4AFPS9bysGTbq09eNSWdzhzdMBs9DS9E'

date = str(datetime.date.today().strftime("%Y-%m-%d"))

hd = 'False'

url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date=2020-09-05&api_key={api_key}"

response = requests.request("GET", url)

_response = json.loads(response.text)

#print(json.dumps(_response, indent=3))

print(_response['near_earth_objects']['2020-09-05'][0])

#print (_response['near_earth_objects']['2020-02-28'][0]['links']['self'])
