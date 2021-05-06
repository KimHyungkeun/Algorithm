def solution(n, times):
    answer = 0
    
    leng = len(times) # 심사관 자리 갯수
    left = 1
    right = (leng+1) * max(times) # 최대 범위
    
    while left <= right :
        mid = (left + right) // 2
        
        cnt = 0
        for time in times :
            cnt += (mid // time)
            # 심사 인원수를 넘으면 다음 단계
            if cnt >= n :
                break
        
        # n명을 심사 할 수 있는 경우
        # 한 심사관에게 주어진 시간을 줄여본다
        if cnt >= n :
            answer = mid
            right = mid - 1
        # 없는 경우
        elif cnt < n :
            left = mid + 1
            
    return answer

n = 6
times = [7,10]
solution(n ,times)