#!/usr/bin/env python3

"""
Write a function called areThereDuplicates which accepts
a variable number of arguments. The function should
check whether there are any duplicates among the arguments
passed.

eg: areThereDuplicates(1, 2, 3) // false
eg: areThereDuplicates(1, 2, 2) // True
eg: areThereDuplicates('a', 'b', 'c', 'y', 'd', 'b', 'j', 'k') // true

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""


def areThereDuplicates(*args):
    tup = args

    print ("Processing: {}".format(tup))

    ptr_1 = 0
    ptr_2 = 1

    duplicates = set()

    while ptr_1 < len(tup) and ptr_1 != ptr_2:

        val_1 = tup [ptr_1]
        val_2 = tup [ptr_2]

        #print ("val_1 = {l}, val_2 = {r}".format(l=val_1, r=val_2))

        if val_1 == val_2:
            duplicates.add(val_1)

            ptr_1 = ptr_1 + 1

            if ptr_1 + 1 < len(tup):
                ptr_2 = ptr_1 + 1
            continue

        if ptr_2 + 1 < len(tup):
            ptr_2 = ptr_2 + 1
        else:
            ptr_1 = ptr_1 + 1

            if ptr_1 + 1 < len(tup):
                ptr_2 = ptr_1 + 1


    if len(duplicates) > 0:
        print ("Yes, there are duplicates. {}".format(duplicates))
    else:
        print ("No, there are no duplicates")

areThereDuplicates('a', 'b', 'c', 'y', 'd', 'b', 'j', 'k', 'a', 'b', 'c', 'y', 'd', 'b', 'j', 'k')
areThereDuplicates(1, 2, 3)
areThereDuplicates(1, 2, 2)
