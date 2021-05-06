import heapq

def solution(jobs):
    answer = []
    # 비어있는 배열
    heap = []
    
    for j in jobs :
        heapq.heappush(heap, [j[1], j[0]])
        
    while heap :
        answer.append(heapq.heappop(heap))
        
    print(answer)
    elapse_time = answer[0][0]
    delay = 0
    for i in range(len(jobs)-1) :
        delay += answer[i][0]
        elapse_time +=  answer[i+1][0] + delay - answer[i+1][1]
    
    elapse_time //= len(jobs)
    return elapse_time