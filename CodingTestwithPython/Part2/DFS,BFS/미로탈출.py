import sys
from collections import deque

# n * m 배열
n, m = map(int, sys.stdin.readline().split())

maze = []
for _ in range (n) :
    row = list(map(int, sys.stdin.readline().rstrip()))
    maze.append(row)

# 우, 좌, 하, 상의 위치
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs (x, y) :

    queue = deque()
    queue.append((x,y))

    while queue : 
        x, y = queue.popleft()
        # 현 좌표를 기준으로 4방향을 탐색 
        for i in range(4) :
            a = x + dx[i]
            b = y + dy[i]
            
            # 해당 좌표가 미로 내에 있을때
            if 0 <= a < n and 0 <= b < m :
                
                # 벽이면 무시한다
                if maze[a][b] == 0 :
                    continue
                
                # 길이라면, 해당 길이 시작부터 몇번째 인지 센다
                if maze[a][b] == 1 :
                    maze[a][b] = maze[x][y] + 1
                    queue.append((a,b))
                    
    # 끝지점이 n,m 이므로 그 지점까지 걸린 발자국 수를 센다
    return maze[n-1][m-1]

result = bfs(0,0)
# print(maze)
print(result)

# -----------------------------------------------------------------------------

# from collections import deque

# # N, M을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, input().split())
# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # BFS 소스코드 구현
# def bfs(x, y):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque()
#     queue.append((x, y))
#     # 큐가 빌 때까지 반복하기
#     while queue:
#         x, y = queue.popleft()
#         # 현재 위치에서 4가지 방향으로의 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 미로 찾기 공간을 벗어난 경우 무시
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             # 벽인 경우 무시
#             if graph[nx][ny] == 0:
#                 continue
#             # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     # 가장 오른쪽 아래까지의 최단 거리 반환
#     return graph[n - 1][m - 1]

# # BFS를 수행한 결과 출력
# print(bfs(0, 0))


