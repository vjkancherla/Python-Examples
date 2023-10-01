#!/usr/bin/env python3

strInput = input("Enter a string for palindrome check: ")

strReverse = strInput[::-1]

if strInput == strReverse:
    print ("{n} is indeed a palindrome".format(n=strInput))
else:
    print ("{n} is not a palindrome".format(n=strInput))
