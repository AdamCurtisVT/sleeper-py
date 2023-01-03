import requests

class Leagues():
    """
        Calls the Sleeper API for league information.
    """
    
    @classmethod
    def get_all_leagues(self, user_id, sport, season):
        """ 
            This endpoint retrieves all leagues for a specific user.
            Only NFL is supported for the sport.
        """
        endpoint = 'https://api.sleeper.app/v1/user/{}/leagues/{}/{}'.format(user_id, sport, season)
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            leagues = list()
            for league in response.json():
                leagues.append(league)
            return leagues
        else:
            return None

    @classmethod
    def get_league(self, league_id):
        """
            This endpoint retrieves a specific league.
        """
        endpoint = 'https://api.sleeper.app/v1/league/{}'.format(league_id)
        response = requests.get(endpoint)
    
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @classmethod
    def get_rosters(self, league_id):
        """
            This endpoint retrieves all rosters in a league.
        """
        endpoint = 'https://api.sleeper.app/v1/league/{}/rosters'.format(league_id)
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            rosters = list()
            for roster in response.json():
                rosters.append(roster)
            return rosters
        else:
            return None

    @classmethod
    def get_users(self, league_id):
        """
            This endpoint retrieves all users in a league.
        """
        endpoint = 'https://api.sleeper.app/v1/league/{}/users'.format(league_id)
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            users = list()
            for user in response.json():
                users.append(user)
            return users
        else:
            return None

    @classmethod
    def get_matchups(self, league_id, week):
        """ 
            This endpoint retrieves all matchups in a league for the given week.
            Each object in the list represents one team. The two teams with the same matchup_id match up against each other.
            The starters is in an ordered list of player_ids, and players is a list of all player_ids in this matchup.
            The bench can be deduced by removing the starters from the players field. 
        """
        endpoint = 'https://api.sleeper.app/v1/league/{}/matchups/{}'.format(league_id, week)
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            matchups = list()
            for matchup in response.json():
                matchups.append(matchup)
            return matchups
        else:
            return None

    @classmethod
    def get_winners_playoff_bracket(self, league_id):
        """
            This endpoint retrieves the winners playoff bracket for a league for 4, 6, and 8 team playoffs.
            Each row represents a matchup between 2 teams.
            r int The round for this matchup, 1st, 2nd, 3rd round, etc.
            m int The match id of the matchup, unique for all matchups within a bracket.
            t1 int The roster_id of a team in this matchup OR {w: 1} which means the winner of match id 1
            t2 int The roster_id of the other team in this matchup OR {l: 1} which means the loser of match id 1
            w int The roster_id of the winning team, if the match has been played.
            l int The roster_id of the losing team, if the match has been played.
            t1_from object Where t1 comes from, either winner or loser of the match id, necessary to show bracket progression.
            t2_from object Where t2 comes from, either winner or loser of the match id, necessary to show bracket progression.
        """
        endpoint = 'https://api.sleeper.app/v1/league/{}/winners_bracket'.format(league_id)
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @classmethod
    def get_losers_playoff_bracket(self, league_id):
        """
            This endpoint retrieves the playoff bracket for a league for 4, 6, and 8 team playoffs.
            Each row represents a matchup between 2 teams.
            r int The round for this matchup, 1st, 2nd, 3rd round, etc.
            m int The match id of the matchup, unique for all matchups within a bracket.
            t1 int The roster_id of a team in this matchup OR {w: 1} which means the winner of match id 1
            t2 int The roster_id of the other team in this matchup OR {l: 1} which means the loser of match id 1
            w int The roster_id of the winning team, if the match has been played.
            l int The roster_id of the losing team, if the match has been played.
            t1_from object Where t1 comes from, either winner or loser of the match id, necessary to show bracket progression.
            t2_from object Where t2 comes from, either winner or loser of the match id, necessary to show bracket progression.
        """
        endpoint = 'https://api.sleeper.app/v1/league/{}/losers_bracket'.format(league_id)
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None

    @classmethod
    def get_transactions(self, league_id, round):
        """
            This endpoint retrieves all free agent transactions, waivers and trades.
        """
        endpoint = 'https://api.sleeper.app/v1/league/{}/transactions/{}'.format(league_id, round)
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            transactions = list()
            for transaction in response.json():
                transactions.append(transaction)
            return transactions
        else:
            return None

    @classmethod
    def get_traded_picks(self, league_id):
        """
            This endpoint retrieves all traded picks in a league, including future picks.
        """
        endpoint = 'https://api.sleeper.app/v1/league/{}/traded_picks'.format(league_id)
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            picks = list()
            for pick in response.json():
                picks.append(pick)
            return picks
        else:
            return None

    @classmethod
    def get_state(self, sport):
        """
            This endpoint returns information about the current state for any sport.
        """
        endpoint = 'https://api.sleeper.app/v1/state/{}'.format(sport)
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None
