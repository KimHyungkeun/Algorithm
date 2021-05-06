import sys

n = int(sys.stdin.readline())

# 정삼각형 넓이 * 6이 정육각형 넓이
answer = (3**0.5) * (n**2) / 4
answer *= 6
print("%.2f" % answer)

# https://level.goorm.io/exam/43134/%EC%A0%95%EC%9C%A1%EA%B0%81%ED%98%95%EC%9D%98-%EB%84%93%EC%9D%B4/quiz/1