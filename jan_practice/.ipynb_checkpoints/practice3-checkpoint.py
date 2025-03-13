"""
Binary tree implementation in Python.

A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.

Types of binary trees:
- Complete: All levels are completely filled except possibly for the last level, which is filled from left to right.
- Perfect: All internal nodes have two children and all leaves are at the same level.
- Full: Every node other than the leaves has two children.
- Balanced: The height of the tree is O(log n), where n is the number of nodes.

Classes:
    Node: Represents a node in the binary tree.
"""
from collections import deque
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        else:
            queue = deque([self.root])
            while queue:
                n = queue.popleft()
                if n.left is None:
                    n.left = Node(data)
                    break
                else:
                    queue.append(n.left)
                if n.right is None:
                    n.right = Node(data)
                    break
                else:
                    queue.append(n.right)
    # Node -> left -> right
    def pre_order(self, node):
        stack = [node]
        while stack:
             current = stack.pop()
             print(current.data, end = " ")
             if current.right:
                 stack.append(current.right)
             if current.left:
                 stack.append(current.left)
        print()
    # left -> Note -> right
    def in_order(self, node):
        pass
    

# Object 
binary = BinaryTree()
binary.insert(1)
binary.insert(2)
binary.insert(3)
binary.insert(4)
binary.insert(5)
binary.insert(6)
binary.insert(7)

binary.pre_order(binary.root)
