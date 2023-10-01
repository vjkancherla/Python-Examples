#!/usr/bin/env python3

"""
Write a function called maxSubArraySum which accepts
a tuple of integers, and a number called n. The
function should calculate the maximum sum of n consequitive
elements in the array.

eg: maxSubArraySum((1,2,5,2,8,1,5),2) // 10
eg: maxSubArraySum((1,2,5,2,8,1,5),4) // 17
eg: maxSubArraySum((4,2,1,6),1) // 6
eg: maxSubArraySum((4,2,1,6,2),4) // 13

A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""


def maxSubArraySum(tup, n):

    maxSum = 0
    tempSum = 0

    for i in range(n):
        maxSum = maxSum + tup [i]

    #print ("MaxSum1 = {}".format(maxSum))

    win_left = 0
    win_right = n

    tempSum = maxSum

    while win_right < len(tup):
        left_val = tup [win_left]
        right_val = tup [win_right]

        #print ("Left Val = {}, Right Val = {}".format(left_val, right_val))

        tempSum = ( tempSum - left_val ) + right_val

        #print ("TempSum = {}".format(tempSum))

        if tempSum > maxSum:
            maxSum = tempSum

        #print ("MaxSum2 = {}".format(maxSum))

        win_left = win_left + 1
        win_right = win_right + 1

    print (maxSum)


maxSubArraySum((1,2,5,2,8,1,5),3)
maxSubArraySum((1,2,5,2,8,1,5),5)
maxSubArraySum((4,2,1,6),1)
maxSubArraySum((4,2,1,6,2),4)
maxSubArraySum((2,6,9,2,1,8,5,6,3),3)
