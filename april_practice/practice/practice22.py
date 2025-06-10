# Quick Sort
# Time: O(n log n)
# Space: O(n)

def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    pivot = arr[-1]

    low = [x for x in arr[:-1] if x <= pivot]
    high = [x for x in arr[:-1] if x > pivot]

    low = quick_sort(low)
    high = quick_sort(high)
 
    return low + [pivot] + high

if __name__ == "__main__":
    A = [-5, 3, 1, -4 , -1, 0, 5, 4]
    print(quick_sort(A))