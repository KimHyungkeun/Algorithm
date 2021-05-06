import sys

n = int(sys.stdin.readline())

# result = (2*n - 1) % 796796
# print(result)

dp = [0] * 1001
dp[1] = 1 # 2*1 타일 1개 (경우의 수 1)
dp[2] = 3 # 2*1 타일 2개, 1*2 타일 2개, 2*2 타일 1개(경우의 수 3)

# i-1번째까지 모두 타일로 덮여있다면 2*1타일 덮개를 채우는 1개의 경우만 발생
# i-2번째까지 모두 타일로 덮여있다면 2*2타일 1개와 1*2타일 2개를 덮는 2개의 경우가 발생
for i in range(3, n+1) :
    dp[i] = dp[i-1] + 2*dp[i-2] 

print(dp[n])