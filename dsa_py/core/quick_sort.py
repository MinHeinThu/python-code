import random

def quick_sort(arr):
    """In-place quicksort wrapper — returns the same list sorted."""
    n = len(arr)
    if n <= 1:
        return arr
    _quick_sort_inplace(arr)
    return arr

def _insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def _partition(arr, low, high):
    # Lomuto partition with a random pivot to avoid worst-case on sorted input
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def _quick_sort_inplace(arr):
    size = len(arr)
    stack = [(0, size - 1)]

    while stack:
        low, high = stack.pop()
        if low >= high:
            continue

        # Use insertion sort for small partitions (reduces overhead)
        if high - low + 1 <= 16:
            _insertion_sort(arr, low, high)
            continue

        p = _partition(arr, low, high)

        # Push larger partition first to keep stack depth small
        left_len = p - low
        right_len = high - p
        if left_len > right_len:
            if low < p - 1:
                stack.append((low, p - 1))
            if p + 1 < high:
                stack.append((p + 1, high))
        else:
            if p + 1 < high:
                stack.append((p + 1, high))
            if low < p - 1:
                stack.append((low, p - 1))

# Time complexity: average Θ(n log n), worst-case Θ(n^2)
# Space complexity (this implementation using slices/new lists):
#   average auxiliary O(n) (arrays) + O(log n) recursion stack
#   worst-case auxiliary O(n^2) with O(n) recursion depth
# To reduce space, implement in-place partitioning (Lomuto/Hoare).

if __name__ == "__main__":
    arr = [8, 3, 1, 9, 5, 7, 4, 6]
    print(quick_sort(arr))
