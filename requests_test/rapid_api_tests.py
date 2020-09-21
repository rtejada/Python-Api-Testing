import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/quickAnswer"

querystring = {"q":"How much vitamin c is in 2 apples%3F"}

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "349560fe26msh3a85d303abc02b9p1eb2cdjsnb45b6f567df4"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print('URL:', response.url)
