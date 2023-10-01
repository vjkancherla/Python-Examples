"""
Write a function called subStringIndex which takes two strings - long string and sub string - as paramters,
and returns index of the substring. If the substring is not found, return -1

eg: subStringIndex("hello hi", "lo") //3
eg: subStringIndex("laura lold", "old") //7
eg: subStringIndex("laura lold", "pop") //-1
"""

def subStringIndex(long_str, sub_str):
    print ("Processing '"+long_str+"' and '"+sub_str+"'")

    long_str_idx = 0
    sub_str_idx = 0
    match_start_idx = 0
    #("laura lol lold", "old")
    while long_str_idx < len (long_str):

        l_char = long_str [long_str_idx]
        s_char = sub_str [sub_str_idx]

        #print ("l_char={}, s_char={}".format(l_char,s_char))

        if l_char == s_char:
            # if its the start of the substring, store the matching index
            if sub_str_idx == 0:
                match_start_idx = long_str_idx
            long_str_idx += 1
            sub_str_idx += 1
        elif l_char != s_char and match_start_idx != 0 :
        # if there was match previously, but not anywhere, reset matching idex and reset substring index
            sub_str_idx = 0
            match_start_idx = 0
        else:
            long_str_idx += 1
            sub_str_idx = 0

        if sub_str_idx == len (sub_str):
            print ("SubString index is {}".format(match_start_idx))
            return


    print ("No match found for substring")

subStringIndex("hello hi", "lo")
subStringIndex("laura lol lold", "old")
subStringIndex("laura lold", "old")
subStringIndex("laura lold", "pop")
subStringIndex("where is the summer", "summer")
