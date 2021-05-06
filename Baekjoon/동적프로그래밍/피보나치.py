memo = [-1]*100

def fibonacci (n) : # 피보나치 구하기
    print(n)
    if n <= 1 :
        return n
    else :
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_memo (n) : #한 번 답을 구할때, 어딘가에 메모해놓고, 중복 호출이면 메모해놓은 값을 리턴한다.
    
    if n <= 1 :
        return n
    else :
        if memo[n] > 0 :
            return memo[n]

        memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
        # print(n, memo[n])
        return memo[n]

def fibonacci_bottom_up (n) : # 작은 수부터 시작하여 입력한 n까지의 피보나치를 구한다.
    print(n)

    memo[0] = 0
    memo[1] = 1
    for i in range(2,n+1) :
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[i]

n = int(input())

# fibonacci(n)
result = fibonacci_memo(n)
print(result)
# fibonacci_bottom_up(n)
