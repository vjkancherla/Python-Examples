"""
Write a function called linearSearch which accepts a list and a value, and
returns the index at which the value exists. If the value dows not exist in
the list, return -1

eg: linearSearch([10,15,20,25,30], 15) //1
eg: linearSearch([9,8,7,6,5,4,3,2,1,0], 4) //5
eg: linearSearch([100], 100) //1
eg: linearSearch([1,2,3,4,5], 6) //-1

Linear Search: checks each item in the list to see if the item is equal to the value
Big O = O(n)
"""

def linearSearch(lis_t, val):
    print ("Processing {} to find {}'s index".format(lis_t, val))

    idx = 0
    for num in lis_t:
        if num == val:
            print ("Index of {} is {}".format(val, idx))
            return
        idx +=1

    print ("Index of {} is -1".format(val))

linearSearch([10,15,20,25,30], 15)
linearSearch([9,8,7,6,5,4,3,2,1,0], 4)
linearSearch([100], 100)
linearSearch([1,2,3,4,5], 6)
