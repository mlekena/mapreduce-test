#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from operator import itemgetter
import sys


for line in sys.stdin:
    line = line.split(',')
    Location = line[24]
    if Location == "": 
        Location = "no_location"
    print ('%s\t%s' % (Location,1))

