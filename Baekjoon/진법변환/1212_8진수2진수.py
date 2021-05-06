n = list(map(int, input()))
length = len(n)
n.reverse() # 낮은 자리수부터 차례대로 계산하기위해 임시로 뒤집음

stack = [] # 8진수 자리 하나당 2진수로 변환된 결과들이 들어간다
total = [] # 최종적으로 전부 변환된 이진수가 들어가 자리
answer = ""

for i in range(length) :

    for _ in range(3) : # 8진수를 2로 3번나누어서 나온 나머지값들이 모인것들이 이진수가 된다.
        if n[i] % 2 == 0 :
            stack.append(0)
        else :
            stack.append(1)
        n[i] = int(n[i] / 2)
    
    
    total.append(stack[0])
    total.append(stack[1])
    total.append(stack[2])
    stack = []

total.reverse()
if total[0] == 0 : # 맨 앞자리가 0이라면 출력할 필요가 없다
    total.pop(0)

if total[0] == 0 : # 맨 앞자리가 0이라면 출력할 필요가 없다
    total.pop(0)

for i in range(len(total)) :
    answer += str(total[i])

print(answer)