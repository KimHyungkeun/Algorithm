import sys
import heapq

# array에 n개의 숫자를 입력
n = int(sys.stdin.readline())

# 비어있는 배열
heap = []

def heap_sort(heap) :   
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

# 절댓갑 힙소트를 사용해 먼저 건물 크기에 대해 정렬한다
heap_sort(heap)
arr = []
while heap :
    arr.append(heapq.heappop(heap)[1])
building = list(reversed(arr))

# print(building)
max_combo = 0
combo = 0
stack = []

for i in range(len(building)) :
    
    if not stack :
        stack.append(building[i])
    
    else :
        if stack[-1] < 0 and building[i] >= 0 :
            stack.append(building[i])
            if len(stack) == 2 :
                combo = 2
            elif len(stack) > 2 :
                combo += 1

        elif stack[-1] >= 0 and building[i] < 0 :
            stack.append(building[i])
            if len(stack) == 2 :
                combo = 2
            elif len(stack) > 2 :
                combo += 1

        else :
            if max_combo < combo :
                max_combo = combo
            combo = 0
            stack = []
            stack.append(building[i])
    
    if i == len(building)-1 :
        if max_combo < combo :
            max_combo = combo

print(max_combo)
    


