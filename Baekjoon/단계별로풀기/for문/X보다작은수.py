import sys

n,x = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))



for a in arr :
    if a < x :
        print(a, end=" ")