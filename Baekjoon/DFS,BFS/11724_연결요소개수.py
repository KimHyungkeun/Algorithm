import sys
sys.setrecursionlimit(10000)

def dfs(graph, v, visitied) :
    # 현재 노드를 방문 처리
    visited[v] = True

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)


n, m = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1,n+1)}

for _ in range(m) :
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 각 노드가 방문된 정보를 표현
visited = [False] * (n+1)

cnt = 0
# 방문하지 않은 노드가 존재할때, 해당 노드를 시작으로 별개 연결요소가 존재한다는 뜻이다
for i in range(1, n+1) :
    if not visited[i] :
        dfs(graph,i,visited) 
        cnt += 1

print(cnt)


























# ----------------------------------------------------------------------------------------------------------------------------
# def dfs(graph, v, visited) :
    
#     # 현재 노드를 방문 처리
#     visited[v] = True

#     # print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v] :
#         if not visited[i] :
#             dfs(graph, i, visited)
    
# # 총 n개의 정점과, m개의 간선
# n, m = map(int, sys.stdin.readline().split())


# # 정점을 모두 이어서 셋팅
# graph = {}
# for _ in range(m) :
#     x, y = map(int, sys.stdin.readline().split())
#     if x not in graph :
#         graph[x] = [y]
#     else :
#         graph[x].append(y)
    
#     if y not in graph :
#         graph[y] = [x]
#     else :
#         graph[y].append(x)


# # 각 노드가 방문된 정보를 표현
# visited = [False] * (n+1)
# cnt = 0

# # print(graph)
# # 정의된 DFS 함수 호출
# for j in range(1, n+1) :
    
#     if not visited[j] :
#         if j not in graph :
#             cnt += 1
#         else :       
#             dfs(graph,j,visited)
#             cnt += 1
# print(cnt)