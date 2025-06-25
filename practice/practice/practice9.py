class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

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
            print(current.val,end= "->")
            current = current.next
        print (None)

# Object
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

single = SingleLinkedList()
single.insertNode(node1)
single.insertNode(node2)
single.insertNode(node3)
single.insertNode(node4)

single.printList()




