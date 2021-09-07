import sys

while True :
    # 남자와 여자의 수를 구한다
    m,f = map(int, sys.stdin.readline().split())
    if m == 0 and f == 0 :
        break
    print(m+f)