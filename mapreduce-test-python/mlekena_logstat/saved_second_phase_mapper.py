#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

#pat = re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')
pat = re.compile('(?P<time>\[\d.:\d.\])(?P<ip_and_count>.*)')
for line in sys.stdin:
    match = pat.search(line)
    if match:
        print '%s\t%s' % (match.group('time') ,match.group('ip_and_count'))
