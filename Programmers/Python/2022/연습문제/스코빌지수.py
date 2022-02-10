import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    
    for s in scoville :
        heapq.heappush(heap, s)
    
    idx = 0
    while True :
        idx += 1
        new = heapq.heappop(heap)
        new2 = heapq.heappop(heap)
        
        val = new + (new2 * 2)
        heapq.heappush(heap, val)
        
        flag = True
        for h in heap :
            if h < K :
                flag = False
                break
        
        if flag :
            return idx
        
        if len(heap) == 1:
            break
        
    return -1