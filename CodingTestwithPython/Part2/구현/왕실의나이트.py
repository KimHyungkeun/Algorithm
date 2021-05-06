import sys

pos = list(sys.stdin.readline().rstrip())
print(pos)

# 가로행을 임의로 1~8까지로 매핑시킨다
col_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

# 나이트가 갈 수 있는 총 경우의 수
dx = [-2,-1,1,2,-2,-1,1,2]
dy = [-1,-2,-2,-1,1,2,2,1]

# a1의 경우 => [1,1]과 같은 좌표로 매핑된다
start = [col_dict[pos[0]], int(pos[1])]
# print(start)

cnt = 0
for i in range(8) :
    # 보드판 내에서 나이트가 갈 수 있는 모든 범위를 구함
    x = start[0] + dx[i]
    y = start[1] + dy[i]

    if 1 <= x <= 8 and 1 <= y <= 8 :
        cnt += 1

print(cnt)


# ------------------------------------------------------------------------------------
# 답안

# # 현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1

# print(result)