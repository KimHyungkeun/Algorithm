def solution(n):
    # 피보나치 수열 생성 (f[n] = f[n-1] + f[n-2])
    fibo = [0,1] + [0]*(n-1)
    
    # i번째 피보나치 수열을 1234567로 나눈 나머지값을 저장
    for i in range(2, n+1) :
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1234567
    
    # 값 리턴
    answer = fibo[n]
    return answer