import sys

# 최소 a자리부터 최대 b자리까지 n개의 문자를 가지고 암호를 만든다
a, b, n = map(int, sys.stdin.readline().split())

total = 0
# n개의 문자를 i개의 자리만큼 제곱한다
for i in range(a,b+1) :
    total += n**i
print(total)

#https://level.goorm.io/exam/43168/%EC%95%94%ED%98%B8%EC%9D%98-%EA%B0%9C%EC%88%98/quiz/1