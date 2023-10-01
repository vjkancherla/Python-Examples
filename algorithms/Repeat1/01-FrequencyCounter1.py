#!/usr/bin/env python3

"""
Check if second tuple contains the square roots of all the numbers in first tuple
if (1,5,9) and (81,1,25) are given, then true

eg: doCompare( (1,5,9), (81,1,25) ) // true
eg: doCompare( (1, 10, 5, 9, 4, 5, 9 ), (81, 1, 25, 16, 100, 25, 81) ) //true
eg: doCompare( (1, 10, 5, 9, 4, 5, 9, 55 ), (81, 1, 25, 16, 100, 25, 81, 225) ) // false


A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""


def doCompare(tuple_1, tuple_2):
    print ("Processing {} and {}".format(tuple_1, tuple_2))

    if len(tuple_1) != len(tuple_2):
        print ("The two tuples are of different length, so there can't be a valid comparision")
        return

    tuple_1_freq = {}
    for val in tuple_1:
        if val in tuple_1_freq:
            tuple_1_freq [val] += 1
        else:
            tuple_1_freq [val] = 1

    tuple_2_freq = {}
    for val in tuple_2:
        if val in tuple_2_freq:
            tuple_2_freq [val] += 1
        else:
            tuple_2_freq [val] = 1

    for key in tuple_1_freq:
        try:
            if not tuple_1_freq [key] == tuple_2_freq [(key**2)]:
                print ("The frequency of {0} is not equal to frequency of {0}^2. So False".format(key))
                return
        except KeyError as e:
            print ("The frequency of {0} is not equal to frequency of {0}^2. So False".format(key))
            return


    print ("True. The second tuple contains the square roots of all the numbers in first tuple")

doCompare( (1,5,9), (81,1,25) )
doCompare( (1, 10, 5, 9, 4, 5, 9 ), (81, 1, 25, 16, 100, 25, 81) )
doCompare( (1, 10, 5, 9, 4, 5, 9, 55 ), (81, 1, 25, 16, 100, 25, 81, 225) )
