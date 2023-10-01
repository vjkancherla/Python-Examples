#!/usr/bin/env python3
import datetime

name = input("tell us your name: ")
age = input("tell us your age: ")

now = datetime.datetime.now()

currentYear = int(now.year)

birthYear = currentYear - int(age)

hundrerYearsBirthYear = birthYear + 100

print ( "{n} you will be 100 in {y}".format(n=name, y=hundrerYearsBirthYear) )
