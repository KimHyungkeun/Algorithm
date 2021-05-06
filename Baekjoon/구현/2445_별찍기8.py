import sys

n = int(sys.stdin.readline())

star = 2*n - 1
mid = star // 2

# 나비 모양
for i in range(star) :
    for j in range(2*n) :
        if i <= mid :
            if j <= i or j >= star - i :
                print("*", end='')
            else :
                print(" ", end='') 
        
        else :
            if mid-(i-mid) < j <= mid+(i-mid) :
                print(" ", end='')
            else :
                print("*",end='')
    print()