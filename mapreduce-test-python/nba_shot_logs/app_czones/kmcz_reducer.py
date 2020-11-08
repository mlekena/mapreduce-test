#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""
input type to output type
<<PLAYER>, <SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK>> --> 
    <<PLAYER, <SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK>, {4}<SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK>> where 
fear_factor = missed_shots/total_shot_attempts

@author Theko Lekena, Suzanne Zhen, Dylan Smith

"""
import re
import sys
from random import randrange

from operator import itemgetter

# (SHOT_DISTANCE, CLOSEDEF_DIST, SHOT_CLOCK)
# Zones = [(20, 5, 15),(15, 1, 3), (10, 5, 3),(5, 5, 6)]


def main():
    player_stats_map = {}
    for line in sys.stdin:
        line.strip()
        sline = line.split('\t')
        player = sline[0].strip()
        player_stats_map[player] = player_stats_map.get(player, [])
        player_stats_map[player].append(sline[1].strip().split(';'))

    player_zones = {}
    for player in player_stats_map:
        pzones = player_stats_map[player]
        random_indexes = []
        while True:
            i = randrange(len(pzones))
            if i not in random_indexes:
                random_indexes.append(i)
            else:
                randrange(len(pzones))

            if len(random_indexes) == 4:
                break
        assert(len(set(random_indexes)) == 4)

        initial_zones = list(map(lambda idx: "{}".format(
            ",".join(pzones[idx])), random_indexes))

        for zone in player_stats_map[player]:
            print("{}\t{}\t{}".format(
                player, ';'.join(zone), '|'.join(initial_zones)))


if __name__ == "__main__":
    main()
