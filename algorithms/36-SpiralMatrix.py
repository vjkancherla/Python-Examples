'''
Write a function call createSpiralMatrix, which accepts the dimensions of the matrix, and prints
a spiral matrix.

For eg:
createSpiralMatrix(rows, colmns)::

createSpiralMatrix(2, 2):
[1, 2]
[3, 4]

createSpiralMatrix(3, 3):
[1, 2, 3]
[8, 9, 4]
[7, 6, 5]

createSpiralMatrix(4, 4):
[1,   2,  3, 4]
[12, 13, 14, 5]
[11, 16, 15, 6]
[10,  9,  8, 7]

createSpiralMatrix(3, 2):
[1, 2]
[6, 3]
[5, 4]
'''

def createSpiralMatrix(rows, colmns):
    print("Printing a {} x {} spiral matrix".format(rows, colmns))

    start_row_idx = 0
    end_row_idx = rows - 1
    start_colmn_idx = 0
    end_colmn_idx = colmns - 1
    number = 1

    #initialise results_matrix with just zeros
    result_matrix = []
    for i in range(rows):
        lis_t = []
        for j in range(colmns):
            lis_t.append(0)

        result_matrix.append(lis_t)


    #the key of the solution is to have 4 loops. One each for:
    # -- building the top row left to right
    # -- building the right most (last) column top to bottom
    # -- building the bottom row right to left
    # -- building the left most (first) column bottom to top

    while start_row_idx <= end_row_idx and start_colmn_idx <= end_colmn_idx:

        #loop-1: building the top row left to right
        i = start_colmn_idx
        while i <= end_colmn_idx:
            result_matrix [start_row_idx][i] = formatNumber(number)
            number += 1
            i += 1

        start_row_idx +=1

        #loop-2: building the right most (last) column top to bottom
        i = start_row_idx
        while i <= end_row_idx:
            result_matrix [i][end_colmn_idx] = formatNumber(number)
            number += 1
            i += 1


        end_colmn_idx -= 1

        #loop-3: building the bottom row right to left
        i = end_colmn_idx
        while i >= start_colmn_idx:
            result_matrix [end_row_idx][i] = formatNumber(number)
            number += 1
            i -= 1

        end_row_idx -=1

        #loop-4: building the left most (first) column bottom to to
        i = end_row_idx
        while i >= start_row_idx:
            result_matrix [i][start_colmn_idx] = formatNumber(number)
            number += 1
            i -= 1

        start_colmn_idx += 1

    for i in range(len(result_matrix)):
        print (result_matrix[i])

    print ("---")


def formatNumber(number):
    if number < 10:
        return "0"+str(number)
    else:
        return str(number)

createSpiralMatrix(2, 2)
createSpiralMatrix(3, 3)
createSpiralMatrix(4, 4)
createSpiralMatrix(5, 5)
createSpiralMatrix(5, 2)
