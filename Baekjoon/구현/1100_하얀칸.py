board = []
# 체스보드판을 형성한다
for i in range(8) :
    row = list(input())
    board.append(row)

# 흰색 칸 위에 말이있다면 카운팅을 한다
cnt = 0
for i in range(8) :
    # 인덱스 i가 짝수번째일때는 W로 시작하고, 홀수번째라면 B로 시작한다
    if i % 2 == 0 :
        start = 'W'
    else :
        start = 'B'
    for j in range(8) :
        # 두번째 칸부터 차례대로 세어서, 이전 색과 서로 반대가 되도록 칸색깔을 주기적으로 바꾼다
        if j >= 1 :
            if start == 'W' :
                start = 'B' 
            else :
                start = 'W'
        
        # 흰색 칸 위에 말이 있다면, 카운팅을 한다
        if board[i][j] == 'F' and start == 'W' :
            cnt += 1
print(cnt)