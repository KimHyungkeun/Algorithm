def solution(n):
    answer = 0
    
    # 해당 숫자를 문자열 타입으로 변환 
    n = str(n)

    # 각 숫자들은 문자열 내에서는 문자타입이므로, 이를 정수타입으로 캐스팅하여 덧셈을 실시
    for num in n :
        answer += int(num)

    # 값 반환
    return answer