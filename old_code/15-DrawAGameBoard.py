#!/usr/bin/env python3

def drawTheBoard(rows, columns):
    tmpRows = rows
    while tmpRows > 0:
        colDraw = "|"
        rowDraw = ""
        tmpColumns = columns
        while tmpColumns > 0:
            rowDraw += " ---"
            if tmpColumns != 1:
                colDraw += "   |"
            else:
                colDraw += "   "
            tmpColumns -= 1
        colDraw += "|"
        if tmpRows == rows:
            print (rowDraw)
        print (colDraw)
        print (rowDraw)
        tmpRows -= 1


def main():
    boardSize = input("Give me the size of the board in AxB format. Eg 8x8: ")
    rowsAndColumns = boardSize.split("x")

    drawTheBoard(int(rowsAndColumns[0]), int(rowsAndColumns[1]))


main()
