import sys

# 탑 갯수
n = int(sys.stdin.readline())

# 탑의 높이를 입력
tmp = list(map(int, sys.stdin.readline().split()))

tower = [] # 탑들 종류
answer = [] # 수신하는 탑들을 모아놓을 배열
stack = [] # 스택

# 탑의 높이와 위치를 기록
for i in range(n) :
    tower.append([tmp[i], i])

for i in range(n) :

    # 스택에 수가 있을때
    while stack :
        # 만약 스택 마지막 탑이, 비교하려는 탑보다 높다면
        if stack[-1][0] > tower[i][0] :
            # 스택 마지막 탑의 높이를 기록(비교하려는 탑은 스택에 넣지 않는다)
            answer.append(stack[-1][1] + 1)
            break
        else : # 비교하려는 탑이 더 높다면, 스택 마지막 탑을 뺀다
            stack.pop()
    # 만약 스택이 비게되면, 그다음에 오게될 탑이 가장 높다고 가정하므로 answer 배열에는 0을 추가
    if not stack :
        answer.append(0)
    # 스택에 새로 올 탑을 넣음
    stack.append(tower[i])

# 출력
for ans in answer :
    print(ans, end=' ')