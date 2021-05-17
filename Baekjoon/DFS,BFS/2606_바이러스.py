# 210517 바이러스
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

if n == 1 :
    print(0)

else :
    graph = {i:[] for i in range(1, n+1)}
    visited = [False] * (n+1)

    for _ in range(m) :
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)

    def dfs (graph, v, visited) :
        visited[v] = True
        for g in graph[v] :
            if not visited[g] :
                dfs(graph, g, visited)


    dfs(graph, 1, visited)
    result = visited[1:].count(True) - 1
    print(result)






























# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

# # 그래프 설정
# graph = {}
# # 각 정점별 연결 상태를 모음
# collect_state = []

# # 주어진 조건에 따라 그래프를 생성
# for _ in range(m) :
#     # 연결된 컴퓨터 쌍
#     n1, n2 = map(int, sys.stdin.readline().split())
#     collect_state.append([n1,n2])

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


# def bfs (graph, start, infected) :
#     # 큐에 시작정점을 넣는다
#     queue = deque([start])
#     # 감염된 컴퓨터를 집어넣는다
#     infected.append(start)

#     while queue :
#         # 큐에서 감염된 컴퓨터번호 v를 하나 선택한다
#         v = queue.popleft()
#         # v번째 컴퓨터와 연결된 다른 컴퓨터를 조사하여, 감염여부를 알아낸다.
#         for i in graph[v] :
#             if i not in infected :
#                 queue.append(i)
#                 infected.append(i)

# infected = []
# bfs(graph, 1, infected)
# print(len(infected)-1)
