class TreeNode:
    def __init__(self, data, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right


# Binary Tree traversal: DFS (recursively)
# node -> left -> right
def preorder_tarversal(node):
    if node is None:
        return
    else:
        print(node.data)
    preorder_tarversal(node.left)
    preorder_tarversal(node.right)

# left -> node -> right
def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.data)
    inorder_traversal(node.right)

# left -> right -> node
def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data)

# Stack (Last in first out)
# node -> left -> right
def stack_preorder_traversal(node):
    if node is None:
        return 
    stack = [node]
    while stack:
        root = stack.pop()
        print(root.data)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)

"""
     1
  0     2
4   3  8  7
"""

# left -> node -> right
def stack_inorder_traversal(node):
    if node is None:
        return
    stack = []
    
    current = node
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
            
        current = stack.pop()
        print(current.data)

        current = current.right
    

        

        

# BFS : level order traversal: Queue(First in First out)
def level_order_traversal(node):
    if node is None:
        return
    queue = [node]
    while queue:
        root = queue.pop(0)
        print(root.data)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

"""
     1
  0     2
4   3  8  7
"""
root_node = TreeNode(1)
first_node = TreeNode(0)
second_node = TreeNode(2)
third_node = TreeNode(4)
fourth_node = TreeNode(3)
fifth_node = TreeNode(8)
sixth_node = TreeNode(7)

root_node.left = first_node
root_node.right = second_node
first_node.left = third_node
first_node.right = fourth_node
second_node.left = fifth_node
second_node.right = sixth_node
# 1 0 2 4 3 8 7
# preorder_tarversal(root_node) # 1 0 4 3 2 8 7
# inorder_traversal(root_node) # 4 0 3 1 8 2 7
# postorder_traversal(root_node) # 4 3 0 8 7 2 1
#level_order_traversal(root_node) # 1 0 2 4 3 8 7
# stack_preorder_traversal(root_node) # 1 0 4 3 2 8 7
stack_inorder_traversal(root_node) # 4 0 3 1 8 2 7

