import os
import unittest
from docomocv import DocomoCVClient, Recog
from requests.exceptions import HTTPError
from .utils import api_key


dir_name = os.path.abspath(os.path.dirname(__file__))


class TestRecognize(unittest.TestCase):
    def test_recognize(self):
        client = DocomoCVClient(api_key)
        img_file = os.path.join(dir_name, 'coffee.jpg')
        result = client.recognize(img_file)
        self.assertIsInstance(result['recognitionId'], str)

    def test_recognize_with_recog(self):
        client = DocomoCVClient(api_key)
        img_file = os.path.join(dir_name, 'coffee.jpg')
        result = client.recognize(img_file, Recog.food)
        self.assertIsInstance(result['recognitionId'], str)

    def test_recognize_with_recog_and_num_of_candidates(self):
        client = DocomoCVClient(api_key)
        img_file = os.path.join(dir_name, 'coffee.jpg')
        result = client.recognize(img_file, Recog.food, 5)
        self.assertIsInstance(result['recognitionId'], str)

    def test_recognize_with_invalid_apikey(self):
        client = DocomoCVClient('') # invalid api key
        img_file = os.path.join(dir_name, 'coffee.jpg')
        self.assertRaises(HTTPError, client.recognize, img_file, Recog.food)
