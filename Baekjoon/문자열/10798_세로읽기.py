import sys

board = []
# 5개 입력이 주어지고, 1줄당 최대 15개의 철자입력이 들어오므로 15*5 배열을 만든다
for _ in range(5) :
    row = [""]*15
    board.append(row)

# 문자열을 입력받아서, 배열에 알맞게 삽입시킨다
for i in range(5) :
    row = sys.stdin.readline().rstrip()
    for j in range(len(row)) :
        board[i][j] = row[j]

answer = ""
# 비어있는 칸을 제외하고, 문자가 존재하는 칸에 대해서 하나하나 철자를 이어붙인다
for i in range(15) :
    for j in range(5) :
        if board[j][i] != "" :
            answer += board[j][i]

print(answer)
