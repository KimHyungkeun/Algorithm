def countingValleys(steps, path):
    # Write your code here
    stack = []
    sea_level = 0 # 바다의 지표면
    cnt = 0 # 지나간 계곡의 수
    
    for i in range(steps) :
        if path[i] == 'U' : # U가 들어오면 지표면에서 증가함
            sea_level += 1
        else : # D가 들어오면 현재 지표면에서 감소함
            sea_level -= 1
        
        if sea_level == 0 : # 만약 지표면이 0으로 돌아왔을때, 이전 수가 음수라면 계곡을 지나간 것이다
            if stack[-1] < 0 :
                cnt += 1
        stack.append(sea_level)
        
        
    return cnt

# https://devalice.tistory.com/13