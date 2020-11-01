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

def main():
    attempts = 0
    missed_attempts = 0
    EMPTY = ""
    player = EMPTY
    for linein in sys.stdin:
        player_attempt = linein.split('\t')
        print(player_attempt[1].strip())
        missed_attempts += 1 if player_attempt[1].strip() == 'missed' else 0
        attempts += 1
        if player == EMPTY:
            player = player_attempt[0]
        
    print("{}\t{}".format(player, missed_attempts/attempts))
if __name__ == "__main__":
    main()