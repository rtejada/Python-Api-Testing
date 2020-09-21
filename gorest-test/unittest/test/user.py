import unittest
from connection.gorest_request import GorestRequests
from connection.logger import logger


class PostUsers(unittest.TestCase):

    def create_user(self):
        r = GorestRequests()
        return r.request_create_user()
        
    def test_post_users(self):

        response = self.create_user()
        body = response.json()
        self.assertTrue(response.status_code, 200)
        
        r = GorestRequests()
        get_post = r.request_get_user(body["data"]["id"])
        code_get = get_post.status_code
        body_get = get_post.json()

        self.assertTrue(code_get, 200)
        self.assertEqual(body_get['data']['id'], body["data"]["id"])
        self.assertEqual(body_get['data']['name'], body["data"]["name"])
        self.assertEqual(body_get['data']['email'], body["data"]["email"])
        self.assertEqual(body_get['data']['gender'], body["data"]["gender"])
        self.assertEqual(body_get['data']['status'], body["data"]["status"])
        self.assertEqual(body_get['data']['created_at'], body["data"]["created_at"])
        self.assertEqual(body_get['data']['updated_at'], body["data"]["updated_at"])
        logger.info(f'user_id: {body["data"]["id"]}')

    def test_put_user(self):

        response = self.create_user()
        data_user = response.json()
        self.assertTrue(response.status_code, 200)
        user_id = data_user["data"]["id"]

        upd = GorestRequests()
        response = upd.request_update_user(user_id)
        body_update = response.json()
        self.assertEqual(response.status_code, 200)

        r = GorestRequests()
        get_post = r.request_get_user(user_id)
        body_get = get_post.json()

        self.assertTrue(get_post.status_code, 200)
        self.assertEqual(body_get['data']['id'], body_update["data"]["id"])
        self.assertEqual(body_get['data']['name'], body_update["data"]["name"])
        self.assertEqual(body_get['data']['email'], body_update["data"]["email"])
        self.assertEqual(body_get['data']['gender'], body_update["data"]["gender"])
        self.assertEqual(body_get['data']['status'], body_update["data"]["status"])
        self.assertEqual(body_get['data']['created_at'], body_update["data"]["created_at"])
        self.assertEqual(body_get['data']['updated_at'], body_update["data"]["updated_at"])
        logger.info(f'user_id: {body_update["data"]["id"]}')









