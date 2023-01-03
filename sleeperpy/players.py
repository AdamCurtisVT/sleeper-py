import requests

class Players():    
    """
        Calls the Sleeper API for player information.
    """
    
    @classmethod
    def get_all_players(self):
        """
            This endpoint retrieves all NFL players.
            Please use this call sparingly, as it is intended only to be used once per day at most to keep your player IDs updated. The average size of this query is 5MB.
            Since rosters and draft picks contain Player IDs which look like "1042", "2403", "CAR", etc, you will need to know what those IDs map to. The /players call provides you the map necessary to look up any player.
            You should save this information on your own servers as this is not intended to be called every time you need to look up players due to the filesize being close to 5MB in size. You do not need to call this endpoint more than once per day.
        """
        endpoint = 'https://api.sleeper.app/v1/players/nfl'
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            players = list()
            for player in response.json():
                players.append(player)
            return players
        else:
            return None

    @classmethod
    def get_trending_players(self, sport, type, hours, limit):
        """
            This endpoint retrieves a list of trending players based on adds or drops in the past 24 hours.
            Please give attribution to Sleeper if you are using their trending data.

            Parameters:
            sport: The sport, such as nfl
            type: Either add or drop
            lookback_hours: Number of hours to look back
            limit: Number of results you want
        """
        endpoint = 'https://api.sleeper.app/v1/players/{}/trending/{}?lookback_hours={}&limit={}'.format(sport, type, hours, limit)
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            players = list()
            for player in response.json():
                players.append(player)
            return players
        else:
            return None
