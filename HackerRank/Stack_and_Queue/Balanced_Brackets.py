# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    
    for w in s :
        # 스택이 비어있다면 괄호기호를 하나 넣는다
        if not stack :
            stack.append(w)
        
        # 스택의 top과 다음에 들어올 문자를 비교했을때, 서로 대칭되는 괄호면 stack에서 pop을 한다
        else :
            if stack[-1] == '{' and w == '}':
                stack.pop()
            elif stack[-1] == '[' and w == ']':
                stack.pop()
            elif stack[-1] == '(' and w == ')':
                stack.pop()
            else :
                stack.append(w)
    
    # 스택이 비어있다면(완전 대칭이라면) YES를 출력하고 아니면 NO이다
    if not stack :
        return "YES"
    else :
        return "NO"