import requests
from dotenv import load_dotenv
import os


class GetData:

    def __init__(self):

        load_dotenv(os.getcwd() + "/../.env.DataBiblia")
        self.key = os.getenv('API_BIBLIA')
        self.url = os.getenv('URl_BIBLIA')
        self.list_id = []
        self.list_name = []

    def bibles_details(self):
        headers = {"api-key": self.key}
        params = {"language": "spa"}
        response = requests.get(self.url, headers=headers, params=params)

        bibles = response.json()

        for i in bibles["data"]:

            self.list_id.append(i["id"])
            self.list_name.append(i["name"])

        return self.list_id, self.list_name






