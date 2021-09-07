import sys

k,n,m = map(int, sys.stdin.readline().split())

# 과자 하나의 액수가 k개 이고, 사야할 갯수가 n개이지만, 가진갯수가 m개이면 비어있는 만큼 추가로 받아야한다

if k * n > m :
    print(k*n-m)

else :
    print(0)