from .api import *


class League(API):
    def __init__(self, region: str):
        super().__init__(region, 4, 'league')

    def by_summoner(self, summoner_id):
        return self.get('entries', f'by-summoner/{summoner_id}')

    def entries(self, queue, tier, division, page: int = None):
        params = {}
        if page:
            params = {'page': page}
        return self.get('entries', f'{queue}/{tier}/{division}', params)

    def league(self, league_id):
        return self.get('leagues', f'{league_id}')

    def master_leagues(self, queue):
        return self.get('masterleagues', f'by-queue/{queue}')

    def grandmaster_leagues(self, queue):
        return self.get('grandmasterleagues', f'by-queue/{queue}')

    def challenger_league(self, queue):
        return self.get('challengerleagues', f'by-queue/{queue}')
