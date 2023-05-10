from collections import deque

class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse(root: node):
    # In-order traversal of the binary tree

    # If root node is None, the function immediately returns
    if root is None:
        return
    # Instantiate the stack to store nodes in the binary tree as they are visited
    stack = deque() # LIFO - Last in, first out
    # set root node as the current variable
    current = root
    # Initialize a variable to store the values of the nodes as they are visited
    values = []

    # Loop through the stack while it exists or while the current node is not None
    while (len(stack) > 0 or current is not None):
        # If the current node is not None
        if current is not None:
            # append it to the stack
            stack.append(current)
            # set current node to its left child
            current = current.left

        else:
            # If the current node is None it means we have reached the leftmost node in
            # the binary tree, so we pop the last node from the stack
            current = stack.pop()
            # add its value to the values list
            values.append(current.value)
            # set current node to its right child
            current = current.right
    # Return a list of the nodes in the order they were visited
    return values

# Test cases:
head = node(6)
head.left = node(3)
head.right = node(9)

print(traverse(head)) # 3, 6, 9

# This is the recursive solution. Could also be implemented with an explicitly-declared stack data structure.