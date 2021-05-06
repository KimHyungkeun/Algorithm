import sys

# n X m의 얼음틀
n, m = map(int, sys.stdin.readline().split())

# 얼음 유무를 입력
ice = []
for _ in range (n) :
    row = list(map(int, sys.stdin.readline().rstrip()))
    ice.append(row)

# print(ice)

def dfs (i,j) :
    # 만약 해당 얼음이 틀 안에 존재하는 얼음이라면
    if 0 <= i < n and 0 <= j < m :
        # 해당 얼음을 중심으로 상하좌우를 모두 탐색한다. 이미 탐색을 마친 곳은 얼음틀과 같이 1로 표시한다
        if ice[i][j] == 0 :
            ice[i][j] = 1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            return True
        # 만약 더이상 아이스크림이 더 만들어질 수 없다면, 여기서 종료
        else :
            return False
    else :
        return False 

# 생길 수 있는 아이스크림의 갯수 판단
cnt = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i,j) :
            cnt += 1

print(cnt)

# ----------------------------------------------------------------------------------------
# 답안

# # N, M을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, input().split())

# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
# def dfs(x, y):
#     # 주어진 범위를 벗어나는 경우에는 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재 노드를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         # 해당 노드 방문 처리
#         graph[x][y] = 1
#         # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False

# # 모든 노드(위치)에 대하여 음료수 채우기
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 DFS 수행
#         if dfs(i, j) == True:
#             result += 1

# print(result) # 정답 출력

