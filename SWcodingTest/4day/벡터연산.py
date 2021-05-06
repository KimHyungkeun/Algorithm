import sys

a_x, a_y = map(int, sys.stdin.readline().split())
b_x, b_y = map(int, sys.stdin.readline().split())
calc = sys.stdin.readline().rstrip()

# print(a_x, a_y)

if calc == '+' :
    x = a_x + b_x
    y = a_y + b_y
    print("%.2f" % x, end = ' ')
    print("%.2f" % y)

else :
    x = a_x - b_x
    y = a_y - b_y
    print("%.2f" % x, end = ' ')
    print("%.2f" % y)

# https://level.goorm.io/exam/43277/%EB%B2%A1%ED%84%B0%EC%9D%98-%EC%97%B0%EC%82%B0/quiz/1
    
