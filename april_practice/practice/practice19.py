# Merge Sort
# Time : O(n log n)
# Space : O(n)

def merge_sort(arr):
    """
    Perform a merge sort on a list of numbers.
    Merge sort is a divide-and-conquer algorithm that splits the input list into two halves,
    recursively sorts each half, and then merges the sorted halves to produce the final sorted list.
    Args:
        arr (list): The list of numbers to be sorted.
    Returns:
        list: A new list containing the sorted numbers.
    Example:
        >>> merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    Steps:
        1. If the list has only one element, return it (base case).
        2. Split the list into two halves.
        3. Recursively sort each half.
        4. Merge the two sorted halves into a single sorted list.
    """
    # Your code here
    n = len(arr)

    if n == 1:
        return arr # for base case if the length of arr is one

    m = n // 2
    left = arr[:m]
    right = arr[m:]
    print(left,right)

    left = merge_sort(left)
    right = merge_sort(right)
    print(left,right)
    l, r = 0, 0
    sorted = [0] * n
    i = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted[i] = left[l]
            l += 1
        else:
            sorted[i] = right[r]
            r += 1
        i += 1
        print(1,i)
    
    while l < len(left):
        sorted[i] = left[l]
        l += 1
        i += 1
        print(2,i)
    
    while r < len(right):
        sorted[i] = right[r]
        r += 1
        i += 1
        print(3,i)

    return sorted

if __name__ == "__main__":
    A = [4, 10, 3, 5, 1]
    print(merge_sort(A))     