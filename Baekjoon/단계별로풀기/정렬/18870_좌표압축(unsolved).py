import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
set_arr = list(set(arr))
cnt_dict = {}
for s in set_arr :
    cnt  = 0
    already = []
    for a in arr :
        if s > a and a not in already:
            cnt += 1
            already.append(a)
    cnt_dict[s] = cnt

for a in arr :
    print(cnt_dict[a],end=' ')





