#!/usr/bin/env python3

def judgeTheGame(game):
    if (game[0][0] !=0 and game[0][0] == game[1][0] == game[2][0]) or \
       (game[0][1] !=0 and game[0][1] == game[1][1] == game[2][1]) or \
       (game[0][2] !=0 and game[0][2] == game[1][2] == game[2][2]) or \
       (game[0][0] !=0 and game[0][0] == game[0][1] == game[0][2]) or \
       (game[1][0] !=0 and game[1][0] == game[1][1] == game[1][2]) or \
       (game[2][0] !=0 and game[2][0] == game[2][1] == game[2][2]) or \
       (game[0][0] !=0 and game[0][0] == game[1][1] == game[2][2]) :
       print ("There is a Winner!")
    else:
       print ("There is No Winner")


def main():
    game1 = [
        [2, 2, 0],
    	[2, 1, 0],
    	[2, 1, 1]
    ]
    game2 = [
        [1, 2, 0],
    	[2, 1, 0],
    	[2, 1, 1]
    ]
    game3 = [
        [0, 1, 0],
    	[2, 1, 0],
    	[2, 1, 1]
    ]
    game4 = [
        [1, 2, 0],
    	[2, 1, 0],
    	[2, 1, 2]
    ]
    game5 = [
        [1, 2, 0],
    	[2, 1, 0],
    	[2, 1, 0]
    ]

    gamesList = [game1, game2, game3, game4, game5]

    for game in gamesList:
        judgeTheGame(game)


main()
