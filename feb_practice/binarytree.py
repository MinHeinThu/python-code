# Binary Tree Implementation in python


class TreeNode:
    def __init__(self, node, right = None, left = None):
        self.right = right
        self.left = left
        self.node = node


class BinaryTree:

    def __init__(self):
        self.root = None
    

    def insert_tree_node(self, node):
        new_node = TreeNode(node)
        if self.root is None:
            self.root = new_node
            return
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            
            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)
        
        
    def pre_order_traversal(self, node):
        if node is None:
            return
        else:
            print(node.node)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)

            
    


binary_tree = BinaryTree()

binary_tree.insert_tree_node(1)
binary_tree.insert_tree_node(2)
binary_tree.insert_tree_node(3)
binary_tree.insert_tree_node(4)
binary_tree.insert_tree_node(5)
binary_tree.insert_tree_node(6)
binary_tree.insert_tree_node(7)


binary_tree.pre_order_traversal(binary_tree.root)
