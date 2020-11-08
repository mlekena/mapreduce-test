#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""
<<PLAYER, SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK>, HIT_RATE> --> <<PLAYER>, <ZONES>>
@author Theko Lekena, Suzanne Zhen, Dylan Smith
"""
import sys

PLAYERS_OF_INTEREST = set(("james harden", "chris paul",
                           "stephen curry", "lebron james", "cody zeller"))


def main():
    for line in sys.stdin:
        sline = line.strip().split('\t')
        player = sline[0].strip().split(',')[0]

        if player in PLAYERS_OF_INTEREST:
            print("{}\t{}".format(player, sline[1]))


if __name__ == "__main__":
    main()
