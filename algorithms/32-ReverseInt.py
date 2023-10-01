"""
Write a function called reverseInt, which accepts a number and reverses it.

eg: reverseInt(10) //01
reverseInt(42) //25
reverseInt(-5) //-5
reverseInt(-73) //-37
reverseInt(4) //4
"""

def reverseInt(intege_r):
    print ("Processing: {}".format(intege_r))

    int_as_str = str(intege_r)
    reversed_int = 0

    if intege_r < 0:
        int_as_str = int_as_str [:0:-1]
        reversed_int = int(int_as_str) * -1
    else:
        int_as_str = int_as_str [::-1]
        reversed_int = int(int_as_str)

    print ("Result: {}".format(reversed_int))

reverseInt(10)
reverseInt(42)
reverseInt(-5)
reverseInt(-73)
reverseInt(4)
