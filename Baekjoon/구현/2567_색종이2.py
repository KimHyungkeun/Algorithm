# 210403
import sys

n = int(sys.stdin.readline())

board = [[0] * 102 for _ in range(102)]

for _ in range(n) :
    x,y = map(int, sys.stdin.readline().split())

    for i in range(x, x+10) :
        for j in range(y, y+10) :
            board[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0

for i in range(1,101) :
    for j in range(1,101) :
        if board[i][j] != 0 :
            for k in range(4) :
                a = i + dx[k]
                b = j + dy[k]
                if 1 <= a <= 100 and 1 <= b <= 100 and board[a][b] == 0:
                    cnt += 1
                elif a < 1 or a > 100 or b < 1 or b > 100 :
                    cnt += 1

print(cnt)




# --------------------------------------------------------------------------------

# # 210330
# import sys

# # 색종이 갯수 n 입력, 도화지 100 X 100 준비
# n = int(sys.stdin.readline())

# # 102 X 102 인 이유는 기존 100X100 도화지의 둘레표현을 위해 가장자리를 한 번 더 뒤덮기 위함이다
# board = [ [0] * 102 for _ in range(102)] 

# for _ in range(n) :
#     a, b = map(int, sys.stdin.readline().split())
#     # a,b 좌표를 기준으로 10 X 10의 색종이를 붙인다
#     for i in range(b, b+10) :
#         for j in range(a, a+10) :
#             board[i][j] = 1

# # 현위치에서의 좌,우,하,상 
# dx = [-1,1,0,0] 
# dy = [0,0,-1,1]

# cnt = 0
# for i in range(1, 101) :
#     for j in range(1, 101) :
#         if board[i][j] == 1 :
#             for k in range(4) :
#                 a = i + dx[k]
#                 b = j + dy[k]
#                 # 도화지 내에서 1을 기준으로 상하좌우 중에 0이 있다면, 도형의 둘레를 표현할 수 있는 영역이다
#                 if 1 <= a <= 100 and 1 <= b <= 100 and board[a][b] == 0 :
#                     cnt += 1
#                 # 둘레표현을 나타내기 위해, 기존 100 X 100 사이즈 도화지 가장자리를 한번 더 덮는다
#                 elif a < 1 or a > 100 or b < 1 or b > 100 :
#                     cnt += 1
                
# print(cnt)

# 힌트참고 : https://parksuu.github.io/189-%EB%B0%B1%EC%A4%80-%EC%83%89%EC%A2%85%EC%9D%B4-2-(java)/

