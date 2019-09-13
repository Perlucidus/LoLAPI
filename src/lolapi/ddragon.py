from lolapi import api_manager
import requests
import json


class DDragon:
    def __init__(self, realm: str):
        self._realm = realm
        metadata = requests.get(f'https://ddragon.leagueoflegends.com/realms/{realm}.json')
        if api_manager.raise_for_status:
            metadata.raise_for_status()
        self._meta = json.loads(metadata.text)
        self._cdn = self._meta['cdn'] + '/' + self._meta['v']

    @property
    def realm(self) -> str:
        return self._realm

    @property
    def meta(self):
        return self._meta

    @property
    def cdn(self) -> str:
        return self._cdn

    def get(self, path: str):
        url = f'{self._cdn}/{path}'
        result = requests.get(url)
        if api_manager.raise_for_status:
            result.raise_for_status()
        return json.loads(result.text)
