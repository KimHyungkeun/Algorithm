import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

maximum = -1
# 카드 3장의 합이 m 이하이면서, 그 중 m과 가장 가까운 수여야 한다
for i in range(len(card)-2) :
    for j in range(i+1, len(card)-1) :
        for k in range(j+1, len(card)) :
            if card[i] + card[j] + card[k] <= m and maximum < card[i] + card[j] + card[k] :
                maximum = card[i] + card[j] + card[k]

print(maximum)