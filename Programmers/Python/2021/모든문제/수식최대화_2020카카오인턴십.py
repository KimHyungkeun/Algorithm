def solution(expression):
    answer = 0
    calc = ['*', '+', '-'] # 연산의 종류 ('*', '+', '-')
    cases = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]] # 가능한 모든 연산 우선순위 경우들
    all_result = [] # 위 경우들 각각에 대한 결과들

    for i in range(len(cases)) :
        s = expression.split(calc[cases[i][0]]) # 먼저 첫번째 경우로 오는 연산자를 기준으로 수식을 나눈다
        new_s = []
        final_result = []

        # 두번째로 오는 연산자를 기준으로 한번 더 수식을 세분화하여 나눈다
        for j in range(len(s)) :
            new_s.append(s[j].split(calc[cases[i][1]]))
        # print(s)
        # print(new_s)

        # 세분화된 연산자를 다시 합쳐나가는 과정

        if calc[cases[i][1]] == '-' : # 두번째 연산자가 뺄셈인 경우
            for k in range(len(new_s)) :
                total = eval(new_s[k][0]) # 해당 표현이 상수가 아닌 수식일 수도 있으므로, eval함수를 통해 계산한 값을 넣는다
                for r in range(1, len(new_s[k])) :
                    total -= eval(new_s[k][r]) # 차례대로 뺄셈을 진행한다
                final_result.append(total) # 해당 항에 대한 계산이 완료되면 final_result 항에 추가한다
     
        elif calc[cases[i][1]] == '+' : # 두번째 연산자가 덧셈인 경우
            for k in range(len(new_s)) :
                total = 0
                for r in range(len(new_s[k])) :
                    total += eval(new_s[k][r]) # 해당 표현이 상수가 아닌 수식일 수도 있으므로, eval함수를 통해 계산한 값을 넣는다
                final_result.append(total)
                
        else :
            for k in range(len(new_s)) : # 세번째 연산자가 곱셈인 경우
                total = 1
                for r in range(len(new_s[k])) :
                    total *= eval(new_s[k][r]) # 해당 표현이 상수가 아닌 수식일 수도 있으므로, eval함수를 통해 계산한 값을 넣는다
                final_result.append(total)

        

        # print(final_result)
        # 세분화된 연산자를 다시 합쳐나가는 과정 (첫번째로 온 연산자를 기준으로 계산 지행)
        if calc[cases[i][0]] == '-' : # 첫번째 연산자가 뺄셈인 경우
            total = final_result[0]
            for k in range(1, len(final_result)) : # 뺄셈을 차례대로 진행
                total -= final_result[k]
            
    
        elif calc[cases[i][0]] == '+' : # 첫번째 연산자가 덧셈인 경우
            total = 0
            for k in range(len(final_result)) : # 덧셈을 차례대로 진행
                total += final_result[k]

        else : # 첫번째 연산자가 곱셈인 경우
            total = 1
            for k in range(len(final_result)) : # 곱셈을 차례대로 진행
                total *= final_result[k]

        all_result.append(abs(total)) # 해당 결과값의 절댓값을 집어넣는다
            
    # print(all_result)
    answer = max(all_result) # 지금까지 나온 계산결과값들 중, 가장 최댓값이 답이다
    # print(answer)
    return answer

# expression = "100-200*300-500+20"
expression = "50*6-3*2"
solution(expression)