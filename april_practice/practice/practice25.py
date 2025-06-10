# Node
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class SingleNode:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = new_data
        new_node.next = self.head
        self.head = new_node
    
    def insertAtEnding(self, new_data):
        if self.head is None:
            self.head = new_data
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_data
        # else:
        #     lastNode = self.head
        #     while True:
        #         if lastNode.next is None:
        #             break
        #         lastNode = lastNode.next
        #     lastNode.next =  new_data

    def deleteFromBeginning(self):
        if self.head is None:
            print("The linked list is empty")  # Changed to print instead of return
            return
        self.head = self.head.next

    def deleteFromEnd(self):
        if self.head is None:
            print("The linked list is empty")  # Changed to print instead of return
            return
    # Fix the logic for single node case
        if self.head.next is None:  # Changed condition
            self.head = None
            return
    # Rest of the code for multiple nodes
        tem = self.head
        while tem.next.next:
            tem = tem.next
        tem.next = None

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Node
node0 = Node("Min")
node1 = Node("Hein")
node2 = Node("Hein")
node3 = Node("Thu")
node4 = Node("Loves")
node5 = Node("Saw")
node6 = Node("Yu")
node7 = Node("Mon")


single = SingleNode()

# insert at begin
single.insertAtBeginning(node0)
single.insertAtBeginning(node1)

# Insert at end
single.insertAtEnding(node2)
single.insertAtEnding(node3)
single.insertAtEnding(node4)
single.insertAtEnding(node5)
single.insertAtEnding(node6)
single.insertAtEnding(node7)
single.printList()

# Delete from begin
single.deleteFromBeginning()
single.printList()

# Delete from end
single.deleteFromEnd()
single.printList()