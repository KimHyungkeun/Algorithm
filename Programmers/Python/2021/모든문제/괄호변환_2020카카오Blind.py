# 올바른 괄호 문자열인지 확인하는 함수 [ 예 : (), (()) 등과 같은 유형]
def correct_string(p) :
    stack = []
    for i in range(len(p)) :
        if not stack :
            stack.append(p[i])
        else :
            if stack[-1] == '(' and p[i] == ')' :
                stack.pop()
            else :
                stack.append(p[i])
    
    # 올바른 괄호 문자열이면 True, 아니면 False를 리턴
    if not stack :
        return True
    else :
        return False

# u가 올바른 괄호 문자열이 아닌 경우에 대한 함수
def merge_string(u,v) :
    result = divide_string(v) # 먼저 v에 대해서 균형잡힌 문자열 + 나머지 문자열에 대한 결과물을 result에 집어넣는다
    string = "(" + result + ")" # result 앞뒤로 "(", ")"를 추가한다
    tmp = list(u) # u의 앞뒤 문자 제거를 위해 임시로 리스트 타입으로 변환한다
    if tmp :
        tmp.pop()
    if tmp :
        tmp.pop(0)
    # 앞뒤 문자를 제거 한 후, 남은 문자열에 대해서 모든 괄호의 방향을 전부 바꿔놓는다
    for i in range(len(tmp)) :
        if tmp[i] == '(' :
            tmp[i] = ')'
        else :
            tmp[i] = '('
    
    # 해당 결과물을 리턴한단 
    string += ''.join(tmp)
    return string


# 문자열을 나누는 유형 u에는 균형잡힌 괄호문자열, v에는 그 나머지 문자열을 넣는다
def divide_string(p) :
    if len(p) == 0 : # 빈 문자열이면 빈 문자열 그대로를 출력한다
        return ""

    stack = []
    # 균형잡힌 문자열은 "))(("와 같이 균형은 잡혀있으나 닫혀있는 모양이 아닌 경우를 말한다
    for i in range(len(p)) :
        if not stack :
            stack.append(p[i])
        else :
            if stack[-1] == '(' and p[i] == '(' :
                stack.append(p[i])
            elif stack[-1] == ')' and p[i] == ')' :
                stack.append(p[i])
            else :
                stack.pop()
        
        if not stack :
            break
    
    u = p[:i+1] # 균형잡힌 문자열 u
    v = p[i+1:] # 그 나머지 문자열 v

    if correct_string(u) : # 균형잡힌 문자열이면서 올바른 문자열인 경우, v에 대해서 다시 문자열을 나눈다
        u += divide_string(v) # 나눠진 문자열에 대한 결과물을 다시 u에 재결합 한다
        return u
            
    else :
        return merge_string(u,v) # 그렇지 않으면 merge_string에 해당하는 조건을 통해 문자열을 결합한다

    
def solution(p):
    
    answer = divide_string(p)
    # print(u,v)
    # print(answer)
    return answer

p = "(()())()"	
# p = ")("
# p = "()))((()"
solution(p)