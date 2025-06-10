# Single Linked list
# each node has data and pointer to next node

class Node:
    def __init__(self, data, next=None):
        """
        Initialize a new node with data and a pointer to the next node.
        
        :param data: The data to store in the node.
        :param next: The next node in the linked list (default is None).
        """
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self, head=None):
        """
        Initialize a new single linked list with an optional head node.
        
        :param head: The first node in the linked list (default is None).
        """
        self.head = head
    
    # Calculting the lenght of the linked list

    def len_linked_list(self):
        """
        Calculate the length of the linked list.
        
        :return: The number of nodes in the linked list.
        
        Time Complexity: O(n) - Must traverse the entire list.
        Space Complexity: O(1) - Uses a constant amount of space.
        """
        current = self.head
        length = 0
        while current is not None:
            current = current.next
            length += 1
        return length   

   # Insert the node at beginning

    def insert_at_beginning(self, new_data):
        """
        Insert a new node at the beginning of the linked list.
        
        :param new_data: The data for the new node.
        
        Time Complexity: O(1) - Directly modifies the head pointer.
        Space Complexity: O(1) - Uses a constant amount of space.
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # Inserting at the end

    def insert_at_end(self, new_data):
        """
        Insert a new node at the end of the linked list.
        
        :param new_data: The data for the new node.
        
        Time Complexity: O(n) - Must traverse to the end of the list.
        Space Complexity: O(1) - Uses a constant amount of space.
        """
        if self.head is None:
            self.head = Node(new_data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(new_data)

    # Insert at position

    def insert_at_middle(self, new_data, position):
        """
        Insert a new node at a specified position in the linked list.
        
        :param new_data: The data for the new node.
        :param position: The position to insert the new node.
        
        Time Complexity: O(n) - Must traverse to the specified position.
        Space Complexity: O(1) - Uses a constant amount of space.
        """
        if position == 0:
            self.insert_at_beginning(new_data)
            return
        if 0 > position or position > self.len_linked_list():
            print("Invalid position")
            return
        current = self.head
        current_position = 0
        while current_position < position and current is not None:
            previous = current
            current = current.next
            current_position += 1
        new_node = Node(new_data)
        previous.next = new_node
        new_node.next = current

    # Deletion at the beginning

    def deletion_at_beginning(self):
        """
        Delete the node at the beginning of the linked list.
        
        Time Complexity: O(1) - Directly modifies the head pointer.
        Space Complexity: O(1) - Uses a constant amount of space.
        """
        if self.head is None:
            print("The linked list is empty")
            return
        self.head = self.head.next

    # Deletion at the end

    def deletion_at_end(self):
        """
        Delete the node at the end of the linked list.
        
        Time Complexity: O(n) - Must traverse to the second-to-last node.
        Space Complexity: O(1) - Uses a constant amount of space.
        """
        if self.head is None:
            print("The linked list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        last_node = self.head
        while last_node.next.next:
            last_node = last_node.next
        last_node.next = None

    # Deletion at the position

    def deletion_at_middle(self, position):
        """
        Delete a node at a specified position in the linked list.
        
        :param position: The position of the node to delete.
        
        Time Complexity: O(n) - Must traverse to the specified position.
        Space Complexity: O(1) - Uses a constant amount of space.
        """
        if self.head is None:
            return
        if position == 0:
            self.deletion_at_beginning()
            return
        if position < 0 or position >= self.len_linked_list():
            print("Invalid position")
            return
        current = self.head
        for i in range(position - 1):
            current = current.next
        if current.next is not None:
            current.next = current.next.next
            
    # Traverse the single linked list

    def traverse(self):
        """
        Traverse the linked list and print each node's data.
        
        Time Complexity: O(n) - Must traverse the entire list.
        Space Complexity: O(1) - Uses a constant amount of space.
        """
        current = self.head
        while current:
            print(current.data, end = " ")
            current = current.next
        print()
    
    # Searching the value

    def search(self, target):
        """
        Search for a node with the specified data in the linked list.
        
        :param target: The data to search for.
        :return: The position of the node with the target data, or -1 if not found.
        
        Time Complexity: O(n) - Must traverse the entire list.
        Space Complexity: O(1) - Uses a constant amount of space.
        """
        current = self.head
        position = 0
        while current is not None:
            if current.data == target:
                return position
            current = current.next
            position += 1
        return -1  # Return -1 if the target is not found

# Node 
node1 = 1
node2 = 2
node3 = 3
node4 = 4
node5 = 5
node6 = 6
node7 = 7

# Single linked object
single_linked_list = SingleLinkedList()

# Insert at beginning
single_linked_list.insert_at_beginning(node3)
single_linked_list.insert_at_beginning(node2)
single_linked_list.insert_at_beginning(node1)

# Insert at end
single_linked_list.insert_at_end(node5)
single_linked_list.insert_at_end(node6)
single_linked_list.insert_at_end(node7)

# Insert at middle
single_linked_list.insert_at_middle(node4, 3)

# Deletion at beginning
single_linked_list.deletion_at_beginning()

# Deletion at beginning
single_linked_list.deletion_at_end()

# Deletion at middle
single_linked_list.traverse()
single_linked_list.deletion_at_middle(1)

# Traverse the single linked list
single_linked_list.traverse()

# Search
print(single_linked_list.search(node5))

