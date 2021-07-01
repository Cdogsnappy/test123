# -*- coding: utf-8 -*-
"""
Created on 6/3/2020

Created by Martin
"""

xp = 50000
level = 60

total = 0
xp_list = []
for i in range(level):
    total += xp
    xp_list.append((total, i+1))
    xp += 250
print(xp_list)

total /= 2

for point in xp_list:
    if point[0] > total:
        print(point)
        break