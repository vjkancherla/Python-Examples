"""
Write a recursive function called capitalizeFirst. Given an array of Strings,
capitalize the first letter of each string in the array

eg: capitalizeFirst(["cap", "tap", "lap"]) // Cap, Tap, Lap
eg: capitalizeFirst(["packer", "racker", "breaker"]) // Packer, Racker, Breaker
"""

def capitalizeFirst(strs_list):
    print ("Processing {}".format(strs_list))

    idx = 0
    def doWork(strs_list, idx):
        if idx == len(strs_list):
            return
        tmp_str = strs_list [idx]
        tmp_str_first_char = tmp_str [0]
        tmp_str_first_char = tmp_str_first_char.upper()
        strs_list [idx] = tmp_str_first_char+tmp_str[1:]
        return doWork(strs_list, idx+1)

    doWork(strs_list, idx)

    print (strs_list)


capitalizeFirst(["cap", "tap", "lap"])
capitalizeFirst(["packer", "racker", "breaker"])
capitalizeFirst([])
