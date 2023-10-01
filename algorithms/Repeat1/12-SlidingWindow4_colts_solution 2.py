#!/usr/bin/env python3

"""
Write a function called findLongestSubstring, which accepts a string and returns the length
of the longest substring with all distinct characters.
Time complexity should be - O(n)
eg: findLongestSubstring("") // 0
eg: findLongestSubstring("cara") // 3 {c,a,r}
eg: findLongestSubstring("rhytmschool") // 7 {r,h,y,t,m,s,c,} + {h,y,t,m,s,c,o}
eg: findLongestSubstring("thisisawesome") // 6 {a,w,e,s,o,m}
eg: findLongestSubstring("thecatinthehat") // 7 {h,e,c,a,t,i,n}
eg: findLongestSubstring("bbbbbbb") // 1 {b}


A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def findLongestSubstring(strin_g):
    print ("Processing '{}'".format(strin_g))

    if len(strin_g) == 0:
        print ("Invalid argument!")
        return

    start_measuring_from = 0
    longest_sub_str_len = 0
    seen_chars = {}

    for current_idx in range(len(strin_g)):
        char = strin_g [current_idx]

        if char in seen_chars:
            start_measuring_from = max (start_measuring_from, seen_chars [char])

        longest_sub_str_len = max (longest_sub_str_len, (current_idx - start_measuring_from) + 1)

        seen_chars [char] = current_idx + 1

    print ("The Longest SubString is of length: {}".format(longest_sub_str_len))


findLongestSubstring("rhytmschool")
findLongestSubstring("")
findLongestSubstring("thisisawesome")
findLongestSubstring("thecatinthehat")
findLongestSubstring("bbbbbbb")
