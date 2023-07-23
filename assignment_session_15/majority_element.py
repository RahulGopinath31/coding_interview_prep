# 4.	Majority Element [Amazon, Google]
# Given array nums of size n, return the majority element present in the array.
# Assume that the majority element always exists in an array.
# For example:
#   Nums = [2, 2, 1, 1, 1, 2, ,2]
#   Output: 2

# partition procedure for quicksort algorithm 
def partition(arr, p, q):
    pivot = arr[p]
    i = p - 1
    j = i + 1
    while(j < q + 1):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
        j += 1

    arr[p], arr[i] = arr[i], arr[p]
    return i

##quicksort procedure to sort the elements
def quickSort(arr, p, q):
    if p < q:
        partitionIndex = partition(arr, p, q)
        quickSort(arr, p, partitionIndex - 1)
        quickSort(arr, partitionIndex+1, q)

    return arr

def majorElement(arr):
    # sort the array 
    arr = quickSort(arr, 0, len(arr)-1)
    print(arr)
    i = 0
    maxCount = -1
    maxIndex = -1
    for j in range(i, len(arr)):
        if arr[j] != arr[i]:
            if maxCount < j - i:
                maxCount = j - i 
                maxIndex = i            
            i = j
   
    if arr[j] == arr[i]:
        if maxCount < len(arr) - i:
                maxCount = len(arr) - i 
                maxIndex = i

    return arr[maxIndex]


#driver code
Nums = [1,1,2,2,2]
print(majorElement(Nums))