"""
Write a recursive function called someRecursive which accepts an array
and a CALLBACK. The function returns true if a single value in the array
returns true when passed to the callback. Otherwise it returns False

eg: CALLBACK FUNCTION =
def isOdd(num):
    return (num % 2) != 0

MAIN FUNCTION =
def main((1,2,3,4,5), isOdd)

the CALLBACK fuction, isOdd is called for each val in the tuple. If any of the vals
is odd, return True

"""
#CallBack function
def callback_isOdd(num):
    return (num % 2) != 0

idx = 0
def someRecursive(tupl_e = None, _callback = None):
    global idx
    if idx == len(tupl_e):
        print ("Found No Odd number in - {}".format(tupl_e))
        return False
    if _callback(tupl_e [idx]):
        print ("Found an Odd number - {}, in {}".format(tupl_e [idx], tupl_e))
        return True
    idx += 1
    return someRecursive(tupl_e, _callback)


print (someRecursive((1,2,3,4,5), callback_isOdd))
print (someRecursive((44,22,56,13), callback_isOdd))
print (someRecursive((44,22,56), callback_isOdd))
