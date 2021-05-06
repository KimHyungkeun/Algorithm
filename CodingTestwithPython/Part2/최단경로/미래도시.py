import sys

INF = int(1e9) # 무한을 의미하는 값으로 10억으로 설정
# cnt = 0

# 노드의 개수 및 간선의 개수 입력
n, m = map(int, sys.stdin.readline().split())



# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신의 비용은 0으로 초기화
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if a == b :
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m) :
    # A에서 B로 가는 비용은 C로 설정
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

# k번 회사를 거쳐 x번 회사로 가는 최소 이동시간
x, k = map(int, sys.stdin.readline().split())
# print("before k : ", k)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for t in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][t] + graph[t][b])

# print("after k : ", k)
distance = graph[1][k] + graph[k][x]


if distance >= INF :
    print(-1, end=' ')
# 도달 가능한 경우에는 거리를 출력
else :
    print(distance, end=' ')  
