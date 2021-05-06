from collections import deque

def solution(maps):
    
    def bfs(x, y) :
        queue = deque()
        queue.append((x,y))

        while queue :
            x, y = queue.popleft()
            # 현 위치에서 4가지 방향으로의 위치확인
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]

                # 미로 공간 벗어날 시는 무시
                if nx < 0 or nx >= n or ny < 0 or ny >= m :
                    continue

                # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
                if graph[nx][ny] == 1 :
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
        #가장 오른쪽 아래까지의 최단거리 반환
        return graph[-1][-1]
    
    # 이동할 네 가지 방향 정의 (상,하,좌,우)
    dx = [-1, 1, 0 ,0]
    dy = [0, 0 ,-1 ,1] 
    
    graph = maps
    n = len(maps) # map 행렬의 행 갯수
    m = len(maps[0]) # map 행렬의 열 갯수

    # BFS를 수행한 결과 출력
    result = bfs(0,0) 

    # 지나간 자리마다 1씩 증가하게되므로 만약 아예 가지 못하는 곳이라면 1로 남아있을 수 밖에 없다 
    if result == 1 : 
        answer = -1
    
    # 지나갈때 마다 1씩증가해서 최종적으로 맵 끝에 다다르면, 총 지나온 발자국 수를 센다
    else :
        answer = result
    
    return answer