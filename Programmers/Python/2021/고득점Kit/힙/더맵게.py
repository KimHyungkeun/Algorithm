import heapq
def solution(scoville, K):
    answer = 0

    # 비어있는 배열
    heap = []
    for num in scoville : # 힙에 넣음
        heapq.heappush(heap, num)
        
    while len(heap) > 1 :
        flag = True

        first = heapq.heappop(heap) # 가장 안매운 음식 스코빌
        second = heapq.heappop(heap) # 두번째로 안매운 음식 스코빌
        mixed = first + (second * 2) # 스코빌 지수 계산
        heapq.heappush(heap, mixed) # 음식 스코빌 리스트에 넣음
        answer += 1 # 횟수 증가

        for n in heap :
            if n < K : # 만약 하나라도 K이상의 스코빌이 아니라면 다시 계산
                flag = False
                break
        
        if flag :
            print(answer) # 만약 모두 K이상을 만족하면 프로그램 종료
            return answer
    
    print(-1) # K이상을 만들 수 없다면 -1 반환
    return -1

scoville = [1, 2, 3, 9, 10, 12]	
K = 7
solution(scoville, K)