#!/usr/bin/env python3

"""
Recursive function to print numbers backwards
"""

def r_print(num):
    if num == 1:
        print("All Done!")
        return
    else:
        print(num)
        r_print(num-1)

r_print(5)
r_print(10)
