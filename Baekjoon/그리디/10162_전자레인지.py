import sys

t = int(sys.stdin.readline())

# 각 5분, 1분 , 10초 타이머이다
timer = [0,0,0]

# 1. 5분 타이머 단위로 맞출수 있는지 확인
timer[0] = (t // 300)    
t %= 300  

# 2. 1분 타이머 단위로 맞출 수 있는지 확인
timer[1] = (t // 60)  
t %= 60

# 3. 10초 타이머 단위로 맞출 수 있는지 확인
timer[2] = (t // 10)
t %= 10 

# t초에 맞게 맞출수있으면 각 timer 설정 횟수를 출력하고, 그렇지 않다면 -1 출력
if t == 0 :
    print(*timer)
else :
    print(-1)