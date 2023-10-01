#!/usr/bin/env python3

"""
Write a function called findLongestSubstring, which accepts a string and
returns the length of the longest substring with all distinct characters.
Time complexity should be - O(n)
eg: findLongestSubstring("") // 0
eg: findLongestSubstring("rhytmschool") // 9 {r,h,y,t,m,s,c,h,o}
eg: findLongestSubstring("thisisawesome") // 6 {a,w,e,s,o,m}
eg: findLongestSubstring("thecatinthehat") // 7 {h,e,c,a,t,i,n}
eg: findLongestSubstring("bbbbbbb") // 1 {b}


A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def findLongestSubstring(supplied_str):
    print ("Processing "+supplied_str)

    left_win_idx = 0
    right_win_idx = 0
    max_substring_len = 0
    frequency_tracker = {}
    results = {}

    while (left_win_idx < len(supplied_str)) and (right_win_idx < len(supplied_str)):
        left_val = supplied_str [left_win_idx]
        right_val = supplied_str [right_win_idx]

        if right_val in frequency_tracker:
            max_substring_len = max(max_substring_len, len(frequency_tracker))

            if not max_substring_len in results:
                results[max_substring_len] = frequency_tracker.keys()
            elif (max_substring_len in results) and (max_substring_len == len(frequency_tracker)):
                results[max_substring_len] = [results[max_substring_len], frequency_tracker.keys()]

            frequency_tracker = {}

            left_win_idx += 1
            right_win_idx = left_win_idx
        else:
            frequency_tracker [right_val] = 1
            right_win_idx += 1

        #print(frequency_tracker)

    if max_substring_len != 0:
        print("The longest substring is of {} chars length".format(max_substring_len))
        the_result = max(results.keys())
        print("The chars are {}".format(results[the_result]))
    else:
        print("Error. Returning 0")

    print("---")

findLongestSubstring("rhytmschool")
findLongestSubstring("")
findLongestSubstring("thisisawesome")
findLongestSubstring("thecatinthehat")
findLongestSubstring("bbbbbbb")
