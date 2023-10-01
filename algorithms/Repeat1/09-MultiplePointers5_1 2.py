#!/usr/bin/env python3

"""
Write a RECURSIVE function called isSubSequence which accepts two strings. The function should
check whether the characters in the first string form a subsequence of the characters
in the second string. In other words, the function should check whether the characters
in first string appear somewhere in the second string, without their order changing.

eg: isSubSequence("hello", "hello world") // true
eg: isSubSequence("sing", "sting") // true
eg: isSubSequence("abc", "abracadabra") // true
eg: isSubSequence("abc", "acb") // false (order matters)
eg: isSubSequence("sing", "retinasting") // true


A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def isSubSequence (str_1, str_2):
    print ("Processing '{}' and '{}'".format(str_1, str_2))

    str_1_start_idx = 0
    str_2_start_idx = 0

    def doWork(str_1, str_2, str_1_start_idx, str_2_start_idx):
        if str_1_start_idx == len(str_1):
            print ("True")
            return
        elif str_2_start_idx == len(str_2):
            print ("False")
            return

        val_1 = str_1 [str_1_start_idx]
        val_2 = str_2 [str_2_start_idx]

        if val_1 == val_2:
            doWork(str_1, str_2, str_1_start_idx+1, str_2_start_idx+1)
        else:
            doWork(str_1, str_2, str_1_start_idx, str_2_start_idx+1)

    doWork(str_1, str_2, str_1_start_idx, str_2_start_idx)


isSubSequence("hello", "hello world")
isSubSequence("sing", "sting")
isSubSequence("abc", "abracadabra")
isSubSequence("abc", "aaaaccbccadbdc")
isSubSequence("abc", "acb")
isSubSequence("abc", "acbkjyrc")
isSubSequence("sing", "retinasting")
