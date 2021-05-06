def solution(A):
    # write your code in Python 3.6
    stack = []
    
    # 짝이 잘 맞도록 오름차순 정렬한다
    A.sort()

    for n in A :
        # 스택이 비어있다면 그냥 수를 추가해주고
        if not stack :
            stack.append(n)
        
        # top의 수가 n과 같다면 top을 스택에서 제외한다
        else :
            if stack[-1] == n :
                stack.pop()
    
    # 남은 수를 반환
    return stack[0]
    