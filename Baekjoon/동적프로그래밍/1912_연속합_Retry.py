import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * n # i번째 까지의 원소들의 합을 저장해놓는 배열
result = -9999

for i in range(n) :
    # 현재의 값과, 현재까지의 배열합을 비교하여 가장 최댓값을 dp에 저장
    dp[i] = max(dp[i-1]+arr[i], arr[i]) 
    # 현재 result보다 더 큰 값이 나타나면 새로 갱신한다
    result = max(dp[i], result)

print(result)

# 참고 https://claude-u.tistory.com/175