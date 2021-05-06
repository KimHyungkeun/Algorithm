def solution(A, B, K):
    # write your code in Python 3.6

    # A와 B 사이의 중간 지점을 구한다
    mid = (A + B) // 2

    # B부터 감소하는 순으로 탐색해서, K의 배수임이 확인되면 그 즉시 루프문을 탈출한다
    while B >= mid :
        if B % K == 0 :
            break
        else :
            B -= 1
    
    # A부터 증가하는 순으로 탐색해서, K의 배수임이 확인되면 그 즉시 루프문을 탈출한다
    while A <= mid :
        if A % K == 0 :
            break
        else :
            A += 1
    
    # 만약 B - A의 값이 음수로 판정이되면 K의 배수가 하나도 없단 뜻이므로 0을 리턴한다
    if B - A < 0 :
        return 0

    # 그런경우가 아니라면 아래의 식이 K의 배수의 갯수이다
    else :
        answer = (B - A) // K + 1
        return answer