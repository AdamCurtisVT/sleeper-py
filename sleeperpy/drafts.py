import requests

class Drafts():    
    """
        Calls the Sleeper API for draft information.
    """

    @classmethod
    def get_all_drafts_for_user(self, user_id, sport, season):
        """
            This endpoint retrieves all drafts by a user within the given season for the specified sport.
            Only NFL is supported for the sport.
        """
        endpoint = 'https://api.sleeper.app/v1/user/{}/drafts/{}/{}'.format(user_id, sport, season)
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            drafts = list()
            for draft in response.json():
                drafts.append(draft)
            return drafts
        else:
            return None
    

    @classmethod
    def get_all_drafts_for_league(self, league_id):
        """
            This endpoint retrieves all drafts for a league. Keep in mind that a league can have multiple drafts, especially dynasty leagues.
            Drafts are sorted by most recent to earliest. Most leagues should only have one draft.
        """
        endpoint = 'https://api.sleeper.app/v1/league/{}/drafts'.format(league_id)
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            drafts = list()
            for draft in response.json():
                drafts.append(draft)
            return drafts
        else:
            return None

    @classmethod
    def get_specific_draft(self, draft_id):
        """
            This endpoint retrieves a specific draft.
        """
        endpoint = 'https://api.sleeper.app/v1/draft/{}'.format(draft_id)
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @classmethod
    def get_all_picks_in_draft(self, draft_id):
        """
            This endpoint retrieves all picks in a draft.
        """
        endpoint = 'https://api.sleeper.app/v1/draft/{}/picks'.format(draft_id)
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            picks = list()
            for pick in response.json():
                picks.append(pick)
            return picks
        else:
            return None

    @classmethod
    def get_traded_picks_in_draft(self, draft_id):
        """
            This endpoint retrieves all picks in a draft.
        """
        endpoint = 'https://api.sleeper.app/v1/draft/{}/traded_picks'.format(draft_id)
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            picks = list()
            for pick in response.json():
                picks.append(pick)
            return picks
        else:
            return None
