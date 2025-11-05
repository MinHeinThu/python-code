# selection sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        print("i",i)
        min_index = i
        # print(i)
        for j in range(i+1,n):
            print("j", j)
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)      
    return arr
if __name__ == '__main__':
    arr = [7, 4, 2, 9]
    sorted_arr = selection_sort(arr)
    print(sorted_arr)
            