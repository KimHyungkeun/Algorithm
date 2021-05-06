import sys

# 스테이지 수 n
n = int(sys.stdin.readline())
cnt = 0

# 레벨별 클리어 점수
score = []
for _ in range(n) :
    score.append(int(sys.stdin.readline()))

# 클리어 점수를 거꾸로 배치 한다
score.reverse()

# 레벨이 상승할수록 획득 점수가 증가하므로, 다음레벨의 획득 점수가 이전레벨의 점수보다 작은 경우가 생겨선 안된다. 
# 따라서, 점수 차감을 진행했을시의 최종결과는 score 리스트가 내림차순의 형태가 되어야하며, 그 과정중에 점수차감이 발생할때마다 cnt가 증가한다
for i in range(1, len(score)) :
    if score[i-1] <= score[i] and score[i-1] >= 0 and score[i] >= 0:
        while score[i-1] - score[i] != 1 :
            score[i] -= 1
            cnt += 1

print(cnt)