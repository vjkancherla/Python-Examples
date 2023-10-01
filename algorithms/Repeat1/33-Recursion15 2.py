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

def addNumbersAtEachLevel(node):

    level = 0
    sum_at_level = []

    def doWork(node, level):
        data = int(node.data)
        c_nodes = node.childrenNodes

        if len(sum_at_level) == level:
            sum_at_level.insert(level, data)
        else:
            tmpSum = sum_at_level [level]
            sum_at_level [level] = tmpSum + data

        if c_nodes != None:
            level += 1
            for nod_e in c_nodes:
                doWork(nod_e, level)
        else: #-- Base case for recursio
            return

    doWork(node, level)

    print ("Result: {}".format(sum_at_level))

addNumbersAtEachLevel(root_node)
