"""
Write a function called binarySearch which accepts a sorted array and a value,
and returns the index at which the value exists. Otherwise, return -1
**IMPORTANT**: Binary Search should only be used for sorted lists/arrays/etc

Time Complexity: O(log n)

eg: binarySearch([1,2,3,4,5],2) //1
eg: binarySearch([1,2,3,4,5],3) //2
eg: binarySearch([1,2,3,4,5],5) //3
eg: binarySearch([1, 5, 7, 8, 13, 19, 20, 23, 29}],23) //8
eg: binarySearch([5, 6, 10, 13, 14, 19, 30, 34, 35, 35, 40,
44, 64, 79, 84, 86, 95, 96, 98, 99}],95) //16
eg: binarySearch([5, 6, 10, 13, 14, 19, 30, 34, 35, 35, 40,
44, 64, 79, 84, 86, 95, 96, 98, 99}],100) //-1
#
"""
import math

def binarySearch(sorted_list, val):
    print ("Processing {} to find {}'s index".format(sorted_list, val))
    start_idx = 0
    end_idx = len(sorted_list) - 1

    while start_idx <= end_idx:
        mid_idx = int(math.ceil((start_idx + end_idx)/2))
        #print("mid_idx={}, sorted_list[mid_idx]={}".format(mid_idx, sorted_list[mid_idx]))
        if sorted_list[mid_idx] == val:
            print ("The index of {} is {}".format(val, mid_idx))
            return
        elif sorted_list[mid_idx] > val:
            end_idx = mid_idx - 1
        elif sorted_list[mid_idx] < val:
            start_idx = mid_idx + 1

    print ("The index of {} is -1".format(val))

binarySearch([1,2,3,3,4,5],2)
binarySearch([1,2,3,4,5],3)
binarySearch([1,2,3,4,5],5)
binarySearch([5, 6, 10, 13, 14, 19, 30, 34, 35, 35, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99],95)
binarySearch([5, 6, 10, 13, 14, 19, 30, 34, 35, 35, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99],100)
