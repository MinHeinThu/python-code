# Double linked list

class Node:
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def lenght_list(self):
        current_node = self.head
        length = 0
        while current.next is not None:
            current = current.next
            length += 1
        return length


    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.previous = current
        self.tail = new_node

    def insert_at_position(self, new_data, position):
        new_node = Node(new_data)

        if position == 0:
            self.insert_at_beginning(new_data)
        
        if position < 0 or position >= self.length_list():
            print("The position is invalid")
            return
        

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end= " <-> ")
            current = current.next
        print(None)


double = DoubleLinkedList()

double.insert_at_beginning("Thu")
double.insert_at_beginning("Hein")
double.insert_at_beginning("Min")

double.insert_at_end("Saw")
double.insert_at_end("Yu")
double.insert_at_end("Mon")

double.traverse()

