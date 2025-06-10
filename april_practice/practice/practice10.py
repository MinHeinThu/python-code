# Node class
# Ever node has two parts one is store data and another node is point to the next node

class Node:
    # Class instance
    def __init__(self, data, next = None):
        self.data =  data
        self.next = next


# Single Linked List
class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print ()


# Object for Node
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

single.printList()