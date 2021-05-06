import sys

# 입력할 횟수 n
n = int(sys.stdin.readline())

stack = []
for _ in range(n) :
    # push, pop에 대한 명령어
    cmd = int(sys.stdin.readline())
    
    # push
    if cmd == 0 : 
        num = int(sys.stdin.readline())
        if len(stack) >= 10 : # 10스택 이상이면 오버플로우로 간주
            print("overflow")
        else :
            stack.append(num) # 스택에 숫자 추가
            # print(num)
    # pop
    elif cmd == 1 :
        if not stack : # 스택이 비어있다면 언더플로우로 간주
            print("underflow")
        else :
            stack.pop() # 스택의 top을 빼버린다
    # 프로그램 종료
    else :
        break

if stack :
    for num in stack :
        print(num, end = ' ')

# https://level.goorm.io/exam/43218/%EC%8A%A4%ED%83%9D-stack/quiz/1
