#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function
import re
import sys

def format_time(t):
    ## only care about hour and time of day
    g=t[-1]
    if t[0]==".":t=t.replace(".","")
    if t[0]=="0":t=t[1:]
    if g=="P" or g=="A": t=t[:-1]
    else:g="A"
    try: v=int(t); t=str(v)
    except: return 'misrecorded'
    if v==0: return "1200"+g
    elif len(t)==5:
        if t[2]=='0': t=t[0:2]+t[3:]
    h=int(t[0:2])
    if h<10:pass
    elif h>9 and h<25:
        if h>12: h=h-12; g="P"
    elif h>24:
        if h%10>5: return 'misrecorded'
        else:h=h//10
    if h<10: return "0"+str(h)+"00"+g
    else: return str(h)+"00"+g


for line in sys.stdin:
    line = line.split(',')
    time = line[19][:2] + '00' + line[19][-1:]
    time = format_time(time)
    print ('%s\t%s' % (time,1))

