#!/usr/bin/env python3

aList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
bList = []

for i in aList:
    if i < 10:
        bList.append(i)

print (*bList)
