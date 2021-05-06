import sys
from collections import deque
n = int(sys.stdin.readline().strip())

queue = deque([])

for _ in range(n) :
    cmd = sys.stdin.readline().strip()

    if 'push' in cmd:
        queue.append(int(cmd.split(" ")[1]))
    
    elif cmd == 'pop' :
        if not queue :
            print(-1)
        else :
            print(queue[0])
            queue.popleft()
    
    elif cmd == 'size' :
        print(len(queue))

    
    elif cmd == 'empty' :
        if not queue :
            print(1)
        else :
            print(0)
    
    elif cmd == 'front' :
        if not queue :
            print(-1)
        else :
            print(queue[0])
    
    elif cmd == 'back' :
        if not queue :
            print(-1)
        else :
            print(queue[-1])