def solution(number, k) :
    answer = ""

    # 숫자를 담을 스택
    stack = []

    for n in number :
        # 스택이 비어있다면 숫자만 추가한다
        if not stack :
            stack.append(n)
        else :
            # 스택의 top보다 다음 들어올 숫자가 크면서, k가 0이 아직 아닐때
            while stack and stack[-1] < n and k > 0 :
                stack.pop() # top을 제외하고 k를 하나 낮춘다
                k -= 1
            # 그 후, 스택에 새 숫자를 집어넣는다
            stack.append(n)
    
    # 만약 k가 아직 남아있다면, 전체길이-k 길이까지의 문자열을 출력한다
    if k != 0 :
        stack = stack[:-k]
    
    # 리스트 글자들을 합쳐서 문자열로 생성
    answer = ''.join(stack)
    # print(answer)
    return answer

# number = "4177252841"
# number = "1231234"
# number = "1924"
number = "87654321"
solution(number,4)