from collections import deque
import sys

# 해당 문자열을 임의로 리스트로만든다
string = list(sys.stdin.readline().rstrip())
# print(string)
string = deque(string) # top과 bottom만을 주로 다르므로 덱으로 설정

i = 0
answer = ''
while string :
    # 짝수번째 차례이면 맨 앞쪽을
    if i % 2 == 0 :
        answer += string.popleft()
    else : # 홀수번째 차례이면 맨 뒤쪽을 넣는다
        answer += string.pop()
    i += 1

print(answer)

# https://level.goorm.io/exam/43110/%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B2%88%EA%B0%88%EC%95%84-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/quiz/1