import sys

a,b = sys.stdin.readline().strip().split()
a = int(a)
b = int(b)

def gcd (a, b) : # 최대공약수 => b가 0이 될때까지 나머지연산과 나누기를 반복(유클리드 호제법)
    while (b != 0) :
        r = a % b
        a = b
        b = r
    return a

def lcm (a, b) : # 최소공배수 => 두 수의 최대공약수 g를 구하고 g * (a/g) * (b/g) 를 한다
    g = gcd(a, b)

    return int(g * (a/g) * (b/g))

print(gcd(a,b))
print(lcm(a,b)) 