"""
Write a function called factorial which accepts a number and returns the
factorial of the number.

eg: factorial(4) // 4 * 3 * 2 * 1 = 24
eg: factorial(0) // 1
"""

def factorial(num):
    if num == 1 or num == 0:
        return 1

    return num * factorial(num-1)


print (factorial(4))
print (factorial(0))
print (factorial(10))
