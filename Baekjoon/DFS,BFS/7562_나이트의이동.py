import sys
from collections import deque
import time

t = int(sys.stdin.readline())

# 나이트가 이동할 수 있는 모든 경우의 수
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

for _ in range(t) :
    
    board = []
    l = int(sys.stdin.readline()) # lxl 짜리 보드판을 생성
    start_x, start_y = map(int, sys.stdin.readline().split()) # 시작지점 지정
    end_x, end_y = map(int, sys.stdin.readline().split()) # 끝지점 지정

    for i in range(l) :
        sub_board = []
        for j in range(l) :
            if i == start_x and j == start_y : # 시작하려는 위치만 1로 설정하고
                sub_board.append(1)
            else :
                sub_board.append(0) # 탐색 이전의 위치는 모두 0으로 초기화한다
        board.append(sub_board)
        

    # start_time = time.time()
    cnt = 0 # 지나간 최소 횟수를 저장하기위한 변수

    # 만약 시작지점과 끝지점이 같다면, 탐색할 필요가 없으므로 바로 0으로 출력
    if start_x == end_x and start_y == end_y :
        print(cnt)
        continue

    else :
        queue = deque()
        queue.append([start_x, start_y]) # 대기열에 시작지점 좌표를 입력
        length = len(queue)
        size = 0

        while queue :
            a, b = queue.popleft()
            size += 1

            # 시작지점을 기준으로 나이트가 갈 수 있는 모든 경우의 수를 전부 구한다
            for i in range(8) :
                x = a + dx[i]
                y = b + dy[i]

                if 0 <= x < l and 0 <= y < l and (board[x][y] == 0):
                    if end_x == x and end_y == y : # 만약 끝지점에 도달했다면 루프문에서 탈출한다
                        break

                    else :
                        board[x][y] = 1 # 탐색한 지점은 모두 1로 표기한다
                        queue.append([x,y])

            # 끝 지점에 도달하면, 지나간 최소 횟수를 출력한다
            if end_x == x and end_y == y : 
                print(cnt+1) 
                # print("elapsed_time : ", time.time() - start_time)
                break
            
            # 대기열에 놓인 모든 경우의 수에 대해 다 비교해보고 나면, 그다음 비교할 좌표들에 대한 큐를 준비한다
            if size == length :
                cnt += 1
                length = len(queue)
                size = 0