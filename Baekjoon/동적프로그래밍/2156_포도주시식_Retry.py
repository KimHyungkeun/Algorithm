import sys

n = int(sys.stdin.readline())
wine = [0] # 와인잔 총 갯수 (인덱스 1부터 셈 시작)
dp = [0] # 와인잔 선택 경우 중 최고 경우들만 나타냄(인덱스 1부터 시작)
for _ in range(n) :
    quantity = int(sys.stdin.readline())
    wine.append(quantity) # 와인에 포도잔을 따른다

dp.append(wine[1]) # 맨 처음 포도잔을 선택

if n > 1 : # 만약 포도잔이 여러개면
    dp.append(max(wine[1], wine[1]+wine[2])) # 먼저 두번째 까지 따르고 나서, 마신다

# 포도잔이 3잔 이상일 경우
# 1. 바로 이전 차례의 잔만 마신 경우
# 2. 현재잔 + 이전잔 + 3번째 이전까지 마시고 나서의 총량
# 3. 현재잔 + 2번째 이전까지 마시고 나서의 총량 
for i in range(3, n+1) : 
    dp.append(max(dp[i-1],  dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i]))

# 가장 많이 마신 경우 출력
print(dp[-1])

# 참고 : https://pacific-ocean.tistory.com/152
