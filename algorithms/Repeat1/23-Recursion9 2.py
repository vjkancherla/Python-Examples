"""
Write a recursive function called 'flatten' which accepts an list of lists
and returns a new array with all value flattened.

eg: flatten([1,2,3,[4,5]]) // [1,2,3,4,5]
eg: flatten([1,[2, [3,4,[5]]]) // [1,2,3,4,5]
eg: flatten([[1],[2],[3]]) // [1,2,3]
eg: flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) // [1,2,3]
eg: flatten([[11,45,[34,55,[22,[4,5]]]],[2],[3]]) // [11, 45, 34, 55, 22, 4, 5, 2, 3]
"""

def flatten(lis_t):
    print ("Processing {}".format(lis_t))
    flattened_list = []

    def doWork(liss_t):
        if len(liss_t) == 0:
            return

        for elmnt in liss_t:
            if type(elmnt) == list:
                doWork(elmnt)
            else:
                flattened_list.append(elmnt)

    doWork(lis_t)

    print ("Flattend list: {}".format(flattened_list))


flatten([1,2,3,[4,5]])
flatten([1,[2, [3,4,[5]]]])
flatten([[1],[2],[3]])
flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])
flatten([[11,45,[34,55,[22,[4,5]]]],[2],[3]])
