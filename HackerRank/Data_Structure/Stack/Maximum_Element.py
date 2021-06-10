def getMax(operations):
    # Write your code here
    stack = []
    answer = [] # 3번째 명령어에 대한 답들만 모아놓는 배열

    max_ele = 0
    # print(operations)
    for o in operations :
        arg = o.split()
        
        if arg[0] == '1' : # '1 x' 처럼 명령어가 오면 x를 stack에 넣는다
            stack.append(int(arg[1]))
            if len(stack) == 1 : # 만약 스택의 길이가 1이면, stacks내의 유일한 값을 최대값으로 지정
                max_ele = stack[-1]
            else : # 스택 길이가 2개 이상이면, 현재 지정된 최댓값보다도 더 큰 수가 있을 경우 새롭게 최대값 갱신
                max_ele = max(max_ele, int(arg[1]))
        
        elif arg[0] == '2' : # '2' 명령이 오면 stack의 top부분을 제외한다
            stack.pop()
            if not stack : # 만약 스택이 비었다면, 최대값은 0으로 갱신한다
                max_ele = 0 
            else : # 만약 스택이 남아있다면 가장 큰 수를 최대값으로 지정한다
                max_ele = max(stack)
        
        # '3' 명령어가 떨어지면 현재 남아있는 stack내에서의 최대값을 출력한다
        else :
            print(max_ele)
            answer.append(max_ele) # 출력된 최대값을 answer 배열에 넣는다
    
    return answer