from collections import deque
def solution(board) :
    result = float('inf')
    
    n = len(board)
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    # 0:상, 1:좌, 2:하, 3:우
    visit = {(0,0,0):0, (0,0,1):0, (0,0,2):0, (0,0,3):0}
    queue = deque()
    queue.append((0,0,-1,0))
    
    while queue :
        
        # print(queue)
        x, y, direct, cost = queue.popleft()
        
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 :
                newcost = cost

                if direct == -1 :
                    newcost += 100
                
                elif (direct - d) % 2 == 0 :
                    newcost += 100
                
                else :
                    newcost += 600
                
                if nx == n-1 and ny == n-1 :
                    result = min(result, newcost)
                

                if not visit.get((nx,ny,d)) or visit[(nx,ny,d)] > newcost:
                    visit[(nx,ny,d)] = newcost
                    queue.append((nx, ny, d, newcost))
                                               
            

    
    # print(result)           
    return result


board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# board = [[0,0,0],[0,0,0],[0,0,0]]
# board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
solution(board)