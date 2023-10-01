#!/usr/bin/env python3


"""
Check if a string is a palindrome
"""

def is_plaindrome(a_str):
    rev_str = a_str[::-1]

    if a_str == rev_str:
        print(f"{a_str} IS a Plaindrome")
    else:
        print(f"{a_str} is NOT a Plaindrome")


is_plaindrome("helloworld")
is_plaindrome("abba")
