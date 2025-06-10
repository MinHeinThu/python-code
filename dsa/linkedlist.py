# Single Linked list
class SingleLinkedList:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    # Methods to print the list
    def print_list(self):
        node = self
        while node:
            print(node.val,end=" ")
            node = node.next  
        print(None)
        
node1 = SingleLinkedList(1)
node2 = SingleLinkedList(2)
node3 = SingleLinkedList(3)
node4 = SingleLinkedList(4)
node5 = SingleLinkedList(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node1.print_list()

# Double linked list

class DoubleLinkedList:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

head = tail = DoubleLinkedList(1)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(elements)
display(head)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinked:
    def __init__(self):
        self.head = None # Initialize head as a none
    
    #method
    def inssertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    lst = SingleLinked()

    lst.insertAtEnd("Min")
    lst.insertAtEnd("Hein")
    lst.insertAtEnd("Thu")
    lst.insertAtEnd("Loves")
    lst.insertAtEnd("Saw")
    lst.insertAtEnd("Yu")
    lst.insertAtEnd("Mon")
    
    lst.printList()