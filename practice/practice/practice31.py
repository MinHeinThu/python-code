def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        flag = True


if __name__ == '__main__':
    arr = [2, 4, 1, 0 , 7, 8, 2, 3]
    sorted = bubble_sort(arr)
    print(sorted)