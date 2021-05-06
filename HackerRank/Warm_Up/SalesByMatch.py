def sockMerchant(n, ar):
    
    ar.sort() # 배열을 먼저 오름차순 정렬한다
    stack = []
    cnt = 0
    for sock in ar :
        if not stack : # 스택이 비어있으면 숫자를 하나 넣는다
            stack.append(sock)
        
        else :
            if stack[-1] == sock : # 만약 스택 top의 숫자와 현 차례의 sock 숫자가 같다면 스택에서 제외한다
                stack.pop()
                cnt += 1 # 하나의 쌍을 이루었기때문에 카운트를 증가시킨다
            else : 
                stack.append(sock)
    
    return cnt