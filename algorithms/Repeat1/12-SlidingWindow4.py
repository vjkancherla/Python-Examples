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
    print ("Processing '"+strin_g+"'")

    if len(strin_g) == 0:
        print ("Invalid arguement.")
        print ("--")
        return

    start_idx = 0
    iterative_idx = 0
    uniq_chars = []
    results_holder = {}

    while iterative_idx < len(strin_g):

        char = strin_g [iterative_idx]

        if not char in uniq_chars:
            uniq_chars.append(char)
            iterative_idx += 1
        else:
            if not len(uniq_chars) in results_holder:
                results_holder [len(uniq_chars)] = uniq_chars
            else:
                results_holder [len(uniq_chars)] = [results_holder [len(uniq_chars)], uniq_chars]

            uniq_chars = []
            start_idx += 1
            iterative_idx = start_idx

    max_subarray_key = max(results_holder.keys())
    max_subarray_chars_list = results_holder [max_subarray_key]
    print ("==>The max subarray is of length {}, made up of {}".format(max_subarray_key, max_subarray_chars_list))
    print ("--")


findLongestSubstring("rhytmschool")
findLongestSubstring("")
findLongestSubstring("thisisawesome")
findLongestSubstring("thecatinthehat")
findLongestSubstring("bbbbbbb")
