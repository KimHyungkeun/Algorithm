import sys

n = int(sys.stdin.readline())

star = 2*n - 1

# 역삼각형
for i in range(n) :
    for j in range(star) :
        if i <= j <= star-1-i :
            print("*", end='')
            if j == star-1-i :
                break
        
        else :
            print(" ",end='')
    print()
