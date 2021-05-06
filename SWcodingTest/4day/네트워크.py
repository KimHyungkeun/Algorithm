from collections import deque
def solution(n, computers):
    
    network = {}

    for i in range(len(computers)) :
        for j in range(len(computers[i])) :
            if i == j : # 만약 본인과 같은 컴퓨터일때
                if i not in network : # 네트워크 테이블에 없다면 새로 표기만 한다
                    network[i] = []
                else :
                    continue
            if computers[i][j] == 1 : # 1이라면 그컴퓨터와의 연결을 시도한다
                if i not in network :
                    network[i] = [j]
                else :
                    network[i].append(j)
            else : # 만약 연결되지 않았다해도 네트워크 테이블에는 없다면 추가 한다
                if i not in network :
                    network[i] = []


    for key,val in network.items() : 
        network[key].sort() # bfs를 위해 오름차순 정렬한다
        
    # print(network)
    def bfs(graph, start, visited) :
        # 큐 구현을 위해 deque 사용
        queue = deque([start])
        # 현재 노드를 방문 처리
        visited[start] = True
        # 큐가 빌 때까지 반복
        while queue :
            # 큐에서 하나의 원소를 뽑아 출력
            v = queue.popleft()
            # print(v, end = ' ')
            # 아직 방문하지 않은 인접 원소들을 큐에 삽입
            for i in graph[v] :
                if not visited[i] :
                    queue.append(i)
                    visited[i] = True
    
    visited = [False] * n # 한번방문할때마다 bfs를 통해 네트워크 연결상태를 확인한다
    answer = 0
    for i in range(n) :
        if not visited[i] :
            bfs(network, i, visited)
            answer += 1 # 연결상태 확인마다 네트워크 갯수가 증가한다 

    
    print(answer)
    return answer

n = 3
# computers = [[1]]
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
solution(n, computers)