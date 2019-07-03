#-------------------------------------------------
# Imports
#-------------------------------------------------
import json
import requests
import sys

#-------------------------------------------------
# Classes
#-------------------------------------------------

# Represents a Sleeper.app draft
class Draft(object):
    Created = None
    Creators = None
    DraftId = None
    DraftOrder = None
    LastMessageId = None
    LastMessageTime = None
    LastPicked = None
    LeagueId = None
    Metadata = None
    Season = None
    SeasonType = None
    Settings = None
    Sport = None
    StartTime = None
    Status = None
    Type = None
    
    # Initializes a new instance of the Draft class.
    def __init__(self, jsonText):
        self.Created = jsonText['created']
        self.Creators = jsonText['creators']
        self.DraftId = jsonText['draft_id']
        self.DraftOrder = jsonText['draft_order']
        self.LastMessageId = jsonText['last_message_id']
        self.LastMessageTime = jsonText['last_message_time']
        self.LastPicked = jsonText['last_picked']
        self.LeagueId = jsonText['league_id']
        self.Metadata = DraftMetadata(jsonText['metadata'])
        self.Season = jsonText['season']
        self.SeasonType = jsonText['season_type']
        self.Settings = DraftSettings(jsonText['settings'])
        self.Sport = jsonText['sport']
        self.Start_time = jsonText['start_time']
        self.Status = jsonText['status']
        self.Type = jsonText['type']

# Represents Sleeper.app draft metadata.
class DraftMetadata(object):
    Description = None
    Name = None
    ScoringType = None

    # Initializes a new instance of the DraftMetadata class.
    def __init__(self, jsonText):
        self.Description = jsonText['description']
        self.Name = jsonText['name']
        self.ScoringType = jsonText['scoring_type']

# Represents a Sleeper.app draft pick.
class DraftPick(object):
    DraftId = None
    DraftSlot = None
    IsKeeper = None
    Metadata = None
    PickNumber = None
    PickedBy = None
    PlayerId = None
    RosterId = None
    Round = None

    # Initializes a new instance of the DraftPick class.
    def __init__(self, jsonText):
        self.DraftId = jsonText['draft_id']
        self.DraftSlot = jsonText['draft_slot']
        self.IsKeeper = jsonText['is_keeper']
        self.Metadata = DraftPickMetadata(jsonText['metadata'])
        self.PickNumber = jsonText['pick_no']
        self.PickedBy = jsonText['picked_by']
        self.PlayerId = jsonText['player_id']
        self.RosterId = jsonText['roster_id']
        self.Round = jsonText['round']

# Represents a Sleeper.app draft pick metadata.
class DraftPickMetadata(object):
    FirstName = None
    InjuryStatus = None
    LastName = None
    NewsUpdated = None
    Number = None
    PlayerId = None
    Position = None
    Sport = None
    Status = None
    Team = None

    # Initializes a new instance of the DraftPickMetadata class.
    def __init__(self, jsonText):
        self.FirstName = jsonText['first_name']
        self.InjuryStatus = jsonText['injury_status']
        self.LastName = jsonText['last_name']
        self.NewsUpdated = jsonText['news_updated']
        self.Number = jsonText['number']
        self.PlayerId = jsonText['player_id']
        self.Position = jsonText['position']
        self.Sport = jsonText['sport']
        self.Status = jsonText['status']
        self.Team = jsonText['team']
        
# Represents Sleeper.app draft settings.
class DraftSettings(object):
    AlphaSort = None
    CpuAutopick = None
    PickTimer = None
    PlayerType = None
    Rounds = None
    SlotsDef = None
    SlotsFlex = None
    SlotsK = None
    SlotsQb = None
    SlotsRb = None
    SlotsTe = None
    SlotsWr = None
    Teams = None

    # Initializes a new instance of the DraftSettings class.
    def __init__(self, jsonText):
        self.AlphaSort = jsonText['alpha_sort']
        self.CpuAutopick = jsonText['cpu_autopick']
        self.PickTimer = jsonText['pick_timer']
        self.PlayerType = jsonText['player_type']
        self.Rounds = jsonText['rounds']
        self.SlotsDef = jsonText['slots_def']
        self.SlotsFlex = jsonText['slots_flex']
        self.SlotsK = jsonText['slots_k']
        self.SlotsQb = jsonText['slots_qb']
        self.SlotsRb = jsonText['slots_rb']
        self.SlotsTe = jsonText['slots_te']
        self.SlotsWr = jsonText['slots_wr']
        self.Teams = jsonText['teams']

# Represents a Sleeper.app traded draft pick.
class TradedDraftPick(object):
    OwnerId = None
    PreviousOwnerId = None
    RosterId = None
    Round = None
    Season = None

    # Initializes a new instance of the TradedDraftPick class.
    def __init__(self, jsonText):
        if 'season' in jsonText:
            self.Season = jsonText['season']
        if 'round' in jsonText:
            self.Round = jsonText['round']
        if 'roster_id' in jsonText:
            self.RosterId = jsonText['roster_id']
        if 'previous_owner_id' in jsonText:
            self.PreviousOwnerId = jsonText['previous_owner_id']
        if 'owner_id' in jsonText:
            self.OwnerId = jsonText['owner_id']

#-------------------------------------------------
# Functions
#-------------------------------------------------

# Call the Sleeper API to retrieve a specific draft.
def GetDraft(draftId):
    if not draftId:
        raise ValueError('The Draft ID must not be null.') 

    endpoint = ('https://api.sleeper.app/v1/draft/{}'.format(draftId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        return Draft(responseJson)
    else:
        return None

# Call the Sleeper API to retrieve all drafts for a specific user.
def GetDraftsForUser(userId, sport, season):
    if not userId:
        raise ValueError('The User ID must not be null.') 
    if not sport:
        raise ValueError('The Sport must not be null.') 
    if not season:
        raise ValueError('The Season must not be null.') 

    endpoint = ('https://api.sleeper.app/v1/user/{}/drafts/{}/{}'.format(userId, sport, season))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        drafts = list()
        for draftJson in responseJson:
            drafts.append(Draft(draftJson))
        return drafts
    else:
        return None

# Call the Sleeper API to retrieve all drafts for a specific league.
def GetDraftsForLeague(leagueId):
    if not leagueId:
        raise ValueError('The League ID must not be null.')

    endpoint = ('https://api.sleeper.app/v1/league/{}/drafts'.format(leagueId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        drafts = list()
        for draftJson in responseJson:
            drafts.append(Draft(draftJson))
        return drafts
    else:
        return None

# Call the Sleeper API to retrieve all draft picks for a specific draft.
def GetDraftPicks(draftId):
    if not draftId:
        raise ValueError('The Draft ID must not be null.')

    endpoint = ('https://api.sleeper.app/v1/draft/{}/picks'.format(draftId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        draftPicks = list()
        for draftPickJson in responseJson:
            draftPicks.append(DraftPick(draftPickJson))
        return draftPicks
    else:
        return None

# Call the Sleeper API to retrieve all traded draft picks for a specific draft.
def GetTradedDraftPicks(draftId):
    if not draftId:
        raise ValueError('The Draft ID must not be null.')

    endpoint = ('https://api.sleeper.app/v1/draft/{}/traded_picks'.format(draftId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        draftPicks = list()
        for draftPickJson in responseJson:
            draftPicks.append(TradedDraftPick(draftPickJson))
        return draftPicks
    else:
        return None
        