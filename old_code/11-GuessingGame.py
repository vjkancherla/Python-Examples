#!/usr/bin/env python3
from random import randint

noOfTries = 0
answerNum = randint(0, 9)

def main():
    global noOfTries
    global userGuess

    userGuess = int(input("What number am I thinking of? "))

    noOfTries += 1

    if userGuess == answerNum:
        print("You are correct! I was, indeed, thinking of {an}. You guessed the number in {nt} tries".format(an=answerNum, nt=noOfTries))
    elif userGuess < answerNum:
        print("Sorry, the number I am thinking off is greater than your guess of {ug}. Have another go".format(ug=userGuess))
        main()
    elif userGuess > answerNum:
        print("Sorry, the number I am thinking off is lesser than your guess of {ug}. Have another go".format(ug=userGuess))
        main()


main()
