# Node
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# Single linked list
class SingleNode:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, new_data):
        current_node = self.head
        self.head = new_data
        self.head.next = current_node
    
    def length_node(self):
        current_node = self.head
        length = 0
        while current_node:
            current_node = current_node.next
            length += 1
        return length

    def insert_at_end(self, new_data):
        if self.head is None:
            self.head = new_data
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_data
    
    def insert_at_middle(self, new_node, position):
        if position == 0:
            self.insert_at_beginning(new_node)
            return
        if position < 0 or position > self.length_node():
            print("The position is invalid")
            return
        current_node = self.head
        current_position = 0
        while True:
            if current_position == position:
                previous_node.next = new_node
                new_node.next = current_node
                break
            previous_node = current_node
            current_node = current_node.next
            current_position += 1
        
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        # if the node is end
        print()

# Object of node
node0 = Node("Min")
node1 = Node("Hein")
node3 = Node("Thu")
node4 = Node("Loves")
node5 = Node("Saw")
node6 = Node("Yu")
node7 = Node("Mon")
node8 = Node("Mon")
node9 = Node("Min")


# Object of single linked list
single = SingleNode()

# Insert from end
single.insert_at_end(node3)
single.insert_at_end(node4)
single.insert_at_end(node5)
single.insert_at_end(node6)
single.insert_at_end(node7)

# Insert from beginning
single.insert_at_beginning(node1)
single.insert_at_beginning(node0)

# Insert at middle
single.insert_at_middle(node8, 6)
single.insert_at_middle(node9, 0)



single.printList()