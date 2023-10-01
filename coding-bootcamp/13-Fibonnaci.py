#!/usr/bin/env python3

'''
Create a function to print the N'th element in the Fibonnaci sequence.

eg:
fib(3) -> 1,1,[2]
fib(5) -> 1,1,2,3,[5]
fib(10) -> 1,1,2,3,5,8,13,21,34,[55]
'''

def fib(num):
    if (num <= 2):
        return 1

    return fib(num-1) + fib(num-2)


print(fib(3))
print(fib(5))
print(fib(10))
