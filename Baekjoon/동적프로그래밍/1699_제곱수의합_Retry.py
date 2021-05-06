import sys
N = int(sys.stdin.readline())

dp = [0] * 100001

for i in range(1, N + 1):
    dp[i] = i
    for j in range(1, i):
        if (j * j) > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
print(dp[N])

# 출처: https://hjp845.tistory.com/123

# import sys

# n = int(sys.stdin.readline())

# if n >= 4 :
#     dp = [0,1,2,3] + [0]*(n-3)
# else :
#     dp = [0,1,2,3]

# cnt = 0
# for i in range(4, n+1) :
#     if int(i ** 0.5) ** 2 == i :
#         dp[i] = 1
#         cnt = i
#     else :
#         dp[i] = 1 + dp[i-cnt]

# print(dp[-1])
     
