n, k = map(int, input().split())

array = []

for i in range(1, n+1) :
    array.append(i) # 1부터 n까지의 배열 셋팅

pos = 0 # 조치되어야 할 위치
turn = 0 # 총 작동 횟수

print("<", end='')
while turn != n : # 작동횟수가 배열길이만큰 작동한다.
    pos = pos + k - 1 # 0부터 인덱스가 시작하므로, 1을 뺀다


    if pos >= len(array) : # 만약 인덱스가 배열범위를 벗어나면, 범위에 맞도록 인덱스를 재조정
        pos %= len(array) 
    
    elif pos < 0: 
        pos %= len(array) # 만약 인덱스가 0보다 작은 위치여도 같은 방식으로 조치

    # 재 조정되는 요소들
    if turn == n - 1 :
        print(array.pop(pos), end = '') 
    
    else :
        print(array.pop(pos), end = ', ')
    turn += 1

print(">")


    
 




