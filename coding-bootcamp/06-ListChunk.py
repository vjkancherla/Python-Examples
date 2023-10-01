#!/usr/bin/env python3

"""
Given an list and chunk size, divide the array into many subarrays where each subarray is of length size
Examples:
chunk([1,2,3,4], 2) => [[1,2], [3,4]]
chunk([1,2,3,4,5], 3) => [[1,2,3], [4,5]]
chunk([1,2,3], 8) => [[1,2,3]]
"""

def chunk(a_list, chunk):
    chunked_list = []

    for i in a_list:
        if len(chunked_list) == 0:
            a_chunk = [i]
            chunked_list.append(a_chunk)
        else:
            a_chunk = chunked_list[-1]
            if len(a_chunk) == chunk:
                new_chunk = [i]
                chunked_list.append(new_chunk)
            else:
                a_chunk.append(i)
                chunked_list[-1] = a_chunk

    print(f"{a_list} chucked with {chunk} is {chunked_list}")


chunk([1,2,3,4], 2)
chunk([1,2,3,4,5], 3)
chunk([1,2,3], 8)
