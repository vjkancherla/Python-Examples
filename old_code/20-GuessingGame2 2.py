#!/usr/bin/env python3

def doTheGuessing():
    allNumbers = range(1, 100)
    guessCount = 1

    first = 0
    last = len(allNumbers) - 1
    mid = (first + last) // 2

    while (last >= first):

        guess = allNumbers[mid]

        userInput = input("is {g} the number you are thinking of? yes/too high(h)/too low(l): ".format(g=guess))

        if userInput == "yes":
            print("The computer guessed the number, {g}, in {t} tries".format(g=guess, t=guessCount))
            return

        if userInput == "h":
            last = mid - 1
            mid = (first + last) // 2
        elif userInput == "l":
            first = mid + 1
            mid = (first + last) // 2

        guessCount += 1


def main():
    input("THINK of a number between 1 and 100. The computer will guess the number. Press enter when ready")

    doTheGuessing()

main()
