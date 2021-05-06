import sys

# 화폐갯수 n과 만들어야할 화폐 m
n, m = map(int, sys.stdin.readline().split())

# 화폐 종류 입력
array = []
for _ in range(n) :
    array.append(int(sys.stdin.readline()))

# 만들기 전 모든 초기값은 10001로 해둔다
dp = [10001] * (m + 1)
dp[0] = 0

for i in range(n) :
    for j in range(array[i], m+1) :
        if dp[j - array[i]] != 10001 : # (i-k)원을 만드는 방법이 있는 경우
            dp[j] = min(dp[j], dp[j - array[i]] + 1)

# 계산된 결과 출력
if dp[m] == 10001 :
    print(-1)
else :
    print(dp[m]) 

