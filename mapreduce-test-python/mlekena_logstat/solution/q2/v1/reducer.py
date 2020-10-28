#!/usr/bin/python
from operator import itemgetter
import sys
import re

dict_ip_count = {}
dict_hour_ip_map = {}
pat = re.compile('\[(?P<time>\d.:\d.)\](?P<ip>\d+.\d+.\d+.\d+)')
for line in sys.stdin:
    line = line.strip()
    ip_and_count, num = line.split('\t')
    match = pat.search(ip_and_count)
    if match:
        dict_hour_ip_map[match.group('time')] = dict_hour_ip_map.get(match.group('time'), {})
        dict_ip_count = dict_hour_ip_map[match.group('time')]
        try:
            ip = match.group('ip')
            num = int(num)
            dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num

        except ValueError:
            pass

sorted_hour_ip_map = sorted(dict_hour_ip_map.items(), key=itemgetter(0))
for hour, ip_count_dict in sorted_hour_ip_map:
    sorted_dict_ip_count = sorted(ip_count_dict.items(), key=itemgetter(1), reverse=True)
    for ip, count in sorted_dict_ip_count[0:3]:
        print '%s\t%s\t%s' % (hour, ip, count)
