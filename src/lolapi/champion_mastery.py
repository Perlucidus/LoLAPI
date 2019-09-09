from .api import *


class ChampionMastery(API):
    def __init__(self, region: str):
        super().__init__(region, 4, 'champion-mastery')

    def masteries(self, summoner_id):
        return self.get('champion-masteries', f'by-summoner/{summoner_id}')

    def mastery(self, summoner_id, champion_id):
        return self.get('champion-masteries', f'by-summoner/{summoner_id}/by-champion/{champion_id}')

    def score(self, summoner_id):
        return self.get('scores', f'by-summoner/{summoner_id}')
