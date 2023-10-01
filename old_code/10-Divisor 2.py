#!/usr/bin/env python3

num = input("Please enter a number: ")

intNum = int(num)
divisors = []

for i in range(1, intNum):
    if intNum % i == 0:
        divisors.append(i)

print ("The divisors for {n} are {l}".format(n=intNum,l=divisors))
