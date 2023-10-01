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

    already_seen_char_idx = 0
    iteration_idx = 0
    longest_substring_len = 0
    seen_char_map = {}

    while iteration_idx < len(strin_g):
        char = strin_g [iteration_idx]

        #print ("1. iteration_idx:{}, already_seen_char_idx:{}".format(iteration_idx, already_seen_char_idx))

        if char in seen_char_map:
            longest_substring_len = max (longest_substring_len, (iteration_idx - already_seen_char_idx))
            #print ("2. iteration_idx:{}, already_seen_char_idx:{}, longest_substring_len:{}".format(iteration_idx, already_seen_char_idx, longest_substring_len))
            already_seen_char_idx = seen_char_map [char]

        seen_char_map [char] = iteration_idx + 1
        iteration_idx += 1

    print ("Result: {}".format(longest_substring_len))

findLongestSubstring("rhytmscm")
findLongestSubstring("rhyrhyrhyrhy")
findLongestSubstring("rhytmschool")
findLongestSubstring("caraaaaaaaaa")
findLongestSubstring("")
findLongestSubstring("thisisawesome")
findLongestSubstring("thecatinthehat")
#findLongestSubstring("bbbbbbb")
