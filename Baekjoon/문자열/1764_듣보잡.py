import sys

# 본적 없는 사람 n, 들은적 없는 사람 m
n, m = map(int, sys.stdin.readline().split())

# 본적없거나 들은적없는사람을 각각 담는 리스트
no_see = []
no_hear = []

# 각각 이름을 입력 받는다
for _ in range(n) :
    no_see.append(sys.stdin.readline().rstrip())

for _ in range(m) :
    no_hear.append(sys.stdin.readline().rstrip())

# 두 리스트를 각각 집합으로 만든다
no_see = set(no_see)
no_hear = set(no_hear)

# 두 리스트의 교집합을 찾은 후, 오름차순 정렬한다
intersection = list(no_see & no_hear)
intersection.sort()

# 결과출력
print(len(intersection))
for _ in intersection :
    print(_)