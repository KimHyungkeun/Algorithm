import sys

# n * n 형태의 배열 만듦
n = int(sys.stdin.readline())

# 배열 내에 값을 추가함
array = []
for _ in range(n) :
    row = list(sys.stdin.readline().split())
    array.append(row)

# 맨 마지막 열부터 아래순서대로 하나씩 읽어들여온다
for i in range(n-1, -1 ,-1) :
    for j in range(n) :
        print(array[j][i], end='')
    print(end='')

# https://level.goorm.io/exam/43087/%EC%84%B8%EB%A1%9C-%EC%9D%BD%EA%B8%B0/quiz/1