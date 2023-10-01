"""
Write a function called recursiveRange which accepts a number and
adds up all the numbers from 0 to the number passed to the function.

eg: recursiveRange(6) // 6 + 5+ 4+3+2+1 =21
eg: recursiveRange(10) // 55
"""

def recursiveRange(num):
    if num == 1:
        return 1
    return num + recursiveRange (num - 1)

print(recursiveRange(6))
print(recursiveRange(10))
