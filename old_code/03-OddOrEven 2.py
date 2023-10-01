#!/usr/bin/env python3

num = input("enter a number: ")

evenOrOdd = "odd"
primeOrNot = "prime"

if int(num) % 2 == 0:
    evenOrOdd = "even"

for i in range(2, (int(num)-1)):
    if int(num) % i == 0:
        primeOrNot = "not prime"


print ("{n} is an {e} number, and {p}".format(n=num, e=evenOrOdd, p=primeOrNot))
