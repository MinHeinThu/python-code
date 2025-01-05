# Merge Sort
# Time: O(n log n)
# Space: O(n)
# 
def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr # for base case
    m = n // 2
    low = arr[:m]
    high = arr[m:]

    low = merge_sort(low)
    high = merge_sort(high)

    len_low = len(low)
    len_high = len(high)

    l, h = 0, 0
 
    sorted = [0] * n
    i = 0

    while l < len_low and h < len_high:
        if arr[l] < arr[h]:
            sorted[i] = low[l]  
            l += 1
        else:
            sorted[i] = high[h]
            h += 1
        i += 1

    while l < len_low:
        sorted[i] = low[l]
        l += 1
        i += 1
    
    while h < len_high:
        sorted[i] = high[h]
        h += 1
        i += 1
    
    return sorted


if __name__ == "__main__":
    A = [-5, 3, 1, -4 , -1, 0, 5, 4]
    print(merge_sort(A))