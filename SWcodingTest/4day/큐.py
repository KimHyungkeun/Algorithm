import sys
from collections import deque

# 테스트횟수 n 입력
n = int(sys.stdin.readline())
queue = deque()

for _ in range(n) :
    # 명령어 입력
    cmd = sys.stdin.readline().rstrip()
    # e나 E를 입력하면 큐에 삽입
    if cmd == 'e' or cmd == 'E' :
        if len(queue) >= 10 :
            print("overflow") # 큐가 10개이상 쌓이면 overflow 출력
        else :
            num = int(sys.stdin.readline())
            queue.append(num)
    
    # d나 D를 입력하면 큐에서 제거
    elif cmd == 'd' or cmd == 'D' :
        if not queue : # 만약 큐가 비었다면 "underflow"를 출력
            print("underflow")
        else : # 숫자가 들어있다면 맨 처음 숫자를 제거
            queue.popleft()
    else :
        break

# 큐에 남아있는 숫자들을 출력
if queue :
    for i in range(len(queue)) :
        if i == len(queue)-1 :
            print(queue[i], end='')
        else :
            print(queue[i], end=' ')


# https://level.goorm.io/exam/43246/%ED%81%90-queue/quiz/1