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
    return num%2 == 1

def someRecursive (tupl_e = None, _callback = None):
    def doWork(idx):
        if idx == len(tupl_e):
            return "No odds found"
        elif _callback (tupl_e [idx]):
            return "Yes, the tuple has an odd number - "+str(tupl_e [idx])
        return doWork(idx+1)

    if _callback:
        return doWork(0)

print (someRecursive((1,2,3,4,5), callback_isOdd))
print (someRecursive((44,22,56,13), callback_isOdd))
print (someRecursive((44,22,56), callback_isOdd))
