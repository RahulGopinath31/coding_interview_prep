# 1.	Kth smallest element [Amazon]
#   Given an array of n-elements and an integer k, find the kth smallest element present in an array.
#   For example:
#       arr = [40, 25, 68, 79, 52, 66, 89, 97]
#       k = 2
#       result = 40
import random

def partition(arr, left, right):
    pivot = arr[left]
    i = left - 1
    j = i+1
    while(j < right+1):
        if arr[j] <= pivot:

            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j = j + 1
    ## swap the pivot position element with i
    arr[i], arr[left] = arr[left], arr[i]
    return i   


def randomizedPartition(arr, p, q):
  if p == q:
      return partition(arr, p, q)
  
  randomPivotIndex = random.randrange(p, q)
 
  ## swap the random index with the first index 
  arr[p], arr[randomPivotIndex] = arr[randomPivotIndex], arr[p]
  return partition(arr, p, q)


def kth_small_elements(arr, k):
    if k > len(arr) or k <= 0:
        return
    
    k_small_ele_found = False
    p = 0
    q = len(arr) - 1

    while(not k_small_ele_found):
        index = randomizedPartition(arr, p, q)       

        if index == k - 1:
            return arr[index]
                   
        elif index > k-1:
            q = index - 1

        else:
            p = index + 1
    return 

        


##driver fucntion
arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
result = kth_small_elements(arr, k)
print(result)

