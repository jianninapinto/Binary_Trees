from collections import deque

class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse(root: node):
    # Check that we are not at the end of the tree
    if root is None:
        return 
    # Instantiate the deque
    queue = deque() # FIFO first element to get in is the first element to get out
    # Add the root node to the queue
    queue.append(root)
    # Create an empty values array to store the nodes that we visit
    values = []

    while len(queue) > 0: # while the queue isn't empty
        # dequeue the node by popping it
        current = queue.popleft()
        # collect the values
        values.append(current.value)
        # add pointers to the queue
        # check if left and right nodes exist
        if current.left:
            # add left neighbor to the queue
            queue.append(current.left)
        if current.right:
            # add right neighbor to the queue
            queue.append(current.right)
    # Return the visited nodes
    return values



# Test cases:
head = node(6)
head.left = node(3)
head.right = node(9)

print(traverse(head)) # 6, 3, 9

# Implement a level-order breadth-first traversal for a binary tree using the provided class for a binary tree node.
# the return should be a list of values in the binary tree, based on a level-order (searching left to right at each "level") breadth-first traversal

# Hint: implementing BFS requires a queue data structure.
# For a quick and easy queue implementation:
# queue = deque()
# then queue.append(value) to push and queue.popleft(value) to dequeue