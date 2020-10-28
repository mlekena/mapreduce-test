#!/usr/bin/python
from operator import itemgetter
import sys

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    hour, ip_count = line.split()
    ip, count = ip_count.split(',')
    try:
        num = int(count)
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num

    except ValueError:
        pass


sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(1), reverse=True)[0:3]
for ip, count in sorted_dict_ip_count:
    print '%s\t%s' % (ip, count)
