def removeOuterParentheses(S: str) -> str:
        list_s = list(S)
        answer = ""
        stack = []
        
        # print(list_s)
        stack.append(list_s[0])
        count = 1
        
        i = 1
        while i != len(list_s) :
            print(i)
            stack.append(list_s[i]) 
            if list_s[i] == '(' :
                count += 1
            else :
                count -= 1
            
            if count == 1 :
                for j in range(1, len(stack)) :
                    answer += stack[j]
                    
                del stack[1:len(stack)]
                
            if count == 0 :
                del stack[0:len(stack)]
            
            i += 1
        
        return answer

S = "(()())(())"
removeOuterParentheses(S)