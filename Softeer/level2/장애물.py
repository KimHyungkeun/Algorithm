import sys

def dfs(x,y) :
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n :
        return False
    
    if arr[x][y] == '1' :
        arr[x][y] = '0'
        cnt += 1
    
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x-1,y)

        return True
    
    return False

n = int(sys.stdin.readline())

arr = []
for _ in range(n) :
    row = list(sys.stdin.readline().rstrip())
    arr.append(row)

ans = []
cnt = 0
for i in range(n) :
    for j in range(n) :
        if dfs(i,j) :   
           ans.append(cnt)
           cnt = 0  

ans.sort()
print(len(ans))
for a in ans :
    print(a)