import sys
import heapq

# array에 n개의 숫자를 입력
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
# 특정구간을 정한다
start, end = map(int, sys.stdin.readline().split())

# 특정구간의 합을 구한다
print(sum(array[start-1:end]))