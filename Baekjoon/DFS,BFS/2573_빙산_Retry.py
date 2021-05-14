# 210331 답 참고, pypy3으로 작성
import sys
from collections import deque

def bfs(i,j,visited) :
    que = deque([[i,j]])
    melting_que = deque() # 빙하가 녹는 위치와 녹는 정도를 저장하는 큐
    visited[i][j] = 1
    while que :
        i,j = que.popleft()
        melt_cnt = 0
        for k in range(4) :
            a = i + dx[k]
            b = j + dy[k]
            if 0 <= a < n and 0 <= b <= m and visited[a][b] == 0:
            # 빙산의 높이가 있고 방문을 안했을 경우 que에 값 넣어주기
                if iceberg[a][b] != 0:
                    visited[a][b] = 1  # 방문 체크
                    que.append([a,b])
            # 사방향 탐색 시 0이 발견될때 마다 melt_cnt 증가
                else :
                    melt_cnt += 1
        if melt_cnt :
            melting_que.append([i,j,melt_cnt])

    return melting_que


year = 0 # 몇 년이 지났는지 판단하는 변수
n, m = map(int,sys.stdin.readline().split())

iceberg = []
for _ in range(n) :
    tmp = list(map(int, sys.stdin.readline().split()))
    iceberg.append(tmp)

# direction = ((1,0),(-1,0),(0,-1),(0,1)) #동서남북
#반복문 종료 조건 -> 빙산의 갯수가 0이거나 2일 경우

# 현위치에서의 좌,우,하,상 
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

while True :
    cnt = 0 # 빙산의 갯수를 담는 cnt 변수
    visited = [[0] * m for _ in range(n)]  # bfs를 위한 탐색 확인 리스트
    for i in range(n) :
        for j in range(m) :
            if iceberg[i][j] != 0 and visited[i][j] == 0 : #빙하의 높이가 남아있고 방문하지 않을 경우
                cnt += 1 # 빙산의 갯수 추가
                melt = bfs(i,j,visited) # bfs 시작을 하고 각 좌표별로 녹는 정도 반환
                while melt :
                    a, b, h = melt.popleft()
                    iceberg[a][b] -= h
                    if iceberg[a][b] < 0 :
                        iceberg[a][b] = 0

    if cnt == 0 :
        year = 0
        break
    if cnt >= 2 :
        break
    year += 1  # 일 년 증가
    # 빙산의 갯수가 0이거나 2일 경우 반복문 종료
print(year)

# https://kangmin1012.tistory.com/7


# 시간초과
# import sys
# sys.setrecursionlimit(100000)

# n, m = map(int, sys.stdin.readline().split())

# def dfs(x, y) :
#     # 주어진 범위를 벗어나는 경우에는 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= n :
#         return False
#     # 현재 노드를 방문하지 않았다면
#     if graph[x][y] == 1 :
#         # 방문 처리
#         graph[x][y] = 0
 
#         # 상하좌우 모두 재귀로 호출
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         dfs(x, y-1)
#         return True
    
#     else :
#         return False

# iceberg = []
# for _ in range(n) :
#     tmp = list(map(int, sys.stdin.readline().split()))
#     iceberg.append(tmp)

# # 현위치에서의 좌,우,하,상 
# dx = [-1,1,0,0] 
# dy = [0,0,-1,1]
# year = 0

# while True :
#     graph = []
#     for i in range(n) :
#         tmp = []
#         for j in range(m) :
#             if iceberg[i][j] >= 1 :
#                 tmp.append(1)
#             else :
#                 tmp.append(0)
#         graph.append(tmp)

#     # print(graph)
#     result = 0
#     for i in range(n) :
#         for j in range(m) :
#             if dfs(i, j) :
#                 result += 1
    
#     print(result)
#     # print(iceberg)
#     # for i in range(n) :
#     #     print(iceberg[i])
    
#     # print("-------------------------")


#     if result >= 2 :
#         print(year)
#         break
    
#     if result == 0 :
#         print(0)
#         break

#     year += 1

#     gone = [[0]*m for _ in range(n)]
#     for i in range(n) :
#         for j in range(m) :
#             if iceberg[i][j] != 0 :
#                 cnt = 0
#                 for k in range(4) :
#                     a = i + dx[k]
#                     b = j + dy[k]
#                     if 0 <= a < n and 0 <= b < m and iceberg[a][b] == 0:
#                         cnt += 1
#                 gone[i][j] = cnt

#     # print(gone)
#     for i in range(n) :
#         for j in range(m) :
#             iceberg[i][j] -= gone[i][j]
#             if iceberg[i][j] <= 0 :
#                 iceberg[i][j] = 0

# -----------------------------------------------------------------------------
