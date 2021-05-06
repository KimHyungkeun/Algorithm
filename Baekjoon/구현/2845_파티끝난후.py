import sys

# 사람수 l과, 파티가 열린 곳의 넓이 p
l, p  = map(int, sys.stdin.readline().split())
# 각 기사에 실려있는 참가자 수
arr = list(map(int, sys.stdin.readline().split()))
answer = []

# 사람 수 * 파티장 넓이
total = l * p
for a in arr :
    # answer에 답 넣음
    answer.append(a - total)

print(*answer)