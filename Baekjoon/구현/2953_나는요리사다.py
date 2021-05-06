import sys

# 각 선수들의 점수를 모아놓는 리스트
score_board = []

# 총 5명의 선수가 참여했으며, 각 선수별 점수를 모아 총합을 계산한다
for i in range(5) :
    score = list(map(int, sys.stdin.readline().split()))
    score_board.append((sum(score), i+1))

# 그 중, 점수가 가장 높은 사람을 선별한다
max_score = max(score_board)
# print(max_score)
print(max_score[1], max_score[0])

