# Time O (n log n) : Space (n)

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2

    left, right = arr[:mid], arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    l , r = 0, 0
    sorted_arr = [0] * n

    i = 0


    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            sorted_arr[i] = left[l]
            l += 1
        else:
            sorted_arr[i] = right[r]
            r += 1
        i += 1
    
    while l < len(left):
        sorted_arr[i] = left[l]
        l += 1
        i += 1

    while r < len(right):
        sorted_arr[i] = right[r]
        r += 1
        i += 1

    print(i)
    
    return sorted_arr

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82 , 10]
    print(merge_sort(arr))
