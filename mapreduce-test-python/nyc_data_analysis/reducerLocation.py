#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from operator import itemgetter
import sys

dict_location_count = {}

for line in sys.stdin:
    line = line.strip()
    location, num = line.split('\t')
    try:
        num = int(num)
        dict_location_count[location] = dict_location_count.get(location, 0) + num

    except ValueError:
        pass


sorted_dict_location_count = sorted(dict_location_count.items(), key=itemgetter(1), reverse = True)
for location, count in sorted_dict_location_count[0:500]: 
     print '%s\t%s' % (location, count)
