from lolapi import api_manager
import requests
import json
from typing import Dict


class API(object):
    def __init__(self, region: str, version: int, api: str):
        self._region = region
        self._version = version
        self._url = f'https://{region}.api.riotgames.com/lol/{api}/v{version}'

    @property
    def region(self) -> str:
        return self._region

    @property
    def version(self) -> int:
        return self._version

    @property
    def url(self) -> str:
        return self._url

    def get(self, sub_api: str, method: str = None, params: Dict[str, str] = None):
        url = f'{self._url}/{sub_api}'
        if method:
            url += f'/{method}'
        result = requests.get(url, params, headers={'X-Riot-Token': api_manager.api_key})
        # noinspection PyProtectedMember
        api_manager._api_request()
        if api_manager.raise_for_status:
            result.raise_for_status()
        return json.loads(result.text)
