# counting sort 
# Time: O(k + n)
# Space: O(k)

def counting_sort(arr):
    
    k = max(arr)

    # This is list that only contain 0s
    count = [0] * (k + 1)

    # The array element is change to count of element by index increacing
    for i in arr:
        count[i] += 1

    i = 0
    # 
    for c in range(k + 1):
        # 
        while count[c] > 0:
            arr[i] = c
            i += 1
            count[c] -= 1

if __name__ == "__main__":
    arr = [5, 3, 2, 1, 3, 3, 7, 1, 3]
    counting_sort(arr)
    print(arr)
    

