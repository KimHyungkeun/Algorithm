# Complete the superReducedString function below.
def superReducedString(s):
    stack = []

    # 스택에 글자 하나하나 넣어본다
    for w in s :
        if not stack :
            stack.append(w)

        # 만약 스택의 top과 다음 철자가 같다면, 스택에서 top을 제외한다
        else :
            if stack[-1] == w :
                stack.pop()
            else :
                stack.append(w)
    
    # 스택에 남는게 없다면 Empty String을 반환하고, 그렇지 않으면 현재 남은 string을 반환한다
    if not stack :
        return "Empty String"
    else :
        return ''.join(stack)