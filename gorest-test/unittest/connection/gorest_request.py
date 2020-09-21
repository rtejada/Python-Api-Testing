from connection.logger import logger
from lib.data_users_generator import GeneratorUsersGorestCo
from dotenv import load_dotenv
import requests
import os
import json


class GorestRequests:

    load_dotenv(os.getcwd() + "/../../.env.gorest")
    token = os.getenv('TOKEN')
    url_base = os.getenv('URL_GOREST')
    url_comment = os.getenv('URL_COMMENTS')
    url_post = os.getenv('URL_POSTS')
    body_post = None

    headers = None
    response = None

    def get_url_base(self):

        return self.url_base

    def get_headers(self):

        if self.headers is None:
            self.headers = {'Authorization': self.token,
                            'Content-Type': 'application/json'
                            }

            logger.debug(f'successful connection: {self.headers}')
            return self.headers

    def request_create_user(self):

        data = GeneratorUsersGorestCo()
        payload = {"name": data.name(), "email": data.email(), "gender": data.gender(), "status": data.status()}
        payload = json.dumps(payload)

        response = requests.post(self.url_base, headers=self.get_headers(), data=payload)

        return response

    def request_get_user(self, user_id):

        get_post = requests.get(self.get_url_base() + '/' + str(user_id), headers=self.get_headers())
        return get_post
  
    def request_post(self):
        
        data = GeneratorUsersGorestCo()
        payload = {"title": data.title(), "body": data.body()}
        payload = json.dumps(payload)
        id = 1825
        response_posts = requests.post(self.url_base + '/' + str(id) + '/posts', headers=self.get_headers(), data=payload)
        return response_posts
    
    def request_post_query(self):

        id = 1825
        response_data_post = requests.get(self.url_base + '/' + str(id) + '/posts', headers=self.get_headers())
        return response_data_post
    
    def request_comment(self):

        comment_id = 1215
        data = GeneratorUsersGorestCo()
        payload = {"body": data.body(), "email": data.email(), "name": data.name(), "post_id": str(comment_id)}
        payload = json.dumps(payload)

        response_comment = requests.post(self.url_comment, headers=self.get_headers(), data=payload)
        return response_comment
   
    def request_get_comment(self, post_id):

        response = requests.get(self.url_post + str(post_id) + '/comments', self.get_headers())
        return response

    def request_update_user(self, user_id):

        data = GeneratorUsersGorestCo()
        payload = {"name": data.name(), "email": data.email(), "gender": data.update_gender(), "status": data.update_status()}
        payload = json.dumps(payload)

        response = requests.put(self.url_base + '/' + str(user_id), headers=self.get_headers(), data=payload)

        return response

    def delete_user(self, payload, user_id):

        payload = json.dumps(payload)

        response = requests.delete(self.url_base + '/' + str(user_id), headers=self.get_headers(), data=payload)

        return response


'''
prueba = GorestRequests()
prueba.connection_to_url_posts()

'''