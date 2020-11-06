#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""
input type to output type
                                                                                                                +                                               +                                +                    +                                                     +                                              
GAME_ID 0, MATCHUP (1), LOCATION (2), W (3), FINAL_MARGIN (4), SHOT_NUMBER (5), PERIOD (6), GAME_CLOCK (7), SHOT_CLOCK (8), DRIBBLES (9), TOUCH_TIME (10), SHOT_DIST (11), PTS_TYPE (12), SHOT_RESULT (13), CLOSEST_DEFENDER (14), CLOSEST_DEFENDER_PLAYER_ID (15), CLOSE_DEF_DIST (16), FGM (17), PTS (18), player_name (19), player_id (20)
21400899,"MAR 04, 2015 - CHA @ BKN",A,W,24,1,1,1:09,+10.8,2,1.9,++7.7,2,+made,"Anderson, Alan",101187,++1.3,1,2,++brian roberts,203148


<All the data> --> <<PLAYER, SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK>, HIT_RATE>
@author Theko Lekena, Suzanne Zhen, Dylan Smith
"""
import re
import sys
OFF_SET = 1 # split creates to cells from the second column due to inner comma
SHOTCLOCKINDEX = 8 + OFF_SET #before defender
SHOTDISTINDEX = 11 + OFF_SET #before defender
CLOSEDEFDISTINDEX = 16 + OFF_SET + 1
PLAYERFIRSTINDEX = 19 + OFF_SET + 1
# PLAYERLASTINDEX = 20
SHOTRESULTINDEX = 13 + OFF_SET #before defender
EMPTY_FIELD = ""
# c = 5
def main():
    for line in sys.stdin:
        line.strip()
        sline = line.split(',')
        if sline[0] == "GAME_ID":
            continue
        if len(sline) != 23:
            continue
        # print(" # ".join(sline))
        # print(len(sline))
        selected_fields = [sline[PLAYERFIRSTINDEX], sline[SHOTDISTINDEX],
                                        sline[CLOSEDEFDISTINDEX], sline[SHOTCLOCKINDEX],
                                        sline[SHOTRESULTINDEX]]
        """Here we have made a decision to invalidate any row with missing data."""
        skip_row = False
        for field in selected_fields:
            if field == EMPTY_FIELD:
                skip_row = True
                break

        if skip_row:
            continue

        print("{};{};{};{}\t{}".format(*selected_fields))

if __name__ == "__main__":
    main()
    # if c < 0:
    #     break
    # c -= 1