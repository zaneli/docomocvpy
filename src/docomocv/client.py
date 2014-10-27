import requests
from enum import Enum
from urllib.parse import urlencode


class DocomoCVClient(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def recognize(self, img_file, recog, numOfCandidates=10):
        with open(img_file, mode='rb') as f:
            result = requests.post(
                url=DocomoCVClient.__build_url('recognize', APIKEY=self.api_key, recog=recog.value, numOfCandidates=numOfCandidates),
                data=f.read(),
                headers={'Content-Type': 'application/octet-stream'})
            result.raise_for_status()
            return result.json()

    @staticmethod
    def __build_url(name, version='v1', **kwargs):
        url = DocomoCVClient.__api_path.format({'version':version, 'name':name})
        return url + '?' + urlencode(kwargs)

    __api_path = 'https://api.apigw.smt.docomo.ne.jp/imageRecognition/{0[version]}/{0[name]}'


class Recog(Enum):
    all='product-all'
    book='book'
    cd='cd'
    dvd='dvd'
    game='game'
    software='software'
    food='food'
