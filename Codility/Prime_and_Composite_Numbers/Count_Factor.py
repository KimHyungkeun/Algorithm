def solution(n):
    n = int(n)
    divisors = []
    divisors_back = [] 

    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            divisors.append(i)

            # 임의의 자연수 N의 약수들 중에서 두 약수의 곱이 N이 되는 약수 A와 약수 B는 반드시 존재한다
            # 자연수 N의 제곱근까지의 약수를 구하면 그 짝이 되는 약수는 자동으로 구해진다. (i, n//i)
            if (i != (n // i)): 
                divisors_back.append(n//i)

    length = len(divisors + divisors_back[::-1])
    return length

# 참고 https://inuplace.tistory.com/459