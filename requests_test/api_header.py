import requests
import os
from dotenv import load_dotenv

api_key = '1d1b897b281a72e6ef07eda2f7a9b288'
url = 'https://api.scripture.api.bible/v1/bibles'
new_header = {'api-key': api_key}

response = requests.get(url, headers=new_header)
print(response.url)

url = "https://gorest.co.in/public-api/users"

header = {"Content-Type": "application/json", "Authorization": "Bearer 1c0d87ee4dbcb663a26c206d83be1ede26a49110bd6b6af8439532a0011bdd42"}

body = '{"first_name":"Mervin","last_name":"Diaz","gender":"male","email":"mervin100@hola.com","status":"active"}'

r = requests.post(url, data=body, headers=header)

url = "https://gorest.co.in/public-api/users"
resp = requests.get(url, headers=header)

print(resp.text)