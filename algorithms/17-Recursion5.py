"""
Write a recursive function called fib which accepts a number and returns the
n-th number in the Fibanocci sequence. Recall that the Fibanocci squence is a
sequence of while number 1,1,2,3,5,8,... which starts with 1 and 1, and where
every number thereafter is equal to the sum of the previous two numbers

eg: fib(4) //3 1,1,2,3
eg: fib(10) // 55
eg: fib(28) // 317811
eg: fib(35) // 9227465
"""

def fib(num):
    if (num <= 2):
         return 1
    return fib(num-1) + fib(num-2)

print (fib(4))
print (fib(10))
print (fib(28))
print (fib(35))
