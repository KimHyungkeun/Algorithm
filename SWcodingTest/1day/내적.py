def solution(a, b):
    answer = 0
    
    # 내적은 a[1]*b[1] + a[2]*b[2] + ... + a[n]*b[n] 이다
    for i in range(len(a)) :
        answer += (a[i]*b[i])
    
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/70128