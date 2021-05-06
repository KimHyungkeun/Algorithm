import sys

# 테스트케이스 수 입력
n = int(sys.stdin.readline())

cnt = 0
for _ in range(n) :
    # 숫자를 입력하여 제곱수 판별
    num = int(sys.stdin.readline())
    tmp = num ** (0.5) 
    if tmp == int(tmp) :
        cnt += 1

print(cnt)

# https://level.goorm.io/exam/43152/%EC%99%84%EC%A0%84-%EC%A0%9C%EA%B3%B1%EC%88%98/quiz/1