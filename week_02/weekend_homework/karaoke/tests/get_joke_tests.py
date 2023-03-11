import unittest
from classes.get_joke import MakeApiCall


class TestApiCall(unittest.TestCase):
    def setUp(self):
        self.get_jokes = MakeApiCall("https://icanhazdadjoke.com/")

    def test_api_response(self):
        self.assertIsNotNone(self.get_jokes.get_data())
