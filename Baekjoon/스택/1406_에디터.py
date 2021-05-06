import sys

left = list(sys.stdin.readline().strip())
right = []
n = int(sys.stdin.readline().strip())


for i in range(n) :
    cmd = sys.stdin.readline().strip()

    if cmd == 'L' and left :
        right.append(left.pop())
       
    elif cmd == 'D' and right :
        left.append(right.pop())
      
    elif cmd == 'B' and left :
        left.pop()
        
    elif cmd[0] == 'P' :
        left.append(cmd[2])
        


print(''.join(left + right[::-1]))

# 출처: https://suri78.tistory.com/112 [공부노트]

