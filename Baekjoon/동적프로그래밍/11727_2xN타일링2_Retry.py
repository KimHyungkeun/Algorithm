import sys

# 2xN에 들어갈 N을 입력
n = int(sys.stdin.readline())

# N이 3이상일때 아래와같은 dp 테이블 형성
if n >= 3 :
    dp = [0,1,3] + [0]*(n-2)
# 그렇지 않다면 아래와 같이 생성
else :
    dp = [0,1,3]

# 2xN을 만들 방법은 2x(N-2)의 방법수의 2배 + 2x(N-1)의 방법수이다 
for i in range(3, n+1) :
    dp[i] = (dp[i-2]*2 + dp[i-1]) % 10007
    

# 결과값을 10007로 나눈 나머지 계산
print(dp[n])
