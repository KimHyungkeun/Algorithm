def solution(number, k):
    answer = ""
    stack = []

    for i in range(len(number)) :
        if len(stack) == 0 :
            stack.append(number[i])
            continue
            
        flag = False

        while len(stack) != 0 and int(stack[-1]) < int(number[i]) :
            del stack[-1]
            k -= 1
            if k == 0 :
                flag = True
                stack.append(number[i:])
                break
        
        if flag == True :
            break
            
        else :
            stack.append(number[i])

    for i in range(len(stack)-k) :
        answer += stack[i]

    print(answer)
    return answer

number = "999"
k = 2

solution(number,k)
# 출처 : https://hellominchan.tistory.com/345

