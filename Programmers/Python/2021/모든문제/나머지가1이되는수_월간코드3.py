def solution(n):
    answer = 0
    
    # n을 어떤 수로 나누었을때 나머지가 1이 되도록하는 수 중, 가장 작은 수를 구한다
    for i in range(1, n+1) : 
        if n % i == 1 :
            answer = i
            break
    return answer