#!/usr/bin/env python3

"""
Trees are a data structure composed of nodes used for storing hierarchical data.

Each tree node typically stores a value and references to its child nodes.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print(f"Adding {child_node.value} as a child")
        self.children.append(child_node)

    def remove_child(self, child_node):
        print(f"Removing {child_node.value} as a child")

        for child in self.children:
            if child.value == child_node.value:
                self.children.remove(child)
                break;

    def __str__(self):
        childs = []
        for child in self.children:
            childs.append(child.value)
        return f"The Node - {self.value} - has the following Children: {childs}"

childN1 = Node("Iam N1")
childN2 = Node("Iam N2")
childN3 = Node("Iam N3")
rootN = Node("Iam Root")
rootN.add_child(childN1)
rootN.add_child(childN2)
rootN.add_child(childN3)
print(rootN)
