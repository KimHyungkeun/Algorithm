import sys
from collections import deque

t = int(sys.stdin.readline()) # 테스트 케이스 설정
q = deque() # 덱크 설정

for _ in range(t) :
    string = sys.stdin.readline().rstrip()
    cmd = string.split()
    if cmd[0] == '1' : # 1은 수를 넣는 것
        q.append(cmd[1])
    elif cmd[0] == '2' : # 2는 수를 제외하는 것
        q.popleft()
    else : # 3은 숫자 중에서 가장 front쪽에 있는 수를 출력
        print(q[0])