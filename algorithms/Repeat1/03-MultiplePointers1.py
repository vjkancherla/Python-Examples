#!/usr/bin/env python3

"""
Write a function called sumZero which accepts a sorted tuple of integers.
The function should find the find FIRST pair which the sume is zero.

eg:
sumzero((-5,-2,-1,0,1,7,9)) // (-1,1)
sumZero((-45,-14,-13,-9,-5,-2,-1,0,-1,3,7,9,13,34,36,99)))  // (-13,13)
sumZero((-5,-2,-1,0,3,7,9))) // No Match

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def sumZero(tupl_e):
    print ("Processing: {}".format(tupl_e))

    start_idx = 0
    end_idx = len(tupl_e) - 1

    while start_idx != end_idx:
        val_1 = tupl_e [start_idx]
        val_2 = tupl_e [end_idx]

        if val_1 + val_2 == 0:
            print ("Found a match: [{},{}]".format(val_1, val_2))
            return
        elif val_1 + val_2 > 0:
            end_idx -= 1
        elif val_1 + val_2 < 0:
            start_idx += 1

    print ("No match found")


sumZero((-5,-2,-1,0,1,7,9))
sumZero((-45,-14,-13,-9,-5,-2,-1,0,-1,3,7,9,13,34,36,99))
sumZero((-5,-2,-1,0,3,7,9))
