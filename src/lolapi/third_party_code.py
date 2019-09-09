from .api import *


class ThirdPartyCode(API):
    def __init__(self, region: str):
        super().__init__(region, 4, 'platform')

    def by_summoner(self, summoner_id):
        return self.get('third-party-code', f'by-summoner/{summoner_id}')
