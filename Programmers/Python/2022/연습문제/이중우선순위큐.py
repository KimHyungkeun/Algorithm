import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    
    for o in operations :
        cmd = o.split()
        
        if cmd[0] == "I" :
            num = int(cmd[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))
        
        else :
            if not min_heap or not max_heap:
                continue
            
            if cmd[1] == "1" :
                max_val = heapq.heappop(max_heap)[1]
                min_heap.remove(max_val)
                
            elif cmd[1] == "-1":
                min_val = heapq.heappop(min_heap)
                max_heap.remove((-min_val, min_val))
        
    if min_heap or max_heap:
        answer = [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    else :
        answer = [0,0]
            
            
    return answer

# 220206 풀이
import heapq
def solution(operations):
    heap = []
    max_heap = []
    
    for o in operations :
        cmd = o.split()
        num = int(cmd[1])
        if cmd[0] == "I" :
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (-num, num))
        
        else :
            if not heap :
                continue
            
            if num == -1 :
                min_val = heapq.heappop(heap)
                max_heap.remove((-min_val,min_val))
                
            else :
                max_val = heapq.heappop(max_heap)[1]
                heap.remove(max_val)
                
        
    if not heap :
        return [0,0]
    else :
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]