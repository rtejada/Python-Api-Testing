from lib.functions_gorest import BasePage
from connection.person_dao import PersonDao
from connection.post_dao import PostDao
import os
import json
from datetime import datetime


class GeneratorUsersGorestCo(BasePage):

    REGISTER_DATA = []
    USER_ID = []
    PERSONS_DB = ''
    id = ''
    db_persons = ''
    POSTS_DB = ''
    post_id = ''
    db_post = ''
    LIST_ID = []

    def __init__(self):

        self.data = ''
        with open(os.getcwd() + "/../data/data_users.json") as file:
            self.data = json.load(file)

    def user_id(self):

        return self.data['id']

    def post(self):

        return self.data['post_id']

    def name(self):
        return self.data["name"] + self.random_name(12)

    def email(self):
        return self.random_email(8) + self.data["email"] + self.random_email(8) + '.es'

    def gender(self):
        return self.data["gender"]

    def update_gender(self):
        return self.data["update_gender"]

    def status(self):
        return self.data["status"]

    def update_status(self):
        return self.data["update_status"]

    def title(self):
        return self.data["title"] + self.random_name(15)

    def body(self):

        return self.data["body"] + self.random_letters(99)

    def select_database_persons(self):

        self.PERSONS_DB = PersonDao.select()

        now = datetime.now()
        #format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
        date = now.strftime('%Y-%m-%d')

        for i in range(len(self.PERSONS_DB)):
            if str(self.PERSONS_DB[i].date) == date:
                self.id = str(self.PERSONS_DB[i].id_user)
                self.db_persons = self.PERSONS_DB[i]
                break

    def select_database_posts(self):

        self.POSTS_DB = PostDao.select()

        now = datetime.now()
        #format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
        date = now.strftime('%Y-%m-%d')

        for i in range(len(self.POSTS_DB)):
            if str(self.POSTS_DB[i].date) == date:
                self.post_id = str(self.POSTS_DB[i].post_id)
                self.db_post = self.POSTS_DB[i]
                break


