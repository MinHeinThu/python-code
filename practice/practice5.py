def merage_sort(arr):

    n = len(arr)

    if n == 1:
        return arr # For base case
    
    m = n // 2
    left = arr[:m]
    right = arr[m:]

    left = merage_sort(left)
    right = merage_sort(right)
    l , r = 0, 0

    sorted_arr = [0] * n
    i = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_arr[i] = left[l]
            l += 1
        else:
            sorted_arr[i] = right[r]
            r += 1
        i += 1
        print(sorted_arr)
    while l < len(left):
        if l < len(left):
            sorted_arr[i] = left[l]
            l += 1
            i += 1
        print(sorted_arr)
    while r < len(right):
        if r < len(right):
            sorted_arr[i] = right[r]
            r += 1
            i += 1
        print(sorted_arr)
    return sorted_arr
if __name__ == "__main__":
    A = [1, -4, -3, 0, 2, 3]
    print(f"Merge sort: {merage_sort(A)}") 
    
        