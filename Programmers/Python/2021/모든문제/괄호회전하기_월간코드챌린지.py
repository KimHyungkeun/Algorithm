from collections import deque

def solution(s):
    cnt = 0
    length = len(s) # s의 길이를 구함
    q = deque(list(s)) # 해당 문자열의 원활한 핸들링을 위해 덱으로 설정
    
    n = 0
    
    while n != length :
        stack = []
        for w in q :
            # 스택이 비어있다면 괄호 추가
            if not stack :
                stack.append(w)
            else :
                # 올바른 대괄호 인지 비교
                if stack[-1] == '[' and w == ']' :
                    stack.pop()
                # 올바른 중괄호 인지 비교
                elif stack[-1] == '{' and w == '}' :
                    stack.pop()
                # 올바른 소괄호 인지 비교
                elif stack[-1] == '(' and w == ')' :
                    stack.pop()
                # 모두 해당 안된다면 스택에 추가
                else :
                    stack.append(w)
        
        # 스택이 비어있다는 것은 올바른 괄호란 뜻이므로 카운트를 증가시킴
        if not stack :
            cnt += 1
        
        # 맨 왼쪽에 있던 괄호를 가장 끝쪽으로 보냄
        q.append(q.popleft())
        n += 1 # 반복문 횟수 증가
     
    return cnt