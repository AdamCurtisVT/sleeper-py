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
    Season = None
    Week = None
    Id = None
    BlockedKicks = None
    BonusPassCompletion_25 = None
    BonusPassYards_300 = None
    BonusPassYards_400 = None
    BonusReceptions_RB = None
    BonusReceptions_TE = None
    BonusReceptions_WR = None
    BonusReceivingYards_100 = None
    BonusRushAttempts_20 = None
    BonusRushReceivingYards_100 = None
    BonusRushReceivingYards_200 = None
    BonusRushYard_100 = None
    BonusRushYard_200 = None
    CompletionPercentage = None
    DefenseKickReturns = None
    DefenseKickReturnLong = None
    DefenseKickReturnYards = None
    DefensePassDefended = None
    DefensePuntReturns = None
    DefensePuntReturnLong = None
    DefensePuntReurnYard = None
    DefenseSnaps = None
    DefenseTouchdowns = None
    ThirdDownAttempts = None
    ThirdDownConversions = None
    ThirdDownPercentage = None
    FourthDownAttempts = None
    FourthDownConversions = None
    FourthDownPercentage = None
    Dropback = None
    FantasyPointsAllowed = None
    FantasyPointsAllowed_K = None
    FantasyPointsAllowed_QB = None
    FantasyPointsAllowed_RB = None
    FantasyPointsAllowed_TE = None
    FantasyPointsAllowed_WR = None
    FirstDowns = None
    ForcedFumble = None
    FieldGoalAttempt = None
    FieldGoalMade = None
    FieldGoalMade_0_19 = None
    FieldGoalMade_20_29 = None
    FieldGoalMade_30_39 = None
    FieldGoalMade_40_49 = None
    FieldGoalMade_50p = None
    FieldGoalMadeLong = None
    FieldGoalMadePercentage = None
    FieldGoalMadeYards = None
    FieldGoalMadeYardsOver30 = None
    FieldGoalMiss = None
    FieldGoalMiss_20_29 = None
    FieldGoalMiss_40_49 = None
    FieldGoalMiss_50p = None
    Fumble = None
    FumbleLost = None
    FumbleRecovered = None
    FumbleReturnYards = None
    Giveaway = None
    GamesActive = None
    GamesPlayed = None
    GamesStarted = None
    Humidity = None
    Interception = None
    InterceptionReturnYards = None
    KickReturn = None
    KickReturnLong = None
    KickReturnYards = None
    KickReturnsYardsPerAttempt = None
    OffensivePlays = None
    OffensiveSnaps = None
    OffensiveYards = None
    OffensiveYardsPerPlay = None
    OpponentFirstDowns = None
    OpponentOffensivePlays = None
    OpponentOffensiveYards = None
    OpponentOffensiveYardsPerPlay = None
    OpponentPassFirstDowns = None
    OpponentRushFirstDowns = None
    OpponentScore = None
    OpponentScoreOvertime = None
    OpponentScoreQuarterOne = None
    OpponentScoreQuarterTwo = None
    OpponentScoreQuarterThree = None
    OpponentScoreQuarterFour = None
    OverUnder = None
    PassTwoPoints = None
    PassAttempts = None
    PassCompletions = None
    PassCompletions_40p = None
    PassFirstDown = None
    PassIncompletions = None
    PassInterceptions = None
    PassInterceptionTouchdowns = None
    PassLong = None
    PassRating = None
    PassSacks = None
    PassSackYards = None
    PassingTouchdowns = None
    PassingTouchdowns_40p = None
    PassYards = None
    PassYardsPerAttempt = None
    PassYardsPerCompletion = None
    Penalty = None
    PenaltyYards = None
    PointSpread = None
    PuntReturn = None
    PuntReturnLong = None
    PuntReturnYards = None
    PuntReturnYardsPerAttempt = None
    PointsAllowed = None
    PointsAllowed_0 = None
    PointsAllowed_1_6 = None
    PointsAllowed_14_20 = None
    PointsAllowed_21_27 = None
    PointsAllowed_28_34 = None
    PointsAllowed_35p = None
    PointsAllowed_7_13 = None
    PointsHalfPpr = None
    PointsPpr = None
    PointsStandard = None
    PuntAverage = None
    Punt_20 = None
    PuntLong = None
    PuntTouchback = None
    PuntYards = None
    Punts = None
    QuarterbackHit = None
    Receptions = None
    Reception_0_4 = None
    Reception_10_19 = None
    Reception_20_29 = None
    ReceptionTwoPoint = None
    Reception_30_39 = None
    Reception_40p = None
    Reception_5_9 = None
    ReceptionFirstDown = None
    ReceptionLong = None
    ReceptionPercentage = None
    ReceptionTouchdown = None
    ReceptionTouchdown_40p = None
    Targets = None
    ReceptionYards = None
    ReceptionsYardPerReception = None
    ReceptionYardsPerTarget = None
    RushTwoPoint = None
    Rush_40p = None
    RushAttempts = None
    RushFirstDowns = None
    RushLong = None
    RushTouchdowns = None
    RushTouchdowns_40p = None
    RushYards = None
    RushYardsPerAttempt = None
    RedZoneAttempts = None
    RedZoneConversions = None
    RedZonePercentage = None
    Sacks = None
    SackYards = None
    Safety = None
    Score = None
    ScoreOvertime = None
    ScoreQuarterOne = None
    ScoreQuarterTwo = None
    ScoreQuarterThree = None
    ScoreQuarterFour = None
    SpecialTeamSnaps = None
    Takeaway = None
    Touchdown = None
    Temperature = None
    TackleAssist = None
    TackleForLoss = None
    TackleSolo = None
    TeamDefensiveSnaps = None
    TeamOffensiveSnaps = None
    TeamSpecialTeamSnaps = None
    TurnoverDifferential = None
    WindSpeed = None
    ExtraPointAttempt = None
    ExtraPointMade = None
    ExtraPointMiss = None
    YardsAllowed = None
    YardsAllowed_0_100 = None
    YardsAllowed_200_299 = None
    YardsAllowed_300_349 = None
    YardsAllowed_350_399 = None
    YardsAllowed_400_449 = None
    YardsAllowed_450_499 = None
    YardsAllowed_500_549 = None
    YardsAllowed_550p = None
    IdpTackleSolo = None
    IdpTackleLoss = None
    IdpTackleAssist = None
    IdpTackle = None
    IdpSack = None
    IdpQbHit = None
    IdpPassDefended = None
    IdpInterception = None
    IdpFumbleRecovered = None
    IdpForcedFumble = None
    IdpDefensiveSnap = None

    # Initializes a new instance of the Stat class.
    def __init__(self, season, week, playerId, jsonText):
        self.Season = season
        self.Week = week
        self.Id = playerId
        
        if 'blk_kick' in jsonText:
            self.BlockedKicks = jsonText['blk_kick']
        if 'bonus_pass_cmp_25' in jsonText:
            self.BonusPassCompletion_25 = jsonText['bonus_pass_cmp_25']
        if 'bonus_pass_yd_300' in jsonText:
            self.BonusPassYards_300 = jsonText['bonus_pass_yd_300']
        if 'bonus_pass_yd_400' in jsonText:
            self.BonusPassYards_400 = jsonText['bonus_pass_yd_400']
        if 'bonus_rec_rb' in jsonText:
            self.BonusReceptions_RB = jsonText['bonus_rec_rb']
        if 'bonus_rec_te' in jsonText:
            self.BonusReceptions_TE = jsonText['bonus_rec_te']
        if 'bonus_rec_wr' in jsonText:
            self.BonusReceptions_WR = jsonText['bonus_rec_wr']
        if 'bonus_rec_yd_100' in jsonText:
            self.BonusReceivingYards_100 = jsonText['bonus_rec_yd_100']
        if 'bonus_rush_att_20' in jsonText:
            self.BonusRushAttempts_20 = jsonText['bonus_rush_att_20']
        if 'bonus_rush_rec_yd_100' in jsonText:
            self.BonusRushReceivingYards_100 = jsonText['bonus_rush_rec_yd_100']
        if 'bonus_rush_rec_yd_200' in jsonText:
            self.BonusRushReceivingYards_200 = jsonText['bonus_rush_rec_yd_200']
        if 'bonus_rush_yd_100' in jsonText:
            self.BonusRushYard_100 = jsonText['bonus_rush_yd_100']
        if 'bonus_rush_yd_200' in jsonText:
            self.BonusRushYard_200 = jsonText['bonus_rush_yd_200']
        if 'cmp_pct' in jsonText:
            self.CompletionPercentage = jsonText['cmp_pct']
        if 'def_kr' in jsonText:
            self.DefenseKickReturns = jsonText['def_kr']
        if 'def_kr_lng' in jsonText:
            self.DefenseKickReturnLong = jsonText['def_kr_lng']
        if 'def_kr_yd' in jsonText:
            self.DefenseKickReturnYards = jsonText['def_kr_yd']
        if 'def_pass_def' in jsonText:
            self.DefensePassDefended = jsonText['def_pass_def']
        if 'def_pr' in jsonText:
            self.DefensePuntReturns = jsonText['def_pr']
        if 'def_pr_lng' in jsonText:
            self.DefensePuntReturnLong = jsonText['def_pr_lng']
        if 'def_pr_yd' in jsonText:
            self.DefensePuntReurnYard = jsonText['def_pr_yd']
        if 'def_snp' in jsonText:
            self.DefenseSnaps = jsonText['def_snp']
        if 'def_td' in jsonText:
            self.DefenseTouchdowns = jsonText['def_td']
        if 'down_3_att' in jsonText:
            self.ThirdDownAttempts = jsonText['down_3_att']
        if 'down_3_conv' in jsonText:
            self.ThirdDownConversions = jsonText['down_3_conv']
        if 'down_3_pct' in jsonText:
            self.ThirdDownPercentage = jsonText['down_3_pct']
        if 'down_4_att' in jsonText:
            self.FourthDownAttempts = jsonText['down_4_att']
        if 'down_4_conv' in jsonText:
            self.FourthDownConversions = jsonText['down_4_conv']
        if 'down_4_pct' in jsonText:
            self.FourthDownPercentage = jsonText['down_4_pct']
        if 'dropback' in jsonText:
            self.Dropback = jsonText['dropback']
        if 'fan_pts_allow' in jsonText:
            self.FantasyPointsAllowed = jsonText['fan_pts_allow']
        if 'fan_pts_allow_k' in jsonText:
            self.FantasyPointsAllowed_K = jsonText['fan_pts_allow_k']
        if 'fan_pts_allow_qb' in jsonText:
            self.FantasyPointsAllowed_QB = jsonText['fan_pts_allow_qb']
        if 'fan_pts_allow_rb' in jsonText:
            self.FantasyPointsAllowed_RB = jsonText['fan_pts_allow_rb']
        if 'fan_pts_allow_te' in jsonText:
            self.FantasyPointsAllowed_TE = jsonText['fan_pts_allow_te']
        if 'fan_pts_allow_wr' in jsonText:
            self.FantasyPointsAllowed_WR = jsonText['fan_pts_allow_wr']
        if 'fd' in jsonText:
            self.FirstDowns = jsonText['fd']
        if 'ff' in jsonText:
            self.ForcedFumble = jsonText['ff']
        if 'fga' in jsonText:
            self.FieldGoalAttempt = jsonText['fga']
        if 'fgm' in jsonText:
            self.FieldGoalMade = jsonText['fgm']
        if 'fgm_0_19' in jsonText:
            self.FieldGoalMade_0_19 = jsonText['fgm_0_19']
        if 'fgm_20_29' in jsonText:
            self.FieldGoalMade_20_29 = jsonText['fgm_20_29']
        if 'fgm_30_39' in jsonText:
            self.FieldGoalMade_30_39 = jsonText['fgm_30_39']
        if 'fgm_40_49' in jsonText:
            self.FieldGoalMade_40_49 = jsonText['fgm_40_49']
        if 'fgm_50p' in jsonText:
            self.FieldGoalMade_50p = jsonText['fgm_50p']
        if 'fgm_lng' in jsonText:
            self.FieldGoalMadeLong = jsonText['fgm_lng']
        if 'fgm_pct' in jsonText:
            self.FieldGoalMadePercentage = jsonText['fgm_pct']
        if 'fgm_yds' in jsonText:
            self.FieldGoalMadeYards = jsonText['fgm_yds']
        if 'fgm_yds_over_30' in jsonText:
            self.FieldGoalMadeYardsOver30 = jsonText['fgm_yds_over_30']
        if 'fgmiss' in jsonText:
            self.FieldGoalMiss = jsonText['fgmiss']
        if 'fgmiss_20_29' in jsonText:
            self.FieldGoalMiss_20_29 = jsonText['fgmiss_20_29']
        if 'fgmiss_40_49' in jsonText:
            self.FieldGoalMiss_40_49 = jsonText['fgmiss_40_49']
        if 'fgmiss_50p' in jsonText:
            self.FieldGoalMiss_50p = jsonText['fgmiss_50p']
        if 'fum' in jsonText:
            self.Fumble = jsonText['fum']
        if 'fum_lost' in jsonText:
            self.FumbleLost = jsonText['fum_lost']
        if 'fum_rec' in jsonText:
            self.FumbleRecovered = jsonText['fum_rec']
        if 'fum_ret_yd' in jsonText:
            self.FumbleReturnYards = jsonText['fum_ret_yd']
        if 'giveaway' in jsonText:
            self.Giveaway = jsonText['giveaway']
        if 'gms_active' in jsonText:
            self.GamesActive = jsonText['gms_active']
        if 'gp' in jsonText:
            self.GamesPlayed = jsonText['gp']
        if 'gs' in jsonText:
            self.GamesStarted = jsonText['gs']
        if 'humidity' in jsonText:
            self.Humidity = jsonText['humidity']
        if 'int' in jsonText:
            self.Interception = jsonText['int']
        if 'int_ret_yd' in jsonText:
            self.InterceptionReturnYards = jsonText['int_ret_yd']
        if 'kr' in jsonText:
            self.KickReturn = jsonText['kr']
        if 'kr_lng' in jsonText:
            self.KickReturnLong = jsonText['kr_lng']
        if 'kr_yd' in jsonText:
            self.KickReturnYards = jsonText['kr_yd']
        if 'kr_ypa' in jsonText:
            self.KickReturnsYardsPerAttempt = jsonText['kr_ypa']
        if 'off_play' in jsonText:
            self.OffensivePlays = jsonText['off_play']
        if 'off_snp' in jsonText:
            self.OffensiveSnaps = jsonText['off_snp']
        if 'off_yd' in jsonText:
            self.OffensiveYards = jsonText['off_yd']
        if 'off_yd_per_play' in jsonText:
            self.OffensiveYardsPerPlay = jsonText['off_yd_per_play']
        if 'opp_fd' in jsonText:
            self.OpponentFirstDowns = jsonText['opp_fd']
        if 'opp_off_play' in jsonText:
            self.OpponentOffensivePlays = jsonText['opp_off_play']
        if 'opp_off_yd' in jsonText:
            self.OpponentOffensiveYards = jsonText['opp_off_yd']
        if 'opp_off_yd_per_play' in jsonText:
            self.OpponentOffensiveYardsPerPlay = jsonText['opp_off_yd_per_play']
        if 'opp_pass_fd' in jsonText:
            self.OpponentPassFirstDowns = jsonText['opp_pass_fd']
        if 'opp_rush_fd' in jsonText:
            self.OpponentRushFirstDowns = jsonText['opp_rush_fd']
        if 'opp_score' in jsonText:
            self.OpponentScore = jsonText['opp_score']
        if 'opp_score_ot' in jsonText:
            self.OpponentScoreOvertime = jsonText['opp_score_ot']
        if 'opp_score_q1' in jsonText:
            self.OpponentScoreQuarterOne = jsonText['opp_score_q1']
        if 'opp_score_q2' in jsonText:
            self.OpponentScoreQuarterTwo = jsonText['opp_score_q2']
        if 'opp_score_q3' in jsonText:
            self.OpponentScoreQuarterThree = jsonText['opp_score_q3']
        if 'opp_score_q4' in jsonText:
            self.OpponentScoreQuarterFour = jsonText['opp_score_q4']
        if 'over_under' in jsonText:
            self.OverUnder = jsonText['over_under']
        if 'pass_2pt' in jsonText:
            self.PassTwoPoints = jsonText['pass_2pt']
        if 'pass_att' in jsonText:
            self.PassAttempts = jsonText['pass_att']
        if 'pass_cmp' in jsonText:
            self.PassCompletions = jsonText['pass_cmp']
        if 'pass_cmp_40p' in jsonText:
            self.PassCompletions_40p = jsonText['pass_cmp_40p']
        if 'pass_fd' in jsonText:
            self.PassFirstDown = jsonText['pass_fd']
        if 'pass_inc' in jsonText:
            self.PassIncompletions = jsonText['pass_inc']
        if 'pass_int' in jsonText:
            self.PassInterceptions = jsonText['pass_int']
        if 'pass_int_td' in jsonText:
            self.PassInterceptionTouchdowns = jsonText['pass_int_td']
        if 'pass_lng' in jsonText:
            self.PassLong = jsonText['pass_lng']
        if 'pass_rtg' in jsonText:
            self.PassRating = jsonText['pass_rtg']
        if 'pass_sack' in jsonText:
            self.PassSacks = jsonText['pass_sack']
        if 'pass_sack_yds' in jsonText:
            self.PassSackYards = jsonText['pass_sack_yds']
        if 'pass_td' in jsonText:
            self.PassingTouchdowns = jsonText['pass_td']
        if 'pass_td_40p' in jsonText:
            self.PassingTouchdowns_40p = jsonText['pass_td_40p']
        if 'pass_yd' in jsonText:
            self.PassYards = jsonText['pass_yd']
        if 'pass_ypa' in jsonText:
            self.PassYardsPerAttempt = jsonText['pass_ypa']
        if 'pass_ypc' in jsonText:
            self.PassYardsPerCompletion = jsonText['pass_ypc']
        if 'penalty' in jsonText:
            self.Penalty = jsonText['penalty']
        if 'penalty_yd' in jsonText:
            self.PenaltyYards = jsonText['penalty_yd']
        if 'point_spread' in jsonText:
            self.PointSpread = jsonText['point_spread']
        if 'pr' in jsonText:
            self.PuntReturn = jsonText['pr']
        if 'pr_lng' in jsonText:
            self.PuntReturnLong = jsonText['pr_lng']
        if 'pr_yd' in jsonText:
            self.PuntReturnYards = jsonText['pr_yd']
        if 'pr_ypa' in jsonText:
            self.PuntReturnYardsPerAttempt = jsonText['pr_ypa']
        if 'pts_allow' in jsonText:
            self.PointsAllowed = jsonText['pts_allow']
        if 'pts_allow_0' in jsonText:
            self.PointsAllowed_0 = jsonText['pts_allow_0']
        if 'pts_allow_1_6' in jsonText:
            self.PointsAllowed_1_6 = jsonText['pts_allow_1_6']
        if 'pts_allow_14_20' in jsonText:
            self.PointsAllowed_14_20 = jsonText['pts_allow_14_20']
        if 'pts_allow_21_27' in jsonText:
            self.PointsAllowed_21_27 = jsonText['pts_allow_21_27']
        if 'pts_allow_28_34' in jsonText:
            self.PointsAllowed_28_34 = jsonText['pts_allow_28_34']
        if 'pts_allow_35p' in jsonText:
            self.PointsAllowed_35p = jsonText['pts_allow_35p']
        if 'pts_allow_7_13' in jsonText:
            self.PointsAllowed_7_13 = jsonText['pts_allow_7_13']
        if 'pts_half_ppr' in jsonText:
            self.PointsHalfPpr = jsonText['pts_half_ppr']
        if 'pts_ppr' in jsonText:
            self.PointsPpr = jsonText['pts_ppr']
        if 'pts_std' in jsonText:
            self.PointsStandard = jsonText['pts_std']
        if 'punt_avg' in jsonText:
            self.PuntAverage = jsonText['punt_avg']
        if 'punt_in_20' in jsonText:
            self.Punt_20 = jsonText['punt_in_20']
        if 'punt_lng' in jsonText:
            self.PuntLong = jsonText['punt_lng']
        if 'punt_tb' in jsonText:
            self.PuntTouchback = jsonText['punt_tb']
        if 'punt_yds' in jsonText:
            self.PuntYards = jsonText['punt_yds']
        if 'punts' in jsonText:
            self.Punts = jsonText['punts']
        if 'qb_hit' in jsonText:
            self.QuarterbackHit = jsonText['qb_hit']
        if 'rec' in jsonText:
            self.Receptions = jsonText['rec']
        if 'rec_0_4' in jsonText:
            self.Reception_0_4 = jsonText['rec_0_4']
        if 'rec_10_19' in jsonText:
            self.Reception_10_19 = jsonText['rec_10_19']
        if 'rec_20_29' in jsonText:
            self.Reception_20_29 = jsonText['rec_20_29']
        if 'rec_2pt' in jsonText:
            self.ReceptionTwoPoint = jsonText['rec_2pt']
        if 'rec_30_39' in jsonText:
            self.Reception_30_39 = jsonText['rec_30_39']
        if 'rec_40p' in jsonText:
            self.Reception_40p = jsonText['rec_40p']
        if 'rec_5_9' in jsonText:
            self.Reception_5_9 = jsonText['rec_5_9']
        if 'rec_fd' in jsonText:
            self.ReceptionFirstDown = jsonText['rec_fd']
        if 'rec_lng' in jsonText:
            self.ReceptionLong = jsonText['rec_lng']
        if 'rec_pct' in jsonText:
            self.ReceptionPercentage = jsonText['rec_pct']
        if 'rec_td' in jsonText:
            self.ReceptionTouchdown = jsonText['rec_td']
        if 'rec_td_40p' in jsonText:
            self.ReceptionTouchdown_40p = jsonText['rec_td_40p']
        if 'rec_tgt' in jsonText:
            self.Targets = jsonText['rec_tgt']
        if 'rec_yd' in jsonText:
            self.ReceptionYards = jsonText['rec_yd']
        if 'rec_ypr' in jsonText:
            self.ReceptionsYardPerReception = jsonText['rec_ypr']
        if 'rec_ypt' in jsonText:
            self.ReceptionYardsPerTarget = jsonText['rec_ypt']
        if 'rush_2pt' in jsonText:
            self.RushTwoPoint = jsonText['rush_2pt']
        if 'rush_40p' in jsonText:
            self.Rush_40p = jsonText['rush_40p']
        if 'rush_att' in jsonText:
            self.RushAttempts = jsonText['rush_att']
        if 'rush_fd' in jsonText:
            self.RushFirstDowns = jsonText['rush_fd']
        if 'rush_lng' in jsonText:
            self.RushLong = jsonText['rush_lng']
        if 'rush_td' in jsonText:
            self.RushTouchdowns = jsonText['rush_td']
        if 'rush_td_40p' in jsonText:
            self.RushTouchdowns_40p = jsonText['rush_td_40p']
        if 'rush_yd' in jsonText:
            self.RushYards = jsonText['rush_yd']
        if 'rush_ypa' in jsonText:
            self.RushYardsPerAttempt = jsonText['rush_ypa']
        if 'rz_att' in jsonText:
            self.RedZoneAttempts = jsonText['rz_att']
        if 'rz_conv' in jsonText:
            self.RedZoneConversions = jsonText['rz_conv']
        if 'rz_pct' in jsonText:
            self.RedZonePercentage = jsonText['rz_pct']
        if 'sack' in jsonText:
            self.Sacks = jsonText['sack']
        if 'sack_yd' in jsonText:
            self.SackYards = jsonText['sack_yd']
        if 'safe' in jsonText:
            self.Safety = jsonText['safe']
        if 'score' in jsonText:
            self.Score = jsonText['score']
        if 'score_ot' in jsonText:
            self.ScoreOvertime = jsonText['score_ot']
        if 'score_q1' in jsonText:
            self.ScoreQuarterOne = jsonText['score_q1']
        if 'score_q2' in jsonText:
            self.ScoreQuarterTwo = jsonText['score_q2']
        if 'score_q3' in jsonText:
            self.ScoreQuarterThree = jsonText['score_q3']
        if 'score_q4' in jsonText:
            self.ScoreQuarterFour = jsonText['score_q4']
        if 'st_snp' in jsonText:
            self.SpecialTeamSnaps = jsonText['st_snp']
        if 'takeaway' in jsonText:
            self.Takeaway = jsonText['takeaway']
        if 'td' in jsonText:
            self.Touchdown = jsonText['td']
        if 'temperature' in jsonText:
            self.Temperature = jsonText['temperature']
        if 'tkl_ast' in jsonText:
            self.TackleAssist = jsonText['tkl_ast']
        if 'tkl_loss' in jsonText:
            self.TackleForLoss = jsonText['tkl_loss']
        if 'tkl_solo' in jsonText:
            self.TackleSolo = jsonText['tkl_solo']
        if 'tm_def_snp' in jsonText:
            self.TeamDefensiveSnaps = jsonText['tm_def_snp']
        if 'tm_off_snp' in jsonText:
            self.TeamOffensiveSnaps = jsonText['tm_off_snp']
        if 'tm_st_snp' in jsonText:
            self.TeamSpecialTeamSnaps = jsonText['tm_st_snp']
        if 'turnover_diff' in jsonText:
            self.TurnoverDifferential = jsonText['turnover_diff']
        if 'wind_speed' in jsonText:
            self.WindSpeed = jsonText['wind_speed']
        if 'xpa' in jsonText:
            self.ExtraPointAttempt = jsonText['xpa']
        if 'xpm' in jsonText:
            self.ExtraPointMade = jsonText['xpm']
        if 'xpmiss' in jsonText:
            self.ExtraPointMiss = jsonText['xpmiss']
        if 'yds_allow' in jsonText:
            self.YardsAllowed = jsonText['yds_allow']
        if 'yds_allow_0_100' in jsonText:
            self.YardsAllowed_0_100 = jsonText['yds_allow_0_100']
        if 'yds_allow_200_299' in jsonText:
            self.YardsAllowed_200_299 = jsonText['yds_allow_200_299']
        if 'yds_allow_300_349' in jsonText:
            self.YardsAllowed_300_349 = jsonText['yds_allow_300_349']
        if 'yds_allow_350_399' in jsonText:
            self.YardsAllowed_350_399 = jsonText['yds_allow_350_399']
        if 'yds_allow_400_449' in jsonText:
            self.YardsAllowed_400_449 = jsonText['yds_allow_400_449']
        if 'yds_allow_450_499' in jsonText:
            self.YardsAllowed_450_499 = jsonText['yds_allow_450_499']
        if 'yds_allow_500_549' in jsonText:
            self.YardsAllowed_500_549 = jsonText['yds_allow_500_549']
        if 'yds_allow_550p' in jsonText:
            self.YardsAllowed_550p = jsonText['yds_allow_550p']
        if 'idp_tkl_solo' in jsonText:
            self.IdpTackleSolo = jsonText['idp_tkl_solo']
        if 'idp_tkl_loss' in jsonText:
            self.IdpTackleLoss = jsonText['idp_tkl_loss']
        if 'idp_tkl_ast' in jsonText:
            self.IdpTackleAssist = jsonText['idp_tkl_ast']
        if 'idp_tkl' in jsonText:
            self.IdpTackle = jsonText['idp_tkl']
        if 'idp_sack' in jsonText:
            self.IdpSack = jsonText['idp_sack']
        if 'idp_qb_hit' in jsonText:
            self.IdpQbHit = jsonText['idp_qb_hit']
        if 'idp_pass_def' in jsonText:
            self.IdpPassDefended = jsonText['idp_pass_def']
        if 'idp_int' in jsonText:
            self.IdpInterception = jsonText['idp_int']
        if 'idp_fum_rec' in jsonText:
            self.IdpFumbleRecovered = jsonText['idp_fum_rec']
        if 'idp_ff' in jsonText:
            self.IdpForcedFumble = jsonText['idp_ff']
        if 'def_snp' in jsonText:
            self.IdpDefensiveSnap = jsonText['def_snp']

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
            stats.append(Stat(season, week, playerKey, playerJson))
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
            stats.append(Stat(season, week, playerKey, playerJson))
        return stats
    else:
        return None
