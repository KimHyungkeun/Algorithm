memo = [-1]*100

def fibonacci_memo (n) : #한 번 답을 구할때, 어딘가에 메모해놓고, 중복 호출이면 메모해놓은 값을 리턴한다.
    
    if n <= 1 :
        return n
    else :
        if memo[n] > 0 :
            return memo[n]

        memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
        # print(n, memo[n])
        return memo[n]


n = int(input())


result = fibonacci_memo(n)
print(result)

