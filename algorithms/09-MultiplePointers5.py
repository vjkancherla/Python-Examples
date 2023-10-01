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
eg: isSubSequence("ln", "excellence") // true


A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""

def isSubSequence(str_1, str_2):
    print ("Processing "+str_1+" and "+str_2)

    result = True

    if str_2.find(str_1) != -1:
        print ("Yes, is subsequence")
        return

    ptr_1 = 0
    ptr_2 = 0

    while ptr_2 < len(str_2):
        val_1 = str_1 [ptr_1]
        val_2 = str_2 [ptr_2]

        #print ("val_1 = {l}, val_2 = {r}".format(l=val_1, r=val_2))

        if val_2 == val_1:
            ptr_1 += 1
            if ptr_1 == len(str_1):
                result = True
                break

        ptr_2 += 1

        result = False

    if result:
        print ("Yes, is subsequence")
    else:
        print ("No, is not subsequence")


isSubSequence("hello", "hello world")
isSubSequence("sing", "sting")
isSubSequence("abc", "abracadabra")
isSubSequence("abc", "aaaaccbccadbdc")
isSubSequence("abc", "acb")
