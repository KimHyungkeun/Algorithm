def solution(n):
    
    # 예를 들어 n이 3이면 "수박수", n이 4이면 "수박수박" 과 같은 결과값을 내야한다
    answer = ''
    for i in range(n) :
        if i % 2 == 0 :
            answer += '수'
        else :
            answer += '박'
    
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/12922