# 210517 촌수계산
import sys

def dfs (graph, v, visited, end) :
    
    global cnt
    visited[v] = True
    if v == end :
        print(cnt)
        return 
    
    for g in graph[v] :
        if not visited[g] :
            cnt += 1
            dfs(graph, g, visited, end)
            cnt -= 1

n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = {i:[] for i in range(1, n+1)}
visited = [False] * (n+1)
cnt = 0
for _ in range(m) :
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)


dfs(graph, start, visited, end)

if visited[start] and not visited[end] :
    print(-1)




























# def dfs(graph, v, visitied) :
#     global cnt, b, flag
    
#     # 현재 노드를 방문 처리
#     visited[v] = True
#     cnt += 1
#     # 만약 v가 찾으려는 인원에 부합한다면 flag를 참값으로 바꾸고 촌수를 출력한다
#     if v == b :
#         flag = True
#         print(cnt)
#         return None
#     # print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v] :
#         if not visited[i] :
#             dfs(graph, i, visited)
#             cnt -= 1
    
# # 총 n명의 인원, a와 b간의 촌수 관계, 촌수관계를 이은 그래프
# n = int(sys.stdin.readline())
# a, b = map(int, sys.stdin.readline().split())
# m = int(sys.stdin.readline())

# # 촌수관계를 이은 그래프를 설정
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
# cnt = -1
# flag = False

# # print(graph)
# # 정의된 DFS 함수 호출
# dfs(graph,a,visited)

# # 만약 a,b가 서로 연관된 친척도 아니라면 -1을 출력
# if not flag :
#     print(-1)
    