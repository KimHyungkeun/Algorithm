import sys
sys.setrecursionlimit(100000)

def dfs(x, y) :
    global n
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n :
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

# n을 입력
n = int(sys.stdin.readline())

# 2차원 리스트의 맵 정보 입력 받기
max_h = 0
territory = []
for i in range(n) :
    tmp = list(map(int, sys.stdin.readline().split()))
    if max(tmp) > max_h :
        max_h = max(tmp)
    territory.append(tmp)


# 높이별 최대 안전영역을 담을 리스트
ans = []
for k in range(1, max_h+1) :
    # print(territory)
    graph = []
    # print(k)
    for i in range(n) :
        tmp = []
        for j in range(n) :
            if territory[i][j] >= k :
                tmp.append(1)
            else :
                tmp.append(0)
        graph.append(tmp)

    # 물에 잠기지 않은 영역을 발견한 경우 그 갯수를 센다
    result = 0
    for i in range(n) :
        for j in range(n) :
            if dfs(i, j) :
                result += 1


    # 총 찾은 영역의 수를 출력
    ans.append(result)

# print(ans)
print(max(ans))
