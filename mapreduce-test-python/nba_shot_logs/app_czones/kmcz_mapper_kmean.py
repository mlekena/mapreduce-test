#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""
<All the data> --> <<PLAYER, SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK>, HIT_RATE>
@author Theko Lekena, Suzanne Zhen, Dylan Smith
"""
import re
import sys
from functools import reduce
import math
# https://stackoverflow.com/a/18207652
from util_belt import euc_dist, to_numbers


def main():
    for line in sys.stdin:
        sline = line.strip().split('\t')
        player = sline[0].strip()
        zone = to_numbers(sline[1].strip().split(';'))
        # [kzone1, kzone2, kzone3, kzone4]
        kzones_raw = sline[2].strip().split('|')
        kzones = list(map(lambda kzone: to_numbers(
            kzone.split(',')), kzones_raw))
        k_euc_distance = list(map(lambda kzone: euc_dist(zone, kzone), kzones))
        # print(k_euc_distance)
        clostest_k = k_euc_distance.index(min(k_euc_distance))
        print("{},{}\t{}".format(sline[0], sline[1], clostest_k))

        # print("{}\t{};{};{}".format(*selected_fields))


if __name__ == "__main__":
    # print("{} = {}".format(euc_dist([-1, 2,3], [4,0,-3]), math.sqrt(65)))
    main()
