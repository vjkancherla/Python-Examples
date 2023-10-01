#!/usr/bin/env python3
from random import randint

def generatePassword(pwdLength):
    numbersList = list(range(0, 9))
    lettersList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "f", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    specialList = ['!', '$', '%', '@']
    masterList = [numbersList, lettersList, specialList]

    count = 0
    pwdList = []
    while count < pwdLength:
        rand1 = randint(0, 2)
        aList = masterList[rand1]

        rand2 = randint(0, len(aList)-1)
        pwdChar = aList[rand2]
        pwdList.append(pwdChar)

        count += 1

    print(''.join(str(i) for i in pwdList))


def main():
    pwdLength = int(input("What is the length of your desired password? "))

    generatePassword(pwdLength)


main()
