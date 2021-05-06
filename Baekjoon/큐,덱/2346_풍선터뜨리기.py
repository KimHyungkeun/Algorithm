import sys
from collections import deque

# 풍선 갯수, 이동해야할 횟수와 방향을 입력받는다  
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# arr를 이용해서 각 풍선이 몇번째에 존재하는지도 기억한다
balloon = []
for i in range(n) :
    balloon.append((arr[i], i+1))

result = []
queue = deque(balloon) # 원할한 pop, append를 위해 deque으로 설정

# 큐가 하나가 남을때까지 반복
while len(queue) != 1:
    # 가장 첫번째 요소를 pop시키고, 해당풍선이 몇번째 풍선이었는지를 result에 넣는다
    val = queue.popleft()
    result.append(val[1])
    
    cnt = 0
    # 만약 풍선에 적힌 수가 양수라면, 오른쪽 방향으로 이동한다
    if val[0] > 0 :
        while cnt != val[0]-1 :
            queue.append(queue.popleft())
            cnt += 1
    # 만약 풍선에 적힌 수가 음수라면, 왼쪽방향으로 이동한다.
    else :
        while cnt != abs(val[0]) :
            queue.appendleft(queue.pop())
            cnt += 1
    
    # print(queue)

result.append(queue[0][1])
print(*result)