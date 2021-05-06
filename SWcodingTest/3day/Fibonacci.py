import sys

# array에 n개의 숫자를 입력
n = int(sys.stdin.readline())
dp = [0,1,1,2] # 이미 출력한값은 미리 저장해둔다

def fibonacci(n) :
    # n이 1이면 1을 리턴
    if n == 1 :
        if n not in dp :
            dp.append(n)
        return n
    
    # n이 0이면 0을 리턴
    elif n == 0 :
        if n not in dp :
            dp.append(n)
        return n
    
    # i번째와 i+1번째를 더한 결과가 i+2번째 피보나치이다
    else :
        result = fibonacci(n-1) + fibonacci(n-2)
        if result not in dp :
            dp.append(result)
        return result

fibonacci(n)
print(sum(dp[:n+1]))