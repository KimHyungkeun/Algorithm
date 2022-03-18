# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque()
for _ in range(n) :
    cmd = sys.stdin.readline().rstrip()
    command = cmd.split()
    
    if command[0] == "append" :
        q.append(int(command[1]))
    
    elif command[0] == "appendleft" :
        q.appendleft(int(command[1]))
    
    elif cmd == "pop" :
        q.pop()
    
    else :
        q.popleft()

for a in q :
    print(a, end=' ')
