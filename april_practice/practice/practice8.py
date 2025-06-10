#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def addTwoNumbers(self, l1 , l2):
        l1, l2 = list(l1), list(l2)
        lst1 = []
        lst2 = []
        for i in range(len(l1)):
            lst1.append(l1[i])
        for i in range(len(l2)):
            lst2.append(l2[i])
        res = ''.join(map(str, lst1))
        res1 = ''.join(map(str, lst2))
        add = int(res)+ int(res1)
        result1 = []
        result = str(add)
        for i in result[::-1]:
            result1.append(int(i))
        print(result1)

        



    
        
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

list1 = ListNode([x for x in l1])

list1.addTwoNumbers(l1,l2)

