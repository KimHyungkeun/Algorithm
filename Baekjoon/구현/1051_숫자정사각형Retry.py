import sys

n, m = map(int, sys.stdin.readline().split())

board = []
for _ in range(n) :
    arr = list(map(int, sys.stdin.readline().rstrip())) # n*m 직사각형 생성
    board.append(arr)


# 해당 직사각형내에서 유효한 정사각형 범위 limit를 지정한다
if n < m :
    limit = n
else :
    limit = m

# 적정 정사각형을 찾았을때의, 그 사각형의 변의 길이
maximum = 0
# limit = min(n, m)

for i in range(n) :
    for j in range(m) :
        for k in range(limit) :
            if i + k < n and j + k < m :
                # 만약 limit길이를 가진 정사각형을 찾게되면, maximum을 새로 갱신한다
                if board[i][j] == board[i][j+k] and board[i][j] == board[i+k][j] and board[i][j] == board[i+k][j+k] :
                    if maximum < k:
                        maximum = k

# 정사각형넓이 구함
print((maximum+1) ** 2)


# --------------------------------------------------------------------------------------------------------------------
# def _1051():
#     F = []
#     N, M = map(int, input().split(' '))

#     for i in range (N):
#         F.append(list(map(int, input())))

#     MAX = min(N, M)
#     max = 0

#     for i in range(N):
#         for j in range(M):
#             for k in range(MAX):
#                 if i + k < N and j + k < M:
#                     if F[i][j] == F[i][j+k] and F[i][j] == F[i+k][j] and F[i][j] == F[i+k][j+k] :
#                         if max < k:
#                             max = k

#     print((max+1)*(max+1))


# _1051()
# https://has3ong.tistory.com/569