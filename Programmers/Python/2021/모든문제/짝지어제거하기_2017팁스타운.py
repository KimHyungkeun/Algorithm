def solution(s):
    answer = 0
    stack = []

    for w in s :
        # 스택이 비어있다면 스택에 새로 추가
        if not stack :
            stack.append(w)
        
        else :
            # 스택의 top부분과 다음에 들어올 철자 w가 같다면, 스택의 top을 제거
            if stack[-1] == w :
                stack.pop()
            # 그렇지 않다면 새로 추가함
            else :
                stack.append(w)

    # 스택이 완전히 비었다면(문자열이 완전히 제거되었다면) 1을 반환
    if not stack :
        answer = 1
    
    # 값 반환
    return answer