# 해당 num을 n진수 수로 바꿔주는 함수
def n_base(n, num) :
    if num == 0 : # 처음 들어온 숫자가 0이면, 그 자체로 돌려준다
        answer = '0'
        return answer
    else :
        answer = ''
        # n진수 변환시 10 이상의 숫자에 대해서는 아래와같이 A,B,C,D,E,F 처럼 나타낸다
        while num != 0 :
            if num % n == 10 :
                answer += 'A'
            elif num % n == 11 :
                answer += 'B'
            elif num % n == 12 :
                answer += 'C' 
            elif num % n == 13 :
                answer += 'D'
            elif num % n == 14 :
                answer += 'E' 
            elif num % n == 15 :
                answer += 'F'
            else :
                answer += str(num % n)

            num //= n
        
        # 차례대로 수들을 이어붙이고 나면, 해당 결과값을 반대순서로 이어붙인다
        return answer[::-1]
    

def solution(n, t, m, p):
    # 나열된 숫자를 저장할 변수
    arr = ''

    # 대략 30000까지에 대한 n진수 수들을 한 자씩 일렬로 나열한다
    for i in range(30000) :
            arr += n_base(n, i)
    
    p -= 1 # 인덱싱을 위해 p의 현재차례 수에서 1을 뺀다
    turn = 0 # 차례
    answer = ""

    # t개의 문자가 모일때 까지 반복
    while t != 0 and turn < len(arr):
        # 만약 해당 차례가 p의 차례라면, 해당 번째의 철자를 answer에 첨가한다
        if turn % m == p :
            answer += arr[turn]
            t -= 1 
        turn += 1 # 차례를 올림
        
    return answer