#!/usr/bin/env python3

"""
Given an array of integers and a number, write a function called maxSubArraySum,
which finds the maximum sum of a subarray with the legth of the number passed to
the function. Note that a subarray must consist of CONSEQUITIVE elements from the
original array. In the first example below, [100, 200, 300] is a subarry of the
original array, but [100, 300] is not.

eg: maxSubArraySum((100, 200, 300, 400), 2) // 700
eg: maxSubArraySum((1, 4, 2, 10, 23, 3, 1, 0, 20), 4) // 39
eg: maxSubArraySum((-3, 4, 0, -2, 6, -1), 2) // 5
eg: maxSubArraySum((3, -2, 7, -4, 1, -1, 4, -2, 1), 2) // 5
eg: maxSubArraySum((2, 3), 3) // null


A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def maxSubArraySum(tupl_e, n):
    print ("Processing {} to find the maxSubArraySum of {} values".format(tupl_e, n))

    if n > len(tupl_e):
        print ("Invalid input params")
        return

    start_idx = 0
    end_idx = n
    max_sum = 0
    matching_elmts = {}

    while end_idx <= len(tupl_e):
        tmp_sum = 0
        for i in range(start_idx,end_idx):
            tmp_sum += tupl_e [i]

        if max_sum < tmp_sum:
            max_sum = tmp_sum
            matching_elmts ["emnts"] = tupl_e[start_idx:end_idx]

        start_idx += 1
        end_idx += 1

    if len(matching_elmts) > 0:
        print ("The  maxSubArraySum of {} values is {}, made up of {}".format(n, max_sum, matching_elmts ["emnts"]))


maxSubArraySum((100, 200, 300, 400), 2)
maxSubArraySum((1, 4, 2, 10, 23, 3, 1, 0, 20), 4)
maxSubArraySum((-3, 4, 0, -2, 6, -1), 2)
maxSubArraySum((3, -2, 7, -4, 1, -1, 4, -2, 1), 2)
maxSubArraySum((2, 3), 3)
maxSubArraySum((1,2,5,2,8,1,5),3)
maxSubArraySum((1,2,5,2,8,1,5),5)
maxSubArraySum((4,2,1,6),1)
maxSubArraySum((4,2,1,6,2),4)
maxSubArraySum((2,6,9,2,1,8,5,6,3),3)
