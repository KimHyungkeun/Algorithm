import sys

arr = list(sys.stdin.readline().rstrip())
stack = []

height = 0
for a in arr :
    # 처음 스택에 쌓이면 10 증가
    if not stack :
        height += 10
    
    # 그릇의 방향이 서로 반대이면 10 증가
    elif stack[-1] == '(' and a == ')' :
        height += 10
    
    elif stack[-1] == ')' and a == '(' :
        height += 10
    
    # 그릇의 방향이 서로 같다면 5 증가
    else :
        height += 5
    
    stack.append(a)

print(height)