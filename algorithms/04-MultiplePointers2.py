#!/usr/bin/env python3

"""
Write a function called countUniqueValues which accepts
a sorted tuple of integers. The function should
count the unique values in the tuple. There can be
negative numbers in the tuple, but will always be sorted
eg: countUniqueValues((1,1,1,1,1,2)) // 2
eg: countUniqueValues((1,2,3,4,4,4,7,7,12,12,13)) // 7

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""


def countUniqueValues(tup):
    ptr_1 = 0
    ptr_2 = 1
    uniqVals = set()

    print ("analysing Tup {}".format(tup))
    while ptr_2 < len(tup):
        val_1 = tup [ptr_1]
        val_2 = tup [ptr_2]

        print ("val_1 = {l}, val_2 = {r}".format(l=val_1, r=val_2))

        if val_1 != val_2:
            uniqVals.add(val_1)

            ptr_1 = ptr_2
            ptr_2 = ptr_2 + 1

            if ptr_2 == len(tup):
                uniqVals.add(val_2)
                break
        elif val_1 == val_2:
            ptr_2 = ptr_2 + 1


    print ("unique values are {} // {}".format(uniqVals, len(uniqVals)))

countUniqueValues((-5,-2,-1,0,3,7,9))
countUniqueValues((-5,-2,-1,0,1,7,9))
countUniqueValues((1,1,1,1,1,2))
countUniqueValues((1,2,3,4,4,4,7,7,12,12,13))
