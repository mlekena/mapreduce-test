#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""
<<PLAYER, SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK>, HIT_RATE> --> <<PLAYER>, <ZONES>>
@author Theko Lekena, Suzanne Zhen, Dylan Smith
"""
import sys


def main():
    players = set()
    for line in sys.stdin:
        sline = line.strip().split('\t')
        if sline[0] not in players:
            print("{}: {}".format(*sline))
            players.add(sline[0])


if __name__ == "__main__":
    main()
