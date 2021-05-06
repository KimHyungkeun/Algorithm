import heapq

def solution(n, edge):
    INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

    # 시작 노드 번호를 입력받기
    start = 1
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [[] for i in range(n + 1)]
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)
    
    # 모든 간선정보를 입력받기
    for e in edge :      
        # e[0]번 노드에서 e[1]번 노드로 가는 비용이 1, 양방향 노드이므로 양방향 설정
        graph[e[0]].append((e[1],1))
        graph[e[1]].append((e[0],1))

    # print(graph)
    def dijkstra(start) :
        q = []
        # 시작 노드에 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q : # 큐가 비어있지 않다면
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist :
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now] :
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧을 경우
                if cost < distance[i[0]] :
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    # 다익스트라 알고리즘 수행
    dijkstra(start)

    maximum = max(distance[1:])
    answer = 0
    for d in distance :
        if d == maximum :
            answer += 1

    print(answer)
    return answer

n = 6 
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
solution(n, edge)