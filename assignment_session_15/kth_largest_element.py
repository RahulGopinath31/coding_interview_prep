# 3.Kth Largest Element in an array [Facebook]
#   Given an integer array nums and an integer k, return the kth largest element present in an array.
#   For example:
#       arr = [40, 25, 68, 79, 52, 66, 89, 97]
#       k = 2
#       result = 89

def partition(arr, left, right):
    pivot = arr[left]
    i = left - 1
    j = i+1
    while(j < right+1):
        if arr[j] >= pivot:

            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j = j + 1
    ## swap the pivot position element with i
    arr[i], arr[left] = arr[left], arr[i]
    return i   


def k_largest_element(arr, k):
    if k > len(arr) or k <= 0:
        return
    
    k_small_ele_found = False
    p = 0
    q = len(arr) - 1

    while(not k_small_ele_found):
        index = partition(arr, p, q)       

        if index == k - 1:
            return arr[index]
                   
        elif index > k-1:
            q = index - 1

        else:
            p = index + 1
    return 
    

## driver code
arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
element = k_largest_element(arr, k)
print(element)

