"""
Write a recrsive function called capitalizeWords. Given an array of words,
return a new array containing each work capitalized.

eg: words = ["i", "am", "learning", "recursion"]// I AM LEARNING RECURSION
"""

def capitalizeWords(lis_t):
    print ("Processing {}".format(lis_t))

    capitalized_list = []

    def doWork(lis_t):
        if len(lis_t) == 0:
            return

        str = lis_t [0]
        capitalized_list.append(str.upper())
        lis_t.pop(0)

        return doWork(lis_t)

    doWork(lis_t)

    print ("Result = {}".format(capitalized_list))


capitalizeWords (["i", "am", "learning", "recursion"])
capitalizeWords (["where", "is", "the", "summer"])
