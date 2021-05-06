import sys

n = int(sys.stdin.readline())

# 총 라인 수는 2n개에서 1개를 뺀 값이다
col = 2*n - 1
# 대칭 기준을 위해 가운데지점 인덱스를 구한다
mid = col // 2

for i in range(col) :
    for j in range(n) :
        # 중간지점까지의 별찍기(증가)
        if i <= mid :
            if j < (n-1-i) :
                print(" ",end='')
            else :
                print("*",end='')
        # 중간지점이후의 별찍기(감소)
        else :
            if j < (i-(n-1)) :
                print(" ", end='')
            else :
                print("*",end='')
    print()
