# Binary Search Tree
# root is greater than root.leftchild
# root is less than root.rightchild

class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data 
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert_the_node(self, node_data):
        if self.root is None:
            self.root = node_data
            return
        else:
            current_node = self.root
            while True:
                if node_data > current_node.data:
                    if current_node.right is None:
                        current_node.right = node_data
                        return
                    else:
                        current_node = current_node.left
                elif node_data < current_node.data:
                    if current_node.left is None:
                        current_node.left = node_data
                        return
                    else:
                        current_node = current_node.right
                
                
        
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

binary = BinarySearchTree()

binary.insert_the_node(node1)
binary.insert_the_node(node2)
binary.insert_the_node(node3)
binary.insert_the_node(node4)
binary.insert_the_node(node5)
binary.insert_the_node(node6)
binary.insert_the_node(node7)