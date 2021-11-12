import sys
from collections import deque

# 아파트 구역은 n*n 으로되어있고, 집이 존재하는 곳은 '1'로 표기된다
n = int(sys.stdin.readline())
house = []
for _ in range(n) :
    row = list(sys.stdin.readline().rstrip())
    house.append(row)


def bfs(x,y,house, visited) :

    # 현재위치를 기준으로 상하좌우를 탐색
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    q = deque()
    q.append((x,y))
    visited.append((x,y))
    cnt = 1

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 해당 위치가 구역을 벗어나면 다른 곳을 탐지
            if nx < 0 or nx >= len(house) or ny < 0 or ny >= len(house) :
                continue
            
            # 해당 위치에 집이 있을 경우, 탐색 후보에 포함시킨다
            if house[nx][ny] == '1' and (nx, ny) not in visited :
                house[nx][ny] = '0'
                visited.append((nx, ny))
                q.append((nx, ny))
                cnt += 1
    
    # 연결된 총 단지의 갯수를 반환
    return cnt

visited = []
home_group = []

for i in range(n) :
    for j in range(n) :
        # 집이 존재하는 곳을 기준으로 상하좌우를 탐색하여 붙어있는 집을 검색
        if house[i][j] == '1' :
            val = bfs(i,j,house,visited)
            home_group.append(val)

home_group.sort()
print(len(home_group))
for h in home_group :
    print(h)
            

