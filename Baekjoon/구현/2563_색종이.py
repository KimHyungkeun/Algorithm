# 210330 풀이
import sys

# 색종이 갯수 n 입력, 도화지 100 X 100 준비
n = int(sys.stdin.readline())
board = [ [0] * 101 for _ in range(101)] 

cnt = 0
for _ in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    # a,b 좌표를 기준으로 10X10의 색종이를 붙인다
    for i in range(b, b+10) :
        for j in range(a, a+10) :
            # 처음 붙이는 곳만 1로 표시하고, 이미 1인곳은 따로 카운트 하지 않는다
            if board[i][j] == 0 :
                board[i][j] = 1
                cnt += 1

print(cnt)

# 주의
# [[0] * 5] * 5 : 주소값이 같은 [0,0,0,0,0] 5개가 반복 
# [[0] * 5 for _ in range(5)] : 기존 리스트에 [0,0,0,0,0]란 리스트가 새로 append 되는 것임
# 위 둘은 완전히 다름


# ----------------------------------------------------------------------------------------------------

# n = int(sys.stdin.readline()) # 색종이 갯수

# board = []
# for _ in range(101) : # 100 X 100 도화지 생성
#     row = [0] * 101
#     board.append(row)


# # print(board[:2])
# cnt = 0
# for _ in range(n) :
#     a, b = map(int, sys.stdin.readline().split()) # 색종이 부착의 시작지점을 구함
#     # 100의 넓이를 가진 정사각형 크기의 종이이므로, 시작지점으로부터 가로+10, 세로+10 지점까지의 부분을 모두 영역으로 지정한다
#     for i in range(b, b+10) : 
#         # print(board[i])
#         for j in range(a, a+10) :
#             if board[i][j] == 0 : 
#                 board[i][j] = 1
#                 cnt += 1 # 새로 부착하는 부분에 대해서만 count를 세며, 이미 언급된 영역은 중복 카운트하지 않는다.
                
                
# print(cnt)

