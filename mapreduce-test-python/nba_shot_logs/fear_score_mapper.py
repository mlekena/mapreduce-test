#!/usr/bin/python3
# --*-- coding:utf-8 --*--

"""
input type to output type
<All the data> --> <<Player>, <Nearest_defender, Shot_result>>
@author Theko Lekena, Suzanne Zhen, Dylan Smith
"""
import re
import sys


def main():
    # Given expected input data, pattern has a runtime of 0ms... nice right!!
    pattern_m = re.compile(
        "(?P<shot_made>missed|made),(?P<defender_name>(\".*,(?!,).*\")|(\\w*)),.*,(?P<player_name>\\w*\\s\\w*),")

    for line in sys.stdin:
        line.strip()
        match = pattern_m.search(line)
        if match:
            n_defender = ''.join(match.group('defender_name').split(" "))
            shot_made = match.group('shot_made').strip()
            player_name = match.group('player_name').strip()
            print("{}\t{};{}".format(player_name, n_defender, shot_made))


if __name__ == "__main__":
    main()
