import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 컴퓨터는 1번부터 n번까지 존재
computer = {i:[] for i in range(1, n+1)}
for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    computer[start].append(end)
    computer[end].append(start)

visited = [False] * n

# 바이러스에 감염되었을 경우, 1번컴퓨터를 포함한 다른 컴퓨터 까지의 갯수를 구한다
def bfs(graph, start, visited) :
    cnt = 0
    q = deque()
    q.append(start)
    visited[start-1] = True

    while q :
        val = q.popleft()
        for g in graph[val] :
            if not visited[g-1] :
                visited[g-1] = True
                q.append(g)
                cnt += 1
    
    return cnt


cnt = bfs(computer, 1, visited)
print(cnt)
