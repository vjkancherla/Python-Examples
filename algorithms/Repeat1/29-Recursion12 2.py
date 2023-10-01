"""
Write a recrsive function called capitalizeWords. Given an array of words,
return a new array containing each work capitalized.

eg: words = ["i", "am", "learning", "recursion"]// I AM LEARNING RECURSION
"""

def capitalizeWords(lis_t):
    print ("Processing: {}".format(lis_t))

    result_list = []

    def doWork(idx):
        if idx == len(lis_t):
            return
        result_list.append(lis_t[idx].upper())
        return doWork(idx+1)

    doWork(0)

    print ("Capitalized List: {}".format(result_list))


capitalizeWords (["i", "am", "learning", "recursion"])
capitalizeWords (["where", "is", "the", "summer"])
