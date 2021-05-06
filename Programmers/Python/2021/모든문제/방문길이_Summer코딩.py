def solution(dirs):
    cnt = 0 # 처음 이동한 영역에 갈때마다 카운트 증가
    board = [[0] * 11 for _ in range(11)] # 좌표가 x축 좌우로 -5 ~ 5, y축 상하로 -5 ~ 5이므로 11 X 11 배열을 만든다
    visited = [] # 이미 방문한 좌표를 넣는다
    
    p = [5,5] # 가장 정중앙을 시작점으로 한다
    
    for d in dirs :
        if d == 'U' and p[0]-1 >= 0 : # 위로 올렸을때
            # 해당 좌표쪽으로 이동한 경험이 없다면 이동
            if {(p[0],p[1]), (p[0]-1,p[1])} not in visited: 
                cnt += 1
                board[p[0]-1][p[1]] = 1
                board[p[0]][p[1]] = 1
                # 이동한 경력 추가
                visited.append({(p[0],p[1]), (p[0]-1,p[1])})
                
            p[0] -= 1
            
        elif d == 'D' and p[0]+1 <= 10 : # 아래로 내려갔을때
            # 해당 좌표쪽으로 이동한 경험이 없다면 이동
            if {(p[0],p[1]), (p[0]+1,p[1])} not in visited:
                cnt += 1
                board[p[0]+1][p[1]] = 1
                board[p[0]][p[1]] = 1
                # 이동한 경력 추가
                visited.append({(p[0],p[1]), (p[0]+1,p[1])})
                
            p[0] += 1
        
        elif d == 'R' and p[1]+1 <= 10 : # 우측으로 이동할때
            # 해당 좌표쪽으로 이동한 경험이 없다면 이동
            if {(p[0],p[1]), (p[0],p[1]+1)} not in visited:
                cnt += 1
                board[p[0]][p[1]+1] = 1
                board[p[0]][p[1]] = 1
                # 이동한 경력 추가
                visited.append({(p[0],p[1]), (p[0],p[1]+1)})
                
            p[1] += 1
            
        elif d == 'L' and p[1]-1 >= 0 : # 좌측으로 이동할때
            # 해당 좌표쪽으로 이동한 경험이 없다면 이동
            if {(p[0],p[1]), (p[0],p[1]-1)} not in visited:
                cnt += 1
                board[p[0]][p[1]-1] = 1
                board[p[0]][p[1]] = 1
                # 이동한 경력 추가
                visited.append({(p[0],p[1]), (p[0],p[1]-1)})
                
            p[1] -= 1
        
        # 다른 명령이 들어오면 무시
        else :
            continue
        
        # for i in range(11) :
        #     print(board[i])
        # print()
        # print(d, p, cnt)
    
    print(cnt)
    return cnt

dirs = "RRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUULU"	
solution(dirs)