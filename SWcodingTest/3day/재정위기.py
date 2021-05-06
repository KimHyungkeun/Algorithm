import sys
from collections import deque

# 연봉을 입력
array = list(map(int, sys.stdin.readline().split()))
array.sort() # 연봉을 정렬 시킴
array = deque(array)

# 최소연봉의 인원과 최대연봉의 인원을 제외시킴
array.pop() 
array.popleft()
print(array[0])