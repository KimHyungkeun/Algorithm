import sys

# 두 수 a,b를 입력
a, b = map(int, sys.stdin.readline().split())

total = 0
for i in range(a, b+1) :
    if i % 2 == 1 : # i가 홀수라면 합계에 넣는다
        total += i
print(total)

# https://level.goorm.io/exam/43124/%ED%99%80%EC%88%98%EC%9D%98-%ED%95%A9/quiz/1