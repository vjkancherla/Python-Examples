#!/usr/bin/env python3

"""
Write a function called averagePair which accepts
a sorted array of integers and a target average. The function should
check whether if there is a pair of values in the array
where the average of the pair equal the target average.
There may be more than one pair that matches the target

eg: averagePair((1,2,3), 2.5) // true
eg: averagePair((1,3,3,5,6,7,19,12,19), 8) // true
eg: averagePair((-1,0,3,4,5,6), 4.1) // false
eg: averagePair((), 4) // false


A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def averagePair(sorted_tup, tgt_avg):
    print ("Processing: {}".format(sorted_tup))

    if len(sorted_tup) == 0:
        print ("The list of numbers is empty")
        return

    ptr_1 = 0
    ptr_2 = len(sorted_tup) - 1

    result_set = set()

    while ptr_1 < len(sorted_tup):
        val_1 = sorted_tup [ptr_1]
        val_2 = sorted_tup [ptr_2]

        print ("val_1 = {l}, val_2 = {r}".format(l=val_1, r=val_2))

        if (val_1 + val_2) / 2.0 == tgt_avg:
            result_set.add((val_1, val_2))
            ptr_1 += 1
            ptr_2 -= 1
            if not (ptr_1 < ptr_2):
                break
        elif (val_1 + val_2) / 2.0 > tgt_avg:
            ptr_2 -= 1
        elif (val_1 + val_2) / 2.0 < tgt_avg:
            ptr_1 += 1

    if len(result_set) > 0:
        print ("Yes, found a pair. {}".format(result_set))
    else:
        print ("No, did not find a pair")


averagePair((1,2,3), 2.5)
averagePair((1,3,3,5,6,7,11,12,19,21,24), 15.5)
averagePair((-1,0,3,4,5,6), 2)
