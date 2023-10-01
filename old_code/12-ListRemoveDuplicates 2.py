#!/usr/bin/env python3

def noDuplicates(aList):
    aSet = set(aList)

    return list(aSet)


def main():
    aList = [1,1,2,2,4,4,5,5,6,6,7,7]

    print ("{o} without duplicates {n}".format(o=aList, n=noDuplicates(aList)))

main()
