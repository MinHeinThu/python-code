class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    # With tail pointer time : O(1)
    def append(self, data): 
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    # We don't need to update the tail 
    # We only need to update the head

    def prepend(self, data): # Insert at head time : O(1)
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    # def insert_at_head(self, Node):
    #     new_node = Node
    #     new_node.next = self.head
    #     self.head = new_node
    
    # Without tailpointer time : O(n)
    # def insert_at_tail(self, Node):
    #     new_node = Node
    #     if self.head is None:
    #         self.head = new_node
    #         return
    #     else:
    #         last_node = self.head
    #         while last_node.next:
    #             last_node = last_node.next
    #         last_node.next = new_node


    def traverse_list(self):
        if self.head is None:
            print('Empty linked list')
        else:
            curr = self.head
            while curr:
                print(curr.data, end = '->')
                curr = curr.next
            print('None')           
a = SingleLinkedList()
a.append(1)
a.append(2)
a.append(3)
a.traverse_list()
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
# f = Node(6)

# s = SingleLinkedList()
# s.insert_at_head(a)
# s.insert_at_head(b)
# s.insert_at_head(c)
# s.insert_at_head(d)
# s.insert_at_tail(e)
# s.insert_at_tail(f)
# s.traverse_list()
