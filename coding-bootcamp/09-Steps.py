#!/usr/bin/env python3

"""
Write a function that accepts a positive number N.
The function should console log a step shape
with N levels using the # char. Make sure the step
has spaces on the right hand side
eg: steps(2)
'# '
'##'

steps(3)
'#  '
'## '
'###'
"""

def steps(no_of_steps):
    for i in range(1, no_of_steps+1):
        p=""
        steps=i
        spaces=no_of_steps-i
        p=('#'*steps)+(' '*spaces)
        print (f"\'{p}\'")

    print("--")


steps(2)
steps(3)
steps(4)
steps(5)
