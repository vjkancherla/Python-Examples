#!/usr/bin/env python3

"""
Use the Queue Class creaed in 15-DataStrc-Queue.py.
Create 2 queues.
Create a new Class called Weave.
The Weave class should accept the two queues as parameters.
And, should return a new queue which has both the items from the passed in queues, interweaved
eg:
q1 - [1,2,3,4]
q2 - [Hi, there, how, are, you]

weave_que - [1, Hi, 2, there, 2, how, 4, are, you]
"""

class Queue:
    list_as_a_queue = []

    #All classes have a function called __init__(), which is always executed when the class is being initiated.
    def __init__(self):
        self.list_as_a_queue = []
        self.index = 0

    #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the clas
    def add(self, anything):
        self.list_as_a_queue.insert(0, anything)

    def remove(self):
        return self.list_as_a_queue.pop(-1)

    def peek(self):
        return self.list_as_a_queue[-1]

    def __len__(self):
        return len(self.list_as_a_queue)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.list_as_a_queue[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def __str__(self):
        return f"{self.list_as_a_queue}"


class Weave:

    #All classes have a function called __init__(), which is always executed when the class is being initiated.
    def __init__(self, queue1, queue2):
        self.weave_que = []
        self.queue1 = queue1
        self.queue2 = queue2
        print("Queue1:")
        print(self.queue1)
        print("Queue2:")
        print(self.queue2)

    #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
    def weave(self):
        q1_len = len(self.queue1)
        q2_len = len(self.queue2)

        if q1_len > q2_len:
            for i in range(q2_len):
                self.weave_que.insert(0,self.queue1.remove())
                self.weave_que.insert(0,self.queue2.remove())

            for i in range(len(self.queue1)):
                self.weave_que.insert(0,self.queue1.remove())
        elif q2_len > q1_len:
            for i in range(q1_len):
                self.weave_que.insert(0,self.queue1.remove())
                self.weave_que.insert(0,self.queue2.remove())

            for i in range(len(self.queue2)):
                self.weave_que.insert(0,self.queue2.remove())
        else:
            for i in range(q1_len):
                self.weave_que.insert(0,self.queue1.remove())
                self.weave_que.insert(0,self.queue2.remove())

        print("Weaved Queue:")
        print(self.weave_que)
        return self.weave_que



q1 = Queue()
q1.add(1)
q1.add(2)
q1.add(3)
q1.add(4)

q2 = Queue()
q2.add("Hi")
q2.add("there")
q2.add("how")
q2.add("are")
q2.add("you")

weave = Weave(q1, q2)
weave.weave()
