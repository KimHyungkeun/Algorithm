import sys

# 탑승중인 총 인구
total = 0
# 4개 역중 사람이 가장 많았을때의 인구수
maximum = 0
for _ in range(4) :
    # 내린사람과 탑승한사람을 각각 입력
    out, ride = map(int, sys.stdin.readline().split())
    # out은 내리므로 감소시키고, ride는 탑승하므로 증가시킨다
    total = total - out + ride
    # 최대 인구수를 갱신
    if total > maximum :
        maximum = total

print(maximum)
