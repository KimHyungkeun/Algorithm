def solution(people, limit):
    answer = 0
    people.sort()
    
    i = 0
    j = len(people)-1
    
    summary = 0
    while i <= j :
        if people[i] + people[j] > limit :
            j -= 1
            answer += 1
        
        else :
            i += 1
            j -= 1
            answer += 1
            
    
    return answer