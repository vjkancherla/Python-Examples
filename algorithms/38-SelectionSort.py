#!/usr/bin/env python3

"""
Selection Sort:

eg:
arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and swap it with the val at the beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and swap it with the val at the beginning[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and swap it with the val at the beginning[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and swap it with the val at the beginning[3...4]
11 12 22 25 64

Big O: O(n^2)
"""

def selectionSort(lis_t):
    print ("About to sort: {}".format(lis_t))

    start_idx = 0

    #[64, 25, 12, 22, 11]
    for i in range(len(lis_t)):
        min_val_in_iteration = lis_t [i]
        index_of_min_val = i

        for j in range(start_idx, len(lis_t)):
            val = lis_t [j]

            if val < min_val_in_iteration:
                min_val_in_iteration = val
                index_of_min_val = j

        #SWAP vals
        val_at_i = lis_t [i]
        lis_t [i] = (val_at_i + min_val_in_iteration) - val_at_i
        lis_t [index_of_min_val] = (val_at_i + min_val_in_iteration) - min_val_in_iteration

        start_idx += 1

    print ("Result: {}".format(lis_t))


selectionSort([64, 25, 12, 22, 11])
selectionSort([124, 33, 1, 222, 11211, 5, 2, 2, 2, 1])
