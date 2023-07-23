# 5.	Find index of peak element [Facebook]
# The peak element is the element that is strictly greater than its neighbors. If an array contains multiple peak elements, return the index of any of the peak elements.
# For example: [1,2,3,1]
# Output: 2

# method for finding peak index
# time complexity = 0(n)
def findPeakIndexIterative(arr):
    p = 0
    q = len(arr)-1
    peak = float('-inf')
    peakIndex = -1
   
    while(p <= q):
        if p == 0:
            if arr[p] > arr[p + 1]:
                peak = arr[p]
                peakIndex = p                

        if p == q:
            if arr[p] > arr[p - 1]:
                if peak < arr[p]:
                    peak = arr[p]
                    peakIndex = p

            break               
                

        if arr[p] > arr[p - 1] and arr[p] > arr[p + 1]:
            if peak < arr[p]:
                peak = arr[p]
                peakIndex = p  

        p += 1    

    return peakIndex   


## time complexity : O(lg(n))
def findPeakIndexBinarySearch(arr):
    start = 0
    end = len(arr) - 1

    if arr[start] > arr[start + 1]:
        return start
    
    if arr[end] > arr[end - 1]:
        return end
    
    start += 1
    end -= 1

    while(start <= end):
        mid = start + (end - start)//2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid - 1] > arr[mid]:
            end = mid - 1

        elif arr[mid + 1] > arr[mid]:
            start = mid + 1
        
        else:
            start += 1

    return -1





## Driver code
arr = [1,8,9,10,15,15,24,10,6,5]
peak_index_interative = findPeakIndexIterative(arr)
print(peak_index_interative)
peak_index_bin_search = findPeakIndexBinarySearch(arr)
print(peak_index_bin_search)

