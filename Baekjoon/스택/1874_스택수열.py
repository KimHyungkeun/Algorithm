n = int(input())

result = []
stack = []
state = ""
flag = 0

for i in range(n) :
    val = int(input())
    result.append(val)

i = 1
while i <= n :
    # print(i)
    if flag == 0 :
        stack.append(i)
        state += "+\n"

    if len(stack) >= 1 and stack[-1] == result[0] :
        flag = 1     
        stack.pop()
        result.pop(0)
        state += "-\n"
        continue

    else :
        flag = 0
        i += 1

if not result :
    print(state)

else :
    print("NO")

    
