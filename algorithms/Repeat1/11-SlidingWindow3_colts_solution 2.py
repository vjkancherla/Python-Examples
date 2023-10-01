#!/usr/bin/env python3

"""
Write a function called minSubArrayLen which accepts two parameters - an array of
positive integers and a positive integer. The function should return the minimal length of
a CONTIGUOUS subarray of which the sum is greater than or equal to the integer passed to
the function. If there isn't one, return 0 instead

eg: minSubarrayLen((2,3,1,2,4,3), 7) // 2 -> because (4,3) is the smallest subarray
eg: minSubarrayLen((2,1,6,5,4), 9) // 2 -> because (5,4) is the smallest subarray
eg: minSubarrayLen((3,1,7,11,2,9,8,21,62,33,19), 52) // 1 -> because (62) is the smalles subarray greater than 52
eg: minSubarrayLen((1,4,16,22,5,7,8,9,10), 39) // 3 -> because (16,22,5) is the smallest subarray
eg: minSubrrayLen((1,1,1,1,1,1,1), 7) // 7

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def minSubarrayLen(tupl_e, target_sum):
    print ("Processing {} to find the min number of vals that is >= {}".format(tupl_e, target_sum))

    start_idx = 0
    end_idx = 0
    running_sum = 0
    min_subarray_len = len(tupl_e)

    #minSubarrayLen((2,3,1,2,4,3), 7)

    while start_idx < len(tupl_e):
        print ("running_sum:{}, min_subarray_len:{}, start_idx:{}, end_idx:{}".format(running_sum, min_subarray_len, start_idx, end_idx))
        if running_sum < target_sum and end_idx < len(tupl_e):

            elmnt = tupl_e [end_idx]
            running_sum += elmnt

            end_idx += 1

        elif running_sum >= target_sum :

            min_subarray_len = min (min_subarray_len, end_idx - start_idx)

            elmnt = tupl_e [start_idx]
            running_sum -= elmnt

            start_idx += 1
        else:
            break

        #print ("running_sum:{}, min_subarray_len:{}".format(running_sum, min_subarray_len))


    print ("Result: {}".format(min_subarray_len))


# minSubarrayLen((1,1,1,1,1,1,1), 7)
minSubarrayLen((2,3,1,2,4,3), 7)
minSubarrayLen((2,1,6,5,4), 9)
minSubarrayLen((3,1,7,11,2,9,8,21,62,33,19), 52)
# minSubarrayLen((3,1,7,11,2,9,8,21,62,33,19,0,70,0,89), 52)
# minSubarrayLen((1,4,16,22,5,7,8,9,10), 39)
# minSubarrayLen((1,4,16,22,5,7,8,9,10), 200)
# minSubarrayLen((756,453,922,13,477,322,811,986,101), 2000)
# minSubarrayLen((756,453,922,13,477,322,811,986,101), 52000)
