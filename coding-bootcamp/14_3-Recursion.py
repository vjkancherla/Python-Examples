
"""
Recursive function to print the the power of a number

EG:
power(2,0) -> 1
power(2,2) -> 4
power(2.4) -> 16
"""

def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent-1)

print(power(2,0))
print(power(2,2))
print(power(2,4))
print(power(2,10))
print(power(2,32))
print(power(2,64))
