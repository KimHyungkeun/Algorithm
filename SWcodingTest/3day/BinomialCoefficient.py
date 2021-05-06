import sys

# array에 n개의 숫자를 입력
n, k = map(int, sys.stdin.readline().split())

# 이항 계수
def binomial_coefficient(n,k) :
    if k == 0 or n == k :
        return 1
    
    # 이항계수의 점화식
    else :
        return binomial_coefficient(n-1,k-1) + binomial_coefficient(n-1,k) 

result = binomial_coefficient(n,k)
print(result)