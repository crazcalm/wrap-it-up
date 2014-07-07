__author__= "crazcalm"

import unittest
from sort_reddits import content_in_list, sort_by_key
from user_class import User

class TestSuite(unittest.TestCase):
    def test_User_class(self):
        user = User("John", "pass")
        self.assertEqual(user.username, "John")
        self.assertEqual(user.password, "pass")

    def test_sort_by_key(self):
        items = [{'name': "B"},{'name': "A"}]
        answer = [{'name': "A"}, {'name': "B"}]
        self.assertEqual(sort_by_key(items, 'name'), answer)

    def test_content_in_list(self):
        items = [{"data": {'name': "Crazcalm"}}]
        answer = [{'name': "Crazcalm"}]
        self.assertEqual(content_in_list(items), answer)

if __name__ == "__main__":
    unittest.main()
