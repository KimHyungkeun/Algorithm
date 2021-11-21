class Solution:
    def isValid(self, s: str) -> bool:
        # 열린괄호와 닫힌괄호가 일정하게 짝을 맞추는지 확인
        stack = []
        for i in range(len(s)) :
            if not stack :
                stack.append(s[i])
            
            else :
                if stack[-1] == '(' and s[i] == ')' :
                    stack.pop()
                
                elif stack[-1] == '{' and s[i] == '}' :
                    stack.pop()
                
                elif stack[-1] == '[' and s[i] == ']' :
                    stack.pop()
                
                else :
                    stack.append(s[i])
        
        if not stack :
            return True
        else :
            return False