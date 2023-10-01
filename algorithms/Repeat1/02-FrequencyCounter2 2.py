#!/usr/bin/env python3

"""
Check if second string is an anagram of the first string.
if "anagram" and "nagaram" are given, then true

eg:
checkIfAnagram( "anagram", "nagaram") //true
checkIfAnagram( "fried", "fired") //true
checkIfAnagram( "amma", "mama") //true
checkIfAnagram( "amma", "papa") //false
checkIfAnagram( "amma", "pop") // false
checkIfAnagram( "Fried!!!", "fired") // true
checkIfAnagram( "Fried! Tar!", "fired rat") // true
A tuple is a collection which is ordered and unchangeable.
You can access tuple items by referring to the index number, inside square brackets
"""


def checkIfAnagram(str_1, str_2):
    print ("Processing: '{}' and '{}'".format(str_1, str_2))

    str_1_char_frq = buildCharDict(str_1)
    str_2_char_frq = buildCharDict(str_2)

    if len(str_1_char_frq) != len (str_2_char_frq):
        print ("The strings are of different lengths. So not an Anagram")

    for key in str_1_char_frq:
        try:
            if str_1_char_frq [key] != str_2_char_frq [key]:
                print ("Not an Anagram")
                return
        except KeyError as e:
            print ("Not an Anagram")
            return

    print ("Yes, its an Anagram")

def buildCharDict(str):
    str_char_frq = {}
    cleaned_str = ""

    for char in str:
        if char.isalpha():
            cleaned_str += char

    for char in cleaned_str.lower():
        if char in str_char_frq:
            str_char_frq [char] += 1
        else:
            str_char_frq [char] = 1
    return str_char_frq

checkIfAnagram( "anagram", "nagaram")
checkIfAnagram( "fried", "fired")
checkIfAnagram( "amma", "mama")
checkIfAnagram( "amma", "papa")
checkIfAnagram( "amma", "pop")
checkIfAnagram( "Fried!!!", "fired")
checkIfAnagram( "Fried! Tar!", "fired rat")
