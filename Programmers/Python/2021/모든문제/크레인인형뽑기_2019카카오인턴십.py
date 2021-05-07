def solution(board, moves):
    cnt = 0
    stack = []
       
    for m in moves :
        pos = m-1 # 인덱싱을 위해 현재 포지션에서 1을 제외
        for i in range(len(board)) :
            if board[i][pos] != 0 : # 만약 인형에 해당될 경우
                if not stack :
                    stack.append(board[i][pos]) # 빈바구니라면 무조건 넣음

                else :
                    if stack[-1] == board[i][pos] : # 바구니 top과 똑같은 종류의 인형이 오게되면
                        stack.pop() # 바구니에서 제외하고, 2를 더한다
                        cnt += 2
                    else :
                        stack.append(board[i][pos]) # 그렇지 않다면 바구니에 추가한다
                        
                board[i][pos] = 0 # 인형을 뽑았으므로 0으로 표시하고, 해당 위치에 대한 탐색을 종료한다
                break
                # print(stack)
                
            
    return cnt