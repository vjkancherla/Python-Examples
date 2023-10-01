"""
Write a function called power, which accepts a base and an exponent.
The function should return the power of the base of the exponent.

eg: power(2,0) // 1
eg: power(2,2) // 4
eg: power(2,4) // 16
"""

def power (bas_e, exponen_t):
    if exponen_t == 0:
        return 1
    return bas_e * power (bas_e, exponen_t-1)

print (power(2,0))
print (power(2,2))
print (power(2,4))
print (power(5,6))
