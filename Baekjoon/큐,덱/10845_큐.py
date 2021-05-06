import sys
N = int(sys.stdin.readline().strip())

queue = []

for i in range(N) :
    cmd = sys.stdin.readline().strip()

    if cmd.split(" ")[0] == 'push' :
        queue.append(int(cmd.split(" ")[1]))

    elif cmd == 'pop' :
        if not queue :
            print(-1)
        else :
            print(queue[0])
            queue.pop(0)
    
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
