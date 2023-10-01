#!/usr/bin/env python3

'''
Write a function that accepts an integer N and
returns a NxN Spiral Martix.
EG:
martix(2)
[
[1,2]
[4,3]
]

martix(3)
[
[1,2,3]
[8,9,4]
[7,6,5]
]

matrix(4)
[
[1,2,3,4]
[12,13,14,5]
[11,16,15,6]
[10,9,8,7]
]
'''

def matrix(a_num):
    result=[]
    start_row=0
    end_row=a_num-1
    start_col=0
    end_col=a_num-1
    count=1

    for i in range(a_num):
        l = []
        for j in range(a_num):
            l.append(0)
        result.append(l)

    print(result)

    while start_row <= end_row and start_col <= end_col:
        print(f"start_row:{start_row}, end_row:{end_row}, start_col={start_col}, end_col={end_col}")

        #Top Row
        for col in range(start_col, end_col+1):
            print(f"T result[{start_row}][{col}] = {count}")
            result[start_row][col] = count
            count+=1

        start_row+=1

        print(f"start_row:{start_row}, end_row:{end_row}, start_col={start_col}, end_col={end_col}")

        #Right Column
        for rw in range(start_row, end_row+1):
            print(f"R result[{rw}][{end_col}] = {count}")
            result[rw][end_col] = count
            count+=1

        end_col-=1

        print(f"start_row:{start_row}, end_row:{end_row}, start_col={start_col}, end_col={end_col}")

        #End Row
        for col in range(end_col, start_col-1, -1):
            print(f"B result[{end_row}][{col}] = {count}")
            result[end_row][col] = count
            count+=1

        end_row-=1

        print(f"start_row:{start_row}, end_row:{end_row}, start_col={start_col}, end_col={end_col}")

        #Left Column
        for rw in range(end_row, start_row-1, -1):
            print(f": result[{rw}][{start_col}] = {count}")
            result[rw][start_col] = count
            count+=1

        start_col+=1

    for i in range(a_num):
        print(result[i])


matrix(4)
