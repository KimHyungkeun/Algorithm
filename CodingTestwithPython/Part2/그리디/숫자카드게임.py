import sys

# n X m 행렬
n, m = map(int, sys.stdin.readline().split())

# 카드의 각 행에 들어있는 카드종류들을 넣음
cards = []
for _ in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    cards.append(row)

# 각 행별로 골라낸 최소 크기의 숫자들만을 담는 배열
minimum = []
for i in range(n) :
    minimum.append(min(cards[i]))

# 작은 숫자들 중 가장 큰 수를 골라낸다
print(max(minimum))

# -------------------------------------------------------------------------------------
# 답안

import sys
# n X m 행렬
n, m = map(int, sys.stdin.readline().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력