import sys

n,m = map(int, sys.stdin.readline().split())
# 전체 n*m 크기에서 1을 빼면 최소로 자른 횟수가 나온다
print( n * m - 1)