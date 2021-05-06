# Complete the gameOfThrones function below.
def gameOfThrones(s):
    # 철자별 확인을 위해 리스트형태로 변환
    s = list(s)
    # 오름차순 정렬
    s.sort()
    stack = []

    for w in s :
        # 스택이 비어있다면 철자 추가
        if not stack :
            stack.append(w)
        # 스택 top과 현재의 철자가 같다면 스택에서 제외하고, 다르다면 스택에 추가한다
        else :
            if stack[-1] == w :
                stack.pop()
            else :
                stack.append(w)
    
    # 만약 스택이 완전히 비었거나, 딱 한글자가 남아있다면 팰린드롬 이므로 YES 출력
    if not stack or len(stack) == 1 :
        return "YES"
    # 아니라면 NO
    else :
        return "NO"

        