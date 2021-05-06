array = [5,7,9,0,3,1,6,2,4,8]

# 힙 소트
def heapify(arr, idx, n) :
    left = idx * 2
    right = idx * 2 + 1
    s_idx = idx
    

    if (left <= n and arr[s_idx] < arr[left]) :
        s_idx = left
    if (right <= n and arr[s_idx] < arr[right]) :
        s_idx = right
    print(arr,"left:",left,"right:",right,"s_idx:",s_idx)
    if s_idx != idx :
        arr[idx], arr[s_idx] = arr[s_idx], arr[idx]
        # print(arr,"left:",left,"right:",right,"idx:",idx,"s_idx:",s_idx)
        return heapify(arr, s_idx, n)

def heap_sort(arr) :
    n = len(arr)
    arr = [0] + arr

    # min heap 생성
    for i in range(n,0,-1) :
        heapify(arr, i ,n)
    
    print(arr)
    # min element extract & heap
    for i in range(n, 0, -1) :
        # print(arr[1])
        arr[i], arr[1] = arr[1], arr[i]
        heapify(arr, 1, i-1)
        # print(arr)
    
    return arr[1:]

array = heap_sort(array)