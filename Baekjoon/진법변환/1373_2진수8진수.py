n = list(map(int, input()))
n.reverse() # 2의 n승부터 차례대로 계산하기 위함
length = len(n)
# print(n)

summary = 0
stack = []
result = []
answer = ""

for i in range(length) :
    stack.append(n[i])
    if len(stack) == 3 : # 2진법 자리 중, 3자리수씩 끊어서 수를 계산하면 8진수가 된다.
        summary = (stack[0] + 2 * stack[1] + 4 * stack[2])
        result.append(summary)
        stack = []

if len(stack) == 1 : # 만약 쌓인 스택이 1이라면, 해당 자리수까지만 계산
    summary = stack[0]
    result.append(summary)

elif len(stack) == 2 : #만약 쌓인 스택이 2라면, 해당 자리수까지만 계산
    summary = (stack[0] + 2 * stack[1])
    result.append(summary)

result.reverse() # 진법계산을 위해 임의로 뒤집어 놨기때문에, 연산이 끝난 후에는 원래대로 돌려놓는다.

for i in range(len(result)) :
    answer += str(result[i])

print(answer)



