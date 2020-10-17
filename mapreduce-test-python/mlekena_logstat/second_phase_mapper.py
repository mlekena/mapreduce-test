#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

#pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
#pat = re.compile('(?P<time>\[\d.:\d.\])(?P<ip_and_count>.*)')
pat = re.compile('\[(?P<time>\d.:\d.)\](?P<ip>\d+.\d+.\d+.\d+)\s+(?P<count>\d)')
for line in sys.stdin:
    match = pat.search(line)
    if match:
        print '%s\t%s,%s' % (match.group('time') ,match.group('ip'), match.group('count'))
