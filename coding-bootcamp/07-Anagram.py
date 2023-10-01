#!/usr/bin/env python3

"""
Given two strings. The task is to check whether the given strings are anagrams of each other or not.

An anagram of a string is another string that contains the same characters,
only the order of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.

eg: anagrams("rail safety", "fairy tales") -> true
    anagrams("RAIL! SAFETY!, "fairy tales") -> true
    anagrams("Hi there", "Bye there") -> false
"""

import re

def anagrams(str1, str2):
    ch_count_str1 = {}
    ch_count_str2 = {}

    org_str1 = str1
    org_str2 = str2

    str1 = str1.lower()
    str2 = str2.lower()

    str1 = str1.replace(" ","")
    str2 = str2.replace(" ","")

    str1 = re.sub(r'[^a-zA-Z0-9]', '', str1)
    str2 = re.sub(r'[^a-zA-Z0-9]', '', str2)

    if len(str1) != len(str2):
        print(f"{org_str1} and {org_str2} are not anagrams because they are of different lengths")
        return 1

    for i in str1:
        if i in ch_count_str1:
            ch_count_str1[i] = ch_count_str1[i] + 1
        else:
            ch_count_str1[i] = 1

    for i in str2:
        if i in ch_count_str2:
            ch_count_str2[i] = ch_count_str2[i] + 1
        else:
            ch_count_str2[i] = 1


    for ch in ch_count_str1:
        if ch in ch_count_str2:
            if ch_count_str1[ch] == ch_count_str2[ch]:
                continue
            else:
                print(f"The occurrances of char {ch}:{ch_count_str1[ch]} in {str1} does not match the occurrances of {ch}:{ch_count_str2[ch]} in {str2}, so they cannot be anagrams")
                return 1
        else:
            print(f"The char {ch} in {str1} does not exist in {str2}, so they cannot be anagrams")
            return 1

    print(f"{org_str1} and {org_str2} are INDEED anagrams")


anagrams("rail safety", "fairy tales")
anagrams("RAIL! SAFETY!", "fairy tales")
anagrams("abcd", "acdb")
anagrams("Hi there", "Bye there")
