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
            # 가장 최대 횟수 
            print(heapq.heappop(heap)[1])
    else :
        # 보통의 heapq는 최소 힙으로 구현 되어있음. 따라서, 그 성질을 역이용해 '-'를 붙여 역으로 순위를 편성
        heapq.heappush(heap, (-num, num))

# --------------------------------------------------------------------------------------

# import heapq

# def heap_sort(nums):
#   heap = []
#   for num in nums:
#     heapq.heappush(heap, num)
#     print(heap)
  
#   sorted_nums = []
#   while heap:
#     sorted_nums.append(heapq.heappop(heap))
#   return sorted_nums

# print(heap_sort([4, 1, 7, 3, 8, 5]))

# heap = []

# heapq.heappush(heap, 1)
# print(heap)
# heapq.heappush(heap, 4)
# print(heap)
# heapq.heappush(heap, 7)
# print(heap)
# heapq.heappush(heap, 3)
# print(heap)
    