#!/usr/bin/env python3

def main():
    with open('primenumbers.txt', 'r') as open_file1:
        primeNumbers = open_file1.read().splitlines()

    with open('happynumbers.txt', 'r') as open_file2:
        happyNumbers = open_file2.read().splitlines()

    overlappingNumbers = []

    for pNum in primeNumbers:
        if pNum in happyNumbers:
            overlappingNumbers.append(pNum)

    print ("The overlapping numbers are {n} ".format(n=overlappingNumbers))


main()
