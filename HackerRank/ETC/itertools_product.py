import sys
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

ans = []
for i in range(len(a)) :
    for j in range(len(b)) :
        ans.append((a[i], b[j]))

for k in ans :
    print(k,end=' ')