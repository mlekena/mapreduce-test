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
from operator import itemgetter
