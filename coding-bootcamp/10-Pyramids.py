#!/usr/bin/env python3

'''
Write a function that accepts a positive number N.
The function should console log a pyramid shape with N levels
with the # char. Make sure that pyramid has spaced on both left
and right nad sides.

eg:
pyramid(1)
'#'
pyramid(2)
' # '
'###'
pyramid(3)
'  #  '
' ### '
'#####'
'''

def pyramid(levels):
    rows = levels
    columns = (levels*2)-1
    mid_point = int(columns/2)

    for rw in range(rows):
        prt = ""
        for cl in range(columns):
            if mid_point - rw <= cl and  mid_point + rw >= cl:
                prt=prt+"#"
            else:
                prt=prt+" "

        print (f"'{prt}'")

pyramid(5)
