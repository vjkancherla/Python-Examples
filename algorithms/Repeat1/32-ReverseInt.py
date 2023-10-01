"""
Write a function called reverseInt, which accepts a number and reverses it.

eg: reverseInt(10) //01
reverseInt(42) //24
reverseInt(-5) //-5
reverseInt(-73) //-37
reverseInt(4) //4
"""

def reverseInt(intege_r):
    print ("Processing int: {}".format(intege_r))

    int_as_str = str(intege_r)

    if intege_r < 0:
        rev_intege_r = int(int_as_str [:0:-1]) * -1
    else:
        rev_intege_r = int_as_str [::-1]

    print ("Result: {}".format(rev_intege_r))

reverseInt(10)
reverseInt(42)
reverseInt(-5)
reverseInt(-73)
reverseInt(4)
