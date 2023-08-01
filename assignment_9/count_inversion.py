# count the number of inversion. 
# An inversion occurs when : arr[i] > arr[j] for j > i
# Method

def mergeInversion(arr, left, mid, right):
    ## assign two pointers for comparison 
    i = left
    j = mid + 1
    k = 0
    tempArr = [0]*(right - left + 1)
    no_of_inversions = 0

    while(i < mid + 1 and j < right + 1):
        if arr[i] <= arr[j]:
            tempArr[k] = arr[i]
            i += 1
            k += 1

        else:
            ## inversion occurs since the condition 
            # 1. i < j
            # 2. arr[i] > arr[j]
            # are met
            # logic : all the numbers between i and mid are sorted and hence all those elements are greater than
            #         arr[j] => the total number of inversion for that value in j's position is arr mid - i + 1.         
            tempArr[k] = arr[j]
            j += 1
            k += 1
            no_of_inversions += (mid - i + 1)

    while(i < mid + 1):
        tempArr[k] = arr[i]
        i += 1
        k += 1

    while(j < right + 1):
        tempArr[k] = arr[j]
        j += 1
        k += 1

    for t in range(len(tempArr)):
        arr[left + t] = tempArr[t]

    return no_of_inversions

def countInversion(arr, left, right):
    inv_number = 0
    if left == right:
        return inv_number
    
    mid = left + (right - left)//2
    left_inv = countInversion(arr, left, mid)
    right_inv = countInversion(arr, mid + 1, right)
    merger_inv = mergeInversion(arr, left, mid, right)

    inv_number = left_inv + right_inv + merger_inv

    return inv_number


## Driver code
arr = [70, 50, 60, 10, 20, 30, 80, 15]
print(countInversion(arr, 0, len(arr)-1))