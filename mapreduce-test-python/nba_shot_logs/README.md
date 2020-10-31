# NBA Shot Log Analysis
## Table Header
GAME_ID,MATCHUP (0),LOCATION (1), W (2), FINAL_MARGIN (3), SHOT_NUMBER (4), PERIOD (5), GAME_CLOCK (6), SHOT_CLOCK (7), DRIBBLES (8), TOUCH_TIME (9), SHOT_DIST (10), PTS_TYPE (11), SHOT_RESULT (12), CLOSEST_DEFENDER (13), CLOSEST_DEFENDER_PLAYER_ID (14), CLOSE_DEF_DIST (15), FGM (16), PTS (17), player_name (18), player_id (19)  
~numbers not included in heading. Simply added for matching with numeric indexing~  

## Fear Score: NBA Most Feared Defender

Map trajectory:  
<All the data> --> <Nearest_defender, Shot_result>
<Nearest_defender, Shot_result> --> <Nearest_defender, overall_hitrate_near_them>

<Nearest_defender, overall_hitrate_near_them> --> <overall_hitrate_near_them, Nearest_defender>
OR
Sort the output file and return the first line.