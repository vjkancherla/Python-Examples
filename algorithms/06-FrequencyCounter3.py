#!/usr/bin/env python3

"""
Write a function called sameFrequency.
Given two positive integers, find out if the two numbers
have the same frequency of digits
Requirements: Time complexity = O(n)

eg: sameFrequency((182, 281)) // true
eg: sameFrequency((34, 14)) // false
eg: sameFrequency((3589578, 5879385)) // true
eg: sameFrequency((22, 222)) // false

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""


def sameFrequency(num_1, num_2):
    if len(str(num_1)) != len(str(num_2)):
        print ("{} and {} have diff num of digits, so False".format(num_1, num_2))
        return

    dict_1 = dict()
    dict_2 = dict()
    same = True

    for x in str(num_1):
        if x in dict_1:
            dict_1 [x] = dict_1 [x] + 1
        else:
            dict_1 [x] = 1

    for y in str(num_2):
        if y in dict_2:
            dict_2 [y] = dict_2 [y] + 1
        else:
            dict_2 [y] = 1

    for z in dict_1:
        try:
            if dict_1 [z] != dict_2 [z]:
                same = False
        except KeyError as e:
            same = False

    print ("frequencies in {} are {}, frequencies in {} are {}. Same frequencices={}".format(num_1, dict_1, num_2, dict_2, same))


sameFrequency(182, 281)
sameFrequency(34, 14)
sameFrequency(3589578, 5879385)
sameFrequency(22, 222)
