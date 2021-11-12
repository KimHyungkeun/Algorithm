import sys
from collections import deque

# 깊이 우선 탐색
def dfs(graph, start, visited) :
    visited[start-1] = True
    print(start, end = ' ')
    if False not in visited :
        return

    for g in graph[start] :
        if not visited[g-1] :
            dfs(graph, g, visited)

# 너비 우선 탐색
def bfs(graph, start, visited) :
    q = deque()
    q.append(start)
    visited[start-1] = True

    while q :
        val = q.popleft()
        print(val, end=' ')
        for g in graph[val] :
            if not visited[g-1] :
                visited[g-1] = True
                q.append(g)




n,m,v = map(int, sys.stdin.readline().split())

graph = {i:[] for i in range(1,n+1)}
for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for key in graph.keys() :
    graph[key].sort()

visited = [False] * n
dfs(graph, v, visited)
print()
visited = [False] * n
bfs(graph, v, visited)




