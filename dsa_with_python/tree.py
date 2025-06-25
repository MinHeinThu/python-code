class TreeNode:
    """A class representing a node in a tree data structure."""
    def __init__(self, data):
        """
        Initialize a tree node.
        
        Args:
            data: The value to be stored in the node
        """
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        """
        Add a child node to the current node.
        
        Args:
            child: TreeNode object to be added as a child
        """
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        """Print the tree structure starting from this node."""
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_electronics_tree():
    """
    Build and return a sample electronics category tree.
    
    Returns:
        TreeNode: Root node of the electronics tree
    """
    # Create root node
    root = TreeNode("Electronics")

    # Create and populate laptop category
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    # Create and populate smartphone category
    smartphone = TreeNode("Smart Phone")
    smartphone.add_child(TreeNode("iPhone"))
    smartphone.add_child(TreeNode("Samsung"))
    smartphone.add_child(TreeNode("Mi"))
    
    # Create and populate TV category
    tv = TreeNode("TV")
    tv.add_child(TreeNode("TCL"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("Panasonic"))

    # Add all categories to root
    root.add_child(laptop)
    root.add_child(smartphone)
    root.add_child(tv)
    
    return root


def main():
    """Main function to demonstrate tree functionality."""
    electronics_tree = build_electronics_tree()
    electronics_tree.print_tree()


if __name__ == "__main__":
    main()