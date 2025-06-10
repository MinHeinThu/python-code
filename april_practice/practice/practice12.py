# Create class node

class Node:
    # Node has two parts store the data and point the next node
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SingleLinkedList:

    def __init__(self):
        self.head = None

    def insertAtBiginning(self, new_node):
        tem = self.head
        self.head = new_node
        self.head.next = tem
        del tem

    def insertMiddle(self):
        pass

    def insertNode(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = new_node
    
    # Traverse the list node
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
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

# Insert at the biginning
single.insertAtBiginning(node0)

# Insert at the end 
single.insertNode(node1)
single.insertNode(node2)
single.insertNode(node3)
single.insertNode(node4)
single.insertNode(node5)
single.insertNode(node6)
single.insertNode(node7)

single.printList()

