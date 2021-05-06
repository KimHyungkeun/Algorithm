import sys

# 세 각을 입력
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

# 세 각의 합이 180도가 이면 Error
if a+b+c != 180 :
    print("Error")

# 세 각이 모두 60도 이면 Equilateral 출력
elif a == 60 and b == 60 and c == 60 :
    print("Equilateral")

# 세 각의 합이 180도이고, 두 각이 같다면 Isosceles 출력
elif a+b+c == 180 and a == b or b == c or a == c :
    print("Isosceles")

# 세 각의 합이 180도이고, 세 각 모두 각기 다르다면 Scalene 출력
else :
    print("Scalene")