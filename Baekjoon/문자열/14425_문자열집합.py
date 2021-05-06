import sys

# n과 m 입력
n, m = map(int, sys.stdin.readline().split())

# 집합 s, 포함여부에 따른 카운트 변수 cnt
s = []
cnt = 0

# 집합 s에 문자열을 입력
for _ in range(n) :
    s.append(sys.stdin.readline().rstrip())

# 해당 문자열이 집합 s에 들어있다면 카운트변수 증가
for _ in range(m) :
    search = sys.stdin.readline().rstrip()
    if search in s :
        cnt += 1

# 출력
print(cnt)