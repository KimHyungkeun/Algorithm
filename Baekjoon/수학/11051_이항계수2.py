n, k = map(int, input().split())

def factorial (n) : # 팩토리얼 구하기
    if n <= 1 :
        return 1
    
    else :
        mul = 1
        for i in range(1, n+1) :
            mul *= i
        return mul

result =  factorial(n) // (factorial(k) * factorial(n-k))
ans = result % 10007 # 이항계수 (n,k)를 10007로 나눈 후 나머지
print(ans)