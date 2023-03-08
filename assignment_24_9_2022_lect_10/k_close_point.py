# 3.Find the k closest points to the origin.
# Points = [[1, 3], [-2, 2]]
# K = 1
# Output = [-2,2]

#function:
def heapify(arr, i):
    small = i
    l_idx = 2*i + 1
    r_idx = 2*i + 2
    n = len(arr)
    small_distance = arr[i][0]**2 + arr[i][1]**2
    
    if l_idx < n and ((arr[l_idx][0]**2 + arr[l_idx][1]**2) < small_distance):
        small = l_idx
        small_distance = arr[l_idx][0]**2 + arr[l_idx][1]**2

    if r_idx < n and ((arr[r_idx][0]**2 + arr[r_idx][1]**2) < small_distance):
        small = r_idx
        

    if small != i:
        arr[i], arr[small] = arr[small], arr[i]

    

def heap_adjust(arr):
    n = len(arr)
    arr[0] = arr[n-1]
    del(arr[n-1])
    


def select_small(arr):
    start_idx = len(arr)//2 - 1
    
    for i in range(start_idx, -1, -1):
        heapify(arr, i)

    return arr[0]


def K_points(arr, K):
    ## form heap with closest point to origin at 0th position
    k_points = []
    for i in range(K):
        small = select_small(arr) 
        k_points.append(small)
        heap_adjust(arr)

    return k_points

def run_test_cases():
    pass

#driver code:
##Points = [[2,3], [-1, 1], [2, -1], [-2, -2], [-3, 1]]
Points = [[1, 3], [2, -2]]
K = 1
print(K_points(Points, K))
