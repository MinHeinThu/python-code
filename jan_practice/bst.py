# Binary Search Tree Implementation

# left child is smallar than root node
# right child is larger than root node
from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None # Initially , no left child
        self.right = None # Initially , no right child
        
class BinarySearchTree:
    def __init__(self):
        self.root = None # Start with empty tree
    # Insertion method Time: O(log n), Space O(1) constant
    def insert(self, data):
        new_node = TreeNode(data) # create the node to insert 
        if self.root is None:
            self.root = new_node
            return
        current = self.root # Start traversal from the root
        while True:
            if data < current.data: # if insert data is small go left
                if current.left is None: # check left and it is empty insert  
                    current.left = new_node
                    break # Done inserting
                current = current.left # left is not empty  current is current.left check again
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
    # DFS stack last in last out
    def preorder(self, node):
        current = [node]
        while current:
            current_node = current.pop()
            print(current_node.data, end= " ")
            if current_node.right:
                current.append(current_node.right)
            if current_node.left:
                current.append(current_node.left)
        print()
    # Time : O(log n) , Space : constand
    # For recusrsive way or worse case O(n)
    # For space complextiy
    # Recursive: O(h) - Where h is the height of the tree. O(log n) in the average case, O(n) in the worst case.
    def search(self, data):
        if self.root is None:
            return "Tree is empty"
        current = self.root
        while current:
            if data == current.data:
                return f'{data} is found'
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return f'{data} is not found'
    # Time: O(log n) avg, O(n) wrost: Space: O(H)
    # 
    def delete(self, data):
        def _delete(node, data):
            # if the node is empty
            if node is None:
                return None
            
            if data < node.data:
                node.left = _delete(node.left, data)
            elif data > node.data:
                node.right = _delete(node.right, data)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.data = successor.data
                node.right = _delete(node.right, successor.data)
            return node
        self.root = _delete(self.root, data)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left),self.height(node.right))
    def height_tree(self, node):
        if node is None:
            return 0
        height = 0
        queue = deque([node])
        while queue:
            level_size = len(queue)
            height += 1

            for i in range(level_size):
                Node = queue.popleft()

                if Node.left:
                    queue.append(Node.left)
                if Node.right:
                    queue.append(Node.right)
        return height
                


# Tree

tree = BinarySearchTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(-1)
tree.insert(-3)
tree.insert(0)
tree.insert(5)

tree.preorder(tree.root)
print(tree.search(6))
# tree.delete(1)
# tree.preorder(tree.root)
print(tree.height(tree.root))
print(tree.height_tree(tree.root))