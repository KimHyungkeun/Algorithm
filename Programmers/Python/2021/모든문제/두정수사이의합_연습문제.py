def solution(a, b):

    # 만약 a가 b보다 크다면 두 수를 서로 바꾼다
    if a > b :
        a,b = b,a
        
    total = 0
    # a부터 b까지 출현하는 모든 수를 더한다
    for i in range(a,b+1) :
        total += i
        
    return total