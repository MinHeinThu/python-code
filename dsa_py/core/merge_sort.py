def mergeSort(arr):
    n = len(arr)
    if n == 1: # base case if len arr is one element is already sorted
        return arr
    mid = n // 2
    L = arr[:mid]
    R = arr[mid:]

    # devide 
    L = mergeSort(L)
    R = mergeSort(R)

    l, r = 0, 0

    l_len = len(L)
    r_len = len(R)

    sorted_arr = [0] * n
    i = 0

    while l < l_len and r < r_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1

    while l < l_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    while r < r_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1
    
    return sorted_arr

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82 , 10]
    print(mergeSort(arr))



#  This part is devide 
# first step 
  # [38, 27, 43]  [3, 9, 82, 10]

# Second step
    # [38] [27, 43]  [3, 9] [82, 10]

# Third Step
    # [38]
            # [27] [43] [3] [9] [82] [10]
            # compare  and merge [25, 43] "1 compare"
            # [3, 9]
            # [10 , 82]

            # Total = 3
# Third step
    #[38] [27, 43] [3, 9] [10, 82]
    
    # [27, 38, 43] [3, 9, 10, 82]
    # [3, 9, 10, 27, 38, 43, 82]

# arr2 = [50, 20, 40, 10, 30, 60, 5, 25]
# # step 1
# [50, 20, 40, 10] [30, 60, 5, 25]
# # step 2
# [50, 20] [40, 10] [30, 60] [5, 25]
# # step 3
# [50] [20] [40] [10] [30] [60] [5] [25]
# # step 4
# [20, 50] [10, 40] [30, 60] [5, 25]
# # step 5
# [10, 20, 40, 50] [5, 25, 30, 60]
# # step 6
# [5, 10, 20, 25, 30, 40, 50 , 60]
