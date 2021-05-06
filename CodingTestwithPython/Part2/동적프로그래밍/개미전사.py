import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

dp = [0] * 101 # 최대 가능한 n이 100이므로 배열을 100개

dp[0] = array[0] # 창고가 1개이면 그 창고만 가능
dp[1] = max(array[0], array[1]) # 창고가 2개이면 둘 중 식량이 가장 많은 곳

for i in range(2, n+1) :
    # dp[i]는 i-1개의 창고까지 있을때 최대로 가질 수 있는 식량 포획량과 i-2개의 창고까지 있을때의 최대개수와 현 i번째 식량을 모두 더한 값중 최댓값을 골라낸다
    dp[i] = max(dp[i-1], dp[i-2] + array[i])

print(dp[n-1])