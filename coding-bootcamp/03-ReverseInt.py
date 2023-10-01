#!/usr/bin/env python3


"""
Reverse a given integer:
43 = 34
15 = 51
-25 = -52
-30 = -03
"""

def reverse_int(a_int):

    if a_int < 0:
        int_as_string = str(a_int)[1:]
        rev_str = int_as_string[::-1]
        print(f"{a_int} reversed is -{rev_str}")
    else:
        int_as_string = str(a_int)
        rev_str = int_as_string[::-1]
        print(f"{a_int} reversed is {rev_str}")


reverse_int(43)
reverse_int(15)
reverse_int(-25)
reverse_int(-30)
