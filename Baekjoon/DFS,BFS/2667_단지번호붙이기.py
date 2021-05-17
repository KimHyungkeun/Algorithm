# 210517 재풀이
import sys
from collections import deque

def bfs(board,i,j,visited) :

    global n
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    cnt = 1

    queue = deque()
    queue.append((i,j))
    
    # if board[i][j] == '1' :
    #     cnt += 1

    while queue :
        x,y = queue.popleft()
        
        for d in range(4) :
            px = x + dx[d]
            py = y + dy[d]
            if px < 0 or px >= n or py < 0 or py >= n :
                continue
            if board[px][py] == '1' and (px, py) not in visited :
                visited.append((px, py))
                queue.append((px, py))
                cnt += 1

    return cnt



n = int(sys.stdin.readline())

visited = []
answer = []
board = []
for _ in range(n) :
    arr = sys.stdin.readline().rstrip()
    board.append(arr)

# bfs(board,0,1,visited)
for i in range(n) :
    for j in range(n) :
        if (i,j) not in visited :
            visited.append((i, j))
            if board[i][j] == '1' :
                result = bfs(board,i,j,visited)
                if result >= 1 :
                    answer.append(result)

answer.sort()
print(len(answer))
for n in answer :
    print(n)


# def dfs(x, y) :
#     global count
#     # 주어진 범위를 벗어나는 경우에는 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= n :
#         return False
#     # 현재 노드를 방문하지 않았다면
#     if graph[x][y] == 1 :
#         # 방문 처리
#         graph[x][y] = 0
#         count += 1
#         # 상하좌우 모두 재귀로 호출
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         dfs(x, y-1)
#         return True
    
#     else :
#         return False

# # n, m을 공백을 기준으로 구분하여 입력
# n = int(sys.stdin.readline())

# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n) :
#     graph.append(list(map(int, input())))

# # 번지수
# home_num = []
# # 모든 위치에 대하여 음료수 채우기
# result = 0
# for i in range(n) :
#     count = 0
#     for j in range(n) :
#         if dfs(i, j) == True :
#             result += 1
#             home_num.append(count)
#             count = 0

# # 총 찾은 번지의 수를 출력
# print(result)
# # 번지수를 오름차순 정렬
# home_num.sort()
# # 각 단지별 번지의 총 갯수를 출력
# for i in range(len(home_num)) :
#     print(home_num[i])