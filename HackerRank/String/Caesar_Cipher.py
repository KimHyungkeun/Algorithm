# Complete the caesarCipher function below.
def caesarCipher(s, k):
    stack = []
    for w in s :
        # 대문자의 경우
        if 'A' <= w <= 'Z' :
            # 해당 문자에 k만큼 더한다(26으로 나누었을때의 나머지는 알파벳이 순환하기 때문이다)
            tmp = ord(w) + (k%26)

            # 만약 해당 글자의 아스키코드가 90을 넘어버리면 다시 A부터 시작한다
            if tmp > 90 :
                tmp = tmp - 90 + 65 - 1 
            
            stack.append(chr(tmp))
        
        elif 'a' <= w <= 'z' :
            # 해당 문자에 k만큼 더한다(26으로 나누었을때의 나머지는 알파벳이 순환하기 때문이다)
            tmp = ord(w) + (k%26)
            # 만약 해당 글자의 아스키코드가 122을 넘어버리면 다시 A부터 시작한다
            if tmp > 122 :
                tmp = tmp - 122 + 97 - 1
            
            stack.append(chr(tmp))
        
        # 그 외의 문자는 그대로 추가
        else :
            stack.append(w)
    
    return ''.join(stack)