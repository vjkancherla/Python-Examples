#!/usr/bin/env python3

"""
Recursive function to print the factorial of a number
"""
def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num-1)

print(factorial(5))
