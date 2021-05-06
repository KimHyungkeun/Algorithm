import sys
sys.setrecursionlimit(10000)

def dfs(x, y) :
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 1 :
        # 방문 처리
        graph[x][y] = 0
     
        # 상하좌우 모두 재귀로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    
    else :
        return False

# 테스트 케이스 t개 
t = int(sys.stdin.readline())

for k in range(t) :
    n, m, k = map(int, sys.stdin.readline().split())

    # 2차원 리스트의 맵 정보 입력 받기
    graph = []
    # 맨 처음 모두 배추가 심어지지 않은 땅을 0으로 채워넣는다
    for i in range(n) :
        sub_graph = []
        for j in range(m) :
            sub_graph.append(0)
        graph.append(sub_graph)
    
    # 배추가 심어진 곳은 1로 채워 넣는다
    for i in range(k) :
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1


    # 모든 위치에 대하여 배추흰지렁이가 최소 있을 곳
    result = 0
    for i in range(n) :
        for j in range(m) :
            if dfs(i, j) == True :
                result += 1
    

    # 최소 필요한 배추 흰지렁이 수
    print(result)
