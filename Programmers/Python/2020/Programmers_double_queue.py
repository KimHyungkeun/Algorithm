def solution(operations):
    answer = []
    queue_list = []
    # print(operations)
    # print(operations[1].split(" ")[1])
    
    for i in range (len(operations)) :
             
        if  'I' in operations[i] :
            num = int(operations[i].split(" ")[1])
            queue_list.append(num)
            
        elif operations[i] == 'D 1' :
            if len(queue_list) != 0 :
                maximum = max(queue_list)
                for j in range (len(queue_list)) :
                    if queue_list[j] == maximum :
                        del queue_list[j]
                        break
                        
        elif operations[i] == 'D -1' :
            if len(queue_list) != 0 :
                minimum = min(queue_list)
                for j in range (len(queue_list)) :
                    if queue_list[j] == minimum :
                        del queue_list[j]
                        break
        # print(queue_list)
                        
        
    
    if len(queue_list) == 0 :
        answer.append(0)
        answer.append(0)
    
    else :
        answer.append(max(queue_list))
        answer.append(min(queue_list))
    
    # print(answer)
    return answer

operations =["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
# operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
solution(operations)