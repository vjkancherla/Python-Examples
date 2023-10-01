#!/usr/bin/env python3

"""
Create a FILO/LIFO Stack Data Stuct.
Stack should be able accept calls to methods push, pop and peek.
Pusing to the queue should store an element until it is Popped.
The peek method should return the item at the top of the stack.
"""

class Stack:

    #All classes have a function called __init__(), which is always executed when the class is being initiated.
    def __init__(self):
        self.the_stack = []

    #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
    def push(self, object):
        self.the_stack.insert(0, object)

    def pop(self):
        return self.the_stack.pop(0)

    def peek(self):
        return self.the_stack[0]

    def __str__(self):
        return f"{self.the_stack}"


#Invoke the class
st = Stack()
st.push(22)
st.push(33)
st.push(44)
st.push(55)
st.push(66)
print("St:")
print(st)
st.pop()
st.pop()
print(st.peek())
print("St:")
print(st)
