#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from operator import itemgetter
import sys

dict_tix_count = {}

for line in sys.stdin:
    line = line.strip()
    time, num = line.split('\t')
    try:
        num = int(num)
        dict_tix_count[time] = dict_tix_count.get(time, 0) + num

    except ValueError:
        pass

sorted_dict_tix_count = sorted(
    dict_tix_count.items(), key=itemgetter(1), reverse=True)
for time, count in sorted_dict_tix_count[0:500]:
    print '%s\t%s' % (time, count)
