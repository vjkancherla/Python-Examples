#!/usr/bin/env python3

def generateFibanocci(totalNumber):
    fib = []
    count = 2
    num = 0
    while count <= totalNumber:
        if len(fib) == 0:
            fib.append(1)
            fib.append(1)
            continue

        num1, num2 = fib[-2:]

        fib.append(num1 + num2)

        count += 1

    print ("here you go: ")
    for i in fib:
        print(i)

def main():
    totalNumber = int(input("How many numbers of Fibanocci should I generate? "))
    generateFibanocci(totalNumber)


main()
