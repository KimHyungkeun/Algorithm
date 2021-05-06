import sys

n = int(sys.stdin.readline())

# 계산값을 저장하기 위한 DP테이블 초기화
dp = [0] * 30001

for i in range(2, n+1) :
    # -1을 뺀다
    dp[i] = dp[i-1] + 1 # 이전 단계를 한번 호출하므로 +1

    # 2로 나누어지면 2로 나눈다
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1) 

    # 3로 나누어지면 3으로 나눈다
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)

    # 5로 나누어지면 5으로 나눈다
    if i % 5 == 0 :
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[n])
    
