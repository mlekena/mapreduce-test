#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function
import sys
alpha="abcdefghijklmnopqrstuvwxyz"
oth=["oth","non","noc","unk","no"]


for line in sys.stdin:
    line = line.split(',')
    color = line[33]
    color=color.lower(); Color=""
    for i in range(len(color)):
	if color[i] in alpha: Color=Color+color[i]
    color=Color.upper()
    if color == "" or Color[:3] in oth:
            color = "UNKNOWN"
    elif color in ['BK', 'BL', 'BLK', 'B', 'BKBL', 'DKBL', 'BLBL','BKL', 'BKNO', 'BKBK', 'BLA', 'BLAC', 'BLAK', 'BLCK' ]:
            color = "BLACK"
    elif color in ['GY', 'GR', 'GRY', 'GL', 'GRAY','LTGY', 'LTG', 'DKGY', 'GYGY','DKGR', 'GRGY', 'GYGR', 'G']:
            color = "GREY"
    elif color in ['W','WH','WHE', 'WHI','WHIT', 'WHT','WHTE', 'WHTIE', 'WHTN','WHWH','WT', 'WHITE']:
            color = "WHITE"
    elif color in ['YELLO','Y','YL', 'YEL', 'YELL', 'YW']:
            color ='YELLOW'
    elif color in ['SIL', 'SILVE', 'SILV', 'SL','SLV', 'SLVR']:
            color = "SILVER"
    elif color in ['BLU']:
            color = 'BLUE'
    elif color in ['RD','R']:
            color ="RED"
    elif color in ['BRN', 'BRO', 'BRW','BR']:
            color = "BROWN"
    elif color in ['TN','T']: color = 'TAN'
    elif color == 'GRN': color = 'GREEN'
    elif color[:3] in ['MAR','MR','M']: color = 'MAROON'
    elif color[:2] in ['ON','OR']: color = 'ORANGE'
    print ('%s\t%s' % (color,1))

