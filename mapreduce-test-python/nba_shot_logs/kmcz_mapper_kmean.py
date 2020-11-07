#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""
                                                                                                              +                                               +                                +                    +                                                     +                                              
GAME_ID 0, MATCHUP (1), LOCATION (2), W (3), FINAL_MARGIN (4), SHOT_NUMBER (5), PERIOD (6), GAME_CLOCK (7), SHOT_CLOCK (8), DRIBBLES (9), TOUCH_TIME (10), SHOT_DIST (11), PTS_TYPE (12), SHOT_RESULT (13), CLOSEST_DEFENDER (14), CLOSEST_DEFENDER_PLAYER_ID (15), CLOSE_DEF_DIST (16), FGM (17), PTS (18), player_name (19), player_id (20)
21400899,"MAR 04, 2015 - CHA @ BKN",A,W,24,1,1,1:09,+10.8,2,1.9,++7.7,2,+made,"Anderson, Alan",101187,++1.3,1,2,++brian roberts,203148


<All the data> --> <<PLAYER, SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK>, HIT_RATE>
@author Theko Lekena, Suzanne Zhen, Dylan Smith
"""
import re
import sys
from functools import reduce
import math

def euc_dist(lhs, rhs):
    assert(len(lhs) == len(rhs)), "euclidian distance candidates are not the same length. :("
    sum_under = reduce(lambda val1, val2: val1+val2, 
            map(lambda lhs_rhs: (lhs_rhs[0] - lhs_rhs[1])**2,zip(lhs, rhs))
        )
    return math.sqrt(sum_under)

def to_numbers(candidates):
    try:
        the_converted = list(map(lambda s: float(s), candidates))
        return the_converted
    except ValueError:
        print("BAD INPUT: {}".format(candidates))
        exit("Failed to convert integers. Terminating exceptional path.")


def main():
    for line in sys.stdin:
        line.strip()
        sline = line.split('\t')
        player = sline[0].strip()
        zone = to_numbers(sline[1].strip().split(';'))
        kzones_raw = sline[2].strip().split('|')
        kzone = list(map(lambda kzone: to_numbers(kzone.split(',')), kzones_raw))
        # kzone


        # print("{}\t{};{};{}".format(*selected_fields))

if __name__ == "__main__":
    # print("{} = {}".format(euc_dist([-1, 2,3], [4,0,-3]), math.sqrt(65)))
    main()
