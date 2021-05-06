import sys

# 사칙연산
n1, calc, n2 = sys.stdin.readline().split()

n1 = int(n1)
n2 = int(n2)

if calc == '+' :
    print(n1 + n2)

elif calc == '-' :
    print(n1 - n2)

elif calc == "*" :
    print(n1 * n2)

elif calc == "/" :
    result = n1 / n2 
    print("%.2f" % result)

# https://level.goorm.io/exam/43241/%EA%B3%84%EC%82%B0%EA%B8%B0/quiz/1
