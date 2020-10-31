#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""
input type to output type
<All the data> --> <Nearest_defender, Shot_result>
"""
import re
import sys
import csv

SHOT_MADE = 12
CLOSEST_DEFENDER = 13
# (missed|made),((\".*,(?!,).*\")|(\w*)),
pattern = re.compile("(\d*),\".*\",[A|H],[W|L],\d{2},\d,\d,\d:\d{2},\d*\.\d,\d,\d\.\d,\d*.\d*,\d*,(?P<shot_made>made|missed),(?P<nearest_defender>\".*\"),.*")

# pattern_2 although slower is less prone to failed due to missing data.
pattern_2 = re.compile(".*,(?P<shot_made>made|missed),(?P<nearest_defender>\".*\"),.*")
count = 0
for line in sys.stdin:
    line.strip()
    s_line = line.split(',')
    to_find = 'made' if 'made' in s_line else 'missed'
    ndefender_index = s_line.index(to_find) + 2
    data = s_line[s_line.index(to_find): ndefender_index]
    print('{} {}'.format(*data))
    break
#     match = pattern_2.search(line)
#     # all_data = line.split(',')
#     if match:
#         count += 1
#         # print("{} {}".format(match.group('shot_made'), match.group('nearest_defender')))
#     else:
#         print("'{}'".format(line))
#         assert(False), "Match failed"
#     # for s, idx in zip(all_data, range(len(all_data))):
#     #     print(s, idx)
#     # print("{} {}".format(all_data[CLOSEST_DEFENDER], all_data[SHOT_MADE]))
#     # break
# print(count)