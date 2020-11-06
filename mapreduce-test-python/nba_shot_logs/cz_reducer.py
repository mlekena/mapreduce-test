#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""
input type to output type
<<PLAYER, SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK>, HIT_RATE> --> <PLAYER, <PLAYER, SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK>> where 
fear_factor = missed_shots/total_shot_attempts
@author Theko Lekena, Suzanne Zhen, Dylan Smith
"""
import re
import sys
import csv
from operator import itemgetter

sought_after_players = []

class HitRate(object):
    def __init__(self, t_made_count = 0, t_taken = 0):
        self.made_count = t_made_count
        self.taken = t_taken
    
    def get_hit_rate(self):
        return self.made_count/self.taken

    def add_shot_made(self):
        self.made_count += 1
        self.taken += 1
    
    def shot_taken(self):
        self.taken += 1


def main():
    player_stats_map = {}
    for line in sys.stdin:
        line.strip()
        sline = line.split('\t')
        print(line)
        player_stats = sline[0].split(';')
        player_stats_map[player_stats[0]] = player_stats_map.get(player_stats[0], {})
        player_m = player_stats_map[player_stats[0]]
        stats = tuple(player_stats[1:])
        player_m[stats] = player_m.get(stats, HitRate())
        if sline[1].strip() == 'made':
            player_m[stats].add_shot_made()
        else:
            player_m[stats].shot_taken()
    
    player_cz = {}
    for k in player_stats_map.keys():
        player_stat = player_stats_map[k]
        czs = list(map(lambda ps: (ps[0], ps[1].get_hit_rate()), player_stat.items()))
        czs.sort(key=itemgetter(1))
        player_cz[k] = czs[-1]

    if sought_after_players:
        for player in sought_after_players:
            print('{}\t==>\t{}'.format(player, player_cz.get(player, 'NOT INFO')))
    else:
        for p_cz in player_cz.items():
            print('{}\t==>\t{}'.format(p_cz[0], p_cz[1]))

if __name__ == "__main__":
    main()