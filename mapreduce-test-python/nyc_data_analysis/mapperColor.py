#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function
import sys


for line in sys.stdin:
    line = line.split(',')
    color = line[33]
    if color == "":
            color = "none"
    elif color in ['BK', 'BL', 'BLK', 'BK.', 'B', 'BK/', 'BKBL', 'DKBL', 'BL.', 'BLBL','BKL', 'B LAC', 'BK NO', 'BK+', 'BK1', 'BKBK', 'BLA', 'BLAC', 'BLAK', 'BLCK', ]:
            color = "BLACK"
    elif color in ['GY', 'GR', 'GRY', 'GL', 'GRAY','LTGY', 'LTG', 'DKGY', 'GYGY','DKGR', 'GRGY', 'GYGR','GY.', 'GY/', 'G']:
            color = "GREY"
    elif color in ['WH', 'WHI', 'WH/', 'WH.', 'WHIT', 'WHT','WHTE', 'WHT.', 'WHTIE', 'WHTN','WHWH','WT', 'WT.', 'White']:
            color = "WHITE"
    elif color in ['YELLO', 'YEL', 'YELL', 'YW']:
            color ='YELLOW'
    elif color in ['SIL', 'SILVE', 'SILV', 'SL', 'SL.','SLV', 'SLVR']:
            color = "SILVER"
    elif color in ['BLU']:
            color = 'BLUE'
    elif color in ['RD', 'RD/', 'RED.']:
            color ="RED"
    elif color in ['BRN', 'BRO', 'BRW','BR']:
            color = "BROWN"
    print ('%s\t%s' % (color,1))

