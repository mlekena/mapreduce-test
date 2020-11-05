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

