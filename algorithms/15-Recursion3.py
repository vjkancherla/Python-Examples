"""
Write a function called productOfArray, which takes in an array
of numbers and returns the product of them all

eg: productOfArray((1,2,3)) //6
eg: productOfArray((1,2,3,10)) //10
"""

def productOfArray(tupl_e):
    print ("The product of the elements in {} is {}".format(tupl_e, product(tupl_e, len(tupl_e)-1)))

def product(tupl_e, idx):
    if idx < 0:
        return 1
    return tupl_e [idx] * product(tupl_e, idx-1)


productOfArray((1,2,3))
productOfArray((1,2,3,10))
productOfArray((14,42,32,102))
