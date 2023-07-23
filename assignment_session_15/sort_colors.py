# 2.	Sort Colors [Amazon]
# Given array nums with n objects colored red, white, or blue, sort them in place so that the objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Solve this question without using the library sort function.
# For example:
#   Nums = [2,0,2,1,1,0]
#   Result = [0,0,1,1,2,2]

def partition(arr, p, q):
  pivot = arr[p]
  i = p
  for j in range(i+1, q+1):
    if arr[j] <= pivot:
      i += 1
      ## swap between the values of arr[i] and arr[j]
      arr[i], arr[j] = arr[j], arr[i]
  ## final swap between the value of arr[i] and arr[p]
  arr[i], arr[p] = arr[p], arr[i]
  return i

## Method definition of quickSort
def sortColors(arr, p, q):
  if p < q:
    ## Divide and Conquer Approach
    ## 1. Divide
    ## function calling for the partition method
    partitionIndex = partition(arr, p, q)
    ## recursive function call for the left subtree
    sortColors(arr, p, partitionIndex-1)
    ## recursive function call for the right subtree
    sortColors(arr, partitionIndex+1, q)
  return arr


#driver code
Nums = [2,0,2,1,1,0,0,2,2,0,1]
Result = sortColors(Nums, 0, len(Nums)-1)
print(Result)

