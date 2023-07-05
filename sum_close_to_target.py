

"""
problem statement :
Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to the target.[Amazon]

You need to return the sum of three integers.

For example:arr = [-1, 2, 1, -4], target = 1
Output: 2
Explanation: [-1+2+1] = 2 (The sum that is closest to the target is 2)

"""

"""
Solution : the time complexity is : O(n log n) (for sorting) + O(n log n) ()
"""
def merge(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[start + i]

 
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = start     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    

## mergesort function has time complexity of O(log n)
def mergesort (arr, start, end):

    if start > end:
        return 
    
    if start == end:
        return 

    mid = start + (end - start)//2
# mergesort function has time complexity of O(log n)
    mergesort(arr, start, mid)
    mergesort(arr, mid+1, end)
# merge function has time complexity O(n) and space complexity of O(n)
    merge(arr, start, mid, end)

# function to find the sum of three number that is close to the target value
def sum_close_to(arr, target):
    ## sort the array first
    mergesort (arr, 0, len(arr)-1)

    ## using two pointers to find sum of three numbers    
    left_ptr = 0
    right_ptr = len(arr)-1
    while(left_ptr < right_ptr): #0(n log n)        
        third_num = target - (arr[left_ptr] + arr[right_ptr]) # O(1)
        ## do a binay search to find thid number
        l = left_ptr # O(1)
        r = right_ptr # O(1)

        while(l < r): # O(log n)
            mid = l + (r - l)//2

            if arr[mid] == third_num:
                break
            elif arr[mid] < third_num:
                l = mid + 1
            else:
                r = mid - 1

        diff = arr[mid] - third_num

        if diff > -2 and diff < 2:
            return arr[left_ptr] + arr[mid] + arr[right_ptr]        
        elif diff <= -2:
            left_ptr += 1
        else:
            right_ptr -= 1

    return
        

# driver fucntion
#arr = [-1, 2, 1, -4]
arr = [-4, 2, 26, -3, -5, 7, 14, 1, 0, 1, -1]
target = 50

print(sum_close_to(arr, target))

## time complexity : O(n log n)
## space complexity : O(n)
