import sys

def bingo_check(board) :

    cnt = 0
    # 가로줄에 대해 빙고 탐색
    for i in range(5) :
        if sum(board[i]) == 0 :
            cnt += 1
        if cnt >= 3 :
            return cnt
    
    # 세로줄에 대해 빙고 탐색
    for i in range(5) :
        total = 0
        for j in range(5) :
            total += board[j][i]
        if total == 0 :
            cnt += 1
        if cnt >= 3 :
            return cnt
    
    # (0,0) -> (4,4) 방향으로 대각선 하향 탐색
    total = 0
    for i in range(5) :
        total += board[i][i]
    if total == 0 :
        cnt += 1
    if cnt >= 3 :
        return cnt
    
    # (0,4) -> (4,0) 방향으로 대각선 하향 탐색
    total = 0
    for i in range(5) :
        total += board[i][4-i]
    if total == 0 :
        cnt += 1
    if cnt >= 3 :
        return cnt
    
    return cnt


# 빙고판 제작
board = []
for _ in range(5) :
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

flag = False
answer = []
# 답란 순서를 차례대로 입력
for i in range(5) :
    row = list(map(int, sys.stdin.readline().split()))
    answer.append(row)

for i in range(len(answer)) :
    for j in range(len(answer[i])) :

        for k in range(len(board)) :
            for t in range(len(board[k])) :
                # 해당 답란을 확인했다면, 그 위치에 0을 넣는다 
                if board[k][t] == answer[i][j] :
                    board[k][t] = 0
                
                # 만약, 현재 상황에서 빙고가 3줄 이상 나온다면 여기서 계산을 중지하고, 그 답이 몇번째에서 나왔는지 출력한다
                if bingo_check(board) >= 3 :
                    flag = True
                    result = (5*i)+(j+1)
                    break

            # 답을 찾으면 반복문에서 탈출
            if flag :
                break
        
        if flag :
            break
    
    if flag :
        break

print(result)