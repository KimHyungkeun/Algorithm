def solution(S):
    # write your code in Python 3.6
    if len(S) == 0 :
        return -1
    
    if len(S) % 2 == 0 :
        return -1
    
    if S != S[::-1] :
        return -1
    
    else :
        return len(S) // 2