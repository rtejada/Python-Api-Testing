from connection.logger import logger
from lib.data_users_generator import GeneratorUsersGorestCo
from dotenv import load_dotenv
import requests
import os
import json


class ConnectionInfo:

    load_dotenv(os.getcwd() + "/../../.env.gorest")
    token = os.getenv('TOKEN')
    url_base = os.getenv('URL_GOREST')
    url_comments = os.getenv('URL_COMMENTS')
    url_post = os.getenv('URL_POSTS')
    body_post = None

    headers = None
    response = None

    @classmethod
    def get_url_base(cls):

        return cls.url_base

    @classmethod
    def get_headers(cls):

        if cls.headers is None:

            cls.headers = {'Authorization': cls.token,
                           'Content-Type': 'application/json'
                           }

            logger.debug(f'successful connection: {cls.headers}')
            return cls.headers

    @classmethod
    def connection_to_url_users(cls):

        data = GeneratorUsersGorestCo()
        payload = {"name": data.name(), "email": data.email(), "gender": data.gender(), "status": data.status()}
        payload = json.dumps(payload)

        cls.response = requests.post(cls.url_base, headers=cls.get_headers(), data=payload)

        return cls.response

    @classmethod
    def connection_to_url_posts(cls):

        data = GeneratorUsersGorestCo()
        payload = {"title": data.title(), "body": data.body()}
        payload = json.dumps(payload)
        id = 1679
        cls.response_posts = requests.post(cls.url_base + '/' + str(id) + '/posts', headers=cls.get_headers(), data=payload)
        print(cls.response_posts.url)
        return cls.response_posts

    @classmethod
    def connect_post_query_url(cls):

        id = 1679
        cls.response_data_post = requests.post(cls.url_base + '/' + str(id) + '/posts', headers=cls.get_headers())
        print(cls.response_data_post.url)
        return cls.response_data_post




prueba = ConnectionInfo()
prueba.connection_to_url_posts()