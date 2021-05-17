# 210517 재풀이
import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

minus_one_cnt = 0
zero_cnt = 0
one_cnt = 0
board = []

visited = []
day = 0

for _ in range(n) :
    tomato = list(map(int, sys.stdin.readline().split()))
    board.append(tomato)

start = []
for i in range(len(board)) :
    for j in range(len(board[i])) :
        if board[i][j] == 1 :
            start.append((i,j))

q = deque(start)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

length = len(q)
while q :
    x, y = q.popleft()
    length -= 1

    for d in range(4) :
        px = x + dx[d]
        py = y + dy[d]
        if 0 <= px < n and 0 <= py < m :
            if board[px][py] == 0 :
                board[px][py] = 1
                q.append((px, py))
            

    if length == 0 :
        day += 1

        if not q :
            break

        length = len(q)
        # print(length, q, day)
        
            
    # for b in board :
    #     print(b)
    # print("--------------")


for tomato in board :
    minus_one_cnt += tomato.count(-1)
    zero_cnt += tomato.count(0)
    one_cnt += tomato.count(1)

if zero_cnt >= 1 :
    print(-1)

elif minus_one_cnt == m*n :
    print(-1)

else :
    print(day-1)



# # 가로 n, 세로 m의 토마토 틀
# n, m = map(int, sys.stdin.readline().split())
# board = []
# queue = deque()

# # 현위치에서의 좌,우,하,상 
# dx = [-1,1,0,0] 
# dy = [0,0,-1,1]
# day = 0 # 지난 횟수

# cnt_one = 0 # 1의 갯수(익은 토마토)
# cnt_m_one = 0 # -1의 갯수(빈칸)


# # 토마토 넣음
# for _ in range(m) :
#     row = list(map(int, sys.stdin.readline().split()))
#     board.append(row)

# # 1의 갯수와 -1의 갯수를 센다
# for i in range(m) :
#     for j in range(n) :
#         if board[i][j] == 1 :
#             cnt_one += 1
#             queue.append((i,j))
#         elif board[i][j] == -1 :
#             cnt_m_one += 1

# # 만약, 처음부터 빈칸을 제외하고 익은토마토만이 존재한다면 0을 출력
# if cnt_one + cnt_m_one == m * n :
#     print(0)

# else :
#     while queue :

#         j = 0
#         length = len(queue)
#         # print(queue)

#         # 해당날의 익은 토마토를 탐색하는 프로그램
#         while j != length :
#             x, y = queue.popleft()
#             for i in range(4) :
#                 a = x + dx[i]
#                 b = y + dy[i]

#                 if 0 <= a < m and 0 <= b < n :
#                     # 만약 이미 익은 토마토라면 다른 위치를 탐색한다
#                     if board[a][b] == -1 or board[a][b] == 1:
#                         continue
#                     # 만약 이번에 새로 익을 토마토라면, 위치를 저장하고 다음 비교를 위해 새 위치도 저장한다
#                     if board[a][b] == 0 :
#                         board[a][b] = 1
#                         queue.append((a,b))
#             j += 1
        
#         # 만약, 당일날의 토마토 익음 유무를 모두 탐색했다면 그 다음날로 넘어간다
#         if length == j :
#             j = 0
#             day += 1
    
#     # 익지 않은 토마토 진위 여부
#     contain_zero = False

#     for i in range(m) :
#         if 0 in board[i] :
#             contain_zero = True
#             break
#     # 만약, 여전히 익지 않은 토마토가 존재한다면 -1을 출력한다
#     if contain_zero or cnt_m_one == m * n :
#         print(-1)
    
#     # 모두 다 익었다면 지난 날을 출력
#     else :
#         print(day-1)
            
        
# --------------------------------------------------------------------------------------------------------------------
# import sys
# from collections import deque

# # 이동할 네 가지 방향 정의 (좌, 우, 하 ,상)
# dx = [-1, 1, 0 ,0]
# dy = [0, 0 ,-1 ,1] 
# queue = deque()

# # N,M을 공백을 기준으로 구분하여 입력 받기
# m, n = map(int, sys.stdin.readline().split())

# box = [] # 토마토가 담긴 박스
# day = 0 # 지난 시간(일)

# count_1 = 0 # 1의 갯수(익은 토마토 갯수)
# count_m1 = 0 # -1의 갯수(비어있는 칸의 개수)

# # 2차원 리스트의 맵 정보 입력 받기
# for i in range(n) :
#     box.append(list(map(int, sys.stdin.readline().split())))

# for i in range(n) :
#     for j in range(m) :
#         if box[i][j] == 1 : # 익은 토마토 갯수를 센다
#             queue.append([i,j])
#             count_1 += 1 # 비어있는 칸 갯수를 센다
#         if box[i][j] == -1 :
#             count_m1 += 1


# def bfs() :
#     global day
#     length = len(queue) # 현재 대기중인 큐의 갯수를 구함
#     size = 0

#     while queue :
#         a, b = queue.popleft() # 해당 좌표에 있는 토마토에대해 검사한다
#         size += 1
#         for i in range(4) : # 상하좌우로 토마토 탐색
#             x = a + dx[i]
#             y = b + dy[i]

#             if 0 <= x < n and 0 <= y < m and box[x][y] == 0 :
#                     box[x][y] = 1 # 만약 박스 범위내에 있고, 익지 않은 토마토라면 익은 토마토로 바꾼다
#                     queue.append([x,y]) # 익은 토마토를 큐에 넣는다

#         # 만약 당일날의 토마토를 모두 검사했다면 하루가 지나고, 새로 탐색할 기준이 되는 토마토가 큐에 준비되어있다
#         if size == length : 
#             # print("OK")
#             day += 1
#             length = len(queue)
#             size = 0

# # 만약 처음부터 모두 익은 토마토만 존재한다면, 0을 출력한다
# if (count_1 + count_m1 == m*n) and (0 not in box) :
#     print(0)

# else :
#     # 날마다 토마토의 상태를 확인한다.
#     bfs()
#     contain_zero = False # 익지않은 토마토가 존재하는지 확인 여부

#     for i in box :
#         for j in i :
#             # 만약 해당 토마토 박스에 익지 않은것이 하나라도 있다면 루프문 탈출
#             if j == 0 :
#                 contain_zero = True
#                 break
#         if contain_zero :
#             break
    
#     # 익지않은 토마토가 하나라도 있다면 -1을 출력하고, 모두 익었다면 지난 일수를 출력한다.
#     if contain_zero :
#         print(-1)
#     else :
#         print(day-1)

#  -------------------------------------------------------------------------------------------------------------------
# def bfs():
#     while queue:
#         a, b = queue.popleft()
#         for i in range(4):
#             x = a + dx[i]
#             y = b + dy[i]
#             if 0 <= x < n and 0 <= y < m and s[x][y] == 0:
#                 s[x][y] = s[a][b] + 1
#                 queue.append([x, y])

# # 토마토가 익었다면 해당 좌표에 대해 기억한다
# for i in range(n) :
#     for j in range(m) :
#         if s[i][j] == 1:
#             queue.append([i,j])


# # BFS를 수행한 결과 출력
# bfs()
# isTrue = False
# result = -2
# for i in s :
#     for j in i :
#         if j == 0 :
#             isTrue = True
#         result = max(result, j)
# if isTrue :
#     print(-1)
# elif result == -1 :
#     print(0)
# else :
#     print(result-1)


#참고 : https://pacific-ocean.tistory.com/267