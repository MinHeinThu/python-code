# import random
# from collections import deque

# name = deque(["Min", "Hein", "Thu"])
# print(type(name))

# for i in range(1-1):
#     print(i)
    

class SingleLinkeList:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

head = SingleLinkeList(1)
A = SingleLinkeList(2)
B = SingleLinkeList(3)
C = SingleLinkeList(4)
D = SingleLinkeList(5)

head.next = A
A.next = B
B.next = C
C.next = D

def print_list(node):
    current = node
    while current:
        print(current.data, end = "->")
        current = current.next
    print(None)
print_list(head)

list = []
current = head
while current:
    list.append(current.data)
    current = current.next
print(list)

current = head
for i in list:
    current.data = i + 1
    current = current.next
print_list(head)