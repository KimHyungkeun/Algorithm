import sys

# 앨범에 수록된 곡의 개수 A, 평균값 i
a, i = map(int, sys.stdin.readline().split())
print(a * (i-1) + 1)