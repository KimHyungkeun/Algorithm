import sys
N = int(sys.stdin.readline().strip())

deque = []

for i in range(N) :
    cmd = sys.stdin.readline().strip()

    if cmd.split(" ")[0] == 'push_back' :
        deque.append(int(cmd.split(" ")[1]))
    
    elif cmd.split(" ")[0] == 'push_front' :
        deque.insert(0, int(cmd.split(" ")[1]))

    elif cmd == 'pop_back' :
        if not deque :
            print(-1)
        else :
            print(deque[-1])
            deque.pop(-1)
    
    elif cmd == 'pop_front' :
        if not deque :
            print(-1)
        else :
            print(deque[0])
            deque.pop(0)
    
    elif cmd == 'size' :
        print(len(deque))
    
    elif cmd == 'empty' :
        if not deque :
            print(1)
        else :
            print(0)
    
    elif cmd == 'front' :
        if not deque :
            print(-1)
        else :
            print(deque[0])
    
    elif cmd == 'back' :
        if not deque :
            print(-1)
        else :
            print(deque[-1])