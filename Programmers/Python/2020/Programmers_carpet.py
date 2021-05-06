def solution(brown, yellow):
    answer = []
    
    summary = brown + yellow
    divisor = []
    
    for i in range(yellow, 0, -1):
        if yellow % i == 0 :
            divisor.append(i)
      
    # print(divisor)
    
    maximum = len(divisor)
    
    if maximum % 2 != 0 or yellow == 1:
        maximum += 1
    
    for i in range (0, maximum) :
        width = divisor[i]
        height = divisor[len(divisor)-1-i]

        if (width+2) * (height+2) == summary and (width >= height):
            answer.append(width+2)
            answer.append(height+2)
            break
        

    print(answer)
    return answer