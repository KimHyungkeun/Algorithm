# 210517 풀이
# import sys
# from collections import deque

# def dfs(graph, v, visited) :
#     visited[v-1] = True
#     print(v, end=' ')
#     if False not in visited :
#         return 
#     for g in graph[v] :
#         if not visited[g-1] :
#             dfs(graph, g, visited) 

# def bfs(graph, v, visited) :
    
#     visited[v-1] = True
#     print(v, end=' ')
#     queue = deque(graph[v])
#     while queue :
#         val = queue.popleft()
#         if not visited[val-1] :
#              visited[val-1] = True
#              print(val, end=' ')

#         for g in graph[val] :
#             if not visited[g-1] :
#                 queue.append(g)

        
#         if False not in visited :
#             break


# n, m, v = map(int, sys.stdin.readline().split())

# graph = {i:[] for i in range(1, n+1)}
# for _ in range(m) :
#     start, end = map(int, sys.stdin.readline().split())
#     graph[start].append(end)
#     graph[end].append(start)

# for key in graph.keys() :
#     graph[key].sort()

# dfs_visited = [False] * n
# bfs_visited = [False] * n

# dfs(graph, v, dfs_visited)
# print()
# bfs(graph, v, bfs_visited)


# # 그래프 설정
# graph = {}
# # 각 정점별 연결 상태를 모음
# collect_state = []


# n, m, v = map(int, sys.stdin.readline().split())

# # 주어진 조건에 따라 그래프를 생성
# for _ in range(m) :
#     n1, n2 = map(int, sys.stdin.readline().split())
#     collect_state.append([n1,n2])

#     # 시작점이 어느것과도 연결되지 않더하더라도, 정점자체에 포함된다
#     if v not in graph :
#         graph[v] = []

#     # n1을 정점으로 하는 그래프 및 연관된 그래프
#     if n1 not in graph :
#         graph[n1] = [n2]
    
#     else :
#         graph[n1].append(n2)
    
#     # n2을 정점으로 하는 그래프 및 연관된 그래프
#     if n2 not in graph :
#         graph[n2] = [n1]
    
#     else :
#         graph[n2].append(n1)

# # 차례대로 정점을 방문하므로, 각 연결된 정점들의 순서를 오름차순 정렬 시킨다
# for key, val in graph.items() :
#     graph[key].sort()

# # print(graph)

# # DFS 풀이
# def dfs(graph, v, visited) :
#     # 현재 노드를 방문 처리
#     visited.append(v)
#     print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v] :
#         if i not in visited :
#             dfs(graph, i, visited)


# # BFS 풀이
# def bfs(graph, start, visited) :
#     # 큐 구현을 위해 deque 사용
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited.append(start)
#     # 큐가 빌 때까지 반복
#     while queue :
#         # 큐에서 하나의 원소를 뽑아 출력
#         v = queue.popleft()
#         print(v, end = ' ')
#         # 아직 방문하지 않은 인접 원소들을 큐에 삽입
#         for i in graph[v] :
#             if i not in visited :
#                 queue.append(i)
#                 visited.append(i)

# # 시작점이 다른 정점들과 연결되지 않은 독립적인 존재일때는 본인만 검색된다.
# visited = []
# dfs(graph, v, visited)
# print()
# visited = []
# bfs(graph, v, visited)

import sys
from collections import deque
n, m, k  = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1, n+1)}

for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for g in graph.keys() :
    graph[g].sort()

def dfs(graph, visited, v) :
    visited[v-1] = True
    print(v, end=' ')

    if False not in visited :
        return
    
    for i in graph[v] :
        if not visited[i-1] :
            dfs(graph, visited, i)  
    
        
visited = [False] * n
dfs(graph, visited, k)
print()

def bfs(graph, visited, k) :
    queue = deque()
    queue.append(k)
    print(k, end = ' ')
    visited[k-1] = True

    while queue :
        val = queue.popleft()
        for i in graph[val] :
            if not visited[i-1] :
                print(i, end = ' ')
                queue.append(i)
                visited[i-1] = True
        

visited = [False] * n
bfs(graph, visited, k)