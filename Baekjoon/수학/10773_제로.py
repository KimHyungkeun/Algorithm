n = int(input()) 

stack = []
for i in range(n) :
    num = int(input()) # 장부에 들어갈 숫자

    if num != 0 : # 만약 0을 외치면, 최근에 들어간 숫자를 지운다
        stack.append(num)
    
    else : # 그렇지 않다면, 장부에 숫자를 계속 기록 한다.
        stack.pop()

print(sum(stack))