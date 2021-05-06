import sys

n = int(sys.stdin.readline())

star = 2*n - 1
mid = star // 2

# 다이아몬드 형태
for i in range(star) :
    for j in range(star) :
        if i > mid :
            if (i-mid) <= j < star - (i-mid) :
                print("*",end='')     
                if j == star - (i-mid) - 1:
                    break      
            else :
                print(" ",end='')

        else :
            if mid - i <= j <= mid + i :
                print("*",end='')
                if j == mid + i :
                    break     
            else :
                print(" ",end='')
    print()
        