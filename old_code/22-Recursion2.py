"""
     3
   / | \\
  4  5  6
 /\\  /\\  /\\
2  7 6 9 5 4

print 
3
4+5+6 = 15
2+7+6+9+5+4 = 33
"""

class Node:
    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by Python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # __repr__ etc. are called special methods (or sometimes called dunder methods)
    # You should not invent such names on your own.
    def __init__(self, data, childrenNodes=None):
        # Assign the argument to the instance's name attribute
        if childrenNodes is None:
          childrenNodes = []
        
        self.data = data
        self.childrenNodes = childrenNodes
  
    def __str__(self):
        return str(self.data)

    __repr__ = __str__

tree = Node("3", [Node("4"), Node("5"), Node("6")])

def traverseNodes(node):
    level = 0
    for nd in (node: )

print(traverseNodes(tree))