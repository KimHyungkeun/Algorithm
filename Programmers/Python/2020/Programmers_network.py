def solution(n, computers):
    answer = 0
    
    # 그래프 설정
    graph = {}
    # 각 정점별 연결 상태를 모음
    network_state = [False] * n
    
    # 컴퓨터별 연결 상태 그래프를 만듦
    for i in range(n) : 
        graph[i] = []
    
    # 해당번호에 1이 되어있으면, 그 번호의 컴퓨터와 연결되어 있다는 뜻이다.
    for i in range(n) :
        for j in range(n) :
            if i == j :
                continue
            if computers[i][j] == 1 :
                graph[i].append(j)
    # print(graph)
    
    def dfs(graph, v, visited) :
        # 현재 노드를 방문 처리
        visited.append(v)
        # print(v, end=' ')
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v] :
            if i not in visited :
                network_state[i] = True
                dfs(graph, i, visited)
    
    # 네트워크 연결 수
    cnt = 0
    
    for i in range(n) : 
        visited = []
        # 만약 하나도 연결되지 않았던 컴퓨터라면, 해당 컴퓨터부터 세어서 네트워크 연결상태를 검사한다.
        if not network_state[i] :
            dfs(graph, i, visited)
            cnt += 1
    
    answer = cnt
    return answer