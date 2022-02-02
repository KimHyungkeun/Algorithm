import sys
import heapq

t = int(sys.stdin.readline())

for _ in range(t) :
    k = int(sys.stdin.readline())
    heap = []
    max_heap = []
    for test in range(k) :
        cmd = sys.stdin.readline().split()
        num = int(cmd[1])
        if cmd[0] == "I" :
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (-num, num))
        
        else :
            if not heap :
                continue

            if cmd[1] == "1" :
                max_val = heapq.heappop(max_heap)[1]
                heap.remove(max_val)
            
            elif cmd[1] == "-1" :
                min_val = heapq.heappop(heap)
                max_heap.remove((-min_val, min_val))
    
    if not heap :
        print("EMPTY")
    else :
        print(heapq.heappop(max_heap)[1], heapq.heappop(heap))

            