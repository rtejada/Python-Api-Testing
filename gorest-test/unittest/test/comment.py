from connection.gorest_request import GorestRequests
import unittest


class CreatePostUsers(unittest.TestCase):

    def setUp(self):
        self.comment_body = ''
        r = GorestRequests()
        self.response = r.request_comment()

    def test_post_comment(self):

        code = self.response.status_code
        self.assertTrue(code, 200)
        self.comment_body = self.response.json()
        r = GorestRequests()
        self.query = r.request_get_comment(self.comment_body["data"]["post_id"])
        body = self.query.json()

        self.assertEqual(self.query.status_code, 200)

        for i in range(len(body["data"])):
            if body['data'][i]['id'] == self.comment_body["data"]["id"]:
                self.assertEqual(body['data'][i]['id'], self.comment_body["data"]["id"])
                self.assertEqual(body['data'][i]['post_id'], self.comment_body["data"]["post_id"])
                self.assertEqual(body['data'][i]['name'], self.comment_body["data"]["name"])
                self.assertEqual(body['data'][i]['body'], self.comment_body["data"]["body"])
                self.assertEqual(body['data'][i]['created_at'], self.comment_body["data"]["created_at"])
                self.assertEqual(body['data'][i]['updated_at'], self.comment_body["data"]["updated_at"])





