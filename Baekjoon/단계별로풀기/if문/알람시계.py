import sys

h, m = map(int, sys.stdin.readline().split())

# 시(hour) 변화 없이 45분 이전이면, 그대로 45분을 뺄셈
if m - 45 >= 0 :
    print(h, m-45)

# 시(hour) 변화가 존재할 경우의 계산
else :
    h -= 1
    m = m - 45 + 60
    # 만약, 0시에서 이전 시간으로 넘어가게되면 24을 더한다
    if h < 0 :
        h += 24
    
    print(h, m)