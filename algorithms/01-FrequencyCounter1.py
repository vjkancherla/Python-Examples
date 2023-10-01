#!/usr/bin/env python3

"""
Check if second tuple contains the square roots of
all the numbers in first tuple
if (1,5,9) and (81,1,25) are given, then true

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""


def compare(t_1, t_2):
    if len(t_1) != len(t_2):
        return False

    t_1_frq_ct = dict()
    t_2_frq_ct = dict()

    for x in t_1:
        if x in t_1_frq_ct:
            t_1_frq_ct [x] = t_1_frq_ct [x] + 1
        else:
            t_1_frq_ct [x] = 1

    print (t_1_frq_ct)

    for y in t_2:
        if y in t_2_frq_ct:
            t_2_frq_ct [y] = t_2_frq_ct [y] + 1
        else:
            t_2_frq_ct [y] = 1

    print (t_2_frq_ct)

    for z in t_1_frq_ct:
        print (z)
        try:
            if t_1_frq_ct [z] != t_2_frq_ct [z ** 2]:
                return False
        except KeyError as e:
            return False

    return True


if compare((1, 10, 5, 9, 4, 5, 9 ), (81, 1, 25, 16, 100, 25, 81)):
    print ("True")
else:
    print ("False")
