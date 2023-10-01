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
    idx = 0
    flattend_list = []

    def doWork(lis_t, idx):
        if idx == len(lis_t):
            return
        elmt = lis_t [idx]
        if type(elmt) != list:
            flattend_list.append(elmt)
        else:
            doWork(elmt, 0)
        doWork(lis_t, idx+1)

    doWork(lis_t, idx)
    print (flattend_list)

flatten([1,2,3,[4,5]])
flatten([1,[2, [3,4,[5]]]])
flatten([[1],[2],[3]])
flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])
flatten([[11,45,[34,55,[22,[4,5]]]],[2],[3]])
