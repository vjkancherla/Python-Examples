"""
CALLBACK Function example

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

def main(tupl_e = None, _callback = None):
    print("Looking for an Odd number in {}".format(tupl_e))
    if _callback and tupl_e:
        for num in tupl_e:
            if _callback(num):
                print ("Found an Odd number - {}".format(num))
                return
        print ("No Odd number found in - {}".format(tupl_e))

main((1,2,3,4,5), callback_isOdd)
main((44,22,56,13), callback_isOdd)
