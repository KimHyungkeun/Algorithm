import sys
from collections import defaultdict

n, m, k, x = map(int, sys.stdin.readline().split())

visited = [0] * (n+1) # 도시 1번부터 시작한다
answer = []
depth = 0

graph = defaultdict(list)
for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    if end not in graph :
        graph[end] = []

# print(graph)

def dfs(graph, v, visited) :
    global depth
    # 현재 노드를 방문 처리

    if visited[v] != 0 :
        visited[v] = min(visited[v], depth)
    
    else :
        visited[v] = depth
    
    if depth == k :
        return None
    # print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v] :
        depth += 1
        # if visited[i] == 0:
        dfs(graph, i, visited)
        depth -= 1

dfs(graph, x, visited)

if k not in visited :
    print(-1)

else :
    for i in range(len(visited)) :    
        if visited[i] == k :
            print(i)
