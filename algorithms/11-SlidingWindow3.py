#!/usr/bin/env python3

"""
Write a function called minSubArrayLen which accepts two
parameters - an array of positive integers and a positive
integer. The function should return the minimal length of
a CONTIGUOUS subarray of which the sum is greater than or
equal to the integer passed to the function. If there isn't
one, return 0 instead

eg: minSubarrayLen((2,3,1,2,4,3), 7) // 2 -> because (4,3) is the smallest subarray
eg: minSubarrayLen((2,1,6,5,4), 9) // 2 -> because (5,4) is the smallest subarray
eg: minSubarrayLen((3,1,7,11,2,9,8,21,62,33,19), 52) // 1 -> because (62) is the smalles subarray greater than 52
eg: minSubarrayLen((1,4,16,22,5,7,8,9,10), 39) // 3 -> because (16,22,5) is the smallest subarray
eg: minSubrrayLen((1,1,1,1,1,1,1), 7) // 7

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def minSubarrayLen(tup, val_to_match_exceed):
    print ("Processing {}, with max_sum={}".format(tup, val_to_match_exceed))

    left_win_idx = 0
    right_win_idx = 0
    running_sum = 0
    min_len = float("inf")
    the_window = []
    matches = {}

    while left_win_idx < len(tup):

        if (running_sum < val_to_match_exceed) and (right_win_idx < len(tup)):
            running_sum = running_sum + tup [right_win_idx]

            #for capturing the vals that make up the subarray
            the_window.append(tup [right_win_idx])
            #print ("add -> {}".format(the_window))

            right_win_idx += 1
            #print ("[1] tup_val:{}, running_sum:{}, rgt_idx:{}".format(tup [right_win_idx-1], running_sum, right_win_idx))
        elif (running_sum >= val_to_match_exceed):
            min_len = min(min_len, right_win_idx - left_win_idx)

            #for capturing the vals that make up the subarray
            if not (len(the_window) in matches):
                matches[len(the_window)] = list(the_window)
            else:
                matches[len(the_window)] = [matches[len(the_window)], list(the_window)]
            #---

            if min_len == 1:
                break;

            running_sum = running_sum - tup [left_win_idx]

            #for capturing the vals that make up the subarray
            the_window.remove(tup [left_win_idx])
            #print ("remove -> {}".format(the_window))

            left_win_idx += 1
            #print ("[2] tup_val:{}, running_sum:{}, lft_idx:{}, min_len:{}".format(tup [left_win_idx-1], running_sum, left_win_idx, min_len))
        else:
            break

        #print (matches)

    if min_len != float("inf"):
        print ("the min legth of subarray that is >= {}, is {}".format(val_to_match_exceed, min_len))
        result = min (matches.keys())
        print ("the subarry list is {}".format(matches[result]))
    else:
        print ("No match found")



minSubarrayLen((1,1,1,1,1,1,1), 7)
minSubarrayLen((2,3,1,2,4,3), 7)
minSubarrayLen((2,1,6,5,4), 9)
minSubarrayLen((3,1,7,11,2,9,8,21,62,33,19), 52)
minSubarrayLen((1,4,16,22,5,7,8,9,10), 39)
minSubarrayLen((1,4,16,22,5,7,8,9,10), 200)
minSubarrayLen((756,453,922,13,477,322,811,986,101), 2000)
