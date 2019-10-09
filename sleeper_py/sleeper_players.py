# -------------------------------------------------
# Imports
# -------------------------------------------------
import json
import requests
import sys

# -------------------------------------------------
# Classes
# -------------------------------------------------

# Represents a Sleeper.app player.
class Player(object):
    Active = None
    Age = None
    BirthCity = None
    BirthCountry = None
    BirthDate = None
    BirthState = None
    College = None
    DepthChartOrder = None
    DepthChartPosition = None
    EspnId = None
    FantasyDataId = None
    FantasyPositions = None
    FirstName = None
    FullName = None
    GsisId = None
    Hashtag = None
    Height = None
    HighSchool = None
    InjuryBodyPart = None
    InjuryNotes = None
    InjuryStartDate = None
    InjuryStatus = None
    LastName = None
    NewsUpdated = None
    Number = None
    PlayerId = None
    Position = None
    PracticeDescription = None
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
        if 'age' in jsonText:
            self.Age = jsonText['age']
        if 'active' in jsonText:
            self.Active = jsonText['active']
        if 'birth_city' in jsonText:
            self.BirthCity = jsonText['birth_city']
        if 'birth_country' in jsonText:
            self.BirthCountry = jsonText['birth_country']
        if 'birth_date' in jsonText:
            self.BirthDate = jsonText['birth_date']
        if 'birth_state' in jsonText:
            self.BirthState = jsonText['birth_state']
        if 'college' in jsonText:
            self.College = jsonText['college']
        if 'depth_chart_order' in jsonText:
            self.DepthChartOrder = jsonText['depth_chart_order']
        if 'depth_chart_position' in jsonText:
            self.DepthChartPosition = jsonText['depth_chart_position']
        if 'espn_id' in jsonText:
            self.EspnId = jsonText['espn_id']
        if 'fantasy_data_id' in jsonText:
            self.FantasyDataId = jsonText['fantasy_data_id']
        if 'fantasy_positions' in jsonText:
            self.FantasyPositions = jsonText['fantasy_positions']
        if 'first_name' in jsonText:
            self.FirstName = jsonText['first_name']
        if 'gsis_id' in jsonText:
            self.GsisId = jsonText['gsis_id']
        if 'hashtag' in jsonText:
            self.Hashtag = jsonText['hashtag']
        if 'height' in jsonText:
            self.Height = jsonText['height']
        if 'high_school' in jsonText:
            self.HighSchool = jsonText['high_school']
        if 'injury_body_part' in jsonText:
            self.InjuryBodyPart = jsonText['injury_body_part']
        if 'injury_notes' in jsonText:
            self.InjuryNotes = jsonText['injury_notes']
        if 'injury_start_date' in jsonText:
            self.InjuryStartDate = jsonText['injury_start_date']
        if 'injury_status' in jsonText:
            self.InjuryStatus = jsonText['injury_status']
        if 'last_name' in jsonText:
            self.LastName = jsonText['last_name']
        if 'news_updated' in jsonText:
            self.NewsUpdated = jsonText['news_updated']
        if 'number' in jsonText:
            self.Number = jsonText['number']
        if 'player_id' in jsonText:
            self.PlayerId = jsonText['player_id']
        if 'position' in jsonText:
            self.Position = jsonText['position']
        if 'practice_description' in jsonText:
            self.PracticeDescription = jsonText['practice_description']
        if 'practice_participation' in jsonText:
            self.PracticeParticipation = jsonText['practice_participation']
        if 'rotowire_id' in jsonText:
            self.RotowireId = jsonText['rotowire_id']
        if 'rotoworld_id' in jsonText:
            self.RotoworldId = jsonText['rotoworld_id']
        if 'search_first_name' in jsonText:
            self.SearchFirstName = jsonText['search_first_name']
        if 'search_full_name' in jsonText:
            self.SearchFullName = jsonText['search_full_name']
        if 'search_last_name' in jsonText:
            self.SearchLastName = jsonText['search_last_name']
        if 'search_rank' in jsonText:
            self.SearchRank = jsonText['search_rank']
        if 'sport' in jsonText:
            self.Sport = jsonText['sport']
        if 'sportradar_id' in jsonText:
            self.SportradarId = jsonText['sportradar_id']
        if 'stats_id' in jsonText:
            self.StatsId = jsonText['stats_id']
        if 'status' in jsonText:
            self.Status = jsonText['status']
        if 'team' in jsonText:
            self.Team = jsonText['team']
        if 'weight' in jsonText:
            self.Weight = jsonText['weight']
        if 'yahoo_id' in jsonText:
            self.YahooId = jsonText['yahoo_id']
        if 'years_exp' in jsonText:
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

# -------------------------------------------------
# Functions
# -------------------------------------------------

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
