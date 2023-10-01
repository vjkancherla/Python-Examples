#!/usr/bin/env python3

"""
Write a function called countUniqueValues which accepts a sorted tuple of integers.
The function should count the unique values in the tuple. There can be negative numbers
in the tuple, but will always be sorted
eg: countUniqueValues((1,1,1,1,1,2)) // 2
eg: countUniqueValues((1,2,3,4,4,4,7,7,12,12,13)) // 7

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def countUniqueValues (tupl_e):
    print ("Processing: {}".format(tupl_e))

    start_idx = 0
    end_idx = 1
    uniq_elmts = [tupl_e [start_idx]]

    while end_idx < len(tupl_e):
        val1 = tupl_e [start_idx]
        val2 = tupl_e [end_idx]

        #print ("val1={}, val2={}".format(val1, val2))

        if val1 == val2:
            end_idx += 1
        else:
            start_idx = end_idx
            end_idx += 1
            uniq_elmts.append(val2)

    print ("There are {} unique values: {}".format(len(uniq_elmts), uniq_elmts))


countUniqueValues((1,1,1,1,1,2))
countUniqueValues((1,2,3,4,4,4,7,7,12,12,13))
countUniqueValues((1,1,1,1,1,2,2))
countUniqueValues((1,2,3,4,4,4,7,7,12,12,13,13))
countUniqueValues((-5,-2,-1,-1,-1,-1,-1,0,3,7,9))
countUniqueValues((-5,-5,-2-2,-1,0,1,1,7,7,9,9,9))
