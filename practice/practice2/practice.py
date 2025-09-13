# Time complexity is O(n ^ 2)
# Space complecity is O(1)

# Note for selection sort 
# If you have the array 
# [64, 25, 12, 22, 11]
# First index 0 of array is assume minimum in the array and that part is sorted
# Second the from the index 1 we find the smallast value and then swap the assume minimun

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i # the is the first assume minimun value
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j # we update the if the j is smaller than the 'min' and find the smallest
            # After the we found the smallest value in the arr we swap the assume one to real smallest one
        arr[i], arr[min] = arr[min], arr[i]

if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    selection_sort(arr)
    print(arr)
