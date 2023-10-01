"""
Write a recursive function called capitalizeFirst. Given an array of Strings,
capitalize the first letter of each string in the array

eg: capitalizeFirst(["cap", "tap", "lap"]) // Cap, Tap, Lap
eg: capitalizeFirst(["packer", "racker", "breaker"]) // Packer, Racker, Breaker
"""

def capitalizeFirst(lis_t):
    print ("Processing {}".format(lis_t))

    result_list = []

    def doWork(idx):
        if idx == len(lis_t):
            return

        val = lis_t [idx]
        val = val[0].upper()+val[1:]

        result_list.append(val)

        return doWork(idx+1)

    doWork(0)
    print ("Result: {}".format(result_list))

capitalizeFirst(["cap", "tap", "lap"])
capitalizeFirst(["packer", "racker", "breaker"])
capitalizeFirst([])
