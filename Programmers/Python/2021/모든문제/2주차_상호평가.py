def solution(scores):
    answer = ''
    
    for i in range(len(scores)) :
        total = [] # 사용자의 점수들을 모음
        for j in range(len(scores[i])) :
            total.append(scores[j][i])
        
        # print(total)
        flag = True
        max_score = max(total) # 사용자가 받은 점수중 최고점
        min_score = min(total) # 사용자가 받은 점수중 최하점
        
        # 만약 본인이 매긴 점수가, 현재 받은 점수중 최고점이거나 최하점이면 조건을 발동
        if total[i] == max_score or total[i] == min_score :
            if total.count(total[i]) < 2 :
                flag = False
        
        # 이변이 없거나 또는 본인한테 매긴 점수가 최고점이나 최하점에 해당하지만 그 점수가 여러개일 경우, 그대로 평균점수를 도출
        if flag :
            avg = sum(total) / len(total)
            # print("true", avg)
        
        # 본인이 매긴 점수가 유일한 최고점이거나 유일한 최하점이면 해당 점수는 평균점수 계산에서 제외
        else :
            avg = (sum(total)-total[i]) / (len(total)-1)
            # print("false", avg)
        
        # 점수에 따른 학점 영역
        if avg >= 90 :
            answer += 'A'
        elif 80 <= avg < 90 :
            answer += 'B'
        elif 70 <= avg < 80 :
            answer += 'C'
        elif 50 <= avg < 70 :
            answer += 'D'
        else :
            answer += 'F'
            
    return answer