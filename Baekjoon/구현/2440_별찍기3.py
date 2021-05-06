import sys

# 직각삼각형
n = int(sys.stdin.readline())

for i in range(n, 0, -1) :
    for j in range(i) :
        print("*",end='')
    print()