import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n) :
    num = int(sys.stdin.readline())
    arr.append(num)

arr.sort()
for a in arr :
    print(a)
