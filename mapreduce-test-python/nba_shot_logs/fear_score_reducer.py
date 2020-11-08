#!/usr/bin/python3
# --*-- coding:utf-8 --*--

"""
input type to output type
<<Player>, <Nearest_defender, Shot_result>> --> <Player, <Nearest_defender, fear_factor>> where 
fear_factor = missed_shots/total_shot_attempts
@author Theko Lekena, Suzanne Zhen, Dylan Smith
"""
import re
import sys
import csv
from operator import itemgetter


def main():
    player_fearscore = {}
    for line in sys.stdin:
        sline = line.strip().split('\t')
        player = sline[0].strip()
        def_shot = sline[1].strip().split(";")
        defender_name = def_shot[0].strip()
        shot_attempt = def_shot[1].strip()
        player_fearscore[player] = player_fearscore.get(player, {})
        fear_map = player_fearscore[player]
        fear_map[defender_name] = fear_map.get(defender_name, [0, 0])
        score_stats = fear_map[defender_name]
        if shot_attempt == "missed":
            score_stats[0] += 1
            score_stats[1] += 1
        else:
            score_stats[1] += 1

    for player in player_fearscore:
        player_defender_fscore_map = list(map(lambda def_stats: (
            def_stats[0], (def_stats[1][0] / def_stats[1][1]) * def_stats[1][0]),
            player_fearscore[player].items()))
        most_feared = sorted(
            player_defender_fscore_map, reverse=True, key=itemgetter(1))[0]
        print("{}\t{} feared rated: {}".format(player, *most_feared))


if __name__ == "__main__":
    main()
