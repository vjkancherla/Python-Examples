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
    start = 1
    fib_ct = 0
    prev_2_nums = {}
    while start <= num:
        if start <= 2:
            fib_ct = 1
            if len(prev_2_nums) == 0:
                prev_2_nums [0] = fib_ct
            else:
                prev_2_nums [1] = fib_ct
        else:
            fib_ct = prev_2_nums [0] + prev_2_nums [1]
            prev_2_nums [0] = prev_2_nums [1]
            prev_2_nums [1] = fib_ct

        start += 1

    print fib_ct

fib(4)
fib(10)
fib(28)
fib(35)
fib(135)
