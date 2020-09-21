import unittest
from connection.gorest_request import GorestRequests
from connection.logger import logger


class PostUsers(unittest.TestCase):

    def setUp(self):
        self.body = ''

    def create_user(self):
        r = GorestRequests()
        return r.request_create_user()

    def test_post_users(self):

        response = self.create_user()
        self.assertTrue(response.status_code, 200)
        body = response.json()
        logger.info(body["data"]["id"])

        reg = ['name', 'email', 'gender', 'status']
        recorded_data = dict.fromkeys(reg)

        recorded_data['name'] = body["data"]["name"]
        recorded_data['email'] = body["data"]["email"]
        recorded_data['gender'] = body["data"]["gender"]
        recorded_data['status'] = body["data"]["status"]

        r = GorestRequests()
        data_response = r.delete_user(recorded_data, body["data"]["id"])
        result = data_response.json()

        self.assertEqual(result["code"], 204)

        query = GorestRequests()
        data = query.request_get_user(body["data"]["id"])
        body_result = data.json()
        self.assertEqual(body_result["code"], 404)
