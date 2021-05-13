# pypy3로는 정답
import sys

# n행 m열의 행렬을 제작
n, m = map(int, sys.stdin.readline().split())

matrix = []
for _ in range(n) :
    tmp = list(map(int, sys.stdin.readline().split()))
    matrix.append(tmp)

# 테스트 케이스 k개를 제공
k = int(sys.stdin.readline())

for _ in range(k) :
    # (i,j) 부터 (x,y)범위 내의 부분합을 구함
    i, j, x, y = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1

    total = 0
    for idx in range(i, x+1) :
        total += sum(matrix[idx][j:y+1])
    print(total)