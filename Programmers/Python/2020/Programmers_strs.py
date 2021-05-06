def solution(s):
    answer = 0
    
    list_s = []

    for i in s :
        if len(list_s) == 0 :
            list_s.append(i)
        elif list_s[-1] == i :
            list_s.pop()
        else :
            list_s.append(i)
        
    
    if len(list_s) == 0 :
        answer = 1
   
    else :
        answer = 0
   
    print(answer)
    return answer

s = "baa"
solution(s)