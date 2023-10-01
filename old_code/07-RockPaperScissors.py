#!/usr/bin/env python3
from random import randint

def playAgain():
    if str(input("Play again? y/n: ")) == "n":
        exit()
    else:
        main()

def main():
    choiceMap = {"1":"Rock", "2":"Scissors", "3":"Paper"}

    for i in choiceMap.keys():
        print (i + ":" + choiceMap.get(i))

    userChoice = int(input("Choose an option: "))

    myChoice = randint(1, 3)

    print ("Your choice is "+choiceMap.get(str(userChoice))+", and my choice is "+choiceMap.get(str(myChoice)))

    while True:
        diff = userChoice - myChoice

        if diff == 0:
            print ("Its a tie")
            playAgain()

        elif diff in [-1, 2]:
            print ("you Win. "+choiceMap.get(str(userChoice))+" trumps "+choiceMap.get(str(myChoice)))
            playAgain()

        elif diff in [1, -2]:
            print ("I Win. "+choiceMap.get(str(userChoice))+" is trumped by "+choiceMap.get(str(myChoice)))
            playAgain()

main()
