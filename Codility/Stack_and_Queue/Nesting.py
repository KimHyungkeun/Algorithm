def solution(S):
    # write your code in Python 3.6

    # 비어있는 문자열이라면 1을 리턴
    if S == "" :
        return 1
    
    else :
        stack = []
        for w in S :
            # 스택이 비어있다면 문자를 채워준다
            if not stack :
                stack.append(w)
            # 만약 각 괄호의 대응대는 괄호가 나오게되면 스택에서 제외시킨다
            else :
                if stack[-1] == '(' and w == ')' :
                    stack.pop()
                else :
                    stack.append(w)
        # 스택이 비어있다면 완전하다는 뜻으로 1을 리턴하고, 그렇지 않으면 0을 리턴한다
        if not stack :
            return 1
        else :
            return 0