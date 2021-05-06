def solution(x, n):
    answer = []
    
    # x * 1 부터 x * n 까지를 구한다
    for i in range(1, n+1) :
        answer.append(x*i)
        
    
    return answer