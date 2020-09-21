from connection.logger import logger
import unittest
from connection.gorest_request import GorestRequests


class CreatePostUsers(unittest.TestCase):

    def setUp(self):
        self.body = ''
        r = GorestRequests()
        self.response = r.request_post()

    def test_get_users(self):

        self.body = self.response.json()
        code = self.response.status_code
        self.assertEqual(code, 200)
        reg = ['post_id', 'title', 'body', 'created_at', 'updated_at']
        recorded_data = dict.fromkeys(reg)

        recorded_data['post_id'] = self.body["data"]["id"]
        recorded_data['title'] = self.body["data"]["title"]
        recorded_data['body'] = self.body["data"]["body"]
        recorded_data['created_at'] = self.body["data"]["created_at"]
        recorded_data['updated_at'] = self.body["data"]["updated_at"]
        logger.info(f'post_id: {recorded_data["post_id"]}')

        r = GorestRequests()
        self.query = r.request_post_query()
        code = self.query.status_code
        body = self.query.json()

        self.assertEqual(code, 200)

        for i in range(len(body["data"])):
            if body['data'][i]['id'] == recorded_data['post_id']:
                self.assertEqual(body['data'][i]['id'], recorded_data['post_id'])
                self.assertEqual(body['data'][i]['title'], recorded_data['title'])
                self.assertEqual(body['data'][i]['body'], recorded_data['body'])
                self.assertEqual(body['data'][i]['created_at'], recorded_data['created_at'])
                self.assertEqual(body['data'][i]['updated_at'], recorded_data['updated_at'])









