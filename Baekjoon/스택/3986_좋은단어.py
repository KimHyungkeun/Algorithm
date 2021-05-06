import sys

# 테스트 케이스 n개 입력
n = int(sys.stdin.readline())

# 올바른 문자열 갯수 카운트
cnt = 0

for _ in range(n) :
    
    stack = [] # 철자를 검사하기위한 스택

    # 문자열 입력
    string = sys.stdin.readline().rstrip()
    
    for s in string :
        # 스택이 비어있다면 추가
        if not stack :
            stack.append(s)
        # 만약 top의 글자와 다음번의 글자가 같다면, stack에서 제외
        else :
            if stack[-1] == s :
                stack.pop()
            else :
                stack.append(s)
    # 스택이 비워져있다면 올바른 문자열이므로 카운트 증가
    if not stack :
        cnt += 1

print(cnt)