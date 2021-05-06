# Complete the hackerrankInString function below.
def hackerrankInString(s):
    # 스택에 hackerrank라는 문자열을 넣음
    stack = list("hackerrank")

    # pop함수를 위해, 위의 문자열을 거꾸로 배치한다
    stack.reverse()
    print(stack)
    
    for w in s :
        # 만약 w가 stack의 top글자와 같다면, stack에서 그 수를 제외한다
        if w == stack[-1] :
            stack.pop()
        # 만약 스택이 비었다면 루프문을 탈출한다
        if not stack :
            break
    
    # 스택이 비어있다면 hackerrank가 해당 문자열 안에 있다는 뜻이므로 YES를 리턴한다
    if not stack :
        return "YES"
    
    # 그렇지 않다면 NO이다
    else :
        return "NO"