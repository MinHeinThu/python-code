# Counting sort 

# Time O(K + n)
# Space: O(K)

def counting_sort(arr):

    # first step find the max value in array
    k = max(arr)

    # count the element in arr
    counts = [0] * (k + 1)
    

    for c in arr:
        counts[c] += 1

    i = 0

    for j in range(k + 1):
        while counts[j] > 0:
            arr[i] = j
            i += 1
            counts[j] -= 1


if __name__ == "__main__":
    arr = [5, 3, 2, 1, 3, 3, 7, 1, 3]
    counting_sort(arr)
    print(arr)


# Object = states + behaviors
# states = variables = attributes
# behavious = methods = functions

class Node:

    #
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SingleLinkedList:
    
    def __init__(self):
        self.head = None


    # Methods
    def add_at_beginnig(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end= '->')
            current = current.next
        print(None)


single = SingleLinkedList()

single.add_at_beginnig(1)
single.add_at_beginnig(3)

single.add_at_end(3)
single.add_at_end(1)

single.traverse()
    


