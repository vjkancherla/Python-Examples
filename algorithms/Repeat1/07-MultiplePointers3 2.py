#!/usr/bin/env python3

"""
Write a function called areThereDuplicates which accepts a variable number of arguments.
The function should check whether there are any duplicates among the arguments passed.

eg: areThereDuplicates(1, 2, 3) // false
eg: areThereDuplicates(1, 2, 2) // True
eg: areThereDuplicates('a', 'b', 'c', 'y', 'd', 'b', 'j', 'k') // true

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def areThereDuplicates (*args):
    tupl_e = args

    print ("Processing {}".format(tupl_e))

    sorted_tuple = sorted(tupl_e)

    start_idx = 0
    end_idx = 1
    duplicates = set()

    while end_idx < len(sorted_tuple):
        val_1 = sorted_tuple [start_idx]
        val_2 = sorted_tuple [end_idx]
        if val_1 == val_2:
            duplicates.add(val_1)
            end_idx +=1
        else:
            start_idx = end_idx
            end_idx += 1

    if len(duplicates) > 0:
        print ("Yes, there are duplicates: {}".format(duplicates))
    else:
        print ("No, there are no duplicates")


areThereDuplicates('a', 'b', 'c', 'y', 'd', 'b', 'j', 'k', 'a', 'b', 'c', 'y', 'd', 'b', 'j', 'k', 'z', 'z')
areThereDuplicates(1, 2, 3)
areThereDuplicates(1, 2, 2)
