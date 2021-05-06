import sys

# array에 n개의 숫자를 입력
n = int(sys.stdin.readline())

def factorial(n) :
    
    # 팩토리얼 0또한 1이다
    if n <= 1 :
        return 1
    # 팩토리얼은 n x (n-1) x ... 1 이다
    else :
        return n * factorial(n-1)

print(factorial(n))