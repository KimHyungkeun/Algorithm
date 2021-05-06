import sys

# 지불한 돈 입력
n = int(sys.stdin.readline())
coin = [500,100,50,10]

cnt = 0 # 동전갯수
i = 0 # 동전 종류위치를 담은 인덱스
while n != 0 :
    
    if n % coin[i] != n : # i번째 동전에 대해서 값을 지불하고, 그다음 단위의 동전으로 넘어간다
        cnt += (n // coin[i])
        n %= coin[i]
    else :
        i += 1
    
# 지불한 최소 동전의 갯수
print(cnt)

# -----------------------------------------------------------------------------------------------------

# # 답안

# n = 1260
# count = 0

# # 큰 단위의 화폐부터 차례대로 확인하기
# coin_types = [500, 100, 50, 10]

# for coin in coin_types:
#     count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
#     n %= coin

# print(count)





