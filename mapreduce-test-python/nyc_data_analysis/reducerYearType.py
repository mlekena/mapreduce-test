#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from operator import itemgetter
import sys

dict_YearType_count = {}

for line in sys.stdin:
    line = line.strip()
    YearType, num = line.split('\t')
    try:
        num = int(num)
        dict_YearType_count[YearType] = dict_YearType_count.get(YearType, 0) + num

    except ValueError:
        pass


sorted_dict_YearType_count = sorted(dict_YearType_count.items(), key=itemgetter(1), reverse = True)
for YearType, count in sorted_dict_YearType_count[0:300]: 
     print '%s\t%s' % (YearType, count)

