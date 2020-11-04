#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""
input type to output type
<Nearest_defender, Shot_result> --> <Nearest_defender, fear_factor> where 
fear_factor = missed_shots/total_shot_attempts
@author Theko Lekena, Suzanne Zhen, Dylan Smith
"""
import re
import sys
import csv
from operator import itemgetter

def main():
    
    player_fearscore = {}
    for linein in sys.stdin:
        player_attempt = linein.split('\t')
        player = player_attempt[0]
        player.strip()
        player_data = player_fearscore.get(player, [0, 0])
        player_data[0] += 1 if player_attempt[1].strip() == 'missed' else 0
        player_data[1] += 1
        player_fearscore[player] = player_data
    player_scores = list(map(lambda p_fs: (p_fs[0], p_fs[1][0]/p_fs[1][1]), player_fearscore.items()))

    player_scores.sort( key=itemgetter(1))
    player_scores.reverse()
    print("{}\t{}".format(*player_scores[0]))

if __name__ == "__main__":
    main()