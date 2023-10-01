"""
Write a recursive function called fib which accepts a number and returns the
n-th number in the Fibanocci sequence. Recall that the Fibanocci squence is a
sequence of while number 1,1,2,3,5,8,... which starts with 1 and 1, and where
every number thereafter is equal to the sum of the previous two numbers

eg: fib(4) //3 1,1,2,3
eg: fib(10) // 55
eg: fib(28) // 317811
eg: fib(35) // 9227465
"""

def fib(num):
    fib_num = 0
    fib_seq = []
    for i in range(1, num+1):
        if i<=2:
            fib_seq.append(1)
        else:
            fib_num = fib_seq [i-3] + fib_seq [i-2]
            fib_seq.append(fib_num)

    print ("The {}th number in the Finonacci sequence is {}".format(num, fib_num))
    print ("The full Fibonnaci sequence is:{}".format(fib_seq))
    print ("---")


fib(4)
fib(10)
fib(28)
fib(35)
fib(135)
