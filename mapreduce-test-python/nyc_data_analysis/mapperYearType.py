#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function
import sys
punc='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


for line in sys.stdin:
    line = line.split(',')
    Year = line[35]
    if Year in ["", "0"]:
        Year = "NoYr"
    Type = line[6].strip(punc)
    if Type == "":
        Type = "NoTy"
    Type = Type.upper()
    match = Year+','+ Type
    print ('%s\t%s' % (match,1))
    print ('%s\t%s' % (Year,1))
    print ('%s\t%s' % (Type,1))

