#!/usr/bin/env python3

"""
Each element in a linked list is stored in the form of a node.
Node: A node is a collection of two sub-elements or parts.
A data part that stores the element and a next part that stores the link/reference to the next node.
"""

class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


class LinkedList:
   def __init__(self, rootNode):
      self.rootNode = rootNode

   def listprint(self):
      printval = self.rootNode
      while printval is not None:
         print (printval.data)
         printval = printval.nextNode


childNode = Node("Iam a Child", None)
rootNode = Node("I am root", childNode)
lkdList = LinkedList(rootNode)
lkdList.listprint()
