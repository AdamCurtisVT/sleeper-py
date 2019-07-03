# -------------------------------------------------
# Imports
# -------------------------------------------------
import json
import requests
import sys

# -------------------------------------------------
# Classes
# -------------------------------------------------

# Represents a Sleeper.app stat.
class Stat(object):
    CompletionPercentage = None
    ExtraPointsAttempted = None
    ExtraPointsMade = None
    FieldGoalsAttempted = None
    FieldGoalsMade = None
    FieldGoalsMade0To19 = None
    FieldGoalsMade20To29 = None
    FieldGoalsMade30Plus = None
    FieldGoalsMade30To39 = None
    FieldGoalsMade40To49 = None
    FieldGoalsMade50Plus = None
    FieldGoalsMadePercentage = None
    FieldGoalsMadeTotalYards = None
    FieldGoalsMissed = None
    Fumbles = None
    FumblesLost = None
    GamesActive = None
    GamesPlayed = None
    GamesStarted = None
    Humidity = None
    IndividualDefensivePlayerQuarterbackHit = None
    IndividualDefensivePlayerQuarterbackSack = None
    IndividualDefensivePlayerQuarterbackTackleForLoss = None
    IndividualDefensivePlayerQuarterbackTackleSolo = None
    IndividualDefensivePlayerQuarterbackTackles = None
    InterceptionReturnYards = None
    Interceptions = None
    OffensiveSnaps = None
    PassingAttempts = None
    PassingCompletions = None
    PassingCompletions40Plus = None
    PassingFirstDowns = None
    PassingIncomple = None
    PassingInterceptions = None
    PassingRating = None
    PassingTouchdowns = None
    PassingTouchdowns40Plus = None
    PassingYards = None
    PassingYardsPerAttempt = None
    PassingYardsPerCompletion = None
    PlayerId = None
    PointsAllowed = None
    PointsAllowed1To6 = None
    PuntAverage = None
    PuntLong = None
    PuntYards = None
    PuntsInsideTheTwenty = None
    PuntsInsideTheTwenty = None
    QuarterbackHits = None
    Receptions = None
    RecievingFirstDowns = None
    RecievingLong = None
    RecievingPercentage = None
    RecievingTouchdowns = None
    RecievingYards = None
    RecievingYardsPerReception = None
    RecievingYardsPerTouchdown = None
    RushingAttempts = None
    RushingTouchdowns = None
    RushingYards = None
    RushingYardsPerAttempt = None
    SackYards = None
    Sacks = None
    SpecialTeamSnaps = None
    TackleAssists = None
    TacklesForLoss = None
    TacklesSolo = None
    TeamDefensiveSnaps = None
    TeamOffensiveSnaps = None
    TeamSpecialTeamSnaps = None
    Temperature = None
    TotalPointsHalfPPR = None
    TotalPointsPPR = None
    TotalPointsStandard = None
    Touchdowns = None
    WideReceiverReceptionBonus = None
    WindSpeed = None
    YardsAllowed = None
    YardsAllowed200To299 = None

    # Initializes a new instance of the Stat class.
    def __init__(self, playerId, jsonText):
        self.PlayerId = playerId
        if 'cmp_pct' in jsonText:
            self.CompletionPercentage = jsonText['cmp_pct']
        if 'xpa' in jsonText:
            self.ExtraPointsAttempted = jsonText['xpa']
        if 'xpm' in jsonText:
            self.ExtraPointsMade = jsonText['xpm']
        if 'fga' in jsonText:
            self.FieldGoalsAttempted = jsonText['fga']
        if 'fgm' in jsonText:
            self.FieldGoalsMade = jsonText['fgm']
        if 'fgm_0_19' in jsonText:
            self.FieldGoalsMade0To19 = jsonText['fgm_0_19']
        if 'sefgm_20_29ason' in jsonText:
            self.FieldGoalsMade20To29 = jsonText['fgm_20_29']
        if 'fgm_yds_over_30' in jsonText:
            self.FieldGoalsMade30Plus = jsonText['fgm_yds_over_30']
        if 'fgm_30_39' in jsonText:
            self.FieldGoalsMade30To39 = jsonText['fgm_30_39']
        if 'fgm_40_49' in jsonText:
            self.FieldGoalsMade40To49 = jsonText['fgm_40_49']
        if 'fgm_50p' in jsonText:
            self.FieldGoalsMade50Plus = jsonText['fgm_50p']
        if 'fgm_pct' in jsonText:
            self.FieldGoalsMadePercentage = jsonText['fgm_pct']
        if 'fgm_yds' in jsonText:
            self.FieldGoalsMadeTotalYards = jsonText['fgm_yds']
        if 'fgmiss' in jsonText:
            self.FieldGoalsMissed = jsonText['fgmiss']
        if 'fum' in jsonText:
            self.Fumbles = jsonText['fum']
        if 'fum_lost' in jsonText:
            self.FumblesLost = jsonText['fum_lost']
        if 'gms_active' in jsonText:
            self.GamesActive = jsonText['gms_active']
        if 'gp' in jsonText:
            self.GamesPlayed = jsonText['gp']
        if 'gs' in jsonText:
            self.GamesStarted = jsonText['gs']
        if 'pass_att' in jsonText:
            self.PassingAttempts = jsonText['pass_att']
        if 'pass_cmp' in jsonText:
            self.PassingCompletions = jsonText['pass_cmp']
        if 'pass_cmp_40p' in jsonText:
            self.PassingCompletions40Plus = jsonText['pass_cmp_40p']
        if 'pass_fd' in jsonText:
            self.PassingFirstDowns = jsonText['pass_fd']
        if 'pass_inc' in jsonText:
            self.PassingIncomple = jsonText['pass_inc']
        if 'pass_int' in jsonText:
            self.PassingInterceptions = jsonText['pass_int']
        if 'pass_rtg' in jsonText:
            self.PassingRating = jsonText['pass_rtg']
        if 'pass_td' in jsonText:
            self.PassingTouchdowns = jsonText['pass_td']
        if 'pass_td_40p' in jsonText:
            self.PassingTouchdowns40Plus = jsonText['pass_td_40p']
        if 'pass_yd' in jsonText:
            self.PassingYards = jsonText['pass_yd']
        if 'pass_ypa' in jsonText:
            self.PassingYardsPerAttempt = jsonText['pass_ypa']
        if 'pass_ypc' in jsonText:
            self.PassingYardsPerCompletion = jsonText['pass_ypc']
        if 'rush_att' in jsonText:
            self.RushingAttempts = jsonText['rush_att']
        if 'rush_td' in jsonText:
            self.RushingTouchdowns = jsonText['rush_td']
        if 'rush_yd' in jsonText:
            self.RushingYards = jsonText['rush_yd']
        if 'rush_ypa' in jsonText:
            self.RushingYardsPerAttempt = jsonText['rush_ypa']
        if 'pts_half_ppr' in jsonText:
            self.TotalPointsHalfPPR = jsonText['pts_half_ppr']
        if 'pts_ppr' in jsonText:
            self.TotalPointsPPR = jsonText['pts_ppr']
        if 'pts_std' in jsonText:
            self.TotalPointsStandard = jsonText['pts_std']
        if 'bonus_rec_wr' in jsonText:
            self.WideReceiverReceptionBonus = jsonText['bonus_rec_wr']
        if 'humidity' in jsonText:
            self.Humidity = jsonText['humidity']
        if 'idp_qb_hit' in jsonText:
            self.IndividualDefensivePlayerQuarterbackHit = jsonText['idp_qb_hit']
        if 'pts_sidp_sacktd' in jsonText:
            self.IndividualDefensivePlayerQuarterbackSack = jsonText['idp_sack']
        if 'idp_tkl' in jsonText:
            self.IndividualDefensivePlayerQuarterbackTackles = jsonText['idp_tkl']
        if 'idp_tkl_loss' in jsonText:
            self.IndividualDefensivePlayerQuarterbackTackleForLoss = jsonText['idp_tkl_loss']
        if 'idp_tkl_solo' in jsonText:
            self.IndividualDefensivePlayerQuarterbackTackleSolo = jsonText['idp_tkl_solo']
        if 'int' in jsonText:
            self.Interceptions = jsonText['int']
        if 'int_ret_yd' in jsonText:
            self.InterceptionReturnYards = jsonText['int_ret_yd']
        if 'off_snp' in jsonText:
            self.OffensiveSnaps = jsonText['off_snp']
        if 'pts_allow' in jsonText:
            self.PointsAllowed = jsonText['pts_allow']
        if 'pts_allow_1_6' in jsonText:
             self.PointsAllowed1To6 = jsonText['pts_allow_1_6']
        if 'punt_avg' in jsonText:
            self.PuntAverage = jsonText['punt_avg']
        if 'punt_in_20' in jsonText:
            self.PuntsInsideTheTwenty = jsonText['punt_in_20']
        if 'punt_lng' in jsonText:
            self.PuntLong = jsonText['punt_lng']
        if 'punt_yds' in jsonText:
            self.PuntYards = jsonText['punt_yds']
        if 'punts' in jsonText:
             self.PuntsInsideTheTwenty = jsonText['punts']
        if 'qb_hit' in jsonText:
            self.QuarterbackHits = jsonText['qb_hit']
        if 'rec' in jsonText:
            self.Receptions = jsonText['rec']
        if 'rec_fd' in jsonText:
            self.RecievingFirstDowns = jsonText['rec_fd']
        if 'rec_lng' in jsonText:
            self.RecievingLong = jsonText['rec_lng']
        if 'rec_pct' in jsonText:
            self.RecievingPercentage = jsonText['rec_pct']
        if 'rec_td' in jsonText:
            self.RecievingTouchdowns = jsonText['rec_td']
        if 'rec_yd' in jsonText:
            self.RecievingYards = jsonText['rec_yd']
        if 'rec_ypr' in jsonText:
            self.RecievingYardsPerReception = jsonText['rec_ypr']
        if 'rec_ypt' in jsonText:
            self.RecievingYardsPerTouchdown = jsonText['rec_ypt']
        if 'sack' in jsonText:
            self.Sacks = jsonText['sack']
        if 'sack_yd' in jsonText:
            self.SackYards = jsonText['sack_yd']
        if 'st_snp' in jsonText:
            self.SpecialTeamSnaps = jsonText['st_snp']
        if 'td' in jsonText:
            self.Touchdowns = jsonText['td']
        if 'temperature' in jsonText:
            self.Temperature = jsonText['temperature']
        if 'tkl_ast' in jsonText:
            self.TackleAssists = jsonText['tkl_ast']
        if 'tkl_loss' in jsonText:
            self.TacklesForLoss = jsonText['tkl_loss']
        if 'tkl_solo' in jsonText:
            self.TacklesSolo = jsonText['tkl_solo']
        if 'tm_def_snp' in jsonText:
            self.TeamDefensiveSnaps = jsonText['tm_def_snp']
        if 'tm_off_snp' in jsonText:
            self.TeamOffensiveSnaps = jsonText['tm_off_snp']
        if 'tm_st_snp' in jsonText:
            self.TeamSpecialTeamSnaps = jsonText['tm_st_snp']
        if 'wind_speed' in jsonText:
            self.WindSpeed = jsonText['wind_speed']
        if 'yds_allow' in jsonText:
            self.YardsAllowed = jsonText['yds_allow']
        if 'yds_allow_200_299' in jsonText:
            self.YardsAllowed200To299 = jsonText['yds_allow_200_299']

# -------------------------------------------------
# Functions
# -------------------------------------------------

# Call the Sleeper API to retrieve stats.
def GetStats(sport, seasonType, season, week):
    if not sport:
        raise ValueError('The sport must not be null.')
    if not seasonType:
        raise ValueError('The season type must not be null.')
    if not season:
        raise ValueError('The season must not be null.')
    if not week:
        raise ValueError('The week must not be null.')

    endpoint = f'https://api.sleeper.app/v1/stats/{sport}/{seasonType}/{season}/{week}'
    response = requests.get(endpoint)

    if response.status_code == 200:
        responseJson = json.loads(response.text)
        stats = list()
        for playerKey in responseJson.keys():
            playerJson = responseJson[playerKey]
            stats.append(Stat(playerKey, playerJson))
        return stats
    else:
        return None

# Call the Sleeper API to retrieve projections.
def GetProjections(sport, seasonType, season, week):
    if not sport:
        raise ValueError('The sport must not be null.')
    if not seasonType:
        raise ValueError('The season type must not be null.')
    if not season:
        raise ValueError('The season must not be null.')
    if not week:
        raise ValueError('The week must not be null.')

    endpoint = f'https://api.sleeper.app/v1/projections/{sport}/{seasonType}/{season}/{week}'
    response = requests.get(endpoint)

    if response.status_code == 200:
        responseJson = json.loads(response.text)
        stats = list()
        for playerKey in responseJson.keys():
            playerJson = responseJson[playerKey]
            stats.append(Stat(playerKey, playerJson))
        return stats
    else:
        return None
        