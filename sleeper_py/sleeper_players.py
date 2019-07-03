#-------------------------------------------------
# Imports
#-------------------------------------------------
import json
import requests
import sys

#-------------------------------------------------
# Classes
#-------------------------------------------------

# Represents a Sleeper.app player.
class Player(object):
    Age = None
    BirthCountry = None
    College = None
    DepthChartOrder = None
    DepthChartPosition = None
    EspnId = None
    FantasyDataId = None
    FantasyPositions = None
    FirstName = None
    Hashtag = None
    Height = None
    InjuryStartDate = None
    InjuryStatus = None
    LastName = None
    Number = None
    PlayerId = None
    Position = None
    PracticeParticipation = None
    RotowireId = None
    RotoworldId = None
    SearchFirstName = None
    SearchFullName = None
    SearchLastName = None
    SearchRank = None
    Sport = None
    SportradarId = None
    StatsId = None
    Status = None
    Team = None
    Weight = None
    YahooId = None
    YearsExp = None

    # Initializes a new instance of the Player class.
    def __init__(self, jsonText):
        self.Age = jsonText['age']
        self.BirthCountry = jsonText['birth_country']
        self.College = jsonText['college']
        self.DepthChartOrder = jsonText['depth_chart_order']
        self.DepthChartPosition = jsonText['depth_chart_position']
        self.EspnId = jsonText['espn_id']
        self.FantasyDataId = jsonText['fantasy_data_id']
        self.FantasyPositions = jsonText['fantasy_positions']
        self.FirstName = jsonText['first_name']
        self.Hashtag = jsonText['hashtag']
        self.Height = jsonText['height']
        self.InjuryStartDate = jsonText['injury_start_date']
        self.InjuryStatus = jsonText['injury_status']
        self.LastName = jsonText['last_name']
        self.Number = jsonText['number']
        self.PlayerId = jsonText['player_id']
        self.Position = jsonText['position']
        self.PracticeParticipation = jsonText['practice_participation']
        self.RotowireId = jsonText['rotowire_id']
        self.RotoworldId = jsonText['rotoworld_id']
        self.SearchFirstName = jsonText['search_first_name']
        self.SearchFullName = jsonText['search_full_name']
        self.SearchLastName = jsonText['search_last_name']
        self.SearchRank = jsonText['search_rank']
        self.Sport = jsonText['sport']
        self.SportradarId = jsonText['sportradar_id']
        self.StatsId = jsonText['stats_id']
        self.Status = jsonText['status']
        self.Team = jsonText['team']
        self.Weight = jsonText['weight']
        self.YahooId = jsonText['yahoo_id']
        self.YearsExp = jsonText['years_exp']

# Represents a Sleeper.app trending player.
class TrendingPlayer(object):
    Count = None
    PlayerId = None
    Type = None
    
    # Initializes a new instance of the TrendingPlayer class.
    def __init__(self, jsonText, type):
        self.Count = jsonText['count']
        self.PlayerId = jsonText['player_id']
        self.Type = type

#-------------------------------------------------
# Functions
#-------------------------------------------------

# Call the Sleeper API to retrieve players.
def GetPlayers():
    endpoint = 'https://api.sleeper.app/v1/players/nfl'
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        players = list()
        for playerKey in responseJson.keys():
            playerJson = responseJson[playerKey]
            players.append(Player(playerJson))
        return players
    else:
        return None

# Call the Sleeper API to retrieve trending players.
def GetTrendingPlayers(sport, type, lookbackHours, limit):
    if not sport:
        raise ValueError('The Sport must not be null.') 
    if not type:
        raise ValueError('The Type must not be null.')
    if not lookbackHours:
        lookbackHours = 24
    if not limit:
        limit = 25     

    endpoint = ('https://api.sleeper.app/v1/players/{}/trending/{}?lookback_hours={}&limit={}'.format(sport, type, lookbackHours, limit))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        trendingPlayers = list()
        for trendingPlayerJson in responseJson:
            trendingPlayers.append(TrendingPlayer(trendingPlayerJson, type))
        return trendingPlayers
    else:
        return None
        