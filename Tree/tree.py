from collections import deque
import random
import numpy as np

###################Setup_Code###################

class ExpressionNode(object):
    def __init__(self, data):
        self.data = random.choice(['+','-','*','/'])
        self.left = random.randint(1,10)
        self.right = random.randint(1,10)
    def __str__(self):
        return f'<{self.data}, {self.left}, {self.right}>'  

class RegularNode(object):
    def __init__(self, data):
        self.data = data
        self.left = '*'
        self.right = '*'
    def __str__(self):
        return f'<{self.data}, {self.left}, {self.right}>' 

# SET NODE EQUAL TO REGULARNODE FOR A STANDARD BINARY TREE, OR EXPRESSIONNODE FOR AN EXPRESSION TREE
Node = RegularNode     


# CREATE THE LIST YOURSELF
data = [3,5,2,1,4,6,7,8,9,10,11,12,13,14]

# OR UN-COMMENT THIS TO CREATE A RANDOM LIST
"""data = np.arange(13)
np.random.shuffle(data)
data = list(data)"""


# TURN THE LIST INTO A TREE STRUCTURE
n = iter(data)
tree = Node(next(n))
fringe = deque([tree])
while True:
    head = fringe.popleft()
    try:
        head.left = Node(next(n))
        fringe.append(head.left)
        head.right = Node(next(n))
        fringe.append(head.right)
    except StopIteration:
        break

###################Setup_Code###################

print(tree)