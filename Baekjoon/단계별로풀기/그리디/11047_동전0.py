import sys

n, k = map(int, sys.stdin.readline().split())

# 동전 종류들을 모아놓는 리스트
coins = []
for _ in range(n) :
    coin = int(sys.stdin.readline())
    coins.append(coin)

# 동전 종류를 단위값이 큰 값을 기준으로 먼저 정렬
coins.sort(reverse=True)

cnt = 0
# 현재 남아있는 값인 k값을 coin 단위로 하나하나씩 거슬러가면서 값 비교
for c in coins :
    if c > k :
        continue
    val = k // c
    cnt += val
    if k % c == 0 :
        break
    k = k % c

print(cnt)