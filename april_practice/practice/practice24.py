class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SingleNode:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_node):
        tem = self.head
        self.head = new_node
        self.head.next = tem
        del tem
    
    def lengthNode(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertAtMiddle(self, new_node, position):
        if position < 0 or position > self.lengthNode():
            print("Invalid position")
            return
        if position == 0:
            self.insertAtBeginning(new_node)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = new_node
                new_node.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1


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
        
    def printList(self):
        curr  = self.head
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
node8 = Node("!")
node5 = Node("Saw")
node6 = Node("Yu")
node7 = Node("Mon")

# Object for Single linked list
single = SingleNode()
single.insertNode(node1)
single.insertNode(node2)
single.insertNode(node3)
single.insertNode(node4)
single.insertNode(node5)
single.insertNode(node6)
single.insertNode(node7)
# Insert at the beginning
single.insertAtBeginning(node0)
single.insertAtMiddle(node8, 5)

single.printList()
