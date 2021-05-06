def solution(n):
    answer = 0
    
    # n의 제곱근을 구한다
    tmp = n ** 0.5
    if int(tmp) == tmp : # n의 제곱근 tmp와 tmp를 int형으로 캐스팅했을때 같다면 제곱근 관계인 것이다
        answer = int(( tmp + 1 )**2) # 해당 제곱근에 1을 더한 값을 제곱한다
    else :
        answer = -1 # 그러지 않다면 -1을 반환
    
    return answer

n = 11
solution(n)