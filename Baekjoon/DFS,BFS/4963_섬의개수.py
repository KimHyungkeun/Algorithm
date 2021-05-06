import sys
sys.setrecursionlimit(10000)

def dfs(x, y) :

    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= w or y <= -1 or y >= h :
        return False
    # 현재 노드를 방문하지 않았다면
    if board[y][x] == 1 :
        # 방문 처리
        board[y][x] = 0

        # 상하좌우,대각선 모두 재귀로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1,y+1)
        dfs(x+1,y-1)
        dfs(x-1,y-1)
        dfs(x-1,y+1)
        return True
    
    else :
        return False

while True :
    # w, h을 공백을 기준으로 구분하여 입력
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0 :
        break

    # 2차원 리스트의 맵 정보 입력 받기
    board = []
    for i in range(h) :
        board.append(list(map(int, sys.stdin.readline().split())))


    result = 0
    for i in range(h) :
        # count = 0
        for j in range(w) :
            if dfs(j, i) == True :
                result += 1


    # 총 찾은 섬의 수를 출력
    print(result)