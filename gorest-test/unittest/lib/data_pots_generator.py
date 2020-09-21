from lib.functions_gorest import BasePage
import os
import json


class PostGorestCo(BasePage):

    def __init__(self):

        self.data = ''
        with open(os.getcwd() + "/../data/data_users.json") as file:
            self.data = json.load(file)

    def id_comment(self):

        return self.data['id_comment']

    def post_id(self):

        return self.data['post_id']

    def name_comment(self):

        return self.data["name_comment"]

    def email_comment(self):

        return self.data["email_comment"]

    def body_comment(self):

        return self.data["body_comment"]

    def date_comment(self):

        return self.data['date_comment']




