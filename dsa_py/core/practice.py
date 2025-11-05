class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None
    
    def appending(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def tranverse(self):
        curr = self.head
        while curr:
            print(curr.val, end = '->')
            curr = curr.next
        print(None)
    
head = SingleLinkedList()
head.appending(5)
head.appending(4)
head.appending(3)
head.appending(2)
head.appending(1)
# head.tranverse()

class Solution:
    def reverse(self, head):
        result = []
        index = 0
        curr_node = head.head
        while curr_node is not None: # Time O(n) Traverse all the node
            result.append(curr_node.val)
            index += 1
            curr_node = curr_node.next
        # print(index)
        # print(result)
        
        # result2 = []
        # for i in range(index-1, -1, -1): # start stop step
        #     result2.append(result[i])
        # print(result2)

        # # result2 = result [::-1]
        # # print(result2)

        reverse_node = SingleLinkedList()
        for i in range(index):
            reverse_node.appending(result[i])
        reverse_node.tranverse()
        
s1 = Solution()
s1.reverse(head)
# s1.tranverse()