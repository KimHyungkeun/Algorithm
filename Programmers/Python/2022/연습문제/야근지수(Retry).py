import heapq
def solution(n, works):
    # 일해야하는 시간이 n보다 작으면 야근 안해도 된다
    if sum(works) < n :
        return 0
    
    # 근무를 먼저 끝내야하는 우선순위를 정한다
    heap = []
    for w in works :
        heapq.heappush(heap, [-w, w])
    
    # n시간이 지날때 까지 근무를 계속한다
    while n != 0 :
        work = heapq.heappop(heap)
        if work != (0,0) :
            work[0] += 1
            work[1] -= 1
        heapq.heappush(heap, work)
        n -= 1
    
    # 이 때, 야근 지수는 현재 heap에 담긴 h의 제곱들의 합이다
    ans = 0
    for h in heap :
        ans += h[1]**2
    return ans

# https://velog.io/@daon9apples/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level3-%EC%95%BC%EA%B7%BC-%EC%A7%80%EC%88%98-Python