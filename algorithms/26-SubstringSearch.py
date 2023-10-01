"""
Write a function called subStringIndex which takes two strings - long string and sub string - as paramters,
and returns index of the substring. If the substring is not found, return -1

eg: subStringIndex("hello hi", "lo") //3
eg: subStringIndex("laura lold", "old") //7
eg: subStringIndex("laura lold", "pop") //-1
"""

def subStringIndex(long_str, sub_str):
    print ("Processing '{}' and '{}'".format(long_str, sub_str))

    long_str_idx = 0
    sub_str_idx = 0
    prev_char_matched = False
    match_found_at_idx = 0

    while long_str_idx < len(long_str) and sub_str_idx < len(sub_str):

        long_str_val = long_str [long_str_idx]
        sub_str_val = sub_str [sub_str_idx]

        #print(long_str_val+"=="+sub_str_val+"?")

        if long_str_val == sub_str_val:
            if (sub_str_idx == 0):
                match_found_at_idx = long_str_idx
            long_str_idx += 1
            sub_str_idx += 1
            prev_char_matched = True
        elif (long_str_val != sub_str_val) and (prev_char_matched):
            sub_str_idx = 0
            prev_char_matched = False
        else:
            long_str_idx += 1
            sub_str_idx = 0

    if match_found_at_idx == 0:
        print ("The index of '{}' is -1".format(sub_str))
    else:
        print ("The index of '{}' in {}".format(sub_str, match_found_at_idx))


subStringIndex("hello hi", "lo")
subStringIndex("laura lold", "old")
subStringIndex("laura lold", "pop")
subStringIndex("where is the summer", "summer")
