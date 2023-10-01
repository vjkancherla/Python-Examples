#!/usr/bin/env python3

def reverseSentance(userInput):
    listOfWords = userInput.split(" ")
    reverseList = listOfWords[::-1]
    print (*reverseList)

def main():
    userInput = input("Please enter a sentance: ")
    reverseSentance(userInput)

main()
