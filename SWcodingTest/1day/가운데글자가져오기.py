def solution(s):
    
    mid = len(s) // 2
    
    if len(s) % 2 == 0 :
        answer = s[mid-1] + s[mid]
    else :
        answer = s[mid]
        
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/12903