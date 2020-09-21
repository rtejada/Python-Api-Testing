import unittest
from ExamplesSeveralApi.unittest.tests.requests_test.base_code import GetData


class MyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def data_bible(self):
        pass

    def test_something(self):

        list = GetData()
        id, name = list.bibles_details()

        print(id, name)


if __name__ == '__main__':
    unittest.main()
