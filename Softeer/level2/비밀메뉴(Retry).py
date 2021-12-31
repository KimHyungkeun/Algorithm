# 211231 풀이 : 20점
import sys
m,n,k = map(int, sys.stdin.readline().split())
sec_num = list(map(int, sys.stdin.readline().split()))
total_num = list(map(int, sys.stdin.readline().split()))

flag = False
if len(sec_num) <= len(total_num) and max(total_num) <= k :
    for i in range(len(total_num) - m) :
        if total_num[i:i+m] == sec_num[:] :
            flag = True
            break

if flag :
    print("secret")

else :
    print("normal")

# 211231 풀이 : 100점
import sys
m,n,k = map(int, sys.stdin.readline().split())
sec_num = list(map(int, sys.stdin.readline().split()))
total_num = list(map(int, sys.stdin.readline().split()))

flag = False
if len(sec_num) <= len(total_num) and max(total_num) <= k :
    for i in range(n) :
        if sec_num[:] == total_num[i:i+m] :
            flag = True
            break

if flag :
    print("secret")

else :
    print("normal")