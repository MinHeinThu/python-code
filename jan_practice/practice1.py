class Node:

    def __init__(self, data, next = None):

        self.data = data
        self.next = next


class SingleNode:

    def __init__(self):
        self.head = None

    # Calculate the length of the node

    def node_length(self):
        
        # Current is self.head lenght is zero 
        current = self.head
        length = 0
        # Loop the node and the if the node is exist add one to the length
        while current:
            current = current.next
            length += 1
        return length
    

    # Insert at beginnig T: O(1), S: O(1)
    
    def insert_at_beginning(self, data):

        new_node = Node(data)
        # Current head is self.head so new_node.next is self.head
        new_node.next = self.head
        # Assign the new_node to new self.head
        self.head = new_node

    # Insert at end T: O(n), S: O(1)
    
    def insert_at_end(self, data):
        new_node = Node(data)

        # if self.head is None new_node is will be insert at self.head
        if self.head is None:
            self.head = new_node
            return
        
        # if self.head is not None go the the last node and last node of next is new_node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Insert at the postition T: O(n), S: O(1)

    def insert_at_position(self, data, position):

        # if the position is zero that look like insert the beginning so call the function insert at beginning
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        # if the position is less than zero or grather than the length th position is invalid
        elif position < 0 or position > self.node_length():
            print("Invalid position")
            return
        # if the positon is equal to the lenth of node is the same with insert at the end
        elif position == self.node_length():
            self.insert_at_end(data)
            return
        
        else:
            current_position = 0

            current_node = self.head
            
            # if the current position is less than the position and current node is not none
            # we increase the current position until the position we want to insert

            while current_position < position and current_node is not None:
                # Assign the variable before the position we want to insert 
                
                previous_node = current_node
    
                current_node = current_node.next
                
                current_position += 1

            new_node = Node(data)

            previous_node.next = new_node
            new_node.next = current_node


    # Delete the node from the beginning T : O(1), S: O(1)

    def delete_at_beginning(self):
        # Override the self.head 
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is Node:
            print("Node has no data")
            return
        
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        # while current_node.next:
        #     prev = current_node
        #     current_node = current_node.next
        # prev.next = None

        for i in range(self.node_length()-2):
            
            # if current_node.next.next is None: for - 1
            #     break
            current_node = current_node.next
            # print(current_node.data)
        
        current_node.next = None
    
    def delete_at_position(self, position):

        if position >= self.node_length() or position < 0:
            print("Invalid")
            return
        
        if position == 0:
            self.delete_at_beginning()
            return
        
        if position == self.node_length()-1:
            self.delete_at_end()
            return
        
        
        current_node = self.head

        for i in range(position-1):
            current_node = current_node.next

        if current_node.next is not None:
            current_node.next = current_node.next.next

        


      
    # Traverse T: O(n), S: O(1)
    def traverse(self):
        list1 = []
        current_node = self.head
        while current_node:
            print(current_node.data, end = '->')
            list1.append(current_node.data)
            current_node = current_node.next
        print(None)
        print(list1)
    
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

single = SingleNode()

single.insert_at_beginning(1)
single.insert_at_beginning(2)
single.insert_at_beginning(3)

single.insert_at_end(4)
single.insert_at_end(5)

single.insert_at_position(6,2)
single.insert_at_position(1,0)
single.insert_at_position(7,7)

print("Traverse the node", end=" ")
single.traverse()

print(f"Length of node : {single.node_length()}")

single.delete_at_beginning()

print("Traverse the node", end=" ")
single.traverse()

print(f"Length of node : {single.node_length()}")

single.delete_at_beginning()


print("Traverse the node", end=" ")
single.traverse()

print(f"Length of node : {single.node_length()}")

single.delete_at_end()

print("Traverse the node", end=" ")
single.traverse()

print(f"Length of node : {single.node_length()}")

single.delete_at_position(0)

print("Traverse the node", end=" ")
single.traverse()

print(f"Length of node : {single.node_length()}")

single.delete_at_position(3)

print("Traverse the node", end=" ")
single.traverse()

print(f"Length of node : {single.node_length()}")

print(single.search(3))