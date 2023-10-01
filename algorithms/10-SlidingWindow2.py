#!/usr/bin/env python3

"""
Given an array of integers and a number, write a
function called maxSubArraySum, which finds the
maximum sum of a subarray with the legth of the
number passed to the function.
Note that a subarray must consist of CONSEQUITIVE
elements from the original array. In the first
example below, [100, 200, 300] is a subarry of the
original array, but [100, 300] is not

eg: maxSubArraySum((100, 200, 300, 400), 2) // 700
eg: maxSubArraySum((1, 4, 2, 10, 23, 3, 1, 0, 20), 4) // 39
eg: maxSubArraySum((-3, 4, 0, -2, 6, -1), 2) // 5
eg: maxSubArraySum((3, -2, 7, -4, 1, -1, 4, -2, 1), 2) // 5
eg: maxSubArraySum((2, 3), 3) // null


A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def maxSubArraySum(tup, seq):
    print ("Processing {}, with seq {}".format(tup, seq))

    if seq > len(tup):
        print("Invalid input. Subsequence is greater than lenth of list")
        return

    maxSum = 0
    tempSum = 0

    temp_list = list()

    for i in range(seq):
        val = tup [i]
        maxSum = maxSum + val
        temp_list.append(val)

    #print ("maxsum={}, list={}".format(maxSum, temp_list))

    tempSum = maxSum

    left_win_ptr = 0
    right_win_ptr = seq

    while right_win_ptr < len(tup):

        left_val = tup [left_win_ptr]
        right_val = tup [right_win_ptr]
        tempSum = (tempSum - left_val) + right_val

        if not (tempSum < maxSum):
            maxSum = tempSum

            temp_list.pop(0)
            temp_list.append(right_val)

        #print ("left_val={}, right_val={}, maxSum={}, tempSum={}, list={}".format(left_val,right_val,maxSum,tempSum,temp_list))

        left_win_ptr += 1
        right_win_ptr += 1

    print ("the maxSubArraySum is {}, made up these numbers {}".format(maxSum, temp_list))


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
