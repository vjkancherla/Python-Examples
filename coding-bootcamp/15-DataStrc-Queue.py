#!/usr/bin/env python3

"""
Create a FIFO Queue Data Stuct.
Queue should be able accept calls to methods add, remove and peek.
Adding to the queue should store an element until it is removed.
The peek method should return the item that will be removed next.
"""

class Queue:
    list_as_a_queue = []

    #All classes have a function called __init__(), which is always executed when the class is being initiated.
    def __init__(self):
        self.list_as_a_queue = []

    #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the clas
    def add(self, anything):
        self.list_as_a_queue.insert(0, anything)

    def remove(self):
        return self.list_as_a_queue.pop(-1)

    def peek(self):
        return self.list_as_a_queue[-1]


##Invoke the class
que = Queue()
que.add(10)
que.add(20)
que.add(30)
print(que.list_as_a_queue)
print(que.peek())
que.remove()
print(que.peek())
que.remove()
print(que.list_as_a_queue)
