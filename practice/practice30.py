# Python binary tree implementation

from os import lseek


class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root = None):
        self.root = root
    
    # Insert the node in the binary Tree
    # T: O(log n), O(n)
    # S: O(h), h = height of tree

    def insertion(self, node_data):
        if self.root is None:
            self.root = node_data
            return
        if self.root.left is None:
            self.root.left = node_data
            self.root = self.root.left
            return 
        elif self.root.left is not None:
            self.root.right = node_data
            self.root = self.root.right
            return
        
    def pre_order(self, node):
        if node is None:
            return
        else:
            print(node.data, end = "")
        self.pre_order(node.left)
        self.pre_order(node.right)
            


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

binary = BinaryTree()
binary.insertion(node1)
binary.insertion(node2)
binary.insertion(node3)
binary.insertion(node4)
binary.insertion(node5)
binary.insertion(node6)
binary.insertion(node7)

binary.pre_order(node1)