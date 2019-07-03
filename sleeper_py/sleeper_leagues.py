#-------------------------------------------------
# Imports
#-------------------------------------------------
import json
import requests
import sys

#-------------------------------------------------
# Classes
#-------------------------------------------------

# Represents a Sleeper.app draft pick.
class DraftPick(object):
    OwnerId = None
    PreviousOwnerId = None
    RosterId = None
    Round = None
    Season = None

    # Initializes a new instance of the DraftPick class.
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

# Represents a Sleeper.app league.
class League(object):
    AvatarId = None
    BracketId = None
    CompanyId = None
    DraftId = None
    GroupId  = None
    LastAuthorAvatar = None
    LastAuthorDisplayName = None
    LastAuthorId = None
    LastAuthorIsBot = None
    LastMessageAttachment = None
    LastMessageId = None
    LastMessageText = None
    LastMessageTextMap = None
    LastMessageTime = None
    LastPinnedMessageId = None
    LastReadId = None
    LeagueId = None
    LoserBracketId = None
    Metadata = None
    Name = None
    PreviousLeagueId = None
    RosterPositions = None
    ScoringSettings = None
    Season = None
    SeasonType = None
    Settings = None
    Shard = None
    Sport = None
    Status = None
    TotalRosters = None
    
    # Initializes a new instance of the League class.
    def __init__(self, jsonText):
        self.AvatarId = jsonText['avatar']
        self.BracketId = jsonText['bracket_id']
        self.CompanyId = jsonText['company_id']
        self.DraftId = jsonText['draft_id']
        self.GroupId  = jsonText['group_id']
        self.LastAuthorAvatar = jsonText['last_author_avatar']
        self.LastAuthorDisplayName = jsonText['last_author_display_name']
        self.LastAuthorId = jsonText['last_author_id']
        self.LastAuthorIsBot = jsonText['last_author_is_bot']
        self.LastMessageAttachment = jsonText['last_message_attachment']
        self.LastMessageId = jsonText['last_message_id']
        self.LastMessageText = jsonText['last_message_text']
        self.LastMessageTextMap = jsonText['last_message_text_map']
        self.LastMessageTime = jsonText['last_message_time']
        self.LastPinnedMessageId = jsonText['last_pinned_message_id']
        self.LastReadId = jsonText['last_read_id']
        self.LeagueId = jsonText['league_id']
        self.LoserBracketId = jsonText['loser_bracket_id']
        self.Metadata = jsonText['metadata']
        self.Name = jsonText['name']
        self.PreviousLeagueId = jsonText['previous_league_id']
        self.RosterPositions = jsonText['roster_positions']
        self.ScoringSettings = ScoringSettings(jsonText['scoring_settings'])
        self.Season = jsonText['season']
        self.SeasonType = jsonText['season_type']
        self.Settings = LeagueSettings(jsonText['settings'])
        self.Shard = jsonText['shard']
        self.Sport = jsonText['sport']
        self.Status = jsonText['status']
        self.TotalRosters = jsonText['total_rosters']

# Represents Sleeper.app league settings.
class LeagueSettings(object):
    BenchLock = None
    DailyWaivers = None
    DailyWaiversHour = None
    DailyWaiversLastRan = None
    DraftRounds = None
    LastReport = None
    LeagueAverageMatch = None
    Leg = None
    MaxKeepers = None
    NumberOfTeams = None
    OffseasonAdds = None
    PickTrading = None
    PlayoffTeams = None
    PlayoffType = None
    PlayoffWeekStart = None
    ReserveAllowDoubtful = None
    ReserveAllowOut = None
    ReserveAllowSuspended = None
    ReserveSlots = None
    StartWeek = None
    TaxiAllowVets = None
    TaxiDeadline = None
    TaxiSlots = None
    TaxiYears = None
    TradeDeadline = None
    TradeReviewDays = None
    Type = None
    WaiverBudget = None
    WaiverClearDays = None
    WaiverDayOfWeek = None
    WaiverType = None

    # Initializes a new instance of the LeagueSettings class.
    def __init__(self, jsonText):
        self.BenchLock = jsonText['bench_lock']
        self.DailyWaivers = jsonText['daily_waivers']
        self.DailyWaiversHour = jsonText['daily_waivers_hour']
        self.DailyWaiversLastRan = jsonText['daily_waivers_last_ran']
        self.DraftRounds = jsonText['draft_rounds']
        self.LastReport = jsonText['last_report']
        self.LeagueAverageMatch = jsonText['league_average_match']
        self.Leg = jsonText['leg']
        self.MaxKeepers = jsonText['max_keepers']
        self.NumberOfTeams = jsonText['num_teams']
        self.OffseasonAdds = jsonText['offseason_adds']
        self.PickTrading = jsonText['pick_trading']
        self.PlayoffTeams = jsonText['playoff_teams']
        self.PlayoffType = jsonText['playoff_type']
        self.PlayoffWeekStart = jsonText['playoff_week_start']
        self.ReserveAllowDoubtful = jsonText['reserve_allow_doubtful']
        self.ReserveAllowOut = jsonText['reserve_allow_out']
        self.ReserveAllowSuspended = jsonText['reserve_allow_sus']
        self.ReserveSlots = jsonText['reserve_slots']
        self.StartWeek = jsonText['start_week']
        self.TaxiAllowVets = jsonText['taxi_allow_vets']
        self.TaxiDeadline = jsonText['taxi_deadline']   
        self.TaxiSlots = jsonText['taxi_slots']
        self.TaxiYears = jsonText['taxi_years']
        self.TradeDeadline = jsonText['trade_deadline']
        self.TradeReviewDays = jsonText['trade_review_days']
        self.Type = jsonText['type']
        self.WaiverBudget = jsonText['waiver_budget']
        self.WaiverClearDays = jsonText['waiver_clear_days']
        self.WaiverDayOfWeek = jsonText['waiver_day_of_week']
        self.WaiverType = jsonText['waiver_type']

# Represents a Sleeper.app league user.
class LeagueUser(object):
    AllowPn = None 
    AvatarId = None
    DisplayName = None   
    IsBot = False
    IsOwner = False
    LeagueId = None 
    MentionPn = None 
    PlayerNicknameUpdate = None
    Settings = None
    TeamName = None 
    TeamNameUpdate = None
    TransactionWaiver = None
    TransactionTrade = None
    TransactionFreeAgent = None
    TransactionCommissioner = None
    UserId = None
    UserMessage = None

    # Initializes a new instance of the LeagueUser class.
    def __init__(self, jsonText):
        self.AvatarId = jsonText['avatar']
        self.DisplayName = jsonText['display_name']
        self.IsBot = jsonText['is_bot']
        self.IsOwner = jsonText['is_owner']
        self.LeagueId = jsonText['league_id']
        self.Settings = jsonText['settings']
        self.UserId = jsonText['user_id']
        self.AllowPn = jsonText['metadata']['allow_pn']
        self.MentionPn = jsonText['metadata']['mention_pn']

        if 'player_nickname_update' in jsonText:
           self.PlayerNicknameUpdate = jsonText['metadata']['player_nickname_update']  
        if 'team_name' in jsonText:
            self.TeamName = jsonText['metadata']['team_name']
        if 'team_name_update' in jsonText:
           self.TeamNameUpdate = jsonText['metadata']['team_name_update']
        if 'transaction_waiver' in jsonText:
           self.TransactionWaiver = jsonText['metadata']['transaction_waiver']
        if 'transaction_trade' in jsonText:
           self.TransactionTrade = jsonText['metadata']['transaction_trade']
        if 'transaction_free_agent' in jsonText:
           self.TransactionFreeAgent = jsonText['metadata']['transaction_free_agent']
        if 'transaction_commissioner' in jsonText:
           self.TransactionCommissioner = jsonText['metadata']['transaction_commissioner']      
        if 'user_message_pn' in jsonText:
           self.UserMessage = jsonText['metadata']['user_message_pn']

# Represents a Sleeper.app matchup.
class Matchup(object):
    CustomPoints = None
    MatchupId = None
    Players = None
    Points = None       
    RosterId = None
    Starters = None

# Initializes a new instance of the Matchup class.
    def __init__(self, jsonText):
        self.CustomPoints = jsonText['custom_points']
        self.MatchupId = jsonText['matchup_id']
        self.Players = jsonText['players']
        self.Points = jsonText['points']
        self.RosterId = jsonText['roster_id']
        self.Starters = jsonText['starters']

# Represents a Sleeper.app roster.
class Roster(object):
    LeagueId = None
    Metadata = None
    OwnerId = None
    PlayerMap = None
    Players = None
    Reserve = None
    RosterId = None
    Settings = None       
    Starters = None
    Taxi = None

    # Initializes a new instance of the Roster class.
    def __init__(self, jsonText):
        self.LeagueId = jsonText['league_id']
        self.Metadata = jsonText['metadata']
        self.OwnerId = jsonText['owner_id']
        self.PlayerMap = jsonText['player_map']
        self.Players = jsonText['players']
        self.Reserve = jsonText['reserve']
        self.RosterId = jsonText['roster_id']
        self.Settings = RosterSettings(jsonText['settings'])
        self.Starters = jsonText['starters']
        self.Taxi = jsonText['taxi']

# Represents Sleeper.app roster settings.
class RosterSettings(object):
    FantasyPoints = None
    FantasyPointsAgainst = None
    FantasyPointsAgainstDecimal = None
    FantasyPointsDecimal = None
    Losses = None
    Ties = None
    TotalMoves = None
    WaiverBudgetUsed = None
    WaiverPosition = None
    Wins = None

    # Initializes a new instance of the RosterSettings class.
    def __init__(self, jsonText):
        self.Losses = jsonText['losses']
        self.Ties = jsonText['ties']
        self.TotalMoves = jsonText['total_moves']
        self.WaiverBudgetUsed = jsonText['waiver_budget_used']
        self.WaiverPosition = jsonText['waiver_position']
        self.Wins = jsonText['wins']
        if 'fpts' in jsonText:
            self.FantasyPoints = jsonText['fpts']
        if 'fpts_against' in jsonText:
            self.FantasyPointsAgainst = jsonText['fpts_against']
        if 'fpts_decimal' in jsonText:
            self.FantasyPointsDecimal = jsonText['fpts_decimal']
        if 'fpts_against_decimal' in jsonText:
            self.FantasyPointsAgainstDecimal = jsonText['fpts_against_decimal']

class ScoringSettings(object):
    BlockedKick = None
    DefensiveTouchdown = None
    ExtraPointMade = None
    ExtraPointMissed = None
    FieldGoalMade = None
    FieldGoalMadeBetween0And19 = None
    FieldGoalMadeBetween20And29 = None
    FieldGoalMadeBetween30And39 = None
    FieldGoalMadeBetween40And49 = None
    FieldGoalMadeOver50 = None
    FieldGoalMissed = None
    ForcedFumble = None    
    Fumble = None
    FumbleLost = None
    FumbleRecovery = None   
    Interception = None
    PassingInterception = None
    PassingTouchdown = None
    PassingTwoPointConversion = None
    PassingYard = None
    PointsAllowed0 = None
    PointsAllowedBetween14And20 = None
    PointsAllowedBetween1And6 = None
    PointsAllowedBetween21And27 = None
    PointsAllowedBetween28And34 = None
    PointsAllowedBetween7And13 = None
    PointsAllowedOver35 = None
    ReceivingTouchdown = None    
    ReceivingYard = None
    Reception = None
    RushingTouchdown = None
    RushingYard = None
    Sack = None
    Safety = None
    SpecialTeamsForcedFumble = None
    SpecialTeamsFumbleRecovery = None
    SpecialTeamsTouchdown = None
    TwoPointReception = None

    # Initializes a new instance of the ScoringSettings class.
    def __init__(self, jsonText):        
        self.BlockedKick = jsonText['blk_kick']
        self.DefensiveTouchdown = jsonText['def_td']
        self.ExtraPointMade = jsonText['xpm']
        self.ExtraPointMissed = jsonText['xpmiss']
        self.FieldGoalMade = jsonText['fgm']
        self.FieldGoalMadeBetween0And19 = jsonText['fgm_0_19']
        self.FieldGoalMadeBetween20And29 = jsonText['fgm_20_29']
        self.FieldGoalMadeBetween30And39 = jsonText['fgm_30_39']
        self.FieldGoalMadeBetween40And49 = jsonText['fgm_40_49']
        self.FieldGoalMadeOver50 = jsonText['fgm_50p']
        self.FieldGoalMissed = jsonText['fgmiss']
        self.ForcedFumble = jsonText['ff']       
        self.Fumble = jsonText['fum']
        self.FumbleLost = jsonText['fum_lost']
        self.FumbleRecovery = jsonText['fum_rec']        
        self.Interception = jsonText['int']
        self.PassingInterception = jsonText['pass_int']
        self.PassingTouchdown = jsonText['pass_td']
        self.PassingTwoPointConversion = jsonText['pass_2pt']
        self.PassingYard = jsonText['pass_yd']
        self.PointsAllowed0 = jsonText['pts_allow_0']
        self.PointsAllowedBetween14And20 = jsonText['pts_allow_14_20']
        self.PointsAllowedBetween1And6 = jsonText['pts_allow_1_6']
        self.PointsAllowedBetween21And27 = jsonText['pts_allow_21_27']
        self.PointsAllowedBetween28And34 = jsonText['pts_allow_28_34'] 
        self.PointsAllowedBetween7And13 = jsonText['pts_allow_7_13']
        self.PointsAllowedOver35 = jsonText['pts_allow_35p']
        self.ReceivingTouchdown = jsonText['rec_td']        
        self.ReceivingYard = jsonText['rec_yd']
        self.Reception = jsonText['rec']
        self.RushingTouchdown = jsonText['rush_td']
        self.RushingYard = jsonText['rush_yd']
        self.Sack = jsonText['sack']  
        self.Safety = jsonText['safe']
        self.SpecialTeamsForcedFumble = jsonText['st_ff']
        self.SpecialTeamsFumbleRecovery = jsonText['st_fum_rec']
        self.SpecialTeamsTouchdown = jsonText['st_td']
        self.TwoPointReception = jsonText['rec_2pt']

class Transaction(object):
    Adds = None
    ConsenterIds = None
    Created = None
    Creator = None
    DraftPicks = None
    Drops = None
    Leg = None
    Metadata = None
    RosterIds = None
    Settings = None
    Status = None
    StatusUpdated = None
    TransactionId = None
    Type = None
    WaiverBudget = None

    # Initializes a new instance of the Transaction class.
    def __init__(self, jsonText):    
        self.Adds = jsonText['adds']
        self.ConsenterIds = jsonText['consenter_ids']
        self.Created = jsonText['created']
        self.Creator = jsonText['creator']
        self.DraftPicks = DraftPick(jsonText['draft_picks'])
        self.Drops = jsonText['drops']
        self.Leg = jsonText['leg']
        self.Metadata = jsonText['metadata']
        self.RosterIds = jsonText['roster_ids']
        self.Status = jsonText['status']        
        self.StatusUpdated = jsonText['status_updated']
        self.TransactionId = jsonText['transaction_id']
        self.Type = jsonText['type']
        self.WaiverBudget = WaiverBudget(jsonText['waiver_budget'])
        if 'settings' in jsonText:
            self.Settings = jsonText['settings']

# Represents a Sleeper.app waiver budget.
class WaiverBudget(object):
    Amount = None
    Receiver = None
    Sender = None

    # Initializes a new instance of the WaiverBudget class.
    def __init__(self, jsonText):
        if 'sender' in jsonText:
            self.Sender = jsonText['sender']
        if 'receiver' in jsonText:
            self.Receiver = jsonText['receiver']
        if 'amount' in jsonText:
            self.Amount = jsonText['amount']

#-------------------------------------------------
# Functions
#-------------------------------------------------

# Call the Sleeper API to retrieve all league for a specific user in a season.
def GetLeaguesForUser(userId, sport, season):
    if not userId:
        raise ValueError('The User ID must not be null.')
    if not season:
        raise ValueError('The season must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/user/{}/leagues/{}/{}'.format(userId, sport, season))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        leagues = list()
        for leagueJson in responseJson:
            leagues.append(League(leagueJson))
        return leagues
    else:
        return None

# Call the Sleeper API to retrieve a specific league.
def GetLeague(leagueId):
    if not leagueId:
        raise ValueError('The League ID must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/league/{}'.format(leagueId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        return League(responseJson)
    else:
        return None

# Call the Sleeper API to retrieve all rosters in a specific league.
def GetLeagueRosters(leagueId):
    if not leagueId:
        raise ValueError('The League ID must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/league/{}/rosters'.format(leagueId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        rosters = list()
        for rosterJson in responseJson:
            rosters.append(Roster(rosterJson))
        return rosters
    else:
        return None

# Call the Sleeper API to retrieve all users in a specific league.
def GetLeagueUsers(leagueId):
    if not leagueId:
        raise ValueError('The League ID must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/league/{}/users'.format(leagueId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        users = list()
        for userJson in responseJson:
            users.append(LeagueUser(userJson))
        return users
    else:
        return None 

# Call the Sleeper API to retrieve all matchups in a league for the specified week.
def GetLeagueMatchups(leagueId, week):
    if not leagueId:
        raise ValueError('The League ID must not be null.') 
    if not week:
        raise ValueError('The week must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/league/{}/matchups/{}'.format(leagueId, week))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        matchups = list()
        for matchupJson in responseJson:
            matchups.append(Matchup(matchupJson))
        return matchups
    else:
        return None

# Call the Sleeper API to retrieve all transactions in a league for the specified week.
def GetLeagueTransactions(leagueId, week):
    if not leagueId:
        raise ValueError('The League ID must not be null.') 
    if not week:
        raise ValueError('The week must not be null.') 
    endpoint = ('https://api.sleeper.app/v1/league/{}/transactions/{}'.format(leagueId, week))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        transactions = list()
        for transactionJson in responseJson:
            transactions.append(Transaction(transactionJson))
        return transactions
    else:
        return None

# Call the Sleeper API to retrieve all traded picks in a league.
def GetTradedPicks(leagueId):
    if not leagueId:
        raise ValueError('The League ID must not be null.') 

    endpoint = ('https://api.sleeper.app/v1/league/{}/traded_picks'.format(leagueId))
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        responseJson = json.loads(response.text)
        tradedPicks = list()
        for draftPickJson in responseJson:
            tradedPicks.append(DraftPick(draftPickJson))
        return tradedPicks
    else:
        return None
        