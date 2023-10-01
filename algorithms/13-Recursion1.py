"""
Write a function called power, which accepts a base and an exponent.
The function should return the power of the base of the exponent.

eg: power(2,0) // 1
eg: power(2,2) // 4
eg: power(2,4) // 16
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print (power(2,0))
print (power(2,2))
print (power(2,4))
print (power(5,6))
