# class LeeClass:
#     pass

# class LooMeNes:

#     # constructur
#     def __init__(name, firstName, lastName = None):
#         name.firstName = firstName
#         name.lastName = lastName

# person1 = LooMeNes()
# print(person1.firstName)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginnig(self, data):
        current = self.head

        new_node = Node(data)

        new_node.next = current

        self.head = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data ,end = " -> ")

            current = current.next
        print(None)

singel = SingleLinkedList()
singel.insert_at_beginnig(1)
singel.insert_at_beginnig(2)

singel.traverse()


