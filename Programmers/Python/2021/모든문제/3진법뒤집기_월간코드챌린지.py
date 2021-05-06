def solution(n):
    answer = 0
    
    result = ""
    # n을 3으로 나눈 나머지값들을 result 문자열 항에 하나씩 추가시킨다
    # n을 3진법으로 바꾸는 동안 붙여지는 나머지값들은, 최종적으로는 사용자가 원하는 값에 대해 거꾸로 배치가 된다
    # 예를 들어 n=45 이면, 3진수로는 "1200" 이지만 result의 결과값은 "0021"이다. 
    while n != 0 :
        result += str(n % 3)
        n //= 3
    

    # 원활한 3**i 계산을 위해, "1200" 형태로 바꾼다 
    result = list(result)
    result.reverse()
    
    # 현재의 3진법 수를 다시 10진수로 바꾼다
    for i in range(len(result)) :
        answer += int(result[i]) * (3 ** i)
    return answer