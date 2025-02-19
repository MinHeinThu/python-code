# Binary Search Tree
from collections import deque
class Node:
    def __init__(self, data , left = None, right = None):
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
                current = queue.popleft()
                if current.left is None:
                    current.left = Node(data)
                    break
                else:
                    queue.append(current.left)
                if current.right is None:
                    current.right = Node(data)
                    break
                else:
                    queue.append(current.right)
    # DFS traversal using stack iterative: node -> left -> right
    def preorder(self, node):
        stack = [node]
        while stack:
            current = stack.pop()
            print(current.data ,end = ' ')
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        print()
    # DFS traversal using stack iterative: left -> node -> right
    def inorder(self, node):
        stack = []
        current = node
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.data, end = ' ')
            current = current.right
        print()
    # DFS traversal using stack iterative: left right node
    def postorder(self, node):
        stack1 = [node]
        stack2 = []
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        while stack2:
            print(stack2.pop().data, end= ' ')
        print()
    # BFS lavel order traversal queue(FIFO)
    def lavelorder(self, node):
        queue = deque([self.root])
        list1 = []
        while queue:
            current = queue.popleft()
            list1.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print(list1) 

    # def delete(self, data):
    #     if self.root is None:
    #         return None
    #     if self.root:
    #         if self.root.left is None and self.root.right is None:
    #             self.root = None
    #     queue = deque([self.root])
    #     key_node = None
    #     deepest_node = None
    #     parent_of_deepest = None
    #     while queue:
    #         node = queue.popleft()
    #         if node.data == data:
    #             key_node = node
    #         if node.left:
    #             parent_of_deepest = node
    #             queue.append(node.left)
    #         if node.right:
    #             parent_of_deepest = node
    #             queue.append(node.right)
    #         deepest_node = node
    #     if key_node:
    #         key_node.data = deepest_node.data
    #         if parent_of_deepest.right == deepest_node:
    #             parent_of_deepest.right = None
    #         else:
    #             parent_of_deepest.left = None
    #     else:
    #         print(False)

    def delete(self, data):
        if self.root is None:
            print('Tree is empty')
            return
        if self.root:
            if self.root.left is None and self.root.right is None:
                self.root = None
                return
        queue = deque([self.root]) 
        key_node = None
        deepest_node = None
        deepest_of_parent = None
        while queue:
            node = queue.popleft()
            if node.data == data:
                key_node = node
            if node.left:
                deepest_of_parent = node
                queue.append(node.left)
            if node.right:
                deepest_of_parent = node
                queue.append(node.right)
            deepest_node = node
        if key_node:
            key_node.data = deepest_node.data
            if deepest_of_parent.right == deepest_node:
                deepest_of_parent.right = None
            else:
                deepest_of_parent.left = None
        else:
            print('Data is not found')
            return
        
"""
        0
    1       2
-1     1 1      3
"""
bst = BinaryTree()
bst.insert(0)
bst.insert(1)
bst.insert(2)
bst.insert(-1)
bst.insert(1)
bst.insert(1)
bst.insert(3)

bst.inorder(bst.root)
bst.preorder(bst.root)
bst.postorder(bst.root)
bst.lavelorder(bst.root)
bst.delete(0)
bst.lavelorder(bst.root)
bst.delete(9)
bst.lavelorder(bst.root)
            
            