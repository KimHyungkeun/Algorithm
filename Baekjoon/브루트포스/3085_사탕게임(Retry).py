import sys
# import time

# n x n 보드 설정
n = int(sys.stdin.readline())

board = []
for i in range(n) :
    row = list(input())
    board.append(row)

# start = time.time()
# 사탕을 아예 못먹는 경우는 없다
max_combo = 0

def row_search () :
    global max_combo

    for k in range(n) :
            combo = 1
            # 가로 방향으로 비교
            for row in range(n-1) :
                if board[k][row] == board[k][row+1] :
                    combo += 1
                    # print(combo)
                else :
                    if combo > max_combo :
                        max_combo = combo
                        # print(max_combo)
                    combo = 1
            if combo > max_combo :
                    max_combo = combo

def col_search () :
    global max_combo

    for k in range(n) :
            combo = 1
            # 세로 방향으로 비교
            for col in range(n-1) : 
                if board[col][k] == board[col+1][k] :
                    combo += 1
                    # print(combo)
                else :
                    if combo > max_combo :
                        max_combo = combo
                        # print(max_combo)
                    combo = 1
            
            if combo > max_combo :
                    max_combo = combo

# print(board)

# 1. 해당 행에서 두 캔디를 서로 바꿔본다
for i in range(n) :
    for j in range(n-1) :
        # 해당 행에서 두 캔디를 서로 바꿔본다
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        
        row_search()
        col_search()
        
        # 원상 복구
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            


# 2. 해당 열에서 두 캔디를 서로 바꿔본다
for i in range(n) :
    for j in range(n-1) :
        # 해당 열에서 두 캔디를 서로 바꿔본다
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

        row_search()
        col_search()
        
        # 원상 복구
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(max_combo)
# print("time :", time.time() - start)