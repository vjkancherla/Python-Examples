#!/usr/bin/env python3

"""
Check if second string is an anagram of the
first string
if "anagram" and "nagaram" are given, then true

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""


def isAnagramSolution_1(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    str_1 = str_1.lower()
    str_2 = str_2.lower()

    for x in str_1:
        if str_1.count(x) != str_2.count(x):
            return False

    return True


def isAnagramSolution_2(str_1, str_2):
    if len(str_1) != len(str_2):
        return False

    str_1_frq_ct = dict()

    str_1 = str_1.lower()
    str_2 = str_2.lower()

    for x in str_1:
        if x in str_1_frq_ct:
            str_1_frq_ct [x] = str_1_frq_ct [x] + 1
        else:
            str_1_frq_ct [x] = 1

    print (str_1_frq_ct)

    for z in str_1_frq_ct:
        try:
            if str_1_frq_ct [z] != str_2.count(z):
                return False
        except:
            return False

    return True


if isAnagramSolution_2("Anagram", "Nagaram"):
    print ("True")
else:
    print ("False")
