def solution(arr, divisor):
    answer = []
    
    # arr 내의 원소들중에 divisor로 나누어 떨어지는 것들만 answer에 포함시킨다
    for a in arr :
        if a % divisor == 0 :
            answer.append(a)
    
    # answer에 아무것도 없다면, 나누어떨어지는게 하나도 없으므로 [-1] 이다
    if not answer :
        answer = [-1]
    
    # 그 외의 숫자들은 오름차순으로 정렬하여 마무리 짓는다
    else :
        answer.sort()
        
    return answer