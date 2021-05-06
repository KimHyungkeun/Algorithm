import sys

# 지불한 값
n = int(sys.stdin.readline())

# 지불하고 남은 잔돈
remind = 1000 - n
coin = [500,100,50,10,5,1] # 낼 수 있는 잔돈의 종류

cnt = 0
for i in range(6) :
    # 만약 남은 잔돈이 i번째 동전으로 지불 가능하다면, 가능한 한 그 동전의 갯수를 채운다
    if remind % coin[i] != remind :
       cnt += (remind // coin[i])
       remind %= coin[i] # 그 후, 다음 단위의 잔돈으로 넘어간다
    
    # 전부 거스른 경우에는 루프문 탈출
    if remind == 0 :
        break

print(cnt)
    