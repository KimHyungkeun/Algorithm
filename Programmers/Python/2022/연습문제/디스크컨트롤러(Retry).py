import heapq
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs) :
        # 현재 시점에서 처리할수 있는 작업을 heap에 저장
        for j in jobs :
            if start < j[0] <= now :
                heapq.heappush(heap, [j[1], j[0]])

        
        # 처리할 작업이 있는 경우
        if heap :
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간부터 종료시간 까지의 시간 계산
            i += 1
        else : # 처리할 작업이 없는 경우 다음 시간 탐색
            now += 1
            
    return answer // len(jobs)

# 참고 : https://soohyun6879.tistory.com/136