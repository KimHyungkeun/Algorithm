def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6 :
        for w in s :
            # print(w)
            if 'a' <= w <= 'z' or 'A' <= w <= 'Z' :
                answer = False
                break
    
    else :
        answer = False
    
    return answer

s = "1234"
solution(s)