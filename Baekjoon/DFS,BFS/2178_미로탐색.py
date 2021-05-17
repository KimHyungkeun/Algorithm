# 210517 재풀이
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

maze = []
for _ in range(n) :
    arr = list(map(int, sys.stdin.readline().rstrip()))
    maze.append(arr)

queue = deque()
queue.append((0,0))

cnt = 0
flag = False
while queue :
    # print(queue)
    pos = queue.popleft()
    
    for d in range(4) :
            px = pos[0] + dx[d]
            py = pos[1] + dy[d]

            if px <= -1 or px >= n or py <= -1 or py >= m :
                continue
            
            if maze[px][py] == 1 :
                # print((px,py))     
                maze[px][py] = maze[pos[0]][pos[1]] + 1                   
                queue.append((px, py))
                   

                # cnt += 1
    if flag :
        break

print(maze[n-1][m-1])

# def bfs(x, y) :
#     global cnt
#     queue = deque()
#     # 큐에 탐색하려하는 곳의 좌표를 입력
#     queue.append((x,y))

#     while queue :
#         x, y = queue.popleft()
#         # 현 위치에서 4가지 방향으로의 위치확인
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # 미로 공간 벗어날 시는 무시
#             if nx <= -1 or nx >= n or ny <= -1 or ny >= m :
#                 continue
            
#             # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
#             if graph[nx][ny] == 1 :
#                 cnt += 1
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     #가장 오른쪽 아래까지의 최단거리 반환
#     return graph[n-1][m-1]

# # N,M을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, input().split())
# cnt = 0

# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n) :
#     graph.append(list(map(int, input())))

# # 이동할 네 가지 방향 정의 (좌, 우, 하 ,상)
# dx = [-1, 1, 0 ,0]
# dy = [0, 0 ,-1 ,1] 

# # BFS를 수행한 결과 출력
# print(bfs(0,0))