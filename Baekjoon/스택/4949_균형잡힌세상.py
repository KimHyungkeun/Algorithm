while True :
    string = input() # 문자열 입력
    stack = []

    if string == '.':
        break

    for w in string :
        if not stack and (w == '(' or w == ')' or w == '[' or w == ']') :
            stack.append(w) # 스택이 완전히 비어있을 경우, 일단 괄호와 관련된 문자차례가 되면 추가시킴
            continue

        if w == '(' or w == '[' : # 왼쪽 괄호가 들어오면 스택에 추가
            stack.append(w)
        
        elif w == ')' : # 오른쪽 소괄호가 들어올 경우
            if stack[-1] == '(' : # 왼쪽 소괄호가 top에 위치하면 제거
                stack.pop()
            else :
                stack.append(w) # 아닐 경우 스택에 추가
        
        elif w == ']' : # 오른쪽 대괄호가 들어올 경우
            if stack[-1] == '[' : # 왼쪽 대괄호가 top에 위치하면 제거
                stack.pop()
            else :
                stack.append(w) # 아닐 경우 스택에 추가
    
    if not stack :
        print("yes") # 모두 균형잡힐 경우 yes
        

    elif stack :
        print("no") # 아닐경우 no
    
 


