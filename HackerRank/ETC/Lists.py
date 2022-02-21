import sys

if __name__ == '__main__':
    N = int(input())
    ans = []
    for _ in range(N) :
        command = sys.stdin.readline().rstrip()
        cmd = command.split()
        
        if cmd[0] == "insert" :
           ans.insert(int(cmd[1]), int(cmd[2])) 
        
        elif cmd[0] == "print" :
            print(ans)
        
        elif cmd[0] == "remove" :
            ans.remove(int(cmd[1]))
        
        elif cmd[0] == "append" :
            ans.append(int(cmd[1]))
        
        elif cmd[0] == "sort" :
            ans.sort()
        
        elif cmd[0] == "pop" :
            ans.pop()
        
        elif cmd[0] == "reverse" :
            ans.reverse()