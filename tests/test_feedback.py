import unittest
from docomocv import DocomoCVClient
from requests.exceptions import HTTPError
from .utils import api_key


class TestFeedback(unittest.TestCase):
    def test_feedback(self):
        client = DocomoCVClient(api_key)
        result = client.feedback('ed626110-5e36-11e4-84c4-065d0f977797', True)
        self.assertIsNone(result)

    def test_feedback_with_comment(self):
        client = DocomoCVClient(api_key)
        result = client.feedback('ed626110-5e36-11e4-84c4-065d0f977797', True, '正しい認識結果です。')
        self.assertIsNone(result)

    def test_recognize_with_invalid_apikey(self):
        client = DocomoCVClient('')  # invalid api key
        self.assertRaises(HTTPError, client.feedback, 'ed626110-5e36-11e4-84c4-065d0f977797', True)
