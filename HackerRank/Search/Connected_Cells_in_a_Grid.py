# Complete the connectedCell function below.
def connectedCell(matrix):
    
    def dfs(x, y) :
        nonlocal cnt
        # 주어진 범위를 벗어나는 경우에는 즉시 종료
        if x <= -1 or x >= n or y <= -1 or y >= m :
            return False
        # 현재 노드를 방문하지 않았다면
        if matrix[x][y] == 1 :
            # 방문 처리
            matrix[x][y] = 0
            cnt += 1
            # 상하좌우, 대각선 모두 재귀로 호출
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            dfs(x-1, y-1)
            dfs(x-1, y+1)
            dfs(x+1, y+1)
            dfs(x+1, y-1)
            return True
        
        else :
            return False

    
    # 아래 n,m은 해커랭크 사이트에서는 따로 지정되어 있으나, 여기는 오로지 솔루션 함수만 다루므로 따로 변수 설정
    maximum = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(len(matrix)) :
        cnt = 0 # 탐색한 영역에 따라 cnt값이 증가함
        for j in range(len(matrix[i])) :        
            if dfs(i, j) :
                if cnt > maximum : # 최대영역을 찾을때마다 값을 갱신한다
                    maximum = cnt
            cnt = 0

    # 정답 출력
    # print(maximum)
    return maximum