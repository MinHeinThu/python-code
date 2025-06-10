# Node
class Node:
    # Node has two parts: data and point to other node
    def __init__(self, data, next = None): # Instructor
        self.data = data
        self.next = next

class SingleNode:
    # Nothing is exist
    def __init__(self):
        self.head = None
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    # Insert the node at the beginning 
    def insert_at_beginning(self, new_data):
        """
        Time Complexity: O(1) - constant time as we only modify the head
        Space Complexity: O(1) - only creating one new pointer
        """
        new_node = new_data
        new_node.next = self.head
        self.head = new_node
    def length_node(self):
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length


    # Insert the node at the middle
    def insert_at_middle(self, new_node, position):
        """
        Time Complexity: O(n) - need to traverse to the desired position
        Space Complexity: O(1) - only creating one new pointer
        """
        if position < 0 or position > self.length_node():
            print("Invalid position")
            return
        if position == 0:
            self.insert_at_beginning(new_node)
            return
        current_node = self.head
        current_position = 0
        while True:
            if current_position == position:
                previous_node.next = new_node
                new_node.next = current_node
                break
            previous_node = current_node
            current_node = current_node.next
            current_position += 1
        
    
    # Insert the node at the end
    def insert_at_end(self, new_data):
        """
        Time Complexity: O(n) - need to traverse to the end of list
        Space Complexity: O(1) - only creating one new pointer
        """
        if self.head is None:
            self.head = new_data
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_data
    
    # Delete from the beginning
    def delete_from_beginning(self):
        """
        Time Complexity: O(1) - only modifying the head pointer
        Space Complexity: O(1) - no extra space needed
        """
        if self.head is None:
            print("This linked list is empty")
            return
        self.head = self.head.next
            
    # Delete for the end
    def delete_from_end(self):
        """
        Time Complexity: O(n) - need to traverse to second-to-last node
        Space Complexity: O(1) - no extra space needed
        """
        if self.head is None:
            print("This linked list is empty") 
            return
        if self.head.next is None:  # Changed condition
            self.head = None
            return
        
        last_node = self.head
        while last_node.next.next:
            last_node = last_node.next
        last_node.next = None  
    
    # Traverse the linked list
    def printList(self):
        """
        Time Complexity: O(n) - need to visit each node
        Space Complexity: O(1) - only using a single pointer
        """
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

# Object of node
node0 = Node("Min")
node1 = Node("Hein")
node3 = Node("Thu")
node4 = Node("Loves")
node5 = Node("Saw")
node6 = Node("Yu")
node7 = Node("Mon")
node8 = Node("Mon")
node9 = Node("Min")


# Object of single linked list
single = SingleNode()

# Insert from end
single.insert_at_end(node3)
single.insert_at_end(node4)
single.insert_at_end(node5)
single.insert_at_end(node6)
single.insert_at_end(node7)

# Insert from beginning
single.insert_at_beginning(node1)
single.insert_at_beginning(node0)

# Insert at middle
single.insert_at_middle(node8, 6)
single.insert_at_middle(node9, 0)

# Delete from begnning
single.delete_from_beginning()

# Delete from end
single.delete_from_end()

single.printList()