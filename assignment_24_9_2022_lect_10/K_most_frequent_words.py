## problem statement : Given an array of strings words and an integer k, return the k most frequent words.
## Your output should be in lexicographical order.
##Words = [‘priya’, ‘bhatia’, ‘akshay’, ‘arpit’, ‘priya’, ‘arpit’]
##K = 3
##Output = [‘arpit’, ‘akshay’, ‘priya’]

def heapify(heap_ds, i, map, n):
    big = i
    l_idx = 2*i + 1
    r_idx = 2*i + 2
        
    if l_idx < n and map[heap_ds[l_idx]] > map[heap_ds[big]]:
        big = l_idx
    
    if r_idx < n and map[heap_ds[r_idx]] > map[heap_ds[big]]:
        big = r_idx

    ## big might be left or right, 
    if big != i :
        ## the largest freq would be either at left or right index
        
        if big == l_idx and big != n-1 and map[heap_ds[big]] == map[heap_ds[r_idx]]:
            if heap_ds[big] > heap_ds[r_idx]:
                big = r_idx

        heap_ds[big], heap_ds[i] = heap_ds[i], heap_ds[big]
        heapify(heap_ds, big, map, n)

    
        

def heap_build(map):
    ## heap ds using an array
    heap_ds = []
    for key in map:
        heap_ds.append(key)

    ## heapify the heap_ds w.r.t
    ## 1. the frequency
    ## 2. if same frequency -> based on lexicography
    start_idx = len(heap_ds)//2 - 1
    for i in range(start_idx, -1, -1):
        heapify(heap_ds, i, map, len(heap_ds))

    return heap_ds


def k_freq_words(arr, K):
    ## create a dictionary/hashmap with "key" as the elements in array and "value" as the frequency of occurance
    ## of the element

    map = dict()

    for ele in arr:
        if ele in map:
            map[ele] += 1
        else:
            map[ele] = 1
    
    for key, value in map.items():
        print('{} : {}'.format(key, value))

    
    freq_word_list = heap_build(map)
    print(freq_word_list)
    k_freq_list = []
    i = 0
    while K > 0 and K < len(freq_word_list):
        k_freq_list.append(freq_word_list[i])
        i = i + 1
        K = K - 1

    k_freq_list.sort()

    return k_freq_list


## driver code
#Words = ['priya', 'bhatia', 'akshay', 'arpit', 'priya', 'arpit']
# K = 3
Words = ['priya', 'bhatia', 'akshay', 'arpit', 'priya', 'arpit']
#Words = ['car','care', 'kid', 'alpha', 'car', 'kid', 'bell', 'bell', 'bottom',  'ace', 'ace', 'alpha', 'ace']
#Words = ["tell"]
print(len(Words))
K = 3
print(k_freq_words(Words, K))