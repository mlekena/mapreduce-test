#!/usr/bin/python
# --*-- coding:utf-8 --*--

"""
input type to output type
<All the data> --> <Nearest_defender, Shot_result>
@author Theko Lekena, Suzanne Zhen, Dylan Smith
"""
import re
import sys
import csv


def main():
    # Given expected input data, pattern has a runtime of 0ms... nice right!!
    pattern_m = re.compile("(?P<shot_made>missed|made),(?P<n_defender>(\".*,(?!,).*\")|(\\w*)),")
    # pattern = re.compile("(\d*),\".*\",[A|H],[W|L],\d{2},\d,\d,\d:\d{2},\d*\.\d,\d,\d\.\d,\d*.\d*,\d*,(?P<shot_made>made|missed),(?P<nearest_defender>\".*\"),.*")

    # pattern_2 although slower is less prone to failed due to missing data.
    # pattern_2 = re.compile(".*,(?P<shot_made>made|missed),(?P<nearest_defender>\".*\"),.*")
    for line in sys.stdin:
        line.strip()
        match = pattern_m.search(line)
        if match:
            print("{}\t{}".format(match.group('n_defender'),match.group('shot_made')))

if __name__ == "__main__":
    main()