#!/usr/bin/env python3

"""
Write a function that accepts a string and capitalises each word in the string.

eg : capitalise("a short sentance") => A Short Sentance
     capitalise("a lazy fox") => A Lazy Fox
     capitalise("Look, a big baloon") => Look, A Big Baloon
"""

def capitalise(a_str):
    result_str = ""
    first_ch = True
    capitalise_next_ch = False
    for i in a_str:
        if first_ch:
            result_str = result_str+i.upper()
            first_ch = False
            continue

        if i == " ":
            capitalise_next_ch = True
            result_str = result_str+i
            continue

        if capitalise_next_ch:
            result_str = result_str+i.upper()
            capitalise_next_ch = False
        else:
            result_str = result_str+i

    print(f"Input='{a_str}', and output='{result_str}'")


capitalise("a short sentance")
capitalise("a lazy fox")
capitalise("Look, a big baloon") 
