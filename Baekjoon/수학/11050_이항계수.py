n, k = map(int, input().split())

def factorial (n) : # 팩토리얼 구하기
    if n <= 1 :
        return 1
    
    else :
        return n * factorial(n-1)

result =  factorial(n) // (factorial(k) * factorial(n-k))
print(result)