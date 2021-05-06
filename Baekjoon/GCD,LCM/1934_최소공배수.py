import sys

n = int(sys.stdin.readline().strip())


def gcd(a, b) :
    while (b != 0) :
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b) :
    g = gcd(a,b)

    return int(g * (a/g) * (b/g))

for _ in range(n) :
    a, b = sys.stdin.readline().strip().split()
    a = int(a)
    b = int(b)

    print(lcm(a,b))