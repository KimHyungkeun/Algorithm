def solution(s):
    answer = True
    
    stack = []
    for w in s :
        # 스택이 비어있다면 무조건 괄호 추가
        if not stack :
            stack.append(w)
        else :
            # 스택의 top이 여는 괄호고, 다음에 들어올 문자가 닫힌 괄호면 스택에서 top을 제외시킨다
            if stack[-1] == '(' and w == ')' :
                stack.pop()
            # 그렇지 않으면 스택에 포함시킨다
            else :
                stack.append(w)
    
    # 만약 스택에 값이 남아있다면 올바른 괄호가 아닌것이 있으므로 False
    if stack :
        answer = False
    return answer