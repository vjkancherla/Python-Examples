"""
Write a function called factorial which accepts a number and returns the
factorial of the number.

eg: factorial(4) // 4 * 3 * 2 * 1 = 24
eg: factorial(0) // 1
"""
printt = ""
def factorial(number):
    global printt
    printt += " * "+str(number)
    if number == 0 or number == 1:
        print (printt)
        printt = ""
        return 1

    return number * factorial(number-1)

print (factorial(4))
print (factorial(0))
print (factorial(10))
