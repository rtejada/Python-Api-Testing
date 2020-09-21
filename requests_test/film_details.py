import requests
import os
from dotenv import load_dotenv

load_dotenv(os.getcwd() + "/../../.env.OpenData")
api_key = os.getenv("OPEN_API_MOVIES")
api_url = os.getenv('URL_BASE_MOVIES')

parameters = {"language": "es-ES", "page": "1", "region": "ES", "api_key": api_key}
r = requests.get(api_url + "movie/popular", params=parameters)

if r.status_code == 200:
    data = r.json()
    cont = 1
    ids = []
    for movie in data["results"]:
        print(cont, movie["title"], "->", movie["vote_average"])
        ids.append(movie["id"])
        cont += 1

    index = int(input("Indica la película de la que quieres obtener información:"))
    id = ids[index-1]
    parameters = {"language": "es-ES", "api_key": api_key}
    r = requests.get(api_url+"movie/"+str(id), params=parameters)
    if r.status_code == 200:
        data = r.json()
        print("Fecha lanzamiento:", data["release_date"])
        print(data["overview"])
else:
    print("Error en la consulta")
