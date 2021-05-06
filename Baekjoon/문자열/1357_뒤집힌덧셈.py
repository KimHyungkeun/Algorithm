import sys

# 역순정렬 함수
def reverse(a) :
    a = list(str(a))
    a.reverse()
    return a

# 두 수를 입력하고 역순으로 정렬
x, y = map(int, sys.stdin.readline().split())
x = reverse(x)
y = reverse(y)

# 역순정렬된 수를 다시 정수형 타입으로 변환
x = int(''.join(x))
y = int(''.join(y))
z = x + y

# 두 수의 합을 구하고, 그 합의 숫자 자리수 순서를 다시 역순으로 정렬
z = reverse(z)
z = int(''.join(z))

# 최종결과 출력
print(z)
