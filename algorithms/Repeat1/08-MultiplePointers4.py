#!/usr/bin/env python3

"""
Write a function called averagePair which accepts a sorted array of integers and
a target average. The function should check whether if there is a pair of values in
the array where the average of the pair equal the target average. There may be more
than one pair that matches the target

eg: averagePair((1,2,3), 2.5) // true
eg: averagePair((1,3,3,5,6,7,19,12,19), 8) // true
eg: averagePair((-1,0,3,4,5,6), 4.1) // false
eg: averagePair((), 4) // false


A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def averagePair(tupl_e, target_avg):
    print ("Processing {} to a pair that equated to the target avg of {}".format(tupl_e, target_avg))

    start_idx = 0
    end_idx = len(tupl_e) - 1
    mathing_pair = []

    while start_idx < end_idx:
        val_1 = tupl_e [start_idx]
        val_2 = tupl_e [end_idx]

        tmp_avg = (val_1 + val_2) / 2.0

        if tmp_avg == target_avg:
            mathing_pair.append((val_1, val_2))
            start_idx += 1
            end_idx -= 1
        elif tmp_avg > target_avg:
            end_idx -= 1
        elif tmp_avg < target_avg:
            start_idx += 1

    if len(mathing_pair) > 0:
        print ("FOUND! The pair[s] {} has the average of {}".format(mathing_pair,target_avg))
    else:
        print ("No Pair found")


averagePair((1,2,3), 2.5)
averagePair((1,3,3,5,6,7,11,12,19,21,24), 15.5)
averagePair((-1,0,3,4,5,6), 2)
