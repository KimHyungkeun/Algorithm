n, k = map(int, input().split())

coins = []
max_unit = 0 # 최대 동전단위
unit_index = 0 # 최대 동전단위의 위치

for i in range(n) :
    coins.append(int(input())) # 동전 단위들을 모음

# k값에 대한 최대 동전단위를 정함
for i in range(n) :
    if k <= coins[i] :  
        break
max_unit = coins[i]
unit_index = i

# 최대 동전단위 구성에 따른, coin 리스트 재구성
extract_coins = []
for i in range(unit_index+1) :
    extract_coins.append(coins[i])
extract_coins.sort(reverse=True) # 내림차순으로 정렬

# print(extract_coins)

i = 0
count = 0
while i < len(extract_coins) :
    # print(extract_coins[i])
    if k % extract_coins[i] == k : # 만약, k가 나누어 떨어지지 않으며 그보다 더 작은 동전단위로 바꾼다
        i += 1
        continue

    val = int(k / extract_coins[i]) # k를 해당 동전단위로 거스른다
    count += val
    k %= extract_coins[i] # 거스르고 난 후의 잔액
    # print(k)

    if k == 0 : # 잔액이 0이 되면 루프문 탈출
        break 
    
    else :
        continue
    
print(count)