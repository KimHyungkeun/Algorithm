def solution(n):
    answer = []

    # 숫자 n을 문자열 형태로 바꾼 후, 리스트로 변환 
    n = list(str(n))
    n.reverse() # 해당 리스트를 역순으로 배치
    
    # 역순으로 배치한 숫자들을 answer 리스트에 차례대로 집어넣음. (단, 넣을때는 정수형태로 넣을 것)
    for num in n :
        answer.append(int(num))
    
    return answer