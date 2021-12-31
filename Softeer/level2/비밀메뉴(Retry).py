# 211231 풀이 : 20점
import sys
m,n,k = map(int, sys.stdin.readline().split())
sec_num = list(map(int, sys.stdin.readline().split()))
total_num = list(map(int, sys.stdin.readline().split()))

flag = False
if len(sec_num) <= len(total_num) and max(total_num) <= k :
    for i in range(len(total_num) - m) : # 원인 : for문 범위를 +1 더해야함. 예를 들어 비밀번호 길이가 3, 전체번호 길이가 10일때 탐색 범위의 시작을 0 ~ 7로 맞추어야 하므로 10 - 3 + 1 = 8이 되어야 한다
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
if len(sec_num) <= len(total_num) :
    for i in range(n) :
        if sec_num[:] == total_num[i:i+m] :
            flag = True
            break

if flag :
    print("secret")

else :
    print("normal")