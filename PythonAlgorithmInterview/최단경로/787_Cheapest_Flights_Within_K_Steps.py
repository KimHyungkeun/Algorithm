from collections import defaultdict
import heapq
# 책 정답 (타임아웃 발생)
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        # 그래프 인접 리스트 구성
        for u,v,w in flights :
            graph[u].append((v,w))

        # 큐 변수 : [(가격, 정점, 남은 가능 경유지 수)]
        q = [(0,src,K)]

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while q :
            price, node, k = heapq.heappop(q)
            if node == dst :
                return price
            if k >= 0 :
                for v, w in graph[node] :
                    alt = price + w
                    heapq.heappush(q, (alt, v, k - 1))

        return -1