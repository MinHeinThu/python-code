# Array in programming logic

class Array:
    def __init__(self):
        self._array = [] # Dynamic array, O(1) to create

    # Append at end -> O(1)
    def add_to_array(self, value):
        self._array.append(value)

    # Insert at index -> O(n)
    def insert_at(self, index, value):
        self._array.insert(index, value)
    
    # Delete at index -> O(n)
    def delete_at(self, index):
        if len(self._array) > index and index >= 0:
            self._array.pop(index)
        else:
            print('Index out of range')

    # Delete from end -> O(1)
    def delete(self):
        if self._array:
            self._array.pop()
        else:
            return -1
    
    # Search the element in the array -> O(n)
    def search(self, value):
        for i, val in enumerate(self._array):
            if val == 'value':
                return i
        return -1

    def show_array(self):
        print(self._array)

arr = Array()
arr.insert_at(0,1)
arr.show_array()
arr.add_to_array(22)
arr.show_array()
print(arr.search(2))

# Two sum array : leet code
# Hash Map

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            print([seen[complement], i])
            # return [seen[complement], i]  
        seen[num] = i
    print((seen))
    
twoSum([2,7,11,15], 9)
