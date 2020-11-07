#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from operator import itemgetter
import sys

d_yt = {}
d_y = {}
d_t = {}

for line in sys.stdin:
    line = line.strip()
    key, num = line.split("\t")
    try:
        key = key.split(",")
        if len(key) == 1:
            key = key[0]
            try:
                int(key[:4])
                D = d_y  # append the year dictionary
            except:
                if key == 'NoYr':
                    D = d_y  # year
                else:
                    D = d_t  # append the type dictionary
        elif len(key) == 2:
            key = ",".join(key)
            D = d_yt  # append the year type dictionary
        num = int(num)
        D[key] = D.get(key, 0) + num

    except ValueError:
        pass


def arrange(x, y, k=15):
    x = str(x)
    y = str(y)
    l1 = len(x)
    l2 = len(y)
    k1 = k-l1
    k2 = k-l2
    return str(x)+" "*k1+str(y)+" "*k2


d_YT = sorted(d_yt.items(), key=itemgetter(1), reverse=True)
d_Y = sorted(d_y.items(), key=itemgetter(1), reverse=True)
d_T = sorted(d_t.items(), key=itemgetter(1), reverse=True)

L = len(d_yt), len(d_t), len(d_y)

for i in range(300):
    pr = arrange(d_YT[i][0], d_YT[i][1], k=15)
    if L[1] > i:
        pr = pr+arrange(d_T[i][0], d_T[i][1], k=10)
    if L[2] > i:
        pr = pr+"     "+arrange(d_Y[i][0], d_Y[i][1], k=10)
    print pr
