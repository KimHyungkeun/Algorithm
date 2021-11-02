import sys

arr = []
for _ in range(10) :
    n = int(sys.stdin.readline())
    arr.append(n % 42)

print(len(set(arr)))