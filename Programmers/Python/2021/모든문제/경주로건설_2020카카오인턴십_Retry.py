from collections import deque
def solution(board) :
    n = len(board)
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    answer = float('inf')
    queue = deque()

    # x좌표, y좌표 방향 비용 순서로 큐에 넣음(방향은 맨 처음 시작할 때 -1로 설정)
    queue.append((0,0,-1,0)) # x좌표, y좌표, 방향, 비용
    visit = {(0,0,0):0, (0,0,1):0, (0,0,2):0, (0,0,3):0} # 0 : 상, 1 : 좌, 2 : 하, 3 : 우
    while queue :
        x, y, dir1, cost = queue.popleft()
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 :
                newcost = cost
                # 방향이 -1인 경우는 가장 처음에는 방향이 없으므로 비용에 100을 추가
                if dir1 == -1 :
                    newcost += 100
                # 기존 방향과 진행 방향이 평행한 경우
                elif (dir1 - d) % 2 == 0 :
                    newcost += 100
                # 기존 방향과 진행 방향이 수직인 경우
                else :
                    newcost += 600
                # 목적지에 도착했을 경우 정답 값과 비교하여 더 작은것으로 정답 값 갱신
                if nx == n-1 and ny == n-1 :
                    answer = min(answer, newcost)
                # 기존에 방문하지 않았거나 방문하였을때 보다 비용이 더 적을 경우에만 큐에 삽입
                elif not visit.get((nx, ny, d)) or visit.get((nx,ny,d)) > newcost :
                    visit[(nx,ny,d)] = newcost
                    queue.append((nx, ny, d, newcost))
        
        # print(visit)
    
    return answer

# https://hose0728.tistory.com/76

# from collections import deque

# def solution(board):
#     answer = 999999
#     q = deque()
#     q.append((0,0,4,0))
    
#     visited = {(0,0,1) : 0, (0,0,3) : 0}
    
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
    
#     while q :
#         x, y, d, c = q.popleft()
        
#         # 마지막에 도달 했을때 최솟값을 결과에 넣음
#         if x == len(board)-1 and y == len(board)-1 :
#             answer = min(answer, c)
        
#         for k in range(4) :
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0 :
#                 nc = c
#                 if d == 4 : # 맨처음엔 어느방향으로나 올 수 있으므로 직선도로 한다,
#                     nc += 100
#                 elif d <= 1 and k <= 1 : # 바라보는 방향과 진행방향이 세로
#                     nc += 100
#                 elif d >= 2 and k >= 2 : # 바라보는 방향과 진행방향이 가로
#                     nc += 100
#                 else : # 바라보는 방향과 진행 방향이 서로 다를 때(코너)
#                     nc += (500 + 100)
                
#                 # 방문한 적이 없거나, 방문한 적이 잇어도 기존 비용보다 지금 온 경로 비용(nc)가 적다면
#                 if not visited.get((nx,ny,k)) or visited[(nx,ny,k)] > nc :
#                     visited[(nx, ny, k)] = nc # 배열에 추가하거나, nc갱신
#                     q.append((nx, ny, k, nc)) # 다음 출발지를 q에 넣음
#     # print(answer)
#     return answer

board = [[0,0,0],[0,0,0],[0,0,0]]
solution(board)

# 참고 : https://deok2kim.tistory.com/92
        
    
   
