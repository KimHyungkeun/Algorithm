import heapq
from collections import defaultdict
def networkDelayTime(times, n: int, k: int) -> int:
        INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

        # 시작 노드 번호를 입력받기
        start = k

        # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
        graph = [[] for i in range(n + 1)]

        # 최단 거리 테이블을 모두 무한으로 초기화
        distance = [INF] * (n + 1)

        # 모든 간선정보를 입력받기
        for t in times :
            a, b, c = t[0], t[1], t[2]
            # a번 노드에서 b번 노드로 가는 비용이 c
            graph[a].append((b,c))



        def dijkstra(start) :
            q = []
            # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
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

        result = []
        # 모든 노드로 가기 위한 최단 거리를 출력
        for i in range(1, n+1) :
            # 도달 불가한 경우, 무한(INF)을 출력
            if distance[i] == INF :
                result.append(-1)
            else :
                result.append(distance[i])
        
        if -1 in result :
            return -1
        else :
            return max(result)

times = [[1,2,1]]
n = 2
k = 2
networkDelayTime(times, n, k)

# 책 정답
def networkDelayTime(times, n: int, k: int) -> int:
    graph = defaultdict(list)
    # 그래프 인접 리스트 구성
    for u,v,w in times :
        graph[u].append((v,w))
    
    # 큐 변수 : [(소요시간, 정점)]
    q = [(0,k)]
    dist = defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while q :
        time, node = heapq.heappop(q)
        if node not in dist :
            dist[node] = time
            for v, w in graph[node] :
                alt = time + w
                heapq.heappush(q, (alt, v))
    
    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == n :
        return max(dist.values())
    
    return -1