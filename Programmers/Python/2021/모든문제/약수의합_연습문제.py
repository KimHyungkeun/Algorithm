def solution(n):
    answer = 0
    # 1 ~ n 까지의 자연수를 나열
    for i in range(1, n+1) :
        # i가 n으로 나누어 떨어지면, n의 약수인것이다.
        if n % i == 0 :
            # answer에 합을 누적
            answer += i
    
    # 값 리턴
    return answer