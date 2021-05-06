import sys

# 총 링들의 갯수
n = int(sys.stdin.readline())

# 각 원들의 원둘레를 구함
circle = list(map(int, sys.stdin.readline().split()))
for i in range(n) :
    circle[i] *= 2

# 첫번째 링을 따로 빼두고, 비교할 링들만 남겨둔다
first_circle = circle[0]
del circle[0]

# 최대공약수 함수(기약분수로 만들기위한 최대공약수를 구하려 함)
def GCD(a, b): 
    while b != 0 : 
        a, b = b, a%b 
    return a #반환되는 a가 두 수의 최대공약수

for i in range(n-1) :
    mul = GCD(first_circle, circle[i]) # 최대공약수 구함
    son = first_circle // mul # 분자 약분
    mom = circle[i] // mul # 분모 약분
    print(str(son) + '/' + str(mom))
