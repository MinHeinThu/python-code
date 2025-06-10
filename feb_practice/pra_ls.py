# Linked list implementation by pyhthon

# Single linked list


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SingleLinkedList:

    def __init__(self, head=None):
        self.head = None

    def length_node(self):
        current = self.head
        length = 0

        while current.next is not None:
            length += 1
            current = current.next

        return length
    
    # Time : O(1), Space : O(1)
    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # Time : O(n), Space : O(1)
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Time : O(n), Space : O(1)
    def insert_at_position(self, data, position):

        new_node = Node(data)
        if position < 0 or position > self.length_node():
            print("Invalid position")
            return

        if position == 0:
            self.insert_at_beginning(data)
            return

        current_node = self.head
        current_position = 0

        while current_position < position and current_node is not None:
            previous_node = current_node
            current_node = current_node.next
            current_position += 1

        previous_node.next = new_node
        new_node.next = current_node

    def delete_head(self):

        if self.head is None:
            print("Linked list is empty") 
            return

        self.head = self.head.next

    def delete_end(self):

        if self.head is None:
            print("Linked list is empty") 
            return
        
        if self.head.next is None:
            self.head = None
            return

    
        last_node = self.head

        while last_node.next.next:
            last_node  = last_node.next
        last_node.next = None


        
        

    # Traverse Time : O(n)
    def travere_list(self):
        current = self.head

        while current:
            print(current.data, end = " -> ")
            current = current.next
        print()

single_node = SingleLinkedList()

single_node.insert_at_beginning('Thu')
single_node.insert_at_beginning('Hein')
single_node.insert_at_beginning('Min')

single_node.insert_at_end('Yu')
single_node.insert_at_end('Mon')

single_node.insert_at_position('Loves', 3)
single_node.insert_at_position('Saw', 4)



single_node.delete_head()
single_node.delete_end()

single_node.travere_list()