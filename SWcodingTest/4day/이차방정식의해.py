import sys

a,b,c = map(int, sys.stdin.readline().split())

# 판별식 b^2 - 4ac < 0 이면 해가 없다
if b**2 - 4*a*c < 0 :
    print("X")

# 판별식 b^2 - 4ac == 0  이면 중근을 가진다
elif b**2 - 4*a*c == 0 :
    x = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    print("%.2f" % x)

# 판별식 b^2 - 4ac > 0  이면 해를 2개 가진다
else :
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    print("%.2f" % x1 ,end=', ')
    print("%.2f" % x2)

# https://level.goorm.io/exam/43188/%EC%9D%B4%EC%B0%A8-%EB%B0%A9%EC%A0%95%EC%8B%9D%EC%9D%98-%ED%95%B4/quiz/1