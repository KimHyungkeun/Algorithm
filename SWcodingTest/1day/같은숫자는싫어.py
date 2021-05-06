def solution(arr):
    
    # 배열 순서대로 세어서, 만약 이전순서와 다음순서에 똑같은수가 반복되면 1번만 출력되게 한다
    answer = []
    cnt = -1
    
    for i in range(len(arr)) :
        
        if arr[i] == cnt :
            continue
            
        else :
            answer.append(arr[i])
            cnt = arr[i]
    
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/12906