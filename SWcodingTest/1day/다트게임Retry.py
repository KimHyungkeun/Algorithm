def solution(dartResult):
    answer = 0
    tmp = ""

    score = [] # 스코어는 0 ~ 10점까지이다
    i = 0
    for w in dartResult :
        # print(w, i)
        # 만약 해당 문자가 숫자라면
        if 48 <= ord(w) <= 57 :

            if tmp == '1' : # 1이될지 10이 될지를 판단하는 임시변수       
                if w == '0' : # 1다음 0이 들어오면 10점으로 간두
                    score.append(10) 
                else :
                    score.append(1)  # 그렇지 않다면 1점 그자체이다
                tmp = ""        
                i += 1
                continue

          
            if w == '1' : #만약 들어온는 숫자가 1일 경우
                if i == len(dartResult)-1 : # 마지막 result가 1하나뿐이라면, tmp에 넣는 작업 없이 바로 1을 추가한다
                    print(i, len(dartResult)-1)
                    score.append(1)
                    tmp = ""
                    
                else : # 만약 1이라면 임시변수에 저장했다가 1과 10중에 판별하는 프로세스로 넘어간다
                    tmp = '1'

                # print(tmp)  
            
            else :               
                score.append(int(w)) # 그 외의 숫자라면 바로 score에 넣는다
                tmp = ""


        else : 
            if tmp == '1' : # 만약 1 판별여부에 대해 남아있다면 1을 score에 추가하고 시작한다
                score.append(1)
                tmp = ""

            # 1제곱
            if w == 'S' :
                continue
            
            # 2제곱
            elif w == 'D' :
                score[-1] = score[-1]**2
            
            # 3제곱
            elif w == 'T' :
                score[-1] = score[-1]**3
            
            # 현재점수와 바로 이전점수를 2배로 한다
            elif w == '*' :
                if len(score) == 1 :
                    score[-1] = score[-1]*2
                else :
                    score[-1] = score[-1]*2
                    score[-2] = score[-2]*2

            # 현재점수를 -2배로 한다
            elif w == '#' : 
                    score[-1] = score[-1]*-1

        # print(score)
        i += 1
        

    answer = sum(score)
    print(answer)
    return answer

dartResult = "1001"
solution(dartResult)

# https://programmers.co.kr/learn/courses/30/lessons/17682