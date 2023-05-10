class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse(root: node):
    # Initialize an empty list to store the values visited
    values = []
    traverse_node(root, values)
    return values

def traverse_node(current, values):
    # visit left node if it exists
    if current.left:
        # call traverse node function recursively 
        traverse_node(current.left, values)
    # capture data of the current node, as it is visited during the traversal
    values.append(current.value)
        # visit right node if it exists
    if current.right:
        # call traverse node function recursively 
        traverse_node(current.right, values)



# Test cases:
head = node(6)
head.left = node(3)
head.right = node(9)

print(traverse(head)) # 3, 6, 9

# Implement an in-order depth-first traversal for a binary tree using the provided class for a binary tree node.
# the return should be a list of values in the binary tree, based on an in-order (left, current, right) depth-first traversal

# Hint: you can implement DFS either with recursion (using the system call stack) or by manually declaring your own stack data structure. 

# For a quick and easy stack implementation:
# from collections import deque
# stack = deque()
# then stack.append(value) to push and stack.pop(value) to pop