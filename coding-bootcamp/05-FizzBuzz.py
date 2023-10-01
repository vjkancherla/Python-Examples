#!/usr/bin/env python3


"""
Print integers one-to-N, but print "Fizz" if an integer is divisible by three,
"Buzz" if an integer is divisible by five, and "FizzBuzz" if an integer is divisible by both three and five.

eg: fizzbuzz(5)
1
2
Fizz
4
Buzz
"""

def fizzbuzz(a_int):
    for i in range(1,a_int+1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print ("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz(5)
fizzbuzz(25)
