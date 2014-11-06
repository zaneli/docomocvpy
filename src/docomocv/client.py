import requests
from enum import Enum


class Recog(Enum):
    all = 'product-all'
    book = 'book'
    cd = 'cd'
    dvd = 'dvd'
    game = 'game'
    software = 'software'
    food = 'food'


class DocomoCVClient(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def recognize(self, img_file, recog=Recog.all, num_of_candidates=10):
        with open(img_file, mode='rb') as f:
            result = requests.post(
                url=DocomoCVClient.__build_url('recognize'),
                params={'APIKEY': self.api_key, 'recog': recog.value, 'numOfCandidates': num_of_candidates},
                data=f,
                headers={'Content-Type': 'application/octet-stream'})
            result.raise_for_status()
            return result.json()

    def feedback(self, recognition_id, is_valid, comment=None):
        result = requests.post(
            url=DocomoCVClient.__build_url('feedback'),
            params={'APIKEY': self.api_key, 'recognitionId': recognition_id, 'isValid': DocomoCVClient.__valid_to_str(is_valid)},
            json={'comment': comment},
            headers={'Content-Type': 'application/json;charset=UTF-8'})
        result.raise_for_status()

    def feedback_to_candidate(self, recognition_id, item_id, is_valid, comment=None):
        result = requests.post(
            url=DocomoCVClient.__build_url('feedbackToCandidate'),
            params={'APIKEY': self.api_key, 'recognitionId': recognition_id, 'itemId': item_id, 'isValid': DocomoCVClient.__valid_to_str(is_valid)},
            json={'comment': comment},
            headers={'Content-Type': 'application/json;charset=UTF-8'})
        result.raise_for_status()

    @staticmethod
    def __build_url(name, version='v1'):
        return DocomoCVClient.__api_path.format({'version': version, 'name': name})

    @staticmethod
    def __valid_to_str(is_valid):
        return 'true' if is_valid else 'false'

    __api_path = 'https://api.apigw.smt.docomo.ne.jp/imageRecognition/{0[version]}/{0[name]}'
