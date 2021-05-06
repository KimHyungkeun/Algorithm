def solution(n):

    # 정수n을 잠시 문자열로 만든 후, 원활한 핸들링을 위해 리스트 형태로 바꾼다
    n = list(str(n))
    n.sort(reverse = True) # 해당 값들을 내림차순 정렬한다.(문자 형태의 숫자여도 아스키코드 값에 따라 내림차순 정렬이 가능하다)
    
    answer = ''.join(n) # 리스트 내의 숫자 원소들을 하나의 문자열로 통합시킨다.
    answer = int(answer) # 통합시킨 문자열 형태의 숫자를 정수타입으로 변환한다
    
    return answer