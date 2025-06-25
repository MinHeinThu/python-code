# Tree implementation with Python

# Binary Tree data structure has left and right child of each node
from collections import deque
# Time , Space : O(n)

"""
        1
    2       3

4      8     9     5

"""
class TreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.right = right
        self.left = left

class BinaryTree:

    def __init__(self):
        self.root = None

    # insert the new node manually level by level
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                if current.left is None:
                    current.left = TreeNode(data)
                    break
                else:
                    queue.append(current.left)

                if current.right is None:
                    current.right = TreeNode(data)
                    break
                else:
                    queue.append(current.right)
    
    # DFS using recursive method 

    # node left right
    def pre_order_traversal(self,node):
        if node is None:
            return
        if node:
            print(node.data, end = " ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
    
    # left node right
    def in_order_traversal(self,node):
        if node is None:
            return
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end = " ")
            self.in_order_traversal(node.right)
    
    # left right node
    def post_order_traversal(self, node):
        if node is None:
            return
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end= " ")

    # DFS Iterative method using stack

    # node left right
    # step one : build the stack with the data root node
    # if stack is true pop from the stack and print it of data
    # check and first right of it node and left and then append to the stack
    
    def preorder(self, node):
        stack = [node]
        while stack:
            n = stack.pop()
            print(n.data, end = ' ')
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)

    # left node right
    def inorder(self, node):
       stack = []
       current = node
       while stack or current:
            while current:
               stack.append(current)
               current = current.left

            current = stack.pop()
            print(current.data, end= ' ')
            current = current.right
    
    # left right node
    def postorder(self, node):
        stack = [node]
        stack2 = []

        while stack:
            n = stack.pop()
            stack2.append(n)
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
        
        while stack2:
            print(stack2.pop().data, end = ' ')
        
    # BFS : Queue (level order traversal)

    def level_order(self, node):
        queue = deque([node])
        while queue:
            n = queue.popleft()
            print(n.data, end= ' ')
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        
binarytree = BinaryTree()

binarytree.insert(1)
binarytree.insert(2)
binarytree.insert(3)
binarytree.insert(4)
binarytree.insert(8)
binarytree.insert(9)
binarytree.insert(5)

print("Preorder traversal:")
binarytree.pre_order_traversal(binarytree.root)
print('\n')
print("Inorder traversal:")
binarytree.in_order_traversal(binarytree.root)
print('\n')
print("Postorder traversal:")
binarytree.post_order_traversal(binarytree.root)
print('\n')

binarytree.preorder(binarytree.root)
print()

binarytree.inorder(binarytree.root)
print()

binarytree.postorder(binarytree.root)
print()

binarytree.level_order(binarytree.root)
print()