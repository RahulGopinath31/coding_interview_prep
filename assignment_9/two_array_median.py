# Median of Two Sorted Arrays (Apple)
# 2. Given two sorted arrays num1 and num2 of size m and n respectively, return the median
#    of the two sorted arrays.

# method to find the median of sorted array
def findMedian(arr1, arr2):
    i = 0
    j = 0
    finalArr = [0]*(len(arr1) + len(arr2))
    k = 0
    while(i < len(arr1) and j < len(arr2)):
        if arr1[i] <= arr2[j]:
            finalArr[k] = arr1[i]
            i += 1            

        else:
            finalArr[k] = arr2[j ]
            j += 1

        k += 1

    while(i < len(arr1)):
        finalArr[k] = arr1[i]
        i += 1
        k += 1

    while(j < len(arr2)):
        finalArr[k] = arr2[j]
        j += 1
        k += 1

    ## check if the size of sorted array is odd or even
    totalSize = len(arr1)+ len(arr2)
    if totalSize % 2 == 0: # even number of elements
        ## the mean of middle two elements.
        mid1 = (totalSize - 1)// 2
        mid2 = mid1 + 1
        return ((finalArr[mid1] + finalArr[mid2]) / 2)
    else:
        return finalArr[int((totalSize - 1)/2)]

    


# Driver code:
arr1 = [1,5,7,11]
arr2 = [2,3,6,8,12]
median = findMedian(arr1, arr2)
print(median)