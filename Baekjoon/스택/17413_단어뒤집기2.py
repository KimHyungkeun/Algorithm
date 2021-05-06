string = input()

stack = []
answer = ""
flag = False

length = len(string)

for i in range(length) :

    if string[i] == '<' :
        answer += ''.join(stack[::-1])
        stack = []
        stack.append(string[i])
        flag = True
        
    
    elif string[i] == '>' :
        stack.append(string[i])        
        answer += ''.join(stack)
        stack = []
        flag = False
    
    elif i == length - 1 :
        stack.append(string[i])
        answer += ''.join(stack[::-1])
        stack = []
    
    elif string[i] == ' ' :
        if flag :
            stack.append(string[i])
        
        else :
            answer += ''.join(stack[::-1])
            stack = []
            answer += ' '
    
    else :
       stack.append(string[i]) 

print(answer)