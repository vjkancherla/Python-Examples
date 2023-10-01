#!/usr/bin/env python3

"""
Write a function called maxSubArraySum which accepts tuple of integers, and a number called n.
The function should calculate the maximum sum of n consequitive elements in the array.

eg: maxSubArraySum((1,2,5,2,8,1,5),2) // 10
eg: maxSubArraySum((1,2,5,2,8,1,5),4) // 17
eg: maxSubArraySum((4,2,1,6),1) // 6
eg: maxSubArraySum((4,2,1,6,2),4) // 13

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def maxSubArraySum(tupl_e, n):
    print ("Processing {} to find the max sum of {} consequitive elements".format(tupl_e,n))

    start_idx = 0
    end_idx = n
    maxSum = 0
    maxSum_elmts = {}

    while end_idx <= len(tupl_e):
        tmpSum = 0
        for i in range(start_idx, end_idx):
            tmpSum += tupl_e [i]

        #print ("tuple={}, tmpSum={}".format(tupl_e[start_idx:end_idx], tmpSum))
        #maxSum = max(maxSum, tmpSum)

        if maxSum < tmpSum:
            maxSum = tmpSum
            maxSum_elmts ["elmts"] = tupl_e[start_idx: end_idx]

        start_idx += 1
        end_idx += 1

    print ("maxSubArraySum is {}, made up of {}".format(maxSum, maxSum_elmts ["elmts"]))


maxSubArraySum((1,2,5,2,8,1,5),3)
maxSubArraySum((1,2,5,2,8,1,5),5)
maxSubArraySum((4,2,1,6),1)
maxSubArraySum((4,2,1,6),4)
maxSubArraySum((4,2,1,6,2),4)
maxSubArraySum((2,6,9,2,1,8,5,6,3),3)
