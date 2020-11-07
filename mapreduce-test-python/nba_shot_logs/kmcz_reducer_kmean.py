#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""

<player_data, nearest_k_group_number> --> <<player_data, new_k_means_group_centroids>

@author Theko Lekena, Suzanne Zhen, Dylan Smith
"""
import re
import sys
from functools import reduce
import math
from util_belt import sum_arrays, to_numbers, centroid_to_string


def calc_group_centroid(group_members):
    n = len(group_members)
    reduced_group = reduce(lambda lhs_gmember, rhs_gmember: sum_arrays(
        lhs_gmember, rhs_gmember), group_members)
    return list(map(lambda x: x/n, reduced_group))


def main():
    player_ks_map = {}
    for line in sys.stdin:
        try:
            sline = line.strip().split('\t')  # <<player_stats>, group_ID>
            k_id = int(sline[1].strip())  # throws
            player_stats = sline[0].strip().split(',')
            player = player_stats[0].strip()
            player_ks_map[player] = player_ks_map.get(player, {})
            player_ks = player_ks_map[player]
            player_ks[k_id] = player_ks.get(k_id, [])
            player_ks[k_id].append(
                to_numbers(player_stats[1].strip().split(';'))
            )
        except ValueError:
            pass

    for player in player_ks_map:
        k_centroids = []
        for k in player_ks_map[player]:
            k_centroids.append(calc_group_centroid(
                player_ks_map[player][k]))

        for k in player_ks_map[player]:
            # print(k_centroids)
            # print(k_centroids[0])
            # ','.join(k_centroids[0])
            # ','.join(k_centroids[1])
            # ','.join(k_centroids[2])
            # ','.join(k_centroids[3])
            centroids_str = centroid_to_string(k_centroids)

            for zone in player_ks_map[player][k]:
                zone_str = ['%10.3f' % z for z in zone]
                print("{}\t{}\t{}".format(
                    player, ';'.join(zone_str), '|'.join(centroids_str)))


if __name__ == "__main__":
    main()
