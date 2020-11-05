#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function
import re
import sys
 


for line in sys.stdin:
    line = line.split(',')
    time = line[19][:2] + '00' + line[19][-1:]
    print ('%s\t%s' % (time,1))

