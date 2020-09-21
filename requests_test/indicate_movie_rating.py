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
    session_id = ''
    
    for movie in data["results"]:
        print(cont, movie["title"], "->", movie["vote_average"])
        ids.append(movie["id"])
        cont += 1
        
    # Primero tengo que conseguir un id de sesión de invitado
    parameters = {"api_key": api_key}
    r = requests.get(api_url + "authentication/guest_session/new", params=parameters)
    if r.status_code == 200:
        data = r.json()
        session_id = data["guest_session_id"]

    # Ahora pido la pélicula y la puntuación
    index = int(input("Indica la película de la que quieres votar:"))
    id = ids[index - 1]
    rating = input("Indica la puntuación de la película:")
    parameters = {"guest_session_id": session_id, "api_key": api_key}
    data = '{"value":%s}' % rating
    heads = {"Content-Type": "application/json;charset=utf-8"}

    r = requests.post(api_url + "movie/" + str(id) + "/rating", params=parameters, headers=heads, data=data)
    if r.status_code == 201:
        data = r.json()
        if data["status_code"] == 1:
            print("Has votado con éxito")
else:
    print("Error en la votación")
