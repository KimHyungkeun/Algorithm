import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 각 원소 하나하나를, 수가 1개인 부분배열로 본다
dp = [1] * n


for i in range(n) :
    for j in range(i) :
        # i번째 수 이전까지의 수들 중, i번째 수보다 작으면서 부분수열의 길이가 긴것을 dp로 설정한다
        if arr[j] < arr[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))