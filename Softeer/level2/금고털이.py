import sys

w,n = map(int, sys.stdin.readline().split())

jewels = []
for _ in range(n) :
    m,p = map(int,sys.stdin.readline().split())
    jewels.append((m,p))

jewels.sort(lambda x : x[1], reverse=True)

ans = 0
for weight,price in jewels :
    if w > weight:
        ans += weight * price
        w -= weight
    else :
        ans += w * price
        break
        
print(ans)