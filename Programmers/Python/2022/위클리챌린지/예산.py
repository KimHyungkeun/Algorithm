def solution(d, budget):
    answer = 0

    # 오름차순 정렬
    d.sort()
    
    # budget내에서 지원해줄 수 있는 최대 인원부서를 구한다
    for money in d :
        if budget < money :
            break
        budget -= money
        answer += 1
            
    return answer