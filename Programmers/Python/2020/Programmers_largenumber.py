def solution(n):
    answer = n
    
    tmp = ""
    binary = ""
    ones_num = 0
    
    while answer != 0 :
        # print(n)
        num = answer % 2
        if num == 1 :
            ones_num += 1
        tmp += str(num)
        answer = int(answer / 2)
        
    for i in range(len(tmp)-1, -1, -1) :
        binary += tmp[i]
    
    # print(binary)
    
    index = 1
    while True :
        answer = n + index
        tmp_answer = answer
        tmp = ""
        large_binary = ""
        large_ones_num = 0
        
        
        while answer != 0 :
            # print(n)
            num = answer % 2
            if num == 1 :
                large_ones_num += 1
            tmp += str(num)
            answer = int(answer / 2)
        
        for i in range(len(tmp)-1, -1, -1) :
            large_binary += tmp[i]
        
        if ones_num == large_ones_num :
            answer = tmp_answer
            break
        
        else :
            index += 1
          
    return answer