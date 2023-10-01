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

    substraction_idx = 0
    addition_idx = 0
    running_sum = 0
    matching_elmts = ()
    results_dict = {}

    while addition_idx < len(tupl_e):
         val_to_add = tupl_e [addition_idx]
         running_sum += val_to_add
         matching_elmts = tupl_e [substraction_idx:addition_idx+1]
         #print ("M1:{}, len(M1):{}".format(matching_elmts, len(matching_elmts)))

         if running_sum >= target_sum:

             """
             # Now that we found AN subarray where sum of subarry elmts > target_sum, find the min subarry
             # within the subarry by substracting one elemt at a time from the totalsum of the subarray
             # and checking if the resultant val is still greater than target_sum
             """
             while substraction_idx <= addition_idx:

                 #print ("M2:{}, len(M2):{}".format(matching_elmts, len(matching_elmts)))
                 if len(matching_elmts) in results_dict:
                     results_dict [len(matching_elmts)] = [results_dict [len(matching_elmts)], matching_elmts]
                 else:
                     results_dict [len(matching_elmts)] = matching_elmts
                     #print(results_dict)

                 val_to_minus = tupl_e [substraction_idx]
                 running_sum -= val_to_minus
                 matching_elmts = tupl_e [substraction_idx+1:addition_idx+1]
                 #print ("M2.1:{}, len(M2.1):{}".format(matching_elmts, len(matching_elmts)))

                 if running_sum >= target_sum:
                     substraction_idx += 1
                 else:
                     substraction_idx += 1
                     addition_idx += 1
                     break
         else:
             addition_idx += 1


    if len(results_dict) > 0:
        the_result_key = min (results_dict.keys())
        result = results_dict [the_result_key]
        print("=>The min subarray len >= {} is {}, made of {}".format(target_sum, the_result_key, result))
    else:
        print("=>No subarray found")

    print ("")

minSubarrayLen((1,1,1,1,1,1,1), 7)
minSubarrayLen((2,3,1,2,4,3), 7)
minSubarrayLen((2,1,6,5,4), 9)
minSubarrayLen((3,1,7,11,2,9,8,21,62,33,19), 52)
minSubarrayLen((3,1,7,11,2,9,8,21,62,33,19,0,70,0,89), 52)
minSubarrayLen((1,4,16,22,5,7,8,9,10), 39)
minSubarrayLen((1,4,16,22,5,7,8,9,10), 200)
minSubarrayLen((756,453,922,13,477,322,811,986,101), 2000)
minSubarrayLen((756,453,922,13,477,322,811,986,101), 52000)
