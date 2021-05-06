import sys

n = int(sys.stdin.readline())

# 양의 정수이므로 최소 1개이상의 1이 있다
cnt = 1

while n != 1 :
    # 2로 나누어서 나머지가 1이면 카운트 추가
    if n % 2 == 1 :
        cnt += 1
    n //= 2

print(cnt)

# https://level.goorm.io/exam/43100/2%EC%A7%84%EC%88%98%EC%9D%98-1-%EA%B0%9C%EC%88%98/quiz/1