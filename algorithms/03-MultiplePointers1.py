#!/usr/bin/env python3

"""
Write a function called sumZero which accepts
a sorted tuple of integers. The function should
find the find FIRST pair which the sume is zero.
sumzero((-5,-2,-1,0,1,7,9)) // (-1,1)

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""


def sumZero(tup):
    ptr_1 = 0
    ptr_2 = len(tup) - 1

    while ptr_1 < ptr_2:
        lft = tup [ptr_1]
        rht = tup [ptr_2]

        print ("left = {l}, right = {r}".format(l=lft, r=rht))

        if lft + rht == 0:
            return (lft, rht)
        elif lft + rht > 0:
            ptr_2 = ptr_2 - 1
        elif lft + rht < 0:
            ptr_1 = ptr_1 + 1

    return "no match"

print (sumZero((-5,-2,-1,0,3,7,9)))
print (sumZero((-5,-2,-1,0,1,7,9)))
