def solution(x):
    answer = True

    # 각 자릿수별로 다루기 위해 string 형태로 변환
    str_x = str(x)
    
    total = 0
    for n in str_x :
        # 각 자릿수들의 수를 모두 더하여 total 변수에 누적시킨다
        total += int(n) # n이 문자타입이므로 정수타입으로 변환하여 계산
    
    # x값이 total로 나누어떨어지지 않으면 하샤드 수가 아니다
    if x % total != 0 :
        answer = False
    return answer