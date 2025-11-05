# Insertion Sort

def insertion_sort(arr):
    n = len(arr)
   
    for i in range(1, n):
        print("i", i)
        for j in range(i, 0, -1):
            print("j", j)
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
    return arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print(insertion_sort(arr))
   