import sys
from collections import deque

graph = {}

# 동기수 n, 리스트 길이 m
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
visited = [False] * (n+1) # 총 인원은 본인1번부터 지인 2~n번까지이다. 
friends = [] # 친구와 친구의 친구까지 모두 포함할 리스트

for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    # a와 b는 서로 친구 관계이므로 a->b 관계와 b->a 관계가 모두 생성되어야 함
    if a not in graph : # a에 대한 그래프가 없으면 생성
        graph[a] = [b]
    else :
        graph[a].append(b)
    
    if b not in graph : # b에 대한 그래프가 없으면 생성
        graph[b] = [a]
    else :
        graph[b].append(a)

# print(graph)
# 각 노드가 방문된 정보를 표현

def bfs(graph, start, visited) :
    # 큐 구현을 위해 deque 사용
    queue = deque(graph[start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue :
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        if not visited[v] :
            friends.append(v) 
            visited[v] = True
            # print(v, end = ' ')
        # 아직 방문하지 않은 인접 원소들을 큐에 삽입
        for i in graph[v] :
            if not visited[i] :
                friends.append(i)
                visited[i] = True

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
# print(friends)
print(len(friends))

