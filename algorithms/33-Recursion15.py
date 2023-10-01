"""
Write a recursion function to accept the following data structure -
     3
   / | \\
  4  5  6
 /\\  /\\  /\\
2  7 6 9 5 4

- and print:
3
4+5+6 = 15
2+7+6+9+5+4 = 33
"""

class Node:
    def __init__(self, data, childrenNodes=None):
        if childrenNodes is None:
          childrenNodes = []

        self.data = data
        self.childrenNodes = childrenNodes

    def __str__(self):
        return "Data: {}, Children: {}".format(self.data, self.childrenNodes)

l3_n2 = Node("2")
l3_n7 = Node("7")
l3_n6 = Node("6")
l3_n9 = Node("9")
l3_n5 = Node("5")
l3_n4 = Node("4")
l2_n4 = Node("4", [l3_n2, l3_n7])
l2_n5 = Node("5", [l3_n6, l3_n9, l3_n5])
l2_n6 = Node("6", [l3_n4])
l1_n3 = Node("3", [l2_n4, l2_n5, l2_n6])

root_node = l1_n3

def addNumbersAtEachLevel(root_node):
    print ("Processing the Node: {}".format(root_node))

    level = 1
    sum_dict = {}

    def doWork(node, level):

        data = int(node.data)
        child_nodes = node.childrenNodes

        key = "level_"+str(level)+"_sum"
        if key in sum_dict:
            sum_dict [key] += data
        else:
            sum_dict [key] = data

        if child_nodes != None:
            level += 1
            for child in child_nodes:
                doWork(child, level)
        else: #Base case for Recursion
            return

    doWork(root_node, level)

    print (sum_dict)

addNumbersAtEachLevel(root_node)
