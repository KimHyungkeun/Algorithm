def solution(progresses, speeds):
    answer = []
    
    while len(progresses) != 0 :
        
        for i in range (len(progresses)) :
            if progresses[i] >= 100 :
                continue
            else :
                progresses[i] += speeds[i]
        
        count = 0
        while len(progresses) != 0 :
            # print(progresses)
            if progresses[0] >= 100 :
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else : break
        
        if count > 0 :
            answer.append(count)
    
    print(answer)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]	
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
solution(progresses, speeds)