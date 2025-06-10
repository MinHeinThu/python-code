# Binary Tree Implementation

class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# Binary tree

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
            return
        else:
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    queue.append(current.left)
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    queue.append(current.right)
    # Node -> left -> right
    def pre_order_traversal(self, node):
        stack = [node]
        while stack:
            current = stack.pop()
            print(current.data)
            if current.right:
                stack.append(current.left)
            if current.left:
                stack.append(current.right)

        

tree = BinaryTree()

tree.insert_node(1)
tree.insert_node(2)
tree.insert_node(3)

tree.pre_order_traversal(tree.root)
        
