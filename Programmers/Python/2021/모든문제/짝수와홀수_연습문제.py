def solution(num):
    answer = ''
    # 짝수면 "Even 출력"
    if num % 2 == 0 :
        answer = "Even"
    # 홀수면 "Odd" 출력
    else :
        answer = "Odd"
    return answer