#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from operator import itemgetter
import sys

dict_color_count = {}

for line in sys.stdin:
    line = line.strip()
    color, num = line.split('\t')
    try:
        num = int(num)
        dict_color_count[color] = dict_color_count.get(color, 0) + num

    except ValueError:
        pass

def arrange(x,y,k=10):
    l1=len(x)
    k=k-l1
    return str(x)+" "*k+str(y)

sorted_dict_color_count = sorted(dict_color_count.items(), key=itemgetter(1), reverse = True)
for color, count in sorted_dict_color_count[:200]:
     print (arrange(color, count))

