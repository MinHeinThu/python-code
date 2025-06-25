class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, new_node):
        temporary_node = self.head
        self.head = new_node
        self.head.next = temporary_node
        del temporary_node

    def insertNode(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            lastest_node = self.head
            while True:
                if lastest_node.next is None:
                    break
                lastest_node = lastest_node.next
            lastest_node.next = new_node
    
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

# Object for Node
node0 = Node("!")
node1 = Node("Min")
node2 = Node("Hein")
node3 = Node("Thu")
node4 = Node("Loves")
node5 = Node("Saw")
node6 = Node("Yu")
node7 = Node("Mon")

# Object for Single linked list
single = SingleLinkedList()
single.insertNode(node1)
single.insertNode(node2)
single.insertNode(node3)
single.insertNode(node4)
single.insertNode(node5)
single.insertNode(node6)
single.insertNode(node7)

# Insert at the beginning
single.insertAtBeginning(node0)

single.printList()