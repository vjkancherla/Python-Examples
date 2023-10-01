#!/usr/bin/env python3

'''
Write a function that returns the number of vowels used
in a string. Vowels are - a, e, i, o, u.

Eg:
vowels('Hi There!') -> 3
vowels('Why do you ask?') -> 4
vowels ('Why?') -> 0
'''

def vowels(a_str):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in a_str.lower():
        if i in vowels:
            count+=1

    print(f"The number of vowels in '{a_str}' is {count}")


vowels('Hi There!')
vowels('Why do you ask?')
vowels ('Why?')
