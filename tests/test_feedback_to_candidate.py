import unittest
from docomocv import DocomoCVClient, Recog
from requests.exceptions import HTTPError
from .utils import api_key


class TestFeedbackToCandidate(unittest.TestCase):
    def test_feedback_to_candidate(self):
        client = DocomoCVClient(api_key)
        result = client.feedback_to_candidate('ed626110-5e36-11e4-84c4-065d0f977797', 'food_0000180195', True)
        self.assertIsNone(result)

    def test_feedback_to_candidate_with_comment(self):
        client = DocomoCVClient(api_key)
        result = client.feedback_to_candidate('ed626110-5e36-11e4-84c4-065d0f977797', 'food_0000180195', True, '正しい認識結果です。')
        self.assertIsNone(result)

    def test_feedback_to_candidate_with_invalid_apikey(self):
        client = DocomoCVClient('') # invalid api key
        self.assertRaises(HTTPError, client.feedback_to_candidate, 'ed626110-5e36-11e4-84c4-065d0f977797', 'food_0000180195', True)
