from .api import *


class Summoner(API):
    def __init__(self, region: str):
        super().__init__(region, 4, 'summoner')

    def by_account(self, account):
        return self.get('summoners', f'by-account/{account}')

    def by_name(self, name):
        return self.get('summoners', f'by-name/{name}')

    def by_puuid(self, puuid):
        return self.get('summoners', f'by-puuid/{puuid}')

    def by_encrypted_summoner_id(self, summoner_id):
        return self.get('summoners', f'{summoner_id}')
