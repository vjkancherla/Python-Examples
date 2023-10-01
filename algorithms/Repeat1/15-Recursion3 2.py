"""
Write a function called productOfArray, which takes in an array
of numbers and returns the product of them all

eg: productOfArray((1,2,3)) //6
eg: productOfArray((1,2,3,10)) //10
"""

def productOfArray (tupl_e):
    def doWork(idx=0):
        if idx == len(tupl_e):
            return 1
        return tupl_e [idx] * doWork(idx+1)

    print (doWork())


productOfArray((1,2,3))
productOfArray((1,2,3,10))
productOfArray((14,42,32,102))
