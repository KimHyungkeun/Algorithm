import sys

n = int(sys.stdin.readline())

# 반대편 직각삼각형
for i in range(n) :
    for j in range(n) :
        if j >= i :
            print("*", end='')
        else :
            print(" ",end='')
    print() 