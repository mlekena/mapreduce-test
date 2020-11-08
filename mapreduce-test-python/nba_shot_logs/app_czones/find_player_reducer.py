#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""
<<PLAYER>, <ZONES>> --> <<PLAYER>, <ZONES>>
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
