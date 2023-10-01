'''
write a function called printPyramid(), with accepts a positive number, and prints a pyramid

for eg:
printPyramid(2)
' # '
'###'

printPyramid(3)
'  #  '
' ### '
'#####'

printPyramid(5)
'    #    '
'   ###   '
'  #####  '
' ####### '
'#########'

printPyramid(7)
'      #      '
'     ###     '
'    #####    '
'   #######   '
'  #########  '
' ########### '
'#############'

'''
import math

def printPyramid(levels):
    print ("Printing a PYRAMID of {} levels".format(levels))

    # Whilst iterating through the levels,
    # each row will contain a total of [(curent_level * 2) -1] "#" chars.
    # The last row will contain (levels * 2) - 1 "#" chars.
    # Regardless of which row, it will always contain (levels * 2) - 1 TOTAL chars

    # The key for the solution is to find the mid-point of the row,
    # add a "#" at the mod-point, and then add "#"s to either side.
    # The number of "#"s to add either side will depend on the level (during iteration)

    mid_point = math.floor(((levels * 2) - 1) / 2)
    total_chars_in_row = (levels * 2) - 1

    for row_idx in range (levels):
        row_str = ""

        for char_idx in range (total_chars_in_row):
            if char_idx == mid_point:
                row_str += "#"
            elif char_idx < mid_point and char_idx >= mid_point - row_idx:
                row_str += "#"
            elif char_idx > mid_point and char_idx <= mid_point + row_idx:
                row_str += "#"
            else:
                row_str += " "

        print (row_str)

    print ("----")

printPyramid(2)
printPyramid(3)
printPyramid(5)
printPyramid(7)
printPyramid(10)
printPyramid(25)
printPyramid(50)
