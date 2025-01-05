# Quick sort
# Time O(n log n)
# Space O(log n)
def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr# for base case

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right

if __name__ == "__main__":
    A = [-5, 3, 1, -4 , -1, 0, 5, 4]
    print(quick_sort(A))


