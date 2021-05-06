import sys

a, b, n = map(int, sys.stdin.readline().split())

total = 0
for i in range(a,b+1) :
    total = n**i
print(total)