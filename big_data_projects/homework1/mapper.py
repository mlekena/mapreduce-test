#!/usr/bin/python
# --*-- coding:utf-8 --*--
from __future__ import print_function
import re
import sys

def error_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def convert_to_hour_range(input_range):
    rang = input_range.split("-")
    if len(rang) != 2:
        error_print("failed to parse input range. Reverting to default query")
        return None
    try:
        lhs_hour = int(rang[0])
        rhs_hour = int(rang[1])
    except ValueError:
        error_print("failed to convert str range to int. Reverting to default query")
        return None

    return (min(lhs_hour, rhs_hour),max(lhs_hour, rhs_hour))

def in_range(x, the_range):
    return True if x >= the_range[0] and x <= the_range[1] else False

if len(sys.argv) > 2:
    assert(false), "To many command arguments passed in"
hour_range = None if len(sys.argv) == 1 else convert_to_hour_range(sys.argv[1])

pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
for line in sys.stdin:
    match = pat.search(line)
    if match:
        if hour_range:
            try:
                h = int(match.group('hour'))
                if in_range(h, hour_range):
                    print ('%s\t%s' % ('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1))
                   
            except ValueError:
		error_print("hour conversion failure: ", match.group('hour'))
                pass
        else:       
            print('%s\t%s' % ('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1))
