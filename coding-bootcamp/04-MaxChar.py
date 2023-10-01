#!/usr/bin/env python3


"""
Given a string, return the char that is most commonly used in the string.

eg: "sssdddffffffff" = f
    "Apple1232131AppleApple" = p
"""

def max_char(a_str):
    tracker = {}
    max = 0
    max_char = ""
    for ch in a_str:
        if ch in tracker:
            tracker[ch] = tracker[ch] + 1
        else:
            tracker[ch] = 1
    print(tracker)

    for ky in tracker:
        val = tracker[ky]
        if val > max:
            max = val
            max_char = ky

    print(f"{max_char} is the most occurring char with {max}")


max_char("sssdddffffffff")
max_char("Apple1232131AppleApple")
