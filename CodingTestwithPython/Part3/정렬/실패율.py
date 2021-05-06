def solution(N, stages):
    answer = []
    
    clear = [] # 스테이지별 실패율을 담을 리스트
    length = len(stages) # 각 플레이어가 현재까지 진행중인 스테이지

    for i in range(1, N+1) :
        cnt = 0 # 해당 i번째 스테이지를 미해결한 사람들 
        for sta in stages :
            if sta == i : # 만약 i번째 스테이지를 해결못한경우 그 인원수를 카운트
                cnt += 1
        if length <= 0 : # 만약 해당 스테이지에 사람이 없다면, 그 스테이지 실패율은 0%이다
            clear.append((i, 0))
        else :
            clear.append((i, cnt / length)) # 해당 스테이지의 실패율을 구한다
            length -= cnt
        
    clear.sort(key = lambda x : x[1], reverse=True) # 실패율이 높은순서대로 정렬한다

    for n in clear :
        answer.append(n[0]) # 스테이지 번호만을 answer에 담는다
    
    # print(answer)
    return answer

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]	

N = 4
stages = [4,4,4,4,4]

solution(N, stages)