import sys
import heapq


# 힙배열은 pop을 할때 기본적으로 수가 낮은것을 먼저 뺀다

n = int(sys.stdin.readline())
# 비어있는 배열
heap = []

for _ in range(n) :
    # 숫자 입력
    num = int(sys.stdin.readline())
    heapq.heappush(heap, num)

summary = 0
# 힙 배열의 크기가 1이될때 까지 반복
while len(heap) != 1 :
    tmp = heapq.heappop(heap) + heapq.heappop(heap) # 2개의 카드를 배열에서 빼낸다
    summary += tmp # 두 카드의 수를 더한다
    heapq.heappush(heap, tmp) # 더한 수를 다시 배열에 넣는다

print(summary)

# https://claude-u.tistory.com/341