from .api import *


class Match(API):
    def __init__(self, region: str):
        super().__init__(region, 4, 'match')

    def match(self, match_id):
        return self.get('matches', f'{match_id}')

    def by_account(self, account):
        return self.get('matchlists', f'by-account/{account}')

    def match_timeline(self, match_id):
        return self.get('timelines', f'by-match/{match_id}')

    def tournament_matches(self, tournament_code):
        return self.get('matches', f'by-tournament-code/{tournament_code}/ids')

    def by_tournament_code(self, match_id, tournament_code):
        return self.get('matches', f'{match_id}/by-tournament-code/{tournament_code}')
