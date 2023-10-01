#read items from a list and sum them up
"""
return statement

This problem actually took me quite a while to grasp when I first started learning recursion.

One thing to keep in mind when dealing with Python functions/methods is that they always return a value no matter what. So say you forget to declare a return statement in the body of your function/method, Python takes care of it for you then and does return None at the end of it.

What this means is that if you screw up in the body of the function and misplace the return or omit it, instead of an expected return your print type(messed_up_function()) will print NoneType.
"""

def doSum(aList):
    if len(aList) == 1:
        return aList[0]
    else:
        return aList[0] + doSum(aList[1:])



print(doSum([1, 2, 3, 4, 5]))
