N = int(input())

for i in range(N) :
    stack = []
    result = input()
    length = len(result)

    for j in range(length) :
        stack.append(result[j])

        if len(stack) >= 2 :
            if stack[-1] == ')' and stack[-2] == '(' :
                stack.pop(-1)
                stack.pop(-1)

    if not stack :
        print("YES")
    
    else :
        print("NO")
            
          




