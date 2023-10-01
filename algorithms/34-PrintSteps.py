"""
Write a function called printSteps, with accepts a positive number and prints "steps".

For eg:
printSteps(2) =>
'# '
'##'

printSteps(3) =>
'#  '
'## '
'###'

printSteps(5) =>
'#    '
'##   '
'###  '
'#### '
'#####'

Note: for each row, if the number of "#"s do not match the parameter's val passed in, then add a space
For eg:
for printSteps(3), the first row will contain one # + 2 spaces, and the second row will contain 2 #s + 1 space
"""

def printSteps (steps_to_print):
    print ("Printing {} steps".format(steps_to_print))

    for i in range(1, steps_to_print+1):
        row_str = ""

        no_of_steps = i
        no_of_spaces = steps_to_print - i

        for j in range(no_of_steps):
            row_str += "#"

        for k in range(no_of_spaces):
            row_str += " "

        print (row_str)

    print ("---")

printSteps(2)
printSteps(3)
printSteps(5)
printSteps(10)
printSteps(20)
printSteps(100)
