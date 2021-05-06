import sys
from collections import deque

# n X n 배열 
n = int(sys.stdin.readline())
board = []
queue = deque()

# 현위치에서의 좌,우,하,상 
dx = [-1,1,0,0] 
dy = [0,0,-1,1]
sec = 0 # 지난 횟수


# 제습기 넣음
for _ in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

# 0의 갯수를 센다
for i in range(n) :
    for j in range(n) :
        if board[i][j] == 0 :
            queue.append((i,j))

while queue :

		j = 0
		length = len(queue)
		# print(queue)

		# 해당 초에 대한 제습현황 탐색
		while j != length :
				x, y = queue.popleft()
				
				for i in range(4) :
						a = x + dx[i]
						b = y + dy[i]

						if 0 <= a < n and 0 <= b < n :
								# 만약 이미 제습했다면 다른 위치를 탐색한다
								if board[a][b] == 0:
										continue
								# 만약 제습기가 근처에 있다면, 해당 제습기는 제습을 끝내고 0이 된다
								if board[a][b] == 1 :
										board[a][b] = 0
										queue.append((a,b))
				j += 1

		# 만약, 해당 초에 모두 탐색했다면 그다음 초로 넘어간다
		if length == j :
				j = 0
				sec += 1

# 남은 제습제 확인
contain_one = False

for i in range(n) :
		if 1 in board[i] :
				contain_one = True
				break
# 만약 아직도 제습제가 남아있다면 -1 출력
if contain_one :
		print(-1)

# 완전 제습하였다면, 지난 날을 출력
else :
		print(sec-1)