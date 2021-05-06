from collections import deque
n = int(input())

card = deque([])
for i in range(1, n+1) :
    card.append(i)

turn = 1
while len(card) != 1 :
    if turn % 2 == 1 : # 홀수번째 차례에서는 맨 윗장 카드를 버림
        card.popleft()
    
    else :  
        card.append(card.popleft()) # 짝수번째 차례에서는 맨 윗장 카드를, 맨 아래로 놓음
    
    turn += 1
    
print(card[0])