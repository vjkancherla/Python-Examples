#!/usr/bin/env python3

"""
Write a function called isSubSequence which accepts
two string. The function should check whether the
characters in the first string form a subsequence of
the characters in the second string. In other words,
the function should check whether the characters in
first string appear somewhere in the second string,
without their order changing.

eg: isSubSequence("hello", "hello world") // true
eg: isSubSequence("sing", "sting") // true
eg: isSubSequence("abc", "abracadabra") // true
eg: isSubSequence("abc", "acb") // false (order matters)


A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def isSubSequence(str_1, str_2):
    if len(str_1) == 0:
        return True

    if len(str_2) == 0:
        return False

    if str_2 [0] == str_1 [0]:
        return isSubSequence(str_1 [1:], str_2 [1:])

    return isSubSequence(str_1, str_2 [1:])



print (isSubSequence("hello", "hello world"))
print (isSubSequence("sing", "sting"))
print (isSubSequence("abc", "abracadabra"))
print (isSubSequence("abc", "aaaaccbccadbdc"))
print (isSubSequence("abc", "acb"))
