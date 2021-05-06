def solution(priorities, location):
    answer = 0
    cnt = 0
    
    while True :
        if len(priorities) == 0 :
                break

        if location == 0 :
            if priorities[0] < max(priorities) :
                tmp = priorities[0]
                del priorities[0]
                priorities.append(tmp)
                location = len(priorities)-1
            
            else :
                return cnt+1
                
        
        else :
            if priorities[0] < max(priorities) :
                tmp = priorities[0]
                del priorities[0]
                priorities.append(tmp)
                location -= 1
            
            else :              
                del priorities[0]
                location -= 1
                cnt += 1
                
    return cnt


# priorities = [2,1,3,2]
# location = 2
priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities, location))
