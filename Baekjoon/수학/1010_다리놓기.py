import sys

# 테스트 케이스 갯수 입력
t = int(sys.stdin.readline())

# n의 팩토리얼을 구하는 함수
def factorial (n) :
    result = 1
    for i in range(1,n+1) :
        result *= i
    return result

for _ in range(t) :
    # 다리를 겹치지 않도록 놓는 방법은 mCn개이다. (조합)
    n, m = map(int, sys.stdin.readline().split())
    cnt = factorial(m) // (factorial(m-n) * factorial(n))
    print(cnt)


    