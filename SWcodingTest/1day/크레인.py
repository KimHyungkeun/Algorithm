def solution(board, moves):
    answer = 0
    stack = []

    for cmd in moves :
        # 크레인 번호는 1~5까지지만, 인덱스 0부터 시작하므로 0~4 까지 이다
        idx = cmd-1
        # print(stack)

        # 스택이 비어있다면, 일단 맨 첫번째 인형을 끌고온다
        if not stack :
            for i in range(len(board)) :
                if board[i][idx] != 0 :
                    stack.append(board[i][idx])
                    board[i][idx] = 0 
                    break
            continue
        
        # 만약 맨 윗쪽에 쌓여있는 인형과, 이번에 넣을 인형이 만약 같은 종류라면 그 2개를 스택에서 제외한다
        for i in range(len(board)) :
                if board[i][idx] != 0 :
                    if stack[-1] == board[i][idx] :
                        stack.pop()
                        answer += 2
                    else :
                        stack.append(board[i][idx])
                    
                    board[i][idx] = 0 
                    break
        
    # print(answer)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]
solution(board,moves)

# https://programmers.co.kr/learn/courses/30/lessons/64061