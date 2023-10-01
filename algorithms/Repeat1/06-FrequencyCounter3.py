#!/usr/bin/env python3

"""
Write a function called sameFrequency. Given two positive integers, find out if the two numbers
have the same frequency of digits. Requirements: Time complexity = O(n)

eg: sameFrequency((182, 281)) // true
eg: sameFrequency((34, 14)) // false
eg: sameFrequency((3589578, 5879385)) // true
eg: sameFrequency((22, 222)) // false

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def sameFrequency(int_1, int_2):
    print ("Processing {} and {}".format(int_1, int_1))

    if len(str(int_1)) != len(str(int_2)):
        print ("The numbers are of different lengths. Result=False")
        return

    freq_map_1 = getFreqMap(int_1)
    freq_map_2 = getFreqMap(int_2)

    for key in freq_map_1:
        try:
            if freq_map_1 [key] != freq_map_2 [key]:
                print ("The numbers do not have the same frequence of digits")
                return
        except Exception as e:
            print ("The numbers do not have the same frequence of digits")
            return

    print ("Yes, the numbers have the same frequence of digits")

def getFreqMap(in_t):
    tmp_str = str(in_t)
    freq_map = {}
    for char in tmp_str:
        if char in freq_map:
            freq_map [char] += 1
        else:
            freq_map [char] = 1
    return freq_map


sameFrequency(182, 281)
sameFrequency(34, 14)
sameFrequency(3589578, 5879385)
sameFrequency(22, 222)
