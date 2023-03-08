## a simple heap data structure.
def heapify(arr, n, i):
    small = i
    l_index = 2*i + 1
    r_index = 2*i + 2

    if l_index < n  and arr[l_index] < arr[small]:
        small = l_index

    if r_index < n  and arr[r_index] < arr[small]:
        small = r_index


    if (small != i):
        arr[small], arr[i] = arr[i], arr[small]
        heapify(arr, n, small)
        
    



def build_heap(arr, n):
    start_idx = n//2 - 1

    for i in range(start_idx, -1, -1):
        heapify(arr, n, i)
        

    return

    
# driver code:
# arr = [1, 3, 7, 9, 12, 10, 8, 16, 18, 22, 27]
#arr = [10, 5, 3, 7, 8, 12, 6, 2]
arr = [21, 22, 19,18,14,12,28,23,16,11, 20, 10, 2]
print("before heap_sort : ",arr)
build_heap(arr, len(arr))
print("after heap sort : ", arr)

