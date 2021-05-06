import sys

n = int(sys.stdin.readline())

# 크리스마스 트리 형태
# 마지막 row에서 찍어야할 별의 갯수
star = 2*n - 1

for i in range(n) :
    for j in range(star) :
        if (n-1) - i <= j <= (n-1) + i :
            print("*",end='')
            # 해당 row에서 별을 다 찍고나면 바로 다음 순서로 넘어가야한다.
            if j == (n-1) + i :
                break       
        else :
            print(end=' ')
    print()

