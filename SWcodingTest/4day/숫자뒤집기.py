import sys

# 숫자 입력
number = list(sys.stdin.readline().rstrip())
number = reversed(number) # 숫자의 순서를 뒤집음
number = list(number) # 뒤집은 숫자들을 다시 리스트로 정리

answer = ''.join(number) # 자릿수하나하나씩 이어붙임
print(int(answer))

# https://level.goorm.io/exam/43142/%EC%88%AB%EC%9E%90-%EB%92%A4%EC%A7%91%EA%B8%B0/quiz/1