#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function
import sys



for line in sys.stdin:
    line = line.split(',')
    Year = line[35]
    if Year in ["", "0"]:
        Year = "none"
    Type = line[6]
    if Type == "":
        Type = "none"
    match = Year+','+ Type
    print ('%s\t%s' % (match,1))

