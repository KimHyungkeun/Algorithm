import sys
import heapq

# 연산 개수 입력
n = int(sys.stdin.readline())

# 비어있는 배열
heap = []

for _ in range(n) :
    # 숫자 입력
    num = int(sys.stdin.readline())

    if num == 0 :
        # 힙이 비어있다면 0 출력
        if not heap :
            print(0) 
        else :
            # 가장 작은 수를 출력
            print(heapq.heappop(heap)[1])
    else :
        # 힙에 값을 넣음, 정렬 기준은 해당 수의 절대값을 기준으로 한다.
        heapq.heappush(heap, (abs(num), num))