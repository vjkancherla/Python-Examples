#!/usr/bin/env python3

def inputToList(userInput):
    return userInput.split(",")

def main():
    userInput = input("Give me a comma separated list of numbers: ")

    userList = inputToList(userInput)

    newList = []
    newList.append(userList[0])
    newList.append(userList[-1])

    print (*newList)

main()
