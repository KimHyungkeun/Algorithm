import sys
n, m = map(int, sys.stdin.readline().split())

# 타워 길이는 100m 이고, n개의 구역마다 해당하는 제한속도가 존재한다
tower_height = {i:0 for i in range(100)}
start = 0
for _ in range(n) :
    area, speed = map(int, sys.stdin.readline().split())
    for i in range(start, start+area) :
        tower_height[i] = speed
    start += area


# 만약, 상단에서 정의한 구역내에서의 제한속도를 넘어서면 초과한 만큼의 속도를 speed_log에 기록한다.
# 제한속도를 넘지 않았다면 0을 기록한다
speed_log = []
start = 0
for _ in range(m) :
    area, speed = map(int, sys.stdin.readline().split()) 
    for i in range(start, start+area) :
        if tower_height[i] > speed :
            speed_log.append(0)
        else :
            speed_log.append(speed - tower_height[i])
    start += area

print(max(speed_log))